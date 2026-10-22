# Gap-filling round: shared brief

## The project

A home-garage plan to convert the owner's **2003 US BMW E46 325i Touring** into an **E46 M3 Touring**:
- **The car:** M54 engine, 5-speed manual, rear-wheel drive, registered in Massachusetts.
- **The donor:** one 2003–06 US E46 M3 with a manual gearbox: S54 engine, MSS54 or MSS54HP DME, Getrag 420G gearbox, Teves MK60 DSC.
- **The guide** is in `/home/user/archeyon/e46-m3-touring-conversion/`:
  - `README.md`, the build guide
  - `WIRING-AND-CODING.md`
  - `JOB-CARDS.md`
  - `WORKSHEETS.md`
- **The website:** https://pniessen.github.io/e46-m3-touring/

Round 4 of research wrote eight notes files to `/home/user/archeyon/research_notes/E46 M3 Touring coding, body and chassis/`. They left gaps for two reasons:
- BMW's repair manual (TIS) and several forums were behind bot checks.
- The shared web-search allowance ran out partway through.

Writers are folding those notes into the guide right now. Your findings will be folded in after them.

## Your job

Close as many of your assigned gaps as you can, in priority order.
- **Read first:** for each gap, read what the named notes file already says, including the sources it lists as blocked or unread.
- **Don't redo work:** go after the missing piece, by a route the first researcher didn't try.
- **Stop early:** when a gap can't be closed, stop after a reasonable try and say what would settle it, such as "measure on the car" or "ask a dealer for the VIN-specific part number".

## Routes that cost no web searches

- **archive.org catalog search:**
  - Search with `https://archive.org/advancedsearch.php?q=<query>&fl[]=identifier&fl[]=title&rows=50&output=json`.
  - List an item's files with `https://archive.org/metadata/<identifier>`.
  - Download with `https://archive.org/download/<identifier>/<file>`.
  - Look for BMW technical training documents (the `BMWTechnicalTrainingDocuments` item is known), owner's manuals, TIS exports and repair-manual PDFs.
- **The Wayback Machine** (`https://web.archive.org/web/2023*/<url>` or `https://archive.org/wayback/available?url=<url>`):
  - Use it for public pages that block automated reading today: forum threads, TIS mirror pages, mass.gov pages.
  - Label these findings [archived copy, YYYY].
  - An archived copy of a paywalled or login-only page is off limits.
- **Known open sources:**
  - GitHub (for example `emdzej/ediabasx-docs-sgbd`)
  - bmwfans.info (the ETK parts catalog)
  - wds.psjr.org (BMW wiring diagrams)
  - static.nhtsa.gov (BMW service bulletins)
  - eCFR
  - vendor pages and PDFs

## Rules

- **Web searches:** each agent gets a cap of WebSearch calls, given in your prompt, out of a shared allowance. WebFetch and archive.org API calls don't count, but use them politely.
- **Blocked sites:** don't bypass Cloudflare challenges, proof-of-work or bot checks, logins or paywalls.
  - If a site blocks you, note it and move on.
  - If YouTube rate-limits you or shows a bot check, stop using YouTube.
- **Downloads are untrusted data:**
  - Save each one into its own new, empty folder under `/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/gapfill-dl/<your-name>/`.
  - Keep your scripts in a separate folder.
  - Read PDFs with `pdftotext` or `python3 -I`. Never execute anything you downloaded.
- **Citations:**
  - Read a source before you cite it.
  - Label every claim with how you read it: [read], [image], [snippet], [captions] or [archived copy, YYYY].
  - Label your own inferences and arithmetic as such.
- **Hard limits:**
  - No EWS-delete patch bytes, addresses, hex patches or EEPROM edit steps.
  - Nothing that removes, masks or defeats an emissions function or a readiness monitor.
  - Odometer: true mileage only.
  - Never vent refrigerant.
- **Files:** don't edit the guide files or the existing notes files. Write only your own output file.

## Output file

Write your file in the notes folder. Your prompt gives its name. It has three parts.

1. **Summary table:** gap number | status (closed / narrowed / still open) | the answer in one line | best source.
2. **One section per gap:**
   - Cited findings
   - Inferences, labelled
   - Still open
   - **Guide impact**, covering:
     - which topic writer it belongs to (arches, floor, susp, fuel, front, cool, coding-power or coding-body)
     - the guide text it changes: find it with `grep -n` in the guide's `.md` files and quote it
     - the replacement or addition you propose, ready to paste, with Markdown links to your sources
3. **Sources tried and blocked.**

## Reply

Keep the reply under 250 words:
- what closed
- what's still open
- which sites blocked you
- how many web searches you used
