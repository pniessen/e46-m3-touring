# Requests from the readme-plan integrator (README 0000–0290)

Three value mismatches between my set and other integrators' sets, found after both gap-fill batches. My set now uses BMW TIS (issue 12/2007): the M3's normal position is loaded (a full tank, 68 kg on each front seat, 14 kg in the trunk), M models are aligned only in design position, and body control dimensions are in TIS group 41 00. Phase 1, Phase 12, "Suspension for Touring weight" and "Wheel alignment" already agree; these three lines don't yet. No change is needed in the reserved 325xi fragment.

### R1: WIRING-AND-CODING 0540__session-7-steering-angle-after-the-alignment.md: "When" line, the alignment condition
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > **When:** after the wheel alignment, done unladen with a full tank ([Wheel alignment](README.md#wheel-alignment)), and after any later steering or suspension work.
- **New text:**
  > **When:** after the wheel alignment, done in BMW's design position at the M3's normal-position load ([Wheel alignment](README.md#wheel-alignment)), and after any later steering or suspension work.
- **Why:** TIS 32 00 defines the M3's normal position as loaded, and TIS 32 00 150 allows only the design-position method for M models; README "Wheel alignment" and my Shop briefs row now say so (gapfill_bmw_chassis_body.md, Gaps 1 and 2).

### R2: README 0470__exhaust-and-the-spare-wheel-well.md: the donor exhaust record's load
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > 2. **On level ground at ride height,** unladen, at placard tire pressures:
- **New text:**
  > 2. **On level ground at ride height,** loaded to BMW's normal position for an M3 (a full tank, 68 kg (150 lb) on each front seat and 14 kg (31 lb) in the middle of the trunk), at placard tire pressures:
- **Why:** matches Phase 1's donor measurement and my Choose the donor Measurements row, which both use TIS's loaded normal position (gapfill_bmw_chassis_body.md, Gap 1).

### R3: README 0480__welding-settings-and-safety.md: the TIS group for body dimensions
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > BMW's body dimensions are in TIS group 51 00.
- **New text:**
  > BMW's body control dimensions are in TIS group 41 00, not 51 00 ([TIS top view](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/10_ra__frame_alignment_control_dimensions_body_top_view_bmw_e_46_4-door___2-door___t/)).
- **Why:** my Factory documentation row now says group 41 00 (gapfill_bmw_chassis_body.md, Gap 6, Guide impact 1, which also offers a fuller paragraph with the rear control dimensions for this spot).
