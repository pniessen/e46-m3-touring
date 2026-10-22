(function () {
  "use strict";

  // Chapter navigation: a chip bar on narrow screens, a sidebar with section links on wide ones.
  // On a page whose chapters are its own sections, mark the chapter (and section) in view and keep
  // its link visible. The guide's chapters are separate pages: the build marks the current one.
  var nav = document.querySelector(".chapters");
  var bar = document.querySelector(".chapters > ol");
  var chapterLinks = Array.prototype.slice.call(document.querySelectorAll(".chapters > ol > li > a"))
    .filter(function (a) { return a.getAttribute("href").charAt(0) === "#"; });
  var subLinks = Array.prototype.slice.call(document.querySelectorAll(".chapters .sub a"));
  var chapterById = {}, subById = {};
  chapterLinks.forEach(function (a) { chapterById[a.getAttribute("href").slice(1)] = a; });
  subLinks.forEach(function (a) { subById[a.getAttribute("href").slice(1)] = a; });
  function sidebarMode() { return window.matchMedia("(min-width: 1100px)").matches; }
  function reveal(a) {
    if (sidebarMode()) {
      var top = a.offsetTop - nav.clientHeight / 3;
      if (a.offsetTop < nav.scrollTop || a.offsetTop > nav.scrollTop + nav.clientHeight - 40) {
        nav.scrollTo({ top: Math.max(0, top), behavior: "auto" });
      }
    } else if (bar) {
      var left = a.offsetLeft - bar.clientWidth / 2 + a.clientWidth / 2;
      bar.scrollTo({ left: Math.max(0, left), behavior: "auto" });
    }
  }
  function setCurrent(id) {
    var a = chapterById[id];
    if (!a || a.getAttribute("aria-current") === "true") return;
    chapterLinks.forEach(function (l) { l.removeAttribute("aria-current"); l.parentNode.classList.remove("open"); });
    a.setAttribute("aria-current", "true");
    a.parentNode.classList.add("open");
    reveal(a);
  }
  function setSection(id) {
    var a = subById[id];
    if (!a) return;
    subLinks.forEach(function (l) { l.removeAttribute("aria-current"); });
    a.setAttribute("aria-current", "location");
    if (sidebarMode()) reveal(a);
  }
  var herePage = document.querySelector('.chapters > ol > li > a[aria-current="page"]');
  if (herePage) reveal(herePage);
  if ("IntersectionObserver" in window) {
    if (chapterLinks.length) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting) setCurrent(e.target.id); });
      }, { rootMargin: "-40% 0px -55% 0px" });
      document.querySelectorAll("main section[id]").forEach(function (s) { io.observe(s); });
    }
    if (subLinks.length) {
      var io2 = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting) setSection(e.target.id); });
      }, { rootMargin: "0px 0px -75% 0px" });
      document.querySelectorAll("main section[id], main section h3[id]").forEach(function (h) { io2.observe(h); });
    }
  }

  // Search: the button in the chapter bar (and the field on the guide's home page) opens a panel
  // that searches every page of the site. The index, search-index.js, loads on first use.
  var panel = document.querySelector(".search-panel");
  if (panel) {
    var qInput = panel.querySelector(".search-q");
    var statusEl = panel.querySelector(".search-status");
    var list = panel.querySelector(".search-results");
    var items = null, pages = null, loading = false, timer = null, opener = null;
    var norm = function (s) { return s.toLowerCase().replace(/[‘’]/g, "'").replace(/[“”]/g, '"'); };
    var esc = function (s) {
      return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; });
    };
    var count = function (s, t) {
      var n = 0, i = s.indexOf(t);
      while (i > -1 && n < 5) { n++; i = s.indexOf(t, i + t.length); }
      return n;
    };
    // Wrap each match of the search terms in <mark>; orig and lower are the same text, as typed and normalised.
    var marked = function (orig, lower, terms) {
      var ranges = [];
      terms.forEach(function (t) {
        var i = lower.indexOf(t);
        while (i > -1) { ranges.push([i, i + t.length]); i = lower.indexOf(t, i + t.length); }
      });
      ranges.sort(function (a, b) { return a[0] - b[0]; });
      var merged = [];
      ranges.forEach(function (r) {
        var last = merged[merged.length - 1];
        if (last && r[0] <= last[1]) { last[1] = Math.max(last[1], r[1]); } else { merged.push([r[0], r[1]]); }
      });
      var out = "", pos = 0;
      merged.forEach(function (r) {
        out += esc(orig.slice(pos, r[0])) + "<mark>" + esc(orig.slice(r[0], r[1])) + "</mark>";
        pos = r[1];
      });
      return out + esc(orig.slice(pos));
    };
    var snippet = function (it, terms, phrase) {
      var at = it.tn.indexOf(phrase);
      for (var j = 0; at < 0 && j < terms.length; j++) at = it.tn.indexOf(terms[j]);
      if (at < 0) at = 0;
      var start = Math.max(0, at - 60), end = Math.min(it.tn.length, at + 170);
      if (start > 0) { var sp = it.tn.indexOf(" ", start); if (sp > -1 && sp < at) start = sp + 1; }
      if (end < it.tn.length) { var sp2 = it.tn.lastIndexOf(" ", end); if (sp2 > at) end = sp2; }
      return (start > 0 ? "… " : "") + marked(it.t.slice(start, end), it.tn.slice(start, end), terms) +
        (end < it.tn.length ? " …" : "");
    };
    var run = function () {
      var q = qInput.value.trim();
      list.innerHTML = "";
      if (q.length < 2) { statusEl.textContent = q ? "Type at least two characters." : ""; return; }
      if (!items) { load(); return; }
      // Every word must match. Rare words count for more than common ones (a part number beats "pin"),
      // a match in a heading counts extra, and so does the whole query as a phrase.
      var terms = norm(q).split(/\s+/).filter(Boolean), phrase = terms.join(" "), hits = [], cands = [];
      var df = terms.map(function () { return 0; });
      for (var i = 0; i < items.length; i++) {
        var it = items[i], all = true, heads = [], counts = [];
        for (var j = 0; j < terms.length; j++) {
          var inHead = it.hn.indexOf(terms[j]) > -1, n = count(it.tn, terms[j]);
          if (inHead || n) { df[j]++; } else { all = false; }
          heads.push(inHead);
          counts.push(n);
        }
        if (all) cands.push([i, heads, counts]);
      }
      var idf = df.map(function (d) { return Math.log(1 + items.length / (d || 1)); });
      cands.forEach(function (c) {
        var it = items[c[0]], score = 0;
        for (var j = 0; j < terms.length; j++) score += idf[j] * ((c[1][j] ? 4 : 0) + c[2][j]);
        if (terms.length > 1 && (it.hn.indexOf(phrase) > -1 || it.tn.indexOf(phrase) > -1)) score *= 1.5;
        hits.push([score, c[0]]);
      });
      hits.sort(function (x, y) { return y[0] - x[0] || x[1] - y[1]; });
      statusEl.textContent = hits.length
        ? (hits.length === 1 ? "1 result" : hits.length + " results") + (hits.length > 60 ? ", the best 60 shown" : "")
        : "Nothing found for “" + q + "”.";
      var out = "";
      hits.slice(0, 60).forEach(function (h) {
        var it = items[h[1]], pg = pages[it.p];
        out += '<li><a href="' + esc(pg[0] + (it.a ? "#" + it.a : "")) + '"><span class="where">' + esc(pg[1]) +
          '</span><span class="head">' + marked(it.h, it.hn, terms) + '</span><span class="snip">' +
          snippet(it, terms, phrase) + "</span></a></li>";
      });
      list.innerHTML = out;
    };
    var load = function () {
      if (items || loading) return;
      loading = true;
      statusEl.textContent = "Loading the search index…";
      var s = document.createElement("script");
      s.src = "search-index.js";
      s.onload = function () {
        loading = false;
        var d = window.E46_SEARCH;
        if (!d) { statusEl.textContent = "Search isn't available on this copy of the site."; return; }
        pages = d.pages;
        items = d.items.map(function (x) { return { p: x[0], a: x[1], h: x[2], t: x[3], hn: norm(x[2]), tn: norm(x[3]) }; });
        statusEl.textContent = "";
        run();
      };
      s.onerror = function () { loading = false; statusEl.textContent = "Search isn't available on this copy of the site."; };
      (document.head || document.body).appendChild(s);
    };
    var openSearch = function (e) {
      opener = (e && e.currentTarget) || document.activeElement;
      panel.hidden = false;
      document.documentElement.classList.add("search-on");
      qInput.focus();
      qInput.select();
      load();
      if (items) run();
    };
    var closeSearch = function () {
      panel.hidden = true;
      document.documentElement.classList.remove("search-on");
      if (opener && opener.focus) { try { opener.focus({ preventScroll: true }); } catch (err) { opener.focus(); } }
    };
    document.querySelectorAll(".search-open").forEach(function (b) { b.addEventListener("click", openSearch); });
    panel.querySelector(".search-close").addEventListener("click", closeSearch);
    panel.querySelector(".search-form").addEventListener("submit", function (e) {
      e.preventDefault();
      var first = list.querySelector("a");
      if (first) first.click();
    });
    qInput.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(run, 120); });
    list.addEventListener("click", function (e) { if (e.target.closest && e.target.closest("a")) closeSearch(); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !panel.hidden) { e.preventDefault(); closeSearch(); return; }
      var tag = (e.target && e.target.tagName) || "";
      if (e.key === "/" && panel.hidden && !/^(input|textarea|select)$/i.test(tag) && !(e.target && e.target.isContentEditable)) {
        e.preventDefault();
        openSearch();
      }
    });
  }

  // Worksheets and job cards: empty table cells become text fields and task lists become tick
  // boxes. Entries are a convenience saved in this browser only; printing keeps what's typed.
  var fillMain = document.querySelector("main[data-fill]");
  if (fillMain) {
    var FKEY = "e46-m3-touring-" + fillMain.getAttribute("data-page") + "-v1";
    var store = {};
    try { store = JSON.parse(localStorage.getItem(FKEY) || "{}") || {}; } catch (e) { store = {}; }
    var saveStore = function () { try { localStorage.setItem(FKEY, JSON.stringify(store)); } catch (e) { /* storage blocked */ } };
    var fields = [];
    fillMain.querySelectorAll("table").forEach(function (table, ti) {
      var heads = table.tHead && table.tHead.rows[0]
        ? Array.prototype.map.call(table.tHead.rows[0].cells, function (c) { return c.textContent.trim(); }) : [];
      Array.prototype.forEach.call(table.tBodies, function (tb) {
        Array.prototype.forEach.call(tb.rows, function (row, ri) {
          Array.prototype.forEach.call(row.cells, function (cell, ci) {
            if (cell.textContent.trim() !== "" || cell.children.length) return;
            var id = "t" + ti + "r" + ri + "c" + ci;
            var input = document.createElement("input");
            input.type = "text";
            input.className = "fill";
            var rowLabel = row.cells[0] && row.cells[0] !== cell ? row.cells[0].textContent.trim() : "";
            input.setAttribute("aria-label", (heads[ci] || "Entry") + (rowLabel ? ", " + rowLabel : ""));
            input.value = store[id] || "";
            input.addEventListener("input", function () {
              if (input.value) { store[id] = input.value; } else { delete store[id]; }
              saveStore();
            });
            cell.classList.add("fill-cell");
            cell.appendChild(input);
            fields.push(input);
          });
        });
      });
    });
    fillMain.querySelectorAll('li input[type="checkbox"]').forEach(function (cb, i) {
      var id = "c" + i;
      cb.disabled = false;
      cb.checked = !!store[id];
      cb.addEventListener("change", function () {
        if (cb.checked) { store[id] = 1; } else { delete store[id]; }
        saveStore();
      });
      fields.push(cb);
    });
    if (fields.length) {
      var bar = document.createElement("div");
      bar.className = "fill-tools";
      var note = document.createElement("span");
      note.className = "note";
      note.textContent = "Type in the blank cells and tick the boxes. Entries are saved in this browser on this device only.";
      var printBtn = document.createElement("button");
      printBtn.type = "button";
      printBtn.textContent = "Print";
      printBtn.addEventListener("click", function () { window.print(); });
      var clearBtn = document.createElement("button");
      clearBtn.type = "button";
      clearBtn.textContent = "Clear my entries";
      var armed = null;
      clearBtn.addEventListener("click", function () {
        if (!armed) {
          clearBtn.textContent = "Tap again to clear everything";
          armed = setTimeout(function () { armed = null; clearBtn.textContent = "Clear my entries"; }, 4000);
          return;
        }
        clearTimeout(armed);
        armed = null;
        clearBtn.textContent = "Clear my entries";
        store = {};
        saveStore();
        fields.forEach(function (f) { if (f.type === "checkbox") { f.checked = false; } else { f.value = ""; } });
      });
      bar.appendChild(note);
      bar.appendChild(printBtn);
      bar.appendChild(clearBtn);
      var holder = fillMain.querySelector(".wrap") || fillMain;
      holder.insertBefore(bar, holder.firstChild);
    }
  }

  // Parts checklist. Ticks are a convenience saved in this browser only.
  var KEY = "e46-m3-touring-parts-v1";
  var saved = {};
  try { saved = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { saved = {}; }
  function persist() { try { localStorage.setItem(KEY, JSON.stringify(saved)); } catch (e) { /* storage blocked */ } }

  function slug(s) {
    var h = 0;
    for (var i = 0; i < s.length; i++) { h = ((h << 5) - h + s.charCodeAt(i)) | 0; }
    return "p" + (h >>> 0).toString(36);
  }
  function kindOf(text) {
    var t = text.toLowerCase();
    if (t.indexOf("donor") > -1) return "donor";
    if (t.indexOf("fab") > -1 || t.indexOf("make") > -1) return "fab";
    if (t.indexOf("keep") > -1 || t.indexOf("reuse") > -1) return "keep";
    return "new";
  }

  var partsSection = document.querySelector('section[data-chapter="parts"]');
  var rows = [];
  if (partsSection) {
    partsSection.querySelectorAll("table").forEach(function (table) {
      var head = table.tHead && table.tHead.rows[0];
      if (!head || !table.tBodies[0]) return;
      var srcIdx = -1;
      Array.prototype.forEach.call(head.cells, function (c, i) { if (/source/i.test(c.textContent)) srcIdx = i; });
      if (srcIdx < 0) return;
      table.classList.add("parts");
      var th = document.createElement("th");
      th.className = "tick-col";
      th.textContent = "Got";
      head.insertBefore(th, head.firstChild);
      Array.prototype.forEach.call(table.tBodies[0].rows, function (row) {
        var name = (row.cells[0] ? row.cells[0].textContent : "").trim();
        var id = slug(name + "|" + (row.cells[srcIdx] ? row.cells[srcIdx].textContent : ""));
        var srcCell = row.cells[srcIdx];
        var kind = kindOf(srcCell ? srcCell.textContent : "");
        row.setAttribute("data-kind", kind);
        if (srcCell) {
          var pill = document.createElement("span");
          pill.className = "pill pill-" + kind;
          pill.textContent = srcCell.textContent.trim();
          srcCell.textContent = "";
          srcCell.appendChild(pill);
        }
        var td = document.createElement("td");
        td.className = "tick-col";
        var cb = document.createElement("input");
        cb.type = "checkbox";
        cb.id = id;
        cb.checked = !!saved[id];
        cb.setAttribute("aria-label", "Got it: " + name);
        if (cb.checked) row.classList.add("done");
        cb.addEventListener("change", function () {
          if (cb.checked) { saved[id] = 1; } else { delete saved[id]; }
          row.classList.toggle("done", cb.checked);
          persist();
          updateCount();
        });
        td.appendChild(cb);
        row.insertBefore(td, row.firstChild);
        rows.push(row);
      });
    });
  }

  var countEl = null;
  function updateCount() {
    if (!countEl) return;
    var done = rows.filter(function (r) { return r.classList.contains("done"); }).length;
    countEl.textContent = done + " of " + rows.length + " ticked";
  }

  if (partsSection && rows.length) {
    var tools = document.createElement("div");
    tools.className = "parts-tools";
    tools.setAttribute("role", "group");
    tools.setAttribute("aria-label", "Filter parts by where they come from");
    var label = document.createElement("span");
    label.className = "label";
    label.textContent = "Show";
    tools.appendChild(label);
    var filters = [["all", "All"], ["donor", "From donor M3"], ["new", "Buy new"], ["fab", "Fabricate"], ["keep", "Keep"]];
    var buttons = [];
    filters.forEach(function (f) {
      var b = document.createElement("button");
      b.type = "button";
      b.id = "filter-" + f[0];
      b.textContent = f[1];
      b.setAttribute("aria-pressed", f[0] === "all" ? "true" : "false");
      b.addEventListener("click", function () {
        buttons.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        rows.forEach(function (r) { r.hidden = !(f[0] === "all" || r.getAttribute("data-kind") === f[0]); });
      });
      buttons.push(b);
      tools.appendChild(b);
    });
    countEl = document.createElement("span");
    countEl.className = "count";
    tools.appendChild(countEl);
    var note = document.createElement("span");
    note.className = "note";
    note.textContent = "Ticks are saved in this browser on this device only.";
    tools.appendChild(note);
    var firstTable = partsSection.querySelector(".table-wrap");
    if (firstTable) firstTable.parentNode.insertBefore(tools, firstTable);
    updateCount();
  }
})();
