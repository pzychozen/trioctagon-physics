# Time, switching, movement and energy

The exact recurrence and source locations are in [CONSTRUCTION.md](CONSTRUCTION.md). This document separates source-derived facts from measurements of the two original logs.

## Frame time and callback history

The source computes t=0.1*frame on every call (plot_1.py:102). It never increments an elapsed-time variable. Its nominal labels are 0–199, so a fresh label pass evaluates H from t=0 to 19.9. The 50 ms display interval and 20 fps movie rate are both nominally 20 images per second. They do not measure the duration of a numerical update, console output or rendering.

Both saved logs contain a singleton label 0 followed by 0–199, then another singleton zero followed by another pass. The longer record contains five complete such passes and a final 0–85 pass; the shorter contains two complete passes and a final 0–36 pass. Their exact callback ranges are tabulated in ORIGINAL_LOG_ANALYSIS.md.

The 1,092 and 440 recorded updates correspond to 109.2 and 44.0 model-step units if one merely counts a fixed 0.1 per logged callback. The spans between the first and last stored states are 109.1 and 43.9 by that accounting. Neither number is a variable the code passes to H, and neither is wall-clock time. The logs have no per-row timestamp.

Local Matplotlib 3.10.9 source inspection establishes the following implementation paths:

- Integer frames produce range(frames): animation.py:1704–1706.
- With no init_func, an initialization draw calls the update on the first frame: 1761–1782.
- Saving initializes and then draws the saved frame sequence: 1120–1138.
- Interactive start initializes: 916–933.
- TimedAnimation defaults to repeat=True, and repeat initializes and restarts the frame sequence: 1442–1469.

The excerpts and hash are included in inspection/matplotlib_callback_excerpts.txt and analysis/independent_checks.json. plot_1.py requests blit=False, so the additional blit-setup path discussed for Simulation 02 is not requested here.

The observed row order is consistent with save/init/display/repeat behavior. The exact historical backend, dependency version and GUI event trace are missing. In particular, the logs alone do not prove which repeated pass was caused by saving, interactive playback, a restart or another draw event. The actual recorded labels and continuing states are preserved without assigning invented GUI events.

## The switch acts on a contribution, not on carried velocity

Source rule: if g>0.5 and a fresh draw is <0.01, b becomes 1−b. Its new value multiplies the force by (1−2b). Conditional on the intended uniform generator and an open gate, the toggle probability is 1% per body per callback. The random values and RNG state are not logged.

All observed callbacks have g>0.5: ranges are 0.633309–0.987992 in A and 0.641949–0.987362 in B. The gate therefore never closes in these records. The logs show 79 and 33 between-block toggles, with none contradicting gate eligibility. These counts cannot recover the missing random draws or certify their distribution.

For H>0, mode 0 adds a contribution toward the chosen wrapped centroid displacement and mode 1 adds the opposite. When H<0 those roles reverse. Red therefore does not mean permanently repulsive. A mode can persist while the sign of H changes, and H can restart while the mode persists.

In B, body 5 switches 0→1 at q=7, Step=6 (CSV line 63). H remains positive in the following window:

| Callback q | Source line | Mode | Speed | Outgoing velocity along the current centroid direction |
|---:|---:|---:|---:|---:|
| 6 | 55 | 0 | 0.570163 | +0.565607 |
| 7 | 63 | 1 | 0.291844 | +0.284300 |
| 8 | 71 | 1 | 0.087759 | +0.062268 |
| 9 | 79 | 1 | 0.141476 | −0.131445 |

The last column is the dot product with the unit wrapped displacement evaluated at that body's update, using the observed mixed old/new positions. Positive means toward that instantaneous direction. The switch first slows the center; the outgoing velocity points away two callbacks later. A's first switch shows the same ordering at q=12→14 for body 4, but that observation is not a universal two-callback theorem.

Across all observed toggles, none has a negative dot product between immediately preceding and outgoing velocity. There are nevertheless 17 such obtuse turns in A and 6 in B at other callbacks. These are consecutive-vector comparisons, not a claim about all possible definitions of reversal.

## H and GRF are separate controls

H is a prescribed, signed, damped oscillatory function of the frame label. It reads no positions, velocities, mode history or saved route. Its positive starting value is 4.5; H(19.9)=0.00261412235. Its decaying envelope tends to zero only as its argument increases, not when the label is repeatedly reset.

GRF uses mean incoming speed, despite accepting unused positions and t arguments (51–54). It is computed once per callback. Faster incoming motion lowers the common response factor; slower motion raises it. It is not a per-body memory score or a direct test of positional stability.

RPCO acts componentwise after the new contribution is added. It preserves each candidate component's sign and shrinks its magnitude. It can alter direction because unequal components shrink by unequal factors. It need not reduce speed relative to the velocity before the drive, and it does not set a small nonzero velocity exactly to zero.

## Energy rises and falls for explicit reasons

Energy is K=0.5*sum|v|², with a zero potential placeholder. It is a diagnostic in the code, not an established physical conserved energy.

For the source-defined contribution a_i and candidate u_i=v_i+a_i, direct algebra gives

\[
K^+-K=\sum_i v_i\cdot a_i+\frac12\sum_i\|a_i\|^2
-\frac12\sum_i\left(\|u_i\|^2-\|R(u_i)\|^2\right).
\]

The final sum is nonnegative damping loss. The first two terms describe the change from the added drive. This is a derived bookkeeping identity for the existing recurrence; it does not introduce a position potential or field equation. The recorded states satisfy this identity on the declared transition samples to at most 6.67e-16.

At the first 199→0 reset in A (q=200→201), K changes from 0.000922772 to 0.479749699. In B it changes from 0.000721817 to 0.473368802 at the same callback indices. H changes from approximately 0.002614 to 4.5 while velocities and modes carry on. The next label 0 adds another strong-drive update. This accounts for repeated energy bursts in the recorded chronology without postulating autonomous regeneration or an unrecorded reservoir.

## Coordinate crossings and the detector

The native displacement associated with a recorded outgoing velocity is 0.1*v. In contrast, a stored coordinate change is

\[
\Delta x=0.1v^++10s,\qquad s\in\mathbb Z^3.
\]

All checkable transitions satisfy this identity. Nonzero s identifies a coordinate seam crossing. Its sign here describes the stored-coordinate shift; a negative native movement through zero gives s=+1.

The source detector instead measures |(Delta x mod 10)|. A single tiny negative component becomes almost 10. For example, A q=1 body 0 changes by (0.040328749,−0.024777022,0.022525770), with native length 0.052418691 and no seam. The detector's distance is 9.975329933, far above its threshold 1. These are recomputed source diagnostics; the original console messages were not recovered.

Of 8,728 checkable body transitions in A, 8,151 would be flagged, including 8,130 without a seam. Of 3,512 in B, 3,129 would be flagged, including 3,122 without a seam. A also has one seam the detector would miss. Thus the source detector is neither a reliable seam detector nor evidence of a native jump greater than one.

The force has its own coordinate sensitivity. It averages wrapped coordinates before wrapping the centroid displacement. One positive boundary crossing shifts that coordinate's arithmetic-centroid contribution by −10/8, plus ordinary motion. This can change later force directions. The display jump and the interaction effect must be distinguished.

B body 7 retains mode 1 throughout q=400–420. It crosses X at q=409,414,418. After q=409, its next wrapped centroid X displacement changes from about +4.92 to −3.80. VX subsequently reverses, carrying it back across the boundary. After q=414, that displacement changes back to about +4.93, and VX reverses again. These values come from observed states in analysis/episode_records.json. The later mode change at q=431 is outside this window.

No position potential, collision rule or physical boundary is needed to describe this source-supported episode. It does not establish a general periodic orbit, an asymptotic attractor or a new physical transport mechanism.
