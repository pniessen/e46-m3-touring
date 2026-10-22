
/* Calculators page (CALCULATORS.md): gearing and road speed, tire size and speedometer,
   wheel fitment, and tire load. Plain ES5 in one closure: no libraries, no network, nothing stored.
   Each .calc[id] container on the page is wired up by its function in INIT, at the bottom.
   The leading semicolon keeps this safe when it is appended straight after page.js. */
;(function () {
  "use strict";

  var MM_PER_INCH = 25.4;          // exact
  var KM_PER_MILE = 1.609344;      // exact
  var LB_PER_KG = 2.2046226218;    // 1 lb = 0.45359237 kg exactly
  var SVG_NS = "http://www.w3.org/2000/svg";
  var MINUS = "−";
  var DASH = "—";
  var GEARS = ["1st", "2nd", "3rd", "4th", "5th", "6th"];

  // Maximum load per tire for load indexes 75 to 130. kg from Pirelli's chart
  // (pirelli.com/tyres/en-gb/car/driving-and-tyre-tips/how-to-read/tyre-load-index), lb from Pirelli's US chart
  // (pirelli.com/tires/en-us/car/driving-and-tire-tips/how-to-read/tire-load-index). Hankook's kg chart
  // agrees up to LI 100. Checked October 2026.
  var LI_FIRST = 75;
  var LI_KG = [387, 400, 412, 425, 437, 450, 462, 475, 487, 500, 515, 530, 545, 560, 580, 600, 615, 630, 650,
    670, 690, 710, 730, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1030, 1060, 1090, 1120, 1150,
    1180, 1215, 1250, 1285, 1320, 1360, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900];
  var LI_LB = [852, 882, 908, 937, 963, 992, 1019, 1047, 1074, 1102, 1135, 1168, 1201, 1235, 1279, 1323, 1356,
    1389, 1433, 1477, 1521, 1565, 1609, 1653, 1709, 1764, 1819, 1874, 1929, 1984, 2039, 2094, 2149, 2205, 2271,
    2337, 2403, 2469, 2535, 2601, 2679, 2756, 2833, 2910, 2998, 3086, 3197, 3307, 3417, 3527, 3638, 3748, 3858,
    3968, 4079, 4189];
  var LI_LAST = LI_FIRST + LI_KG.length - 1;

  /* ---------- Helpers ---------- */

  function byId(id) { return document.getElementById(id); }
  function each(list, fn) { Array.prototype.forEach.call(list, fn); }
  function trim(s) { return String(s == null ? "" : s).replace(/^\s+|\s+$/g, ""); }

  // Round half away from zero. The small nudge stops values such as 5.35, stored as 5.34999..., rounding down.
  function round(x, dp) {
    var f = Math.pow(10, dp || 0);
    var r = (x < 0 ? -1 : 1) * Math.round(Math.abs(x) * f + 1e-7) / f;
    return r === 0 ? 0 : r;
  }
  // 12,345.6 style, with a true minus sign.
  function num(x, dp) {
    dp = dp || 0;
    var r = round(x, dp);
    var parts = Math.abs(r).toFixed(dp).split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    return (r < 0 ? MINUS : "") + parts.join(".");
  }
  function signed(x, dp) {
    var r = round(x, dp);
    return (r > 0 ? "+" : "") + num(r, dp);
  }
  function rpm10(x) { return num(round(x / 10) * 10); }
  // Gear ratios show two decimals, or three when typed that way (4.227).
  function ratioText(x) {
    var three = round(x, 3).toFixed(3);
    return three.charAt(three.length - 1) === "0" ? round(x, 2).toFixed(2) : three;
  }
  function decimals(x) {
    var s = String(x), i = s.indexOf(".");
    return i < 0 ? 0 : s.length - i - 1;
  }

  function setText(el, text) {
    if (el && el.textContent !== text) { el.textContent = text; }
  }
  // Fill an element with text and spans. parts: [[className or null, text], ...].
  // Only touches the DOM when the content changes, so live regions don't repeat themselves.
  function setParts(el, parts) {
    var key = JSON.stringify(parts);
    if (!el || el.getAttribute("data-shown") === key) { return; }
    el.setAttribute("data-shown", key);
    while (el.firstChild) { el.removeChild(el.firstChild); }
    each(parts, function (p) {
      if (!p[0]) {
        el.appendChild(document.createTextNode(p[1]));
        return;
      }
      var span = document.createElement("span");
      span.className = p[0];
      span.textContent = p[1];
      if (p[0] === "calc-mark") { span.setAttribute("aria-hidden", "true"); }
      el.appendChild(span);
    });
  }

  // Read a number field. An empty field is not an error (its results wait); anything outside min..max is.
  function readNumber(input, min, max, unit) {
    var res = { ok: false, empty: false, value: NaN, msg: "" };
    if (input.validity && input.validity.badInput) {
      res.msg = "Type a number, digits only.";
      return res;
    }
    var raw = trim(input.value);
    if (raw === "") {
      res.empty = true;
      return res;
    }
    var v = parseFloat(raw.replace(",", "."));
    if (!isFinite(v)) {
      res.msg = "Type a number.";
      return res;
    }
    res.value = v;
    if (v < min || v > max) {
      res.msg = "Use " + num(min, decimals(min)) + " to " + num(max, decimals(max)) + (unit ? " " + unit : "") + ".";
      return res;
    }
    res.ok = true;
    return res;
  }
  function showError(input, msg) {
    var el = byId(input.getAttribute("data-err") || input.id + "-err");
    if (msg) { input.setAttribute("aria-invalid", "true"); } else { input.removeAttribute("aria-invalid"); }
    if (el) { setText(el, msg || ""); }
  }

  // Tire sizes: 255/40R18, 255/40ZR18, 255/40 R18, 255/40-18, 255/40/18, P205/55R16, 255 40 18;
  // a load and speed rating after a space (255/40R18 99Y XL) is ignored.
  var TIRE_RE = /^\s*P?\s*(\d{3})\s*[\/ ]\s*(\d{2})\s*(?:Z?R|[\/\-])?\s*(\d{2})(?:\s.*)?$/i;
  function parseTire(text) {
    var m = TIRE_RE.exec(text);
    if (!m) { return null; }
    var w = +m[1], ar = +m[2], rim = +m[3];
    if (w < 105 || w > 455 || ar < 20 || ar > 95 || rim < 10 || rim > 26) { return null; }
    var side = w * ar / 100;                    // sidewall height, mm
    var dia = rim * MM_PER_INCH + 2 * side;     // overall diameter, mm
    return { w: w, ar: ar, rim: rim, side: side, dia: dia, circ: Math.PI * dia, name: w + "/" + ar + "R" + rim };
  }
  function readTire(input) {
    var raw = trim(input.value);
    if (raw === "") { return { ok: false, empty: true, msg: "" }; }
    var t = parseTire(raw);
    return t ? { ok: true, value: t, msg: "" } : { ok: false, msg: "Type a size like 255/40R18." };
  }
  function revsPerMile(t) { return KM_PER_MILE * 1e6 / t.circ; }
  function revsPerKm(t) { return 1e6 / t.circ; }

  function checkedValue(root, name) {
    var r = root.querySelector('input[name="' + name + '"]:checked');
    return r ? r.value : "";
  }
  function setUnitLabels(root, text) {
    each(root.querySelectorAll(".calc-unit"), function (el) { setText(el, text); });
  }
  function headerRow(table, labels) {
    var row = table.createTHead().insertRow(-1);
    return labels.map(function (text) {
      var th = document.createElement("th");
      th.scope = "col";
      th.textContent = text;
      row.appendChild(th);
      return th;
    });
  }
  function bodyRow(body, label, cells) {
    var tr = body.insertRow(-1);
    var th = document.createElement("th");
    th.scope = "row";
    th.textContent = label;
    tr.appendChild(th);
    var out = { tr: tr, head: th, cells: [] };
    for (var i = 0; i < cells; i++) { out.cells.push(tr.insertCell(-1)); }
    return out;
  }
  // A header cell that is blank on screen but named for screen readers.
  function srLabel(cell, text) {
    var span = document.createElement("span");
    span.className = "calc-sr";
    span.textContent = text;
    cell.appendChild(span);
  }
  function noSubmit(form) {
    form.addEventListener("submit", function (e) { e.preventDefault(); });
  }

  /* ---------- 1. Gearing and road speed ---------- */

  function initGearing(root) {
    var form = root.querySelector("form");
    var rpmIn = byId("g-rpm"), speedIn = byId("g-speed"), compare = byId("g-compare");
    var unit = checkedValue(root, "g-unit") || "mph";
    var setups = ["a", "b"].map(function (k) {
      var s = {
        name: k.toUpperCase(), preset: byId("g-" + k + "-preset"), fd: byId("g-" + k + "-fd"),
        tire: byId("g-" + k + "-tire"), facts: byId("g-" + k + "-facts"), box: byId("g-" + k + "-table"),
        ratioErr: byId("g-" + k + "-ratio-err"), ratios: []
      };
      for (var i = 1; i <= 6; i++) { s.ratios.push(byId("g-" + k + "-r" + i)); }
      var table = document.createElement("table");
      s.caption = table.createCaption();
      s.caption.className = "calc-sr";
      s.th = headerRow(table, ["Gear", "Ratio", "Overall ratio", "", ""]);
      var body = table.createTBody();
      s.rows = GEARS.map(function (g) { return bodyRow(body, g, 4); });
      s.box.appendChild(table);
      s.note = document.createElement("p");
      s.note.className = "calc-note";
      s.box.parentNode.insertBefore(s.note, s.box.nextSibling);
      return s;
    });

    function applyPreset(s) {
      var opt = s.preset.options[s.preset.selectedIndex];
      if (!opt || !opt.getAttribute("data-ratios")) { return; }
      var rs = trim(opt.getAttribute("data-ratios")).split(/\s+/);
      s.ratios.forEach(function (input, i) { input.value = rs[i] || ""; });
      s.fd.value = opt.getAttribute("data-fd") || "";
    }
    // Show the preset whose numbers match the fields, or Custom.
    function matchPreset(s) {
      var match = "custom";
      each(s.preset.options, function (opt) {
        if (match !== "custom" || !opt.getAttribute("data-ratios")) { return; }
        var rs = trim(opt.getAttribute("data-ratios")).split(/\s+/);
        var same = parseFloat(s.fd.value) === parseFloat(opt.getAttribute("data-fd"));
        s.ratios.forEach(function (input, i) {
          var a = trim(input.value) === "" ? null : parseFloat(input.value);
          var b = rs[i] ? parseFloat(rs[i]) : null;
          if (a !== b) { same = false; }
        });
        if (same) { match = opt.value; }
      });
      if (s.preset.value !== match) { s.preset.value = match; }
    }
    function setUnit(next) {
      if (next === unit) { return; }
      var r = readNumber(speedIn, 0, 1e9, "");
      if (r.ok) { speedIn.value = String(round(next === "kmh" ? r.value * KM_PER_MILE : r.value / KM_PER_MILE)); }
      speedIn.max = next === "kmh" ? "400" : "250";
      unit = next;
    }

    function update() {
      var uLabel = unit === "kmh" ? "km/h" : "mph";
      setUnitLabels(root, uLabel);
      var rpm = readNumber(rpmIn, 500, 10000, "rpm");
      showError(rpmIn, rpm.msg);
      var spd = readNumber(speedIn, 1, unit === "kmh" ? 400 : 250, uLabel);
      showError(speedIn, spd.msg);
      var kmh = spd.ok ? (unit === "kmh" ? spd.value : spd.value * KM_PER_MILE) : NaN;

      var tops = setups.map(function (s) {
        // Gear ratios: an empty field means the box doesn't have that gear.
        var ratios = [], ratioMsg = "";
        s.ratios.forEach(function (input, i) {
          var r = readNumber(input, 0.3, 7, "");
          ratios.push(r.ok ? r.value : (r.empty ? null : NaN));
          if (r.msg) {
            input.setAttribute("aria-invalid", "true");
            if (!ratioMsg) { ratioMsg = "Check " + GEARS[i] + ": " + (isFinite(r.value) ? "use a ratio from 0.3 to 7." : "type a number."); }
          } else {
            input.removeAttribute("aria-invalid");
          }
        });
        setText(s.ratioErr, ratioMsg);
        var fd = readNumber(s.fd, 1.5, 7, "");
        showError(s.fd, fd.msg);
        var tire = readTire(s.tire);
        showError(s.tire, tire.msg);
        var t = tire.ok ? tire.value : null;

        if (t) {
          setParts(s.facts, [["calc-k", "Diameter "], ["calc-v", num(t.dia, 1) + " mm (" + num(t.dia / MM_PER_INCH, 2) + " in)"],
            ["calc-k", ", circumference "], ["calc-v", num(t.circ, 1) + " mm"],
            ["calc-k", ", "], ["calc-v", num(revsPerMile(t))], ["calc-k", " revolutions per mile"]]);
        } else {
          setParts(s.facts, [["calc-k", "Type a tire size to see its diameter."]]);
        }

        setText(s.th[3], uLabel + " at " + (rpm.ok ? num(rpm.value) : "…") + " rpm");
        setText(s.th[4], "rpm at " + (spd.ok ? num(spd.value) + " " + uLabel : "…"));
        setText(s.caption, "Setup " + s.name + ": road speed at the engine speed you set, and engine speed at the road speed you set, in each gear");

        var top = null, over = false;
        s.rows.forEach(function (row, i) {
          var g = ratios[i];
          row.tr.hidden = g === null;
          var gOk = typeof g === "number" && isFinite(g);
          var overall = gOk && fd.ok ? g * fd.value : NaN;
          var speedAt = NaN, rpmAt = NaN;
          if (isFinite(overall) && t) {
            if (rpm.ok) {
              var kmhAt = rpm.value / overall * t.circ * 60 / 1e6;
              speedAt = unit === "kmh" ? kmhAt : kmhAt / KM_PER_MILE;
            }
            if (spd.ok) { rpmAt = kmh * 1e6 / 60 / t.circ * overall; }
            top = { gear: GEARS[i], speed: speedAt, rpm: rpmAt };
          }
          setText(row.cells[0], gOk ? ratioText(g) : DASH);
          setText(row.cells[1], isFinite(overall) ? num(overall, 2) : DASH);
          setText(row.cells[2], isFinite(speedAt) ? num(speedAt) : DASH);
          var isOver = isFinite(rpmAt) && rpm.ok && round(rpmAt / 10) * 10 > rpm.value;
          over = over || isOver;
          row.cells[3].className = isOver ? "calc-over" : "";
          if (!isFinite(rpmAt)) {
            setParts(row.cells[3], [[null, DASH]]);
          } else if (isOver) {
            setParts(row.cells[3], [[null, rpm10(rpmAt)], ["calc-mark", "†"], ["calc-sr", " (above " + num(rpm.value) + " rpm)"]]);
          } else {
            setParts(row.cells[3], [[null, rpm10(rpmAt)]]);
          }
        });
        setText(s.note, over ? "† Above the " + num(rpm.value) + " rpm you set." : "");
        return top;
      });

      var a = tops[0], b = tops[1];
      if (a && b && isFinite(a.rpm) && isFinite(b.rpm) && isFinite(a.speed) && isFinite(b.speed)) {
        setParts(compare, [
          [null, "At " + num(spd.value) + " " + uLabel + " in top gear, setup A turns "], ["calc-v", rpm10(a.rpm) + " rpm"],
          [null, " (" + a.gear + ") and setup B "], ["calc-v", rpm10(b.rpm) + " rpm"], [null, " (" + b.gear + "). "],
          [null, "At " + num(rpm.value) + " rpm in top gear, A would reach "], ["calc-v", num(a.speed) + " " + uLabel],
          [null, " and B "], ["calc-v", num(b.speed) + " " + uLabel], [null, "."]
        ]);
      } else {
        setParts(compare, [[null, "Fill in both setups and the speeds above to compare them."]]);
      }
    }

    noSubmit(form);
    form.addEventListener("input", function (e) {
      var t = e.target;
      if (t.type === "radio" || t.tagName === "SELECT") { return; }   // handled on change
      setups.forEach(function (s) {
        if (t === s.fd || s.ratios.indexOf(t) > -1) { matchPreset(s); }
      });
      update();
    });
    form.addEventListener("change", function (e) {
      var t = e.target;
      if (t.name === "g-unit") { setUnit(t.value); }
      setups.forEach(function (s) {
        if (t === s.preset) { applyPreset(s); }
      });
      update();
    });
    setups.forEach(matchPreset);
    update();
  }

  /* ---------- 2. Tire size and speedometer ---------- */

  function initSpeedo(root) {
    var form = root.querySelector("form");
    var refIn = byId("s-ref"), newIn = byId("s-new"), speedIn = byId("s-speed");
    var outChange = byId("s-change"), outShows = byId("s-shows"), outTrue = byId("s-true");
    var unit = checkedValue(root, "s-unit") || "mph";
    var DEFAULT_SPEED = { mph: 60, kmh: 100 };

    var table = document.createElement("table");
    var caption = table.createCaption();
    caption.className = "calc-sr";
    caption.textContent = "Reference and new tire compared";
    var th = headerRow(table, ["", "Reference", "New", "Change"]);
    srLabel(th[0], "Measure");
    var body = table.createTBody();
    var rows = {
      dia: bodyRow(body, "Diameter, mm", 3),
      diaIn: bodyRow(body, "Diameter, in", 3),
      circ: bodyRow(body, "Circumference, mm", 3),
      mile: bodyRow(body, "Revolutions per mile", 3),
      km: bodyRow(body, "Revolutions per km", 3)
    };
    byId("s-table").appendChild(table);

    function setRow(row, a, b, change) {
      setText(row.cells[0], a);
      setText(row.cells[1], b);
      setText(row.cells[2], change);
    }
    function setUnit(next) {
      if (next === unit) { return; }
      var r = readNumber(speedIn, 0, 1e9, "");
      if (r.ok) {
        speedIn.value = String(r.value === DEFAULT_SPEED[unit] ? DEFAULT_SPEED[next]
          : round(next === "kmh" ? r.value * KM_PER_MILE : r.value / KM_PER_MILE));
      }
      speedIn.max = next === "kmh" ? "400" : "250";
      unit = next;
    }

    function update() {
      var uLabel = unit === "kmh" ? "km/h" : "mph";
      setUnitLabels(root, uLabel);
      var a = readTire(refIn), b = readTire(newIn);
      var v = readNumber(speedIn, 1, unit === "kmh" ? 400 : 250, uLabel);
      showError(refIn, a.msg);
      showError(newIn, b.msg);
      showError(speedIn, v.msg);
      var ta = a.ok ? a.value : null, tb = b.ok ? b.value : null;

      setRow(rows.dia, ta ? num(ta.dia, 1) : DASH, tb ? num(tb.dia, 1) : DASH, ta && tb ? signed(tb.dia - ta.dia, 1) : DASH);
      setRow(rows.diaIn, ta ? num(ta.dia / MM_PER_INCH, 2) : DASH, tb ? num(tb.dia / MM_PER_INCH, 2) : DASH,
        ta && tb ? signed((tb.dia - ta.dia) / MM_PER_INCH, 2) : DASH);
      setRow(rows.circ, ta ? num(ta.circ, 1) : DASH, tb ? num(tb.circ, 1) : DASH, ta && tb ? signed(tb.circ - ta.circ, 1) : DASH);
      // Revolutions: the change is between the rounded figures shown, so the row adds up.
      setRow(rows.mile, ta ? num(revsPerMile(ta)) : DASH, tb ? num(revsPerMile(tb)) : DASH,
        ta && tb ? signed(round(revsPerMile(tb)) - round(revsPerMile(ta)), 0) : DASH);
      setRow(rows.km, ta ? num(revsPerKm(ta)) : DASH, tb ? num(revsPerKm(tb)) : DASH,
        ta && tb ? signed(round(revsPerKm(tb)) - round(revsPerKm(ta)), 0) : DASH);

      if (!ta || !tb) {
        setParts(outChange, [[null, "Type both tire sizes to compare them."]]);
        setParts(outShows, []);
        setParts(outTrue, []);
        return;
      }
      var k = tb.dia / ta.dia;             // circumference ratio, new over reference
      var pct = (k - 1) * 100;
      if (round(pct, 1) === 0) {
        setParts(outChange, [[null, "The two tires are the same diameter to within 0.05%."]]);
      } else {
        setParts(outChange, [[null, "The new tire is "], ["calc-v", num(Math.abs(pct), 1) + "% " + (pct > 0 ? "larger" : "smaller")],
          [null, " in diameter than the reference (" + signed(tb.dia - ta.dia, 1) + " mm)."]]);
      }
      if (!v.ok) {
        setParts(outShows, [[null, "Type a true speed to see what the speedometer shows."]]);
        setParts(outTrue, []);
        return;
      }
      var err = (1 / k - 1) * 100;
      setParts(outShows, [[null, "At a true " + num(v.value) + " " + uLabel + " the speedometer shows "],
        ["calc-v", num(v.value / k) + " " + uLabel],
        [null, round(err, 1) === 0 ? "." : " (it reads " + num(Math.abs(err), 1) + "% " + (err < 0 ? "low" : "high") + ")."]]);
      setParts(outTrue, [[null, "When it shows " + num(v.value) + " " + uLabel + ", you are doing "],
        ["calc-v", num(v.value * k) + " " + uLabel], [null, "."]]);
    }

    noSubmit(form);
    form.addEventListener("input", function (e) {
      if (e.target.type === "radio") { return; }
      update();
    });
    form.addEventListener("change", function (e) {
      if (e.target.name === "s-unit") { setUnit(e.target.value); }
      update();
    });
    update();
  }

  /* ---------- 3. Wheel fitment ---------- */

  function initFitment(root) {
    var form = root.querySelector("form");
    var axle = byId("f-axle");
    var wheels = ["ref", "new"].map(function (k) {
      return { key: k, preset: byId("f-" + k + "-preset"), w: byId("f-" + k + "-w"), et: byId("f-" + k + "-et"), tire: byId("f-" + k + "-tire") };
    });
    var out = { inner: byId("f-inner"), outer: byId("f-outer"), tout: byId("f-tout"), tin: byId("f-tin"), track: byId("f-track") };
    var draw = byId("f-draw");

    var table = document.createElement("table");
    var caption = table.createCaption();
    var th = headerRow(table, ["", "Reference", "New", "Change"]);
    srLabel(th[0], "Position");
    var body = table.createTBody();
    var rows = {
      rimIn: bodyRow(body, "Rim inner edge", 3),
      c: bodyRow(body, "Rim centerline", 3),
      rimOut: bodyRow(body, "Rim outer face", 3),
      tireIn: bodyRow(body, "Tire inner sidewall", 3),
      tireOut: bodyRow(body, "Tire outer sidewall", 3),
      track: bodyRow(body, "Track", 3),
      width: bodyRow(body, "Width over the tires", 3)
    };
    byId("f-table").appendChild(table);

    function applyPreset(wh) {
      var opt = wh.preset.options[wh.preset.selectedIndex];
      if (!opt || !opt.getAttribute("data-et")) { return; }
      wh.w.value = opt.getAttribute("data-width");
      wh.et.value = opt.getAttribute("data-et");
      wh.tire.value = opt.getAttribute("data-tire");
    }
    // Show the preset whose numbers match the fields, or Custom. Two presets share the same numbers
    // (Style 67 19-inch and Style 163M), so the one already chosen wins a tie.
    function matchPreset(wh) {
      var t = parseTire(trim(wh.tire.value));
      function fits(opt) {
        var pt = opt && opt.getAttribute("data-et") ? parseTire(opt.getAttribute("data-tire")) : null;
        return !!(pt && t && pt.name === t.name &&
          parseFloat(wh.w.value) === parseFloat(opt.getAttribute("data-width")) &&
          parseFloat(wh.et.value) === parseFloat(opt.getAttribute("data-et")));
      }
      var match = fits(wh.preset.options[wh.preset.selectedIndex]) ? wh.preset.value : "custom";
      each(wh.preset.options, function (opt) {
        if (match === "custom" && fits(opt)) { match = opt.value; }
      });
      if (wh.preset.value !== match) { wh.preset.value = match; }
    }

    // Positions in mm from the hub face, outboard positive.
    function readWheel(wh) {
      var w = readNumber(wh.w, 4, 13, "in"), et = readNumber(wh.et, -50, 80, "mm"), t = readTire(wh.tire);
      showError(wh.w, w.msg);
      showError(wh.et, et.msg);
      showError(wh.tire, t.msg);
      if (!w.ok || !et.ok || !t.ok) { return null; }
      var half = w.value * MM_PER_INCH / 2, c = -et.value, tire = t.value;
      return {
        width: w.value, et: et.value, tire: tire, c: c,
        rimIn: c - half, rimOut: c + half, tireIn: c - tire.w / 2, tireOut: c + tire.w / 2,
        r: tire.rim * MM_PER_INCH / 2, h: tire.side,
        label: num(w.value, decimals(w.value)) + "J ET" + num(et.value) + " with " + tire.name
      };
    }
    function move(label, d) {
      var r = round(d, 1);
      return [["calc-k", label + ": "], ["calc-v", r === 0 ? "no change" : num(Math.abs(r), 1) + " mm further " + (r > 0 ? "out" : "in")]];
    }

    function update() {
      var hub = trim(axle.value) === "" ? NaN : parseFloat(axle.value);
      var ref = readWheel(wheels[0]), nw = readWheel(wheels[1]);
      var abs = isFinite(hub);
      setText(caption, abs ? "Distance from the car's centerline, mm" : "Distance from the hub face, mm (minus is inboard)");
      setText(rows.c.head, abs ? "Rim centerline (half the track)" : "Rim centerline");
      rows.track.tr.hidden = !abs;
      rows.width.tr.hidden = !abs;

      ["rimIn", "c", "rimOut", "tireIn", "tireOut"].forEach(function (k) {
        var base = abs ? hub : 0;
        setText(rows[k].cells[0], ref ? num(base + ref[k], 1) : DASH);
        setText(rows[k].cells[1], nw ? num(base + nw[k], 1) : DASH);
        setText(rows[k].cells[2], ref && nw ? signed(nw[k] - ref[k], 1) : DASH);
      });
      setText(rows.track.cells[0], ref && abs ? num(2 * (hub + ref.c), 1) : DASH);
      setText(rows.track.cells[1], nw && abs ? num(2 * (hub + nw.c), 1) : DASH);
      setText(rows.track.cells[2], ref && nw && abs ? signed(2 * (nw.c - ref.c), 1) : DASH);
      setText(rows.width.cells[0], ref && abs ? num(2 * (hub + ref.tireOut), 1) : DASH);
      setText(rows.width.cells[1], nw && abs ? num(2 * (hub + nw.tireOut), 1) : DASH);
      setText(rows.width.cells[2], ref && nw && abs ? signed(2 * (nw.tireOut - ref.tireOut), 1) : DASH);

      if (!ref || !nw) {
        setParts(out.inner, [[null, "Fill in both wheels to compare them."]]);
        setParts(out.outer, []);
        setParts(out.tout, []);
        setParts(out.tin, []);
        setParts(out.track, []);
        while (draw.firstChild) { draw.removeChild(draw.firstChild); }
        return;
      }
      setParts(out.inner, move("Rim inner edge", nw.rimIn - ref.rimIn));
      setParts(out.outer, move("Rim outer face", nw.rimOut - ref.rimOut));
      setParts(out.tout, move("Tire outer sidewall", nw.tireOut - ref.tireOut));
      setParts(out.tin, move("Tire inner sidewall", nw.tireIn - ref.tireIn));
      var dt = round(2 * (nw.c - ref.c), 1);
      setParts(out.track, [["calc-k", "Track: "], ["calc-v", dt === 0 ? "no change" : num(Math.abs(dt), 1) + " mm " + (dt > 0 ? "wider" : "narrower")]]);
      drawFitment(draw, ref, nw, hub);
    }

    noSubmit(form);
    form.addEventListener("input", function (e) {
      var t = e.target;
      if (t.tagName === "SELECT") { return; }   // handled on change
      wheels.forEach(function (wh) {
        if (t === wh.w || t === wh.et || t === wh.tire) { matchPreset(wh); }
      });
      update();
    });
    form.addEventListener("change", function (e) {
      wheels.forEach(function (wh) {
        if (e.target === wh.preset) { applyPreset(wh); }
      });
      update();
    });
    wheels.forEach(matchPreset);
    update();
  }

  function svgEl(name, attrs, parent) {
    var el = document.createElementNS(SVG_NS, name);
    for (var k in attrs) {
      if (Object.prototype.hasOwnProperty.call(attrs, k)) { el.setAttribute(k, String(attrs[k])); }
    }
    if (parent) { parent.appendChild(el); }
    return el;
  }
  function f1(x) { return String(round(x, 1)); }
  // A point in drawing coordinates (mm, y up from the wheel axis) as SVG "x y" (y down).
  function pt(x, y) { return f1(x) + " " + f1(-y); }

  // Tire section: from the inner bead, out to the widest point at mid-height, over the shoulder,
  // across the tread and back down to the outer bead.
  function tirePath(p) {
    var r = p.r, h = p.h, si = p.tireIn, so = p.tireOut, bi = p.rimIn, bo = p.rimOut;
    var k = Math.min(0.16 * (so - si), 0.45 * h);
    var yMid = r + 0.5 * h, yTop = r + h;
    return "M" + pt(bi, r) +
      " C" + pt(bi + 0.15 * (si - bi), r + 0.18 * h) + " " + pt(si, yMid - 0.25 * h) + " " + pt(si, yMid) +
      " C" + pt(si, yMid + 0.3 * h) + " " + pt(si + 0.2 * k, yTop) + " " + pt(si + k, yTop) +
      " L" + pt(so - k, yTop) +
      " C" + pt(so - 0.2 * k, yTop) + " " + pt(so, yMid + 0.3 * h) + " " + pt(so, yMid) +
      " C" + pt(so, yMid - 0.25 * h) + " " + pt(bo + 0.15 * (so - bo), r + 0.18 * h) + " " + pt(bo, r) + " Z";
  }
  // Rim: a U-shaped channel. The nominal width runs between the flanges' inner faces at the bead seat;
  // the flanges (4 mm thick, 14 mm tall) and the 6 mm barrel are drawn schematically.
  function rimPath(p) {
    var r = p.r, a = p.rimIn, b = p.rimOut;
    return "M" + pt(a - 4, r + 14) + " L" + pt(a, r + 14) + " L" + pt(a, r) + " L" + pt(b, r) + " L" + pt(b, r + 14) +
      " L" + pt(b + 4, r + 14) + " L" + pt(b + 4, r - 6) + " L" + pt(a - 4, r - 6) + " Z";
  }

  // Draw the two wheels to scale (1 unit = 1 mm), seen from behind with the outboard side on the right.
  function drawFitment(box, ref, nw, hub) {
    var x0 = Math.min(0, ref.tireIn, ref.rimIn, nw.tireIn, nw.rimIn) - 26;
    var x1 = Math.max(0, ref.tireOut, ref.rimOut, nw.tireOut, nw.rimOut) + 26;
    var yb = Math.min(ref.r, nw.r) - 58;
    var yt = Math.max(ref.r + ref.h, nw.r + nw.h) + 50;   // room for two rows: the change label, then the scale bar
    var dOut = round(nw.tireOut - ref.tireOut, 1);
    var svg = svgEl("svg", {
      viewBox: [f1(x0), f1(-yt), f1(x1 - x0), f1(yt - yb)].join(" "),
      role: "img", "aria-labelledby": "f-svg-title f-svg-desc", focusable: "false"
    });
    svgEl("title", { id: "f-svg-title" }, svg).textContent = "Wheel cross-section, to scale";
    svgEl("desc", { id: "f-svg-desc" }, svg).textContent = "Reference: " + ref.label + ". New: " + nw.label +
      ". The new tire's outer sidewall is " + (dOut === 0 ? "in the same place" : num(Math.abs(dOut), 1) + " mm further " + (dOut > 0 ? "out" : "in")) +
      (isFinite(hub) ? ". The hub face is " + num(hub, 1) + " mm from the car's centerline." : ".");

    // The wheel's mounting face on the hub: a solid line up to the lower barrel, then the plane dashed
    // through the tire, so the offset between it and each tire's middle shows.
    var barrel = Math.min(ref.r, nw.r) - 6;
    svgEl("line", { "class": "fit-hub", x1: 0, y1: f1(-yb), x2: 0, y2: f1(-barrel) }, svg);
    // New wheel filled underneath, reference dashed on top so both stay visible.
    svgEl("path", { "class": "fit-new-tire", d: tirePath(nw) }, svg);
    svgEl("path", { "class": "fit-new-rim", d: rimPath(nw) }, svg);
    svgEl("path", { "class": "fit-ref-tire", d: tirePath(ref) }, svg);
    svgEl("path", { "class": "fit-ref-rim", d: rimPath(ref) }, svg);
    svgEl("line", { "class": "fit-plane", x1: 0, y1: f1(-barrel), x2: 0, y2: f1(-(yt - 36)) }, svg);

    // Guides up from each tire's outer sidewall, with the change between them.
    var gTop = yt - 20;
    svgEl("line", { "class": "fit-guide", x1: f1(ref.tireOut), y1: f1(-(ref.r + 0.5 * ref.h)), x2: f1(ref.tireOut), y2: f1(-gTop) }, svg);
    svgEl("line", { "class": "fit-guide", x1: f1(nw.tireOut), y1: f1(-(nw.r + 0.5 * nw.h)), x2: f1(nw.tireOut), y2: f1(-gTop) }, svg);
    // The label sits just inboard of the guides, so it never runs off the outboard edge.
    svgEl("text", { "class": "fit-strong", x: f1(Math.min(ref.tireOut, nw.tireOut) - 4), y: f1(-(yt - 12)), "text-anchor": "end" }, svg)
      .textContent = "sidewall " + (dOut === 0 ? "±0" : signed(dOut, 1)) + " mm";

    // 50 mm scale bar, top left, on the row below the label.
    var sx = x0 + 8, sy = -(yt - 32);
    svgEl("path", { "class": "fit-scale", d: "M" + f1(sx) + " " + f1(sy - 4) + " V" + f1(sy) + " H" + f1(sx + 50) + " V" + f1(sy - 4) }, svg);
    svgEl("text", { x: f1(sx + 56), y: f1(sy + 1) }, svg).textContent = "50 mm";

    // Direction labels along the bottom.
    svgEl("text", { x: f1(x0 + 4), y: f1(-(yb + 8)) }, svg).textContent =
      isFinite(hub) ? "◀ " + num(hub, 1) + " mm to centerline" : "◀ inboard";
    svgEl("text", { x: f1(x1 - 4), y: f1(-(yb + 8)), "text-anchor": "end" }, svg).textContent = "outboard ▶";
    svgEl("text", { x: 5, y: f1(-(yb + 27)) }, svg).textContent = "hub face";

    while (box.firstChild) { box.removeChild(box.firstChild); }
    box.appendChild(svg);
  }

  /* ---------- 4. Tire load check ---------- */

  function initLoad(root) {
    var form = root.querySelector("form");
    var unit = checkedValue(root, "l-unit") || "kg";
    var LIMITS = { kg: [100, 3000], lb: [220, 6600] };
    var axles = [["f", "front"], ["r", "rear"]].map(function (a) {
      return { name: a[1], li: byId("l-" + a[0] + "-li"), xl: byId("l-" + a[0] + "-xl"), gawr: byId("l-" + a[0] + "-gawr"), out: byId("l-" + a[0] + "-out") };
    });

    function setUnit(next) {
      if (next === unit) { return; }
      axles.forEach(function (a) {
        var r = readNumber(a.gawr, 0, 1e9, "");
        if (r.ok) { a.gawr.value = String(round(next === "lb" ? r.value * LB_PER_KG : r.value / LB_PER_KG)); }
      });
      unit = next;
    }

    function update() {
      var other = unit === "kg" ? "lb" : "kg";
      setUnitLabels(root, unit);
      axles.forEach(function (a) {
        var li = readNumber(a.li, LI_FIRST, LI_LAST, "");
        if (li.msg && isFinite(li.value)) { li.msg = "This table covers load indexes " + LI_FIRST + " to " + LI_LAST + "."; }
        if (li.ok && li.value !== Math.floor(li.value)) {
          li.ok = false;
          li.msg = "Load indexes are whole numbers.";
        }
        showError(a.li, li.msg);
        var g = readNumber(a.gawr, LIMITS[unit][0], LIMITS[unit][1], unit);
        showError(a.gawr, g.msg);
        if (!li.ok || !g.ok) {
          setParts(a.out, [[null, "Type the tire's load index and the " + a.name + " axle rating to check them."]]);
          return;
        }
        var i = li.value - LI_FIRST;
        var one = unit === "kg" ? LI_KG[i] : LI_LB[i], oneOther = unit === "kg" ? LI_LB[i] : LI_KG[i];
        var both = 2 * one, margin = both - g.value, pass = margin >= 0;
        var parts = [
          [pass ? "calc-badge calc-pass" : "calc-badge calc-fail", pass ? "Pass" : "Fail"],
          [null, " Two tires carry "], ["calc-v", num(both) + " " + unit],
          [null, " (" + num(2 * oneOther) + " " + other + "), " + num(one) + " " + unit + " each, against a rating of " + num(g.value) + " " + unit + ": "],
          ["calc-v", pass ? num(margin) + " " + unit + " (" + num(margin / g.value * 100) + "%) to spare" : num(-margin) + " " + unit + " short"],
          [null, "."]
        ];
        if (a.xl.checked) { parts.push([null, " As an XL tire, it carries this only at its higher XL reference pressure."]); }
        setParts(a.out, parts);
      });
    }

    noSubmit(form);
    form.addEventListener("input", function (e) {
      if (e.target.type === "radio" || e.target.type === "checkbox") { return; }   // handled on change
      update();
    });
    form.addEventListener("change", function (e) {
      if (e.target.name === "l-unit") { setUnit(e.target.value); }
      update();
    });
    update();
  }

  /* ---------- Start ---------- */

  var INIT = { "calc-gearing": initGearing, "calc-speedo": initSpeedo, "calc-fitment": initFitment, "calc-load": initLoad };
  function start() {
    each(document.querySelectorAll(".calc[id]"), function (root) {
      var init = INIT[root.id];
      if (!init || root.getAttribute("data-ready")) { return; }
      try {
        init(root);
        root.setAttribute("data-ready", "true");
        root.className += " is-ready";
      } catch (err) {
        // One broken calculator shouldn't stop the others.
        if (window.console && window.console.error) { window.console.error("Calculator " + root.id + " failed:", err); }
      }
    });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
