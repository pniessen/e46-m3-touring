# Calculators

Four calculators for planning the conversion: gearing and road speed, tire size and the speedometer, wheel fitment, and tire load. They run in your browser and save nothing: reload the page and they start again.

## Gearing and speed

Compare two drivetrains side by side: the road speed in each gear at an engine speed you choose, and the engine speed in each gear at a road speed. Setup A starts as the M3's six-speed and final drive on its 18-inch rear tire. Setup B starts as a US 325i Touring's five-speed and final drive on its standard tire. Pick another preset, or type your own ratios.

<div class="calc" id="calc-gearing">
<p class="calc-nojs">This calculator needs JavaScript.</p>
<form class="calc-form" autocomplete="off" novalidate>
<fieldset class="calc-group">
<legend>Compare at</legend>
<div class="calc-fields">
<div class="calc-field">
<label for="g-rpm">Engine speed (rpm)</label>
<input id="g-rpm" type="number" inputmode="numeric" min="500" max="10000" step="100" value="8000" aria-describedby="g-rpm-hint g-rpm-err">
<span class="calc-hint" id="g-rpm-hint">The S54 revs to 8,000 rpm.</span>
<span class="calc-error" id="g-rpm-err"></span>
</div>
<div class="calc-field">
<label for="g-speed">Road speed (<span class="calc-unit">mph</span>)</label>
<input id="g-speed" type="number" inputmode="decimal" min="1" max="250" step="1" value="70" aria-describedby="g-speed-err">
<span class="calc-error" id="g-speed-err"></span>
</div>
<fieldset class="calc-field calc-choice">
<legend>Speed in</legend>
<div class="calc-options">
<label><input type="radio" name="g-unit" value="mph" checked> mph</label>
<label><input type="radio" name="g-unit" value="kmh"> km/h</label>
</div>
</fieldset>
</div>
</fieldset>
<div class="calc-cols">
<div class="calc-panel" id="g-a">
<fieldset class="calc-group">
<legend class="calc-panel-title">Setup A</legend>
<div class="calc-field">
<label for="g-a-preset">Gearbox and final drive</label>
<select id="g-a-preset" class="calc-preset">
<option value="m3" data-ratios="4.23 2.53 1.67 1.23 1.00 0.83" data-fd="3.62" selected>E46 M3 6-speed, 3.62</option>
<option value="t325" data-ratios="4.23 2.52 1.66 1.22 1.00" data-fd="3.46">US 325i Touring 5-speed, 3.46</option>
<option value="custom">Custom</option>
</select>
</div>
<fieldset class="calc-ratios">
<legend>Gear ratios</legend>
<div class="calc-ratio-grid">
<div class="calc-field"><label for="g-a-r1">1st</label><input id="g-a-r1" type="number" inputmode="decimal" min="0.3" max="7" step="0.01" value="4.23" data-err="g-a-ratio-err" aria-describedby="g-a-ratio-err"></div>
<div class="calc-field"><label for="g-a-r2">2nd</label><input id="g-a-r2" type="number" inputmode="decimal" min="0.3" max="7" step="0.01" value="2.53" data-err="g-a-ratio-err" aria-describedby="g-a-ratio-err"></div>
<div class="calc-field"><label for="g-a-r3">3rd</label><input id="g-a-r3" type="number" inputmode="decimal" min="0.3" max="7" step="0.01" value="1.67" data-err="g-a-ratio-err" aria-describedby="g-a-ratio-err"></div>
<div class="calc-field"><label for="g-a-r4">4th</label><input id="g-a-r4" type="number" inputmode="decimal" min="0.3" max="7" step="0.01" value="1.23" data-err="g-a-ratio-err" aria-describedby="g-a-ratio-err"></div>
<div class="calc-field"><label for="g-a-r5">5th</label><input id="g-a-r5" type="number" inputmode="decimal" min="0.3" max="7" step="0.01" value="1.00" data-err="g-a-ratio-err" aria-describedby="g-a-ratio-err"></div>
<div class="calc-field"><label for="g-a-r6">6th</label><input id="g-a-r6" type="number" inputmode="decimal" min="0.3" max="7" step="0.01" value="0.83" data-err="g-a-ratio-err" aria-describedby="g-a-ratio-err"></div>
</div>
<span class="calc-hint">Leave 6th empty for a five-speed.</span>
<span class="calc-error" id="g-a-ratio-err"></span>
</fieldset>
<div class="calc-fields">
<div class="calc-field">
<label for="g-a-fd">Final drive</label>
<input id="g-a-fd" type="number" inputmode="decimal" min="1.5" max="7" step="0.01" value="3.62" aria-describedby="g-a-fd-err">
<span class="calc-error" id="g-a-fd-err"></span>
</div>
<div class="calc-field">
<label for="g-a-tire">Tire size</label>
<input id="g-a-tire" type="text" value="255/40R18" list="calc-tire-sizes" autocomplete="off" autocapitalize="characters" spellcheck="false" aria-describedby="g-a-tire-hint g-a-tire-err">
<span class="calc-hint" id="g-a-tire-hint">Like 255/40R18</span>
<span class="calc-error" id="g-a-tire-err"></span>
</div>
</div>
</fieldset>
<p class="calc-facts"><output id="g-a-facts" for="g-a-tire" aria-live="polite"></output></p>
<div class="calc-table" id="g-a-table"></div>
</div>
<div class="calc-panel" id="g-b">
<fieldset class="calc-group">
<legend class="calc-panel-title">Setup B</legend>
<div class="calc-field">
<label for="g-b-preset">Gearbox and final drive</label>
<select id="g-b-preset" class="calc-preset">
<option value="m3" data-ratios="4.23 2.53 1.67 1.23 1.00 0.83" data-fd="3.62">E46 M3 6-speed, 3.62</option>
<option value="t325" data-ratios="4.23 2.52 1.66 1.22 1.00" data-fd="3.46" selected>US 325i Touring 5-speed, 3.46</option>
<option value="custom">Custom</option>
</select>
</div>
<fieldset class="calc-ratios">
<legend>Gear ratios</legend>
<div class="calc-ratio-grid">
<div class="calc-field"><label for="g-b-r1">1st</label><input id="g-b-r1" type="number" inputmode="decimal" min="0.3" max="7" step="0.01" value="4.23" data-err="g-b-ratio-err" aria-describedby="g-b-ratio-err"></div>
<div class="calc-field"><label for="g-b-r2">2nd</label><input id="g-b-r2" type="number" inputmode="decimal" min="0.3" max="7" step="0.01" value="2.52" data-err="g-b-ratio-err" aria-describedby="g-b-ratio-err"></div>
<div class="calc-field"><label for="g-b-r3">3rd</label><input id="g-b-r3" type="number" inputmode="decimal" min="0.3" max="7" step="0.01" value="1.66" data-err="g-b-ratio-err" aria-describedby="g-b-ratio-err"></div>
<div class="calc-field"><label for="g-b-r4">4th</label><input id="g-b-r4" type="number" inputmode="decimal" min="0.3" max="7" step="0.01" value="1.22" data-err="g-b-ratio-err" aria-describedby="g-b-ratio-err"></div>
<div class="calc-field"><label for="g-b-r5">5th</label><input id="g-b-r5" type="number" inputmode="decimal" min="0.3" max="7" step="0.01" value="1.00" data-err="g-b-ratio-err" aria-describedby="g-b-ratio-err"></div>
<div class="calc-field"><label for="g-b-r6">6th</label><input id="g-b-r6" type="number" inputmode="decimal" min="0.3" max="7" step="0.01" value="" data-err="g-b-ratio-err" aria-describedby="g-b-ratio-err"></div>
</div>
<span class="calc-hint">Leave 6th empty for a five-speed.</span>
<span class="calc-error" id="g-b-ratio-err"></span>
</fieldset>
<div class="calc-fields">
<div class="calc-field">
<label for="g-b-fd">Final drive</label>
<input id="g-b-fd" type="number" inputmode="decimal" min="1.5" max="7" step="0.01" value="3.46" aria-describedby="g-b-fd-err">
<span class="calc-error" id="g-b-fd-err"></span>
</div>
<div class="calc-field">
<label for="g-b-tire">Tire size</label>
<input id="g-b-tire" type="text" value="205/55R16" list="calc-tire-sizes" autocomplete="off" autocapitalize="characters" spellcheck="false" aria-describedby="g-b-tire-hint g-b-tire-err">
<span class="calc-hint" id="g-b-tire-hint">Like 255/40R18</span>
<span class="calc-error" id="g-b-tire-err"></span>
</div>
</div>
</fieldset>
<p class="calc-facts"><output id="g-b-facts" for="g-b-tire" aria-live="polite"></output></p>
<div class="calc-table" id="g-b-table"></div>
</div>
</div>
<p class="calc-summary"><output id="g-compare" for="g-rpm g-speed g-a-preset g-b-preset g-a-tire g-b-tire" aria-live="polite"></output></p>
<datalist id="calc-tire-sizes">
<option value="205/55R16">US 325i standard</option>
<option value="225/45R17">US 325i Sport Package</option>
<option value="225/45R18">M3 front, 18-inch</option>
<option value="255/40R18">M3 rear, 18-inch</option>
<option value="225/40R19">M3 front, 19-inch</option>
<option value="255/35R19">M3 rear, 19-inch</option>
<option value="235/35R19">CSL front</option>
<option value="265/30R19">CSL rear</option>
</datalist>
</form>
</div>

The figures use the tire's nominal size, which Hankook defines for a tire that is inflated and carrying no load ([Hankook](https://www.hankooktire.com/uk/en/help-support/tire-guide/sizes-specs.html)), so treat them as close estimates. The US M3 is electronically limited to 155 mph ([BMW USA](https://www.press.bmwgroup.com/usa/article/attachment/T0022127EN_US/41385)), so faster top-gear figures are theoretical.

**Where the numbers come from:** M3 gear ratios and the 3.62 final drive from BMW USA's [2002](https://www.press.bmwgroup.com/usa/article/attachment/T0022127EN_US/41385) and [2003](https://www.press.bmwgroup.com/usa/article/attachment/T0022150EN_US/41463) M3 spec sheets; BMW's [2006 sheet](https://www.press.bmwgroup.com/usa/article/attachment/T0019121EN_US/37451) and [ST041 training manual](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf) print 3.64, about 0.6% shorter. US 325i Touring five-speed ratios and the 3.46 final drive from BMW USA's [2002](https://www.press.bmwgroup.com/usa/article/attachment/T0022131EN_US/41405) and [2003](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41437) spec sheets for the 325i Sport Wagon, as BMW USA called the Touring; we found no sheet for 2001, 2004 or 2005 cars, so confirm your own car's ratio. The 8,000 rpm default is the S54's maximum engine speed ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf)). Tire sizes come from the same BMW USA sheets, and from [BimmerTips](https://bimmertips.com/oem-bmw-e46-m3-wheel-options-specs/) for the CSL.

## Tire size change

Compare a reference tire with a new one: diameter, circumference and the change between them. The speedometer figures assume your speedometer read true on the reference tire, and show only the effect of the tire change.

<div class="calc" id="calc-speedo">
<p class="calc-nojs">This calculator needs JavaScript.</p>
<form class="calc-form" autocomplete="off" novalidate>
<div class="calc-fields">
<div class="calc-field">
<label for="s-ref">Reference tire</label>
<input id="s-ref" type="text" value="205/55R16" list="calc-tire-sizes" autocomplete="off" autocapitalize="characters" spellcheck="false" aria-describedby="s-ref-hint s-ref-err">
<span class="calc-hint" id="s-ref-hint">The size your speedometer reads true on</span>
<span class="calc-error" id="s-ref-err"></span>
</div>
<div class="calc-field">
<label for="s-new">New tire</label>
<input id="s-new" type="text" value="255/40R18" list="calc-tire-sizes" autocomplete="off" autocapitalize="characters" spellcheck="false" aria-describedby="s-new-hint s-new-err">
<span class="calc-hint" id="s-new-hint">Like 255/40R18</span>
<span class="calc-error" id="s-new-err"></span>
</div>
<div class="calc-field">
<label for="s-speed">True speed (<span class="calc-unit">mph</span>)</label>
<input id="s-speed" type="number" inputmode="decimal" min="1" max="250" step="1" value="60" aria-describedby="s-speed-err">
<span class="calc-error" id="s-speed-err"></span>
</div>
<fieldset class="calc-field calc-choice">
<legend>Speed in</legend>
<div class="calc-options">
<label><input type="radio" name="s-unit" value="mph" checked> mph</label>
<label><input type="radio" name="s-unit" value="kmh"> km/h</label>
</div>
</fieldset>
</div>
<div class="calc-results">
<div class="calc-summary">
<p><output id="s-change" for="s-ref s-new" aria-live="polite"></output></p>
<p><output id="s-shows" for="s-ref s-new s-speed" aria-live="polite"></output></p>
<p><output id="s-true" for="s-ref s-new s-speed" aria-live="polite"></output></p>
</div>
<div class="calc-table" id="s-table"></div>
</div>
</form>
</div>

**Where the numbers come from:** the presets are the US 325i's standard and Sport Package sizes ([BMW USA](https://www.press.bmwgroup.com/usa/article/attachment/T0022131EN_US/41405)), the M3's 18- and 19-inch sizes ([BMW USA](https://www.press.bmwgroup.com/usa/article/attachment/T0022150EN_US/41463)) and the CSL's ([BimmerTips](https://bimmertips.com/oem-bmw-e46-m3-wheel-options-specs/)). Diameters follow Hankook's definitions of the size code ([Hankook](https://www.hankooktire.com/uk/en/help-support/tire-guide/sizes-specs.html)).

## Wheel fitment

Compare a new wheel and tire with a reference wheel on the same hub: how far the rim's inner edge, the rim's outer face and the tire's sidewalls move in or out, and how the track changes. On the rear axle the M3 and the 325i Touring both have their hub faces about 788.5 mm from the car's centerline (BMW's published tracks put it between about 788 and 790 mm, so treat absolute positions as good to about 1 mm) (see [Rear arches and doors](README.md#rear-arches-and-doors)), so there the calculator also gives positions from the centerline and the track. To compare with your Touring's current wheels, choose **Custom** and type the width and ET marked on the wheel.

<div class="calc" id="calc-fitment">
<p class="calc-nojs">This calculator needs JavaScript.</p>
<form class="calc-form" autocomplete="off" novalidate>
<div class="calc-fields calc-fields-wide">
<div class="calc-field">
<label for="f-axle">Axle</label>
<select id="f-axle" aria-describedby="f-axle-hint">
<option value="788.5" selected>Rear: hub face at 788.5 mm</option>
<option value="801">Front, M3 parts: hub face at 801 mm</option>
<option value="">Any axle: from the hub face only</option>
</select>
<span class="calc-hint" id="f-axle-hint">Hub face distance from the car's centerline</span>
</div>
</div>
<div class="calc-cols">
<div class="calc-panel" id="f-ref">
<fieldset class="calc-group">
<legend class="calc-panel-title">Reference wheel</legend>
<div class="calc-field">
<label for="f-ref-preset">Wheel</label>
<select id="f-ref-preset" class="calc-preset">
<optgroup label="Rear">
<option value="s67-18-r" data-width="9" data-et="26" data-tire="255/40R18" selected>Style 67 18-inch rear: 9J ET26, 255/40R18</option>
<option value="s67-19-r" data-width="9.5" data-et="27" data-tire="255/35R19">Style 67 19-inch rear: 9.5J ET27, 255/35R19</option>
<option value="s163-r" data-width="9.5" data-et="27" data-tire="255/35R19">Style 163M rear: 9.5J ET27, 255/35R19</option>
<option value="csl-r" data-width="9.5" data-et="27" data-tire="265/30R19">CSL rear: 9.5J ET27, 265/30R19</option>
</optgroup>
<optgroup label="Front">
<option value="s67-18-f" data-width="8" data-et="47" data-tire="225/45R18">Style 67 18-inch front: 8J ET47, 225/45R18</option>
<option value="s67-19-f" data-width="8" data-et="47" data-tire="225/40R19">Style 67 19-inch front: 8J ET47, 225/40R19</option>
<option value="s163-f" data-width="8" data-et="47" data-tire="225/40R19">Style 163M front: 8J ET47, 225/40R19</option>
<option value="csl-f" data-width="8.5" data-et="44" data-tire="235/35R19">CSL front: 8.5J ET44, 235/35R19</option>
</optgroup>
<option value="custom">Custom</option>
</select>
</div>
<div class="calc-fields calc-fields-3">
<div class="calc-field">
<label for="f-ref-w">Rim width (in)</label>
<input id="f-ref-w" type="number" inputmode="decimal" min="4" max="13" step="0.5" value="9" aria-describedby="f-ref-w-err">
<span class="calc-error" id="f-ref-w-err"></span>
</div>
<div class="calc-field">
<label for="f-ref-et">Offset (ET, mm)</label>
<input id="f-ref-et" type="number" min="-50" max="80" step="1" value="26" aria-describedby="f-ref-et-err">
<span class="calc-error" id="f-ref-et-err"></span>
</div>
<div class="calc-field">
<label for="f-ref-tire">Tire size</label>
<input id="f-ref-tire" type="text" value="255/40R18" list="calc-tire-sizes" autocomplete="off" autocapitalize="characters" spellcheck="false" aria-describedby="f-ref-tire-err">
<span class="calc-error" id="f-ref-tire-err"></span>
</div>
</div>
</fieldset>
</div>
<div class="calc-panel" id="f-new">
<fieldset class="calc-group">
<legend class="calc-panel-title">New wheel</legend>
<div class="calc-field">
<label for="f-new-preset">Wheel</label>
<select id="f-new-preset" class="calc-preset">
<optgroup label="Rear">
<option value="s67-18-r" data-width="9" data-et="26" data-tire="255/40R18">Style 67 18-inch rear: 9J ET26, 255/40R18</option>
<option value="s67-19-r" data-width="9.5" data-et="27" data-tire="255/35R19">Style 67 19-inch rear: 9.5J ET27, 255/35R19</option>
<option value="s163-r" data-width="9.5" data-et="27" data-tire="255/35R19" selected>Style 163M rear: 9.5J ET27, 255/35R19</option>
<option value="csl-r" data-width="9.5" data-et="27" data-tire="265/30R19">CSL rear: 9.5J ET27, 265/30R19</option>
</optgroup>
<optgroup label="Front">
<option value="s67-18-f" data-width="8" data-et="47" data-tire="225/45R18">Style 67 18-inch front: 8J ET47, 225/45R18</option>
<option value="s67-19-f" data-width="8" data-et="47" data-tire="225/40R19">Style 67 19-inch front: 8J ET47, 225/40R19</option>
<option value="s163-f" data-width="8" data-et="47" data-tire="225/40R19">Style 163M front: 8J ET47, 225/40R19</option>
<option value="csl-f" data-width="8.5" data-et="44" data-tire="235/35R19">CSL front: 8.5J ET44, 235/35R19</option>
</optgroup>
<option value="custom">Custom</option>
</select>
</div>
<div class="calc-fields calc-fields-3">
<div class="calc-field">
<label for="f-new-w">Rim width (in)</label>
<input id="f-new-w" type="number" inputmode="decimal" min="4" max="13" step="0.5" value="9.5" aria-describedby="f-new-w-err">
<span class="calc-error" id="f-new-w-err"></span>
</div>
<div class="calc-field">
<label for="f-new-et">Offset (ET, mm)</label>
<input id="f-new-et" type="number" min="-50" max="80" step="1" value="27" aria-describedby="f-new-et-err">
<span class="calc-error" id="f-new-et-err"></span>
</div>
<div class="calc-field">
<label for="f-new-tire">Tire size</label>
<input id="f-new-tire" type="text" value="255/35R19" list="calc-tire-sizes" autocomplete="off" autocapitalize="characters" spellcheck="false" aria-describedby="f-new-tire-err">
<span class="calc-error" id="f-new-tire-err"></span>
</div>
</div>
</fieldset>
</div>
</div>
<div class="calc-results">
<ul class="calc-list">
<li><output id="f-inner" for="f-ref-w f-ref-et f-new-w f-new-et" aria-live="polite"></output></li>
<li><output id="f-outer" for="f-ref-w f-ref-et f-new-w f-new-et" aria-live="polite"></output></li>
<li><output id="f-tout" for="f-ref-et f-ref-tire f-new-et f-new-tire" aria-live="polite"></output></li>
<li><output id="f-tin" for="f-ref-et f-ref-tire f-new-et f-new-tire" aria-live="polite"></output></li>
<li><output id="f-track" for="f-ref-et f-new-et" aria-live="polite"></output></li>
</ul>
<figure class="calc-fit">
<div class="calc-fit-draw" id="f-draw"></div>
<figcaption><span class="calc-key calc-key-new" aria-hidden="true"></span> New wheel and tire <span class="calc-key calc-key-ref" aria-hidden="true"></span> Reference (dashed). A section through the top of the wheel, seen from behind, drawn to scale. The rim flanges are drawn schematically.</figcaption>
</figure>
<div class="calc-table" id="f-table"></div>
</div>
</form>
</div>

The sidewalls are placed half the tire's nominal section width either side of the rim's centerline. Hankook defines that width for a tire that is mounted, inflated and carrying no load ([Hankook](https://www.hankooktire.com/uk/en/help-support/tire-guide/sizes-specs.html)), so check clearances with the actual tire before you cut or weld. The track figures behind those positions are given to the nearest millimeter or tenth of an inch, so treat positions from the centerline as good to a millimeter or two.

**Where the numbers come from:** wheel and tire presets from [BMW's wheel and tire list](https://myair-bdr.bmwgroup.com/static/manual/RadReif/RadReif/00/M-GmbH/MJ2005/e46m3_2005.htm), and from [BimmerTips](https://bimmertips.com/oem-bmw-e46-m3-wheel-options-specs/) for the CSL. The rear hub face is half the M3's 1,525 mm rear track ([Motorsport Australia](https://motorsport.org.au/wpblob0fe832abcb/wp-content/uploads/docs/default-source/sporting-technical/group-3e/3-18-007-bmw-e46-m3.pdf)) plus the 26 mm offset of its standard rear wheel; half the 325i Sport Wagon's 1,483 mm ([BMW USA](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41437)) plus a 47 mm offset gives the same. The front hub face is half the M3's 1,508 mm front track plus its 47 mm offset ([Motorsport Australia](https://motorsport.org.au/wpblob0fe832abcb/wp-content/uploads/docs/default-source/sporting-technical/group-3e/3-18-007-bmw-e46-m3.pdf)). Offset (ET) is the distance from the rim's centerline to its mounting face, positive when the face sits outboard of the centerline ([Method Race Wheels](https://www.methodracewheels.com/pages/what-is-offset)).

## Tire load check

Check that each axle's two tires can carry that axle's rated load. Type each tire's load index (the number after the size: the 91 in 205/55R16 91V, [Continental](https://www.continental-tires.com/tire-knowledge/load-index--li-/)) and tick XL if the tire is marked XL, Reinforced or Extra Load. Then type the gross axle weight ratings (GAWR) from your Touring's door-jamb sticker.

<div class="calc" id="calc-load">
<p class="calc-nojs">This calculator needs JavaScript.</p>
<form class="calc-form" autocomplete="off" novalidate>
<fieldset class="calc-group calc-choice">
<legend>Axle ratings in</legend>
<div class="calc-options">
<label><input type="radio" name="l-unit" value="kg" checked> kg</label>
<label><input type="radio" name="l-unit" value="lb"> lb</label>
</div>
</fieldset>
<div class="calc-cols">
<div class="calc-panel" id="l-front">
<fieldset class="calc-group">
<legend class="calc-panel-title">Front axle</legend>
<div class="calc-fields">
<div class="calc-field">
<label for="l-f-li">Tire load index</label>
<input id="l-f-li" type="number" inputmode="numeric" min="75" max="130" step="1" aria-describedby="l-f-li-err">
<span class="calc-error" id="l-f-li-err"></span>
</div>
<div class="calc-field">
<label for="l-f-gawr">Front GAWR (<span class="calc-unit">kg</span>)</label>
<input id="l-f-gawr" type="number" inputmode="numeric" min="0" step="1" aria-describedby="l-f-gawr-err">
<span class="calc-error" id="l-f-gawr-err"></span>
</div>
</div>
<div class="calc-check"><input id="l-f-xl" type="checkbox"><label for="l-f-xl">XL (reinforced) tire</label></div>
</fieldset>
<p class="calc-out"><output id="l-f-out" for="l-f-li l-f-xl l-f-gawr" aria-live="polite"></output></p>
</div>
<div class="calc-panel" id="l-rear">
<fieldset class="calc-group">
<legend class="calc-panel-title">Rear axle</legend>
<div class="calc-fields">
<div class="calc-field">
<label for="l-r-li">Tire load index</label>
<input id="l-r-li" type="number" inputmode="numeric" min="75" max="130" step="1" aria-describedby="l-r-li-err">
<span class="calc-error" id="l-r-li-err"></span>
</div>
<div class="calc-field">
<label for="l-r-gawr">Rear GAWR (<span class="calc-unit">kg</span>)</label>
<input id="l-r-gawr" type="number" inputmode="numeric" min="0" step="1" aria-describedby="l-r-gawr-err">
<span class="calc-error" id="l-r-gawr-err"></span>
</div>
</div>
<div class="calc-check"><input id="l-r-xl" type="checkbox"><label for="l-r-xl">XL (reinforced) tire</label></div>
</fieldset>
<p class="calc-out"><output id="l-r-out" for="l-r-li l-r-xl l-r-gawr" aria-live="polite"></output></p>
</div>
</div>
</form>
</div>

> [!WARNING]
> A tire carries its maximum load only at the inflation pressure its maker specifies for that load ([Continental](https://www.continental-tires.com/tire-knowledge/load-index--li-/)). XL (reinforced) tires reach theirs only at a higher reference pressure, about 0.4 bar above a standard tire ([Continental](https://www.continental-tires.com/tire-knowledge/reinforced-tires/)). A pass here doesn't mean your pressures are right: check the tire maker's load and inflation table for your size, and the pressures on your door placard.

**Where the numbers come from:** the load-index table is Pirelli's, in [kilograms](https://www.pirelli.com/tyres/en-gb/car/driving-and-tyre-tips/how-to-read/tyre-load-index) and [pounds](https://www.pirelli.com/tires/en-us/car/driving-and-tire-tips/how-to-read/tire-load-index), for load indexes 75 to 130. It matches [Hankook's table](https://www.hankooktire.com/uk/en/help-support/tire-guide/load-speed.html) up to 100, the end of Hankook's chart. Nothing about your car is built in: the axle ratings and load indexes are the ones you type.
