# NCM-Z-01 v0.1 — GPT scientific review

**Disposition: accepted as a completed bounded retained-observation study. No blocking scientific or software correction identified.**

Review date: 31 October 2026. This review concerns the supplied NCM-Z-01 report, calculations, figures, and archive. It is not publication approval, a native trajectory certification, a Windows certification, or a new motion experiment.

## 1. Controlling material and intake

Reviewed archive: `NCM_Z_01_v0.1_REVIEW.zip`.

SHA-256: `92f9b1ab59d60333470956d49681849939e6def28d8bc84d976261f045f28a2e`.

The archive has 74 file members: 73 payload files listed in `OUTPUT_HASHES.json`, plus that manifest itself. All 73 listed sizes/hashes match and membership is exact. The separate report, START_HERE, top figure, original work order, original task packet, and earlier `interactive.motion.json` match their corresponding archive copies byte-for-byte. The 11 source snapshots match the source manifest. These checks establish consistency with the supplied evidence, not authentication of the original producer.

The separately attached side figure is a lower-resolution copy (2048 x 1170); the manifest-bound original is 2520 x 1440. They are not byte- or decoded-pixel-identical. Their displayed content is visually consistent. This review uses the original figure in the verified ZIP, not the attachment as an identity substitute.

The historical/current `_records.py` difference was disclosed and properly separated from actual data integrity. A source file named by a historical producer does not have to equal a later checkout's serialization helper. The required parent bytes, canonical and deterministic digests, native states/indices, and relevant observer/native formula identities are checked. The initially overstrict gate and its correction remain in the submitted record. I found no scientific-data mismatch waived by that correction.

## 2. Scientific scope

The subject is the existing **staged** Z readout and its already-declared placement, evaluated at two retained native states (indices 0 and 1). Frozen means the observer angle and envelope time both remain at their first-sample settings; it does not mean the native state remains unchanged.

The source geometry remains stationary. The primary comparison is PLUS tau=0; PLUS tau=h and MINUS tau=h are separate static sensitivity references, not frames in a motion. The original close sphere is a geometric reference, not a wall, energy detector or demonstrated core interior. Central openings are broken two-segment arcs; finite host-notch triangles are separate measurement regions.

Neither the submitted investigation nor this review evaluates native F or updates EMA memory. The retained-state linkage is checked, but the claim that these are consecutive native outputs is inherited from the admitted record; it is not freshly certified by executing F.

Source locations: REPORT, “Typed map”, “Reproduction and numeric meaning”, “Six finite central opening boundaries”, and “Limits, verdict and stop”; `source_snapshots/observer.py`, `z.py`, `central.tex` and `host.tex` were read as text, not executed as project modules.

## 3. Principal findings retained

Lengths below use the host's width as unit. The position angles are measured from the fixed center; they are not angles between consecutive displacement vectors.

| Point | Native index; observer | Center radius | Azimuth | Nearest opening boundary | Distance to that boundary |
|---|---|---:|---:|---|---:|
| S0 = F0 | 0; initial settings | 0.318787828 | 9.648620286 deg | G+0 | 0.080823611 |
| F1 | 1; frozen settings | 0.162943001 | 2.061171441 deg | G+0 | 0.115853365 |
| S1 | 1; scheduled settings | 0.141756790 | 30.874449136 deg | G+1 | 0.161455173 |

Thus an inward endpoint change survives freezing the observer. The observer schedule additionally changes the point and its nearest-opening label. This is not merely rotating the camera: the observer formulas change the computed point in the same spatial frame.

All four labeled point evaluations are above the center and inside the original reference sphere. None is on a central boundary arc or finite host notch patch, and none of the outward rays from the center through the evaluated points hits a finite notch triangle. These facts concern the supplied endpoints; they establish neither a continuous trajectory nor aperture passage. Since the opening interior is not an admitted filled domain, missing its boundary does not exclude passage through an undefined interior.

There are only three distinct evaluated placements because S0=F0. There are only two native states: F1 and S1 do not constitute two successive native updates.

An instructive numerical distinction: the initial point is closer to its nearest boundary (0.080824) than either final evaluation is (0.115853 frozen; 0.161455 scheduled). Moving closer to the center is not the same as moving closer to an opening boundary. “Nearest” is a relative classification, not a claim of attraction, flow, intensity or physical coupling.

At S1, G+1 is only approximately 0.002206213 width units nearer than G+0. This is well outside the stated numerical tie tolerance, but it remains a small geometric classification difference rather than evidence of strong activation toward G+1.

## 4. Attribution and observer controls

The ordered native -> envelope -> clock telescope is algebraically valid. It is formed by inserting the already-defined intermediate observations. The native term contains both the norm-dependent macro change and the chiral contribution; these are not independent physical sources.

The submitted component norms are approximately 0.157094883 (native), 0.008169853 (envelope), 0.049721906 (clock), and 0.184296146 (total). These norms are **not additive percentages**. The vector identity is what is exact. A different ordering redistributes mixed changes; this is not a uniquely causal force decomposition.

The controlled centered-direction comparisons are about 4.973766 degrees for the native-state change at frozen settings, 0.222623 degrees for envelope-only change, and 18.640689 degrees for clock-only change in the stated order. These angles must not be added as a rotation budget or assigned physical angular velocities.

### Reviewer clarification using retained intermediate values only

The report already stores the four intermediate observations used by the telescope. I evaluated their distances against the same six fixed arcs, without creating any native state or adding any clock sample:

| Accounting stage | State | Observer angle | Envelope time | Nearest arc | Distance |
|---|---:|---:|---:|---|---:|
| Initial | 0 | 0 | 0 | G+0 | 0.080823611 |
| Native-state replacement | 1 | 0 | 0 | G+0 | 0.115853365 |
| Envelope replacement | 1 | 0 | 0.1 | G+0 | 0.121209612 |
| Clock replacement | 1 | pi/6 | 0.1 | G+1 | 0.161455173 |

In this **ordered accounting**, the label changes at the clock replacement, not at the native or envelope replacement. That is a statement about these existing counterfactual endpoint evaluations, not a traced temporal crossing. It does not exclude observer/native interaction in other states or another ordering.

A conditional geometric check also explains the final comparison: when both nearest points are the upper ring elbows, their squared-distance difference is `a*(sqrt(3)*x - 3*y)`. This condition holds for both endpoints of the clock-only comparison, but not for every earlier evaluation or nonwinning arc. It is not a global azimuth-to-nearest-gap rule. The direct finite-segment calculation remains controlling.

## 5. Two corollaries

**Common-phase non-identifiability through frozen staged Z.** A common phase rotates the real/imaginary channel vectors by a real 2D rotation, preserving their cross product and the state norm. With observer settings and placement fixed, Z and its placed point therefore remain identical. Any deterministic measurement of that same point against fixed geometry is identical too. The face decoder can still change. This proves a limitation of this observation, not a global equivariance theorem for the native map on its zero stratum, and not a native temporal trajectory inferred from a display probe. EMA is a distinct observer and is not covered by a blanket phase-invariance assertion.

**Envelope-only direction change.** For fixed native state and observer angle, `Z(E)=A*E*H+b*C` gives

`Z(E1) cross Z(E2) = A*b*(E1-E2)*(H cross C)`.

With nonzero prefactor and nonzero `H cross C`, the two full readouts are nonzero and nonparallel. A fixed isotropic nonzero placement scale/rotation preserves that distinction. A decaying macro weight therefore need not be a purely radial rescaling of the blended observation. The stored state-1 comparison is a numerical illustration, not a universal calibration.

Both are elementary consequences of existing definitions. The report appropriately makes no foundational novelty claim.

## 6. Verification actually performed here

1. Read the work order, report, summary, source snapshots and standalone calculation code. Inspected both original archived PNGs visually. No PDF was involved in this task.
2. Verified all 73 manifest-listed payload files and the exact 74-member archive membership; compared the independent attachments and all 11 source snapshots.
3. Ran the unchanged `checks.py --portable` in a separate sandbox copy. **186/186 assertions passed.** Native F and EMA updates: zero. The portable mode checks the 11 packaged source snapshots, not the 17 original Windows files.
4. Compared submitted and replayed numerical ledgers. They are **not byte-identical across these environments**. OBSERVATIONS has 244 differing float leaves, maximum absolute difference 1.7763568394002505e-15 (an angle in degrees). GAP_COMPARISON has 310 differing float leaves, maximum absolute difference 1.2789769243681803e-13 (a non-hitting carrier-ray parameter around 59). All nonnumeric fields, gap labels, point/ray incidence decisions, ties and zero-direction flags match. These observed differences are consistent with last-place arithmetic variation; they are not formal error enclosures.
5. Independently reconstructed the geometry with exact radical directions evaluated at 80 decimal digits. At the retained binary64 point values, all 72 arc distances and 24 point/patch plus 24 ray/patch decisions agree. Maximum distance discrepancy is approximately 7.10e-17 width units; maximum notch-plane-distance discrepancy is 1.33e-16. This is high-precision diagnostic agreement, not interval certification.
6. Ran **39 independent review check groups**, including symbolic common-phase norm/area identities, the envelope cross identity, finite geometry classifications, and the intermediate-value clarification. All final groups passed. Counts are implementation checks, not theorem counts.
7. Checked consistency of the submitted 17-file before/after preservation record. Original Windows files and the original producer process were not accessible here. No whole-checkout audit, live Windows validation or producer authentication is claimed.

Replay environment: Linux, Python 3.13.5, mpmath 1.3.0, Matplotlib 3.10.8; the supplied Windows study used Python 3.11.15 and Matplotlib 3.10.9. Figures regenerated in the replay copy are not replacements for the manifest-bound Windows figures.

Reviewer helper corrections are retained in the evidence: an initial manifest-key assumption (`sources` versus `files`) stopped the intake helper; the attachment check exposed the lower-resolution side copy; and one optional reviewer elbow simplification was too broad when applied to the nonwinning G+1 distance at F1. The corrected independent check retains true finite-segment minima. None required a change to the submitted mathematics, data or script; none was used to waive a reported failure.

## 7. Disposition and next scientific question

Accept NCM-Z-01 as a completed two-state descriptive and interpretive study. No repair work order, new paper, application change or publication follows from this review.

This is real progress in separating internal-state-dependent observations from observer-dependent appearance. It does not establish persistent inward motion, a preferred upper side, circulation, physical velocity, energy flow, support motion or cone reorientation.

The narrowly justified next question remains: **in an independently admitted longer existing record, does an opening-proximity change persist with the staged observer angle and envelope frozen?** At least three states are needed for two displacements and their discrete turn; even three states would not establish a sustained orbit or a continuous path. First reuse an adequate existing record if one can be identified by the established source route. Do not force the result, alter the coefficients, or automatically authorize a fresh run. No successor task was executed here.
