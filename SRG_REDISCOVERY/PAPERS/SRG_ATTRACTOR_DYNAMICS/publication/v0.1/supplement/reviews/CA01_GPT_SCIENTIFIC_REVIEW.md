# CA01 — GPT scientific review

**Date:** 21 October 2026  
**Disposition:** **ACCEPTED_WITHIN_PRINTED_MAP_AND_PASSIVE_MEASUREMENT_SCOPE**  
**Required scientific revisions:** None identified.  
**Historical reproduction:** Not established for either original figure.  
**Publication:** This review does not authorize staging, committing, pushing, or publication.

## 1. What has been accepted

CA01 successfully separates three different things: a statistic computed from a prescribed field, a genuinely evolving three-component state, and a passive geometric reference used to display them.

For Figure 3, the printed detector reports the average coordinates of selected outer grid points. Its average can be central without the selected points being central. Exact symmetry gives a zero centroid when the mask is nonempty. The saved numerical controls demonstrate that floating-point thresholding can move this marker without integrating a particle trajectory. The report does not claim to have reproduced the original Figure 3 sequence.

For Figure 4, the printed toroidal remapping is an active part of the update, not merely a display transform or an idempotent projection. CA01 establishes a fixed circle for the remap-only rule and forward convergence to individual points on that circle for the printed, continuously advancing, decaying-drive schedule. The latter is a conditional theorem, not a general statement about every historical SRG implementation.

The new Tri-Octagon/crystal reference is passive throughout. Its role is to expose the distinction between coordinates, observations and evolving state. It is not treated as a physical container, a new force, or a boundary that confines the SRG state.

## 2. Exact submission and review activity

Input archive: `CA01_GPT_REVIEW.zip`  
Size: **7,630,962 bytes**  
SHA-256: `f44ecb11036f72971048c7d6c268233f43b36c06bb1a1204dc1896c6bcd2d8a0`

The archive contains 90 files: 89 manifested payloads plus `MANIFEST.json`. CRC, member-name safety, uniqueness, payload size, SHA-256 and manifest completeness checks passed. All 27 consumed-source snapshots match the registry. The separate uploaded summary, historical PDF and work order match the corresponding bundle bytes.

I read the analysis, execution plan, claim/source map, review guide, execution receipt, numerical records, and relevant source snapshots. I inspected the check and observer code without launching the historical scripts or the fresh-rollout script. The historical PDF was freshly rendered at physical pages 5–8; both methods and both original figure images were inspected. All five delivered explanatory images were also visually inspected.

Independent saved-evidence checks covered:

| Evidence | Independent review coverage |
|---|---:|
| Manifested payloads | 89 |
| Consumed-source snapshots | 27 |
| Saved Figure 3 detector cases | 16 |
| Saved Figure 4 isolated fixtures | 12 |
| Saved Figure 4 successor transitions | 200 |
| Saved Figure 4 states used for passive-frame checks | 201 |
| New trajectories / rollout updates | 0 / 0 |
| New grid-field experiments | 0 |
| Native-kernel or SIM01 updates | 0 |

The independent script evaluates definitions on saved inputs; it does not feed a newly calculated output into another evolution step. Supporting symbolic identities supplement a written proof review; they are not proof-assistant certification. The 374 Boolean checks recorded in the JSON include integrity and record-consistency tests, not 374 distinct mathematical theorems. The script was run twice, with the second run checking its configurable command-line version; record counts above are unique coverage, not cumulative computation counts.

Reviewer environment: Python 3.13.5, NumPy 2.3.5, SymPy 1.14.0. This is not the author's Windows `torment` environment. No dependency was installed.

## 3. Figure 3: accepted mathematical reading

The printed field has exact magnitude

\[
M(X,Y,t)=\frac{|H(t)|}{1+X^2+Y^2},\qquad
M_{\rm clip}=\min(M,1).
\]

The angular modulation cancels from this magnitude. Away from the zero-drive and clipping degeneracies, smaller magnitudes occur farther from the origin, not in a quiet central core. The origin is absent from the even 100-by-100 grid; the odd-grid diagnostic explicitly states its angular convention at the origin.

On an exactly inversion-paired grid, the strict percentile mask contains each selected point together with its opposite. Its arithmetic centroid is therefore zero whenever it exists. This is a statement about a statistic, not about a point moving under an attraction law. Empty masks remain undefined: a zero drive, or a completely saturated exact field under the printed clip, must not be assigned a fictitious central centroid.

The saved grids support the stated numerical mechanism. I independently checked thresholds, strict masks, counts, means, inversion mismatches, vector-magnitude consistency and the radial magnitude identity. The epsilon-clip cases were checked against their own definition rather than silently treated as the printed clip. The radial-control U/V arrays are documented unused placeholders, not reconstructed vector fields.

The source distinction is substantive. The surviving `attractor_trajector_over_time.py` uses one flattened `argmin`, not the paper's percentile centroid, and has a different clip. Its field is overwritten from coordinates and time; the stored detector list is not fed back. It is a related source, not a certified producer for Figure 3.

**Accepted limitation:** the controls demonstrate a mechanism capable of generating the observed scale of apparent wandering. They do not establish which exact producer, settings or runtime produced every old plotted point.

## 4. Figure 4: accepted attraction theorem

### The numerical increment is not the continuous flow

For the declared roll C(x,y,z)=(z,x,y), the torque increment and its scalar clipping remain perpendicular to the incoming state. Consequently,

\[
\|s+\Delta t\widehat q\|^2
=\|s\|^2+\Delta t^2\|\widehat q\|^2.
\]

The finite Euler increment grows squared radius when the increment is nonzero. The continuous-flow identity d||s||²/dt=0 cannot be substituted for this numerical-step identity. The report correctly keeps the subsequent remap separate.

### The remap itself creates attraction

For off-axis input with rho=sqrt(x²+y²) and L=||s||, the printed map is

\[
P(s)=\left((1+z/(2L))x/\rho,
(1+z/(2L))y/\rho,\rho/(2L)\right).
\]

It erases positive radial scale and maps onto the open upper half of the specified torus; the closed half-torus is its closure. Axis/origin conventions are explicitly excluded from the smooth off-axis definition or declared separately in fixtures.

Repeated application is not inert. In particular,

\[
P(1,0,0)=(1,0,1/2),\quad
P^2(1,0,0)=(1+1/(2\sqrt5),0,1/\sqrt5).
\]

On the torus, the poloidal-angle recurrence is

\[
g(\theta)=\operatorname{atan2}(1+\tfrac12\cos\theta,
\tfrac12\sin\theta).
\]

It sends [0,pi] into [pi/3,pi/2]. On [0,pi/2],

\[
g'(\theta)=-\frac{1/4+(1/2)\cos\theta}{5/4+\cos\theta},
\qquad |g'|\le 1/3.
\]

The contraction bound and fixed-point calculation are correct. The unique fixed poloidal angle has cos(theta*)=(sqrt(3)-1)/2, giving

\[
\rho_*=(3+\sqrt3)/4,\qquad
z_*={1\over2}\sqrt{\sqrt3/2},
\]

and the fixed circle

\[
\mathcal C=\{(\rho_*\cos\phi,\rho_*\sin\phi,z_*):\phi\in S^1\}.
\]

This is a circle of possible resting positions, not an orbit that a trajectory must traverse. Remap-only azimuth is unchanged. The local multipliers 0, sqrt(3)-2 and 1 correctly distinguish erased radial scale, contracting/alternating meridional behavior, and neutral azimuth.

### Why the decaying drive does not destroy the endpoint result

The theorem assumes exact arithmetic, fixed finite alpha, the printed update order and constants, an admissible first remap, and t_n=0.1n without resets.

After the first remap, the state is bounded with horizontal radius at least 0.5 and norm at most 1.5. Clipping bounds the pre-remap increment by 0.08. Hence its whole straight increment segment stays at horizontal radius at least 0.42. The report's polar- and azimuth-angle perturbation bounds follow on this nonsingular region.

The four exponentially decaying envelopes in H make the increments summable. The stated height bound makes the poloidal parameter enter the contraction interval after finitely many steps. A contraction with vanishing perturbations gives theta_n -> theta*. Summability of the lifted azimuth increments gives a finite limiting azimuth. These arguments establish convergence of the whole state to one point of C.

The stronger endpoint-family statement also checks out: on any initial torus latitude circle, finite-time azimuth lifts have degree one, and the uniform summable tail gives a continuous limiting degree-one map. The possible limiting endpoints cover C; the theorem does not select one universal endpoint for all starts.

C need not be invariant at each finite-time driven step. It is the fixed set of the limiting remap and the family of possible asymptotic endpoints. The report states this distinction correctly. A persistent nonzero triangular cycle is excluded under these assumptions, not under every possible clock or every historical program sharing the same operator names.

### Saved evidence

The independent closed-form remap check on saved inputs has maximum residual 2.22e-16. The independently grouped Euler-identity residual is at most 2.75e-16; componentwise torque checks agree exactly in these fixtures. These are well below the predeclared 1e-12 tolerance.

The only trajectory is the declared alpha=0, s0=(1,0,0), 200-update control. Its initial zigzag and settling are consistent with the contraction theorem. No driven historical replay or nearby-start experiment is claimed.

The supplied endpoint distance is zero in its binary64 evaluation. An independently grouped evaluation of the exact radius gives a distance approximately 2.22e-16 instead. This is ordinary final-bit rounding, not a contradiction; neither is a proof of finite-time exact arrival. The proof is the contraction/summability argument.

## 5. Passive geometry and physical interpretation

I independently reconstructed the zero-member coordinates and face list from the supplied definitions without importing the original geometry module. The saved PLUS/MINUS arrays agree. Counts are 18 vertices, 24 triangular faces, 42 edges and two open six-edge boundary cycles. Host arrays and their recorded source identities agree with the bundled references. This checks the representation used here; it is not a new full audit of the accepted crystal family.

The observer is the fixed translation y=O+s with O=(0,sqrt(3)/6,0), unit scale and no time-dependent normalization. Pairwise distances survive the translation and the separate rigid-frame control. All 201 F4 control states remain outside the declared central display window; none has been hidden or rescaled into the central region.

That outside-window fact is **not** a rejection of the author's analytical framework. The unit correspondence is an illustrative convention, not a recovered physical calibration. Nor is it a reason to force a fit. CA01 appropriately leaves an SRG-to-Z mapping and any further observer construction unestablished.

The old TGMO remap is active dynamics; the new Tri-Octagon/crystal reference is passive measurement. These two roles of geometry must remain distinct.

No supported identification with heat, magnetism or light has been obtained. This does not prove that a physical interpretation is impossible. It means the supplied variables and operations have not supplied that identification.

## 6. Preservation and limits of this review

All bundled consumed snapshots match their recorded identities. The before/after preservation records agree for 27 sources. The supplied starting/ending status files are byte-identical, and both index-diff records are empty. All input payload hashes remained unchanged during this review.

I did not access the author's Windows filesystem or Git remote. Thus these findings verify supplied preservation evidence, not direct independent observation of every local file or Git action. I did not repeat the historical source search; its bounded negative result remains Codex's documented search evidence, not proof of global absence.

The five new images are legible and distinguish controls from historical figures. The historical captions should not be silently rewritten. CA01's separate source-linked analysis is the appropriate place for these corrections and newly proved statements.

## 7. Corrections to GPT's earlier conversational account

The suggestion that Figure 3 could locate a quiet central neighborhood was not supported. The selected low-magnitude sites are peripheral; the central marker is their average. CA01 corrects that interpretation.

The earlier continuous cross-product discussion was valid only for the isolated continuous torque law. For the printed discrete implementation, the Euler radius increment and the active remap are essential. CA01 correctly supplies both.

## 8. Scientific closeout

No scientific repair is required for acceptance within the declared scope. No new simulation is required to substantiate the accepted conclusions. Missing producer inputs continue to limit exact historical replay, not the validity of the conditional printed-map theorem.

A useful subsequent question, under a separate work order, would be which initial-state information survives in the limiting azimuth and how a passive geometric observer makes that relation visible. This is a proposal, not an executed experiment or a publication authorization.

## Review files and reproducibility

`CA01_INDEPENDENT_RESULTS.json` records the independent checks. `review_ca01.py` performs only saved-record, integrity, symbolic-identity and reference-geometry checks. Example Windows CMD invocation after extracting the submission and reviewer packages:

```bat
call conda activate torment
python -B review_ca01.py --input-dir "C:\path\to\extracted_CA01" --archive "C:\path\to\CA01_GPT_REVIEW.zip" --output-dir "C:\path\to\new_review_output"
```

The optional `--attachments-dir` adds comparisons against separate copies of `READ_ME_FIRST.md`, `SGR_simulations.pdf` and `SRG_CA01_CODEX_WORK_ORDER.md`. The checker does not need GitHub, a kernel import, or an original-source execution. Do not rerun `run_checks.py` to review the saved submission.

**Principal submission sources:** `CA01_ANALYSIS.md` §§1–7; `READ_ME_FIRST.md`; `SOURCE_AND_CLAIM_MAP.md`; `ALGEBRA_AND_CHECK_PLAN.md`; `RESULTS.json`; `raw/*.npz`; `evidence/geometry_reference.npz`; `evidence/consumed_sources.json`; `PRESERVATION.json`; the source snapshots identified in the claim map; and historical PDF physical pp.5–8.
