# Requests from the readme-back integrator

Mismatches between the README Appendix (the reference tables) and other integrators' sets, found on 22 October 2026 after the writer requests and gap-fill batches 1–2 were applied. Everything else checked (strut-top 34 Nm, inner tie rod 110 Nm, 420G about 1.8 L, coolant 9.3 L, DOT 4 low-viscosity, ATF, A/C charge) already matches in JOB-CARDS, WORKSHEETS and the README phases.

### R1: WIRING-AND-CODING 0540__session-7-steering-angle-after-the-alignment.md: the alignment load (duplicate of integrator-readme-plan R1: apply theirs)
- **Change:** replace
- **Find (exact current text):**
  > after the wheel alignment, done unladen with a full tank ([Wheel alignment](README.md#wheel-alignment))
- **New text:**
  > after the wheel alignment, done in BMW's design position with the M3's load ([Wheel alignment](README.md#wheel-alignment))
- **Why:** gap-fill batch 2 (TIS 32 00 150/155, normal position E46 / M3): BMW aligns M models and accident-repaired cars only in design position, loaded; README Wheel alignment, 0520 and the torque table now say so.

### R2: README 0470__exhaust-and-the-spare-wheel-well.md: the donor exhaust record's load (duplicate of integrator-readme-plan R2: apply theirs)
- **Change:** replace
- **Find (exact current text):**
  > 2. **On level ground at ride height,** unladen, at placard tire pressures:
- **New text:**
  > 2. **On level ground at ride height,** loaded to the M3's normal position as for its ride-height check ([Ride height: BMW's method and figures](#ride-height-bmws-method-and-figures)), at placard tire pressures:
- **Why:** 0520 now measures the donor loaded to the M3's normal position in Phase 1; record the exhaust at the same load so the two sets of readings match. Optional if you prefer to keep the record unladen, but then say so in 0520's Phase 1 step.

### R3: README 0510__driveline-and-rear-axle.md: 420G oil, decided
- **Change:** replace
- **Find (exact current text):**
  > BMW's 2003 US M3 owner's manuals give about 1.8 L (1.9 US qt) and ST041 prints 1.9 L, so buy 2 L
- **New text:**
  > BMW's US M3 owner's manuals give about 1.8 L (1.9 US qt), and ST041's "1.9 L" matches the quart figure (our inference), so buy 2 L
- **Why:** gap-fill batch 1 (four editions of the US M3 manual); the Appendix Fluids table, Card 9b and the Fluids log now give about 1.8 L.

### R4 (note only): WIRING-AND-CODING 0530__session-6-first-start-adaptations-and-throttle-check.md: source for the cam ranges
- **Change:** none required; check the citation
- **Find (exact current text):**
  > BMW gives the adjustment ranges: 60° on the intake camshaft, 45° on the exhaust ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/2%20M3%20DriveLine.pdf)).
- **New text (if the coding-power notes are right):**
  > BMW gives the adjustment ranges: 60° on the intake camshaft, 45° on the exhaust ([BMW S54 module](https://www.billswebspace.com/MS54B32TrainingModule.pdf)).
- **Why:** `coding_powertrain_chassis.md` (Q3 and correction 7) names the BMW S54 training module as the page it read for 60°/45°; the Key numbers VANOS row cites that module.
