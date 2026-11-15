# GPT scientific review — Native response asymmetry and common-phase drift

**Task:** NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01  
**Review date:** 15 November 2026  
**Author:** Hilmir Frímann Halldórsson (pzychozen)  
**Disposition:** RD01–RD05 accepted at their stated local assumptions. No mathematical correction required. Project-internal scientific acceptance only; no manuscript acceptance, author publication approval, external peer review or proof-assistant verification is implied.

## 1. Submission and accepted conclusion

The reviewed submission is `NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01_REVIEW.zip`, 464,150 bytes, SHA-256 `980cb8702ee0210c4b5054aca1a42b902cd6801cf52a370197de92e588b9ba10`.

The unchanged family is the three-channel simultaneous cubic/graph prestage followed by the simultaneous harmonic-three phase synchronizer, with epsilon=h, g=h/6, lambda=h/30 and k_i=1+xi_i, sum xi_i=0. The positive step range is 0<h<=1/4. At h=0 the specific divided equations select analytic/generator extensions; the discrete map itself is the identity.

On one sufficiently small permutation-invariant coefficient neighborhood, valid for every h in [0,1/4], the assigned in-phase response diagnostic and the two D1 rates satisfy

\[
\overline{\mathcal C}=\mathcal A S_C,\qquad
\nu_+=\mathcal A S_D,\qquad
\nu_-=-\mathcal A S_D,\qquad S_C,S_D>0,
\]

where A=(xi0-xi1)(xi1-xi2)(xi2-xi0). The factors are symmetric and jointly real analytic. Their common local zero set is precisely the union of the three equal-coefficient sets. The positive analytic ratio Theta=S_D/S_C extends through those sets. Only its leading value c_+(h)/a_C(h) is explicitly evaluated, not its entire coefficient dependence.

The actual full state remains necessary: the same ordered coefficients and the same diagnostic **evaluated at the aligned state** accompany a stationary aligned state and two different chiral relative equilibria with opposite nonzero small phase advances. This is a comparison across different states, not nondeterminism of one full state or equality of their own local response matrices.

## 2. Review by claim

### RD01 — Matched domains

Accepted. Dividing the positive fixed equation by h produces an h-independent equation E(r,xi)=0, with derivative -2I+L3/6. Its eigenvalues -2,-5/2,-5/2 are nonzero and its zero-mean derivative is dr=(2/5) dxi. Local analytic existence and permutation equivariance follow without selecting a new equilibrium or solving a numerical fixture.

The D1 border determinant and branch theorem are inherited from the preserved D1 source (D23–D27), not re-established by the 60 checks. The report correctly supplements them with a uniform-neighborhood argument: continuity of the inverse reference border on a compact h interval, a common regular state/prestage neighborhood, a uniformly small derivative defect, and a common self-map bound. This is stronger than simply taking an unjustified minimum of independently chosen pointwise radii. Local analytic roots agree by uniqueness and extend slightly beyond the closed parameter endpoints.

The aligned and twisted reference orbits remain separate under sufficiently small perturbation. The conclusion identifies shared *parameters*, not a trajectory joining these states. The reference saddle directions remain in the full border; they are not removed by a gauge or treated as attracting directions.

### RD02 — Native response, orientation and factorization

Accepted. The response is the native ordered product

\[
J_h=(I+hL_3/10)(I+h\mathsf B_r),
\]

with off-diagonal B_ij=r_j/(6r_i). It is not the reversed product or the additive approximation. Every off-diagonal J entry contains h, making C=h^3 cyc(D_h) exact and supplying the normalized extension without evaluating 0/0.

Direct algebra and specialization of the corrected GR1 formula give the same symmetric cubic K_h and cycle factor. The useful exact identity

\[
\xi_i-\xi_j=(r_i-r_j)\left(r_i+r_j+\frac{s_1}{6r_ir_j}\right)
\]

has strictly positive parentheses on the positive branch. It supplies analytic divisibility of each radius difference and the explicit symmetric factor S_C, including at equal coefficients. The oriented increasing-pair product is -A, not A. Along (-eta,0,eta), A=2 eta^3; the factor of two is retained on both sides of the comparison.

The specialized coefficient is

\[
a_C(h)=\frac{(1-3h/10)(8-18h-3h^2)}{112500}.
\]

The D1 coefficient c_+(h)=sqrt(3)(33h^2-240h+688)/(6(1-3h)^3) is inherited unchanged from D36–D37. No new D1 jet or finite-state theorem is claimed.

### RD03 — Local zeros, signs and ratio

Accepted. Analytic division is justified before taking a ratio. On the zero-sum coefficient plane the equal-coefficient conditions are three distinct lines. Successive division of an alternating analytic function is valid: after division by one line the quotient still vanishes on the others away from their intersection, and analyticity/continuity restores the intersection. The quotient is symmetric because both numerator and A are alternating.

The uniform lower bounds a_C>=1961/72000000 and c_+>=314 sqrt(3)/3 are positive. Combined with the common analytic neighborhood, they justify one further uniform shrinking on which both full factors remain positive. This establishes complete local zero and sign statements rather than merely a leading-order suggestion.

The neighborhood radius is existential, not numerically certified. Historical finite D1 fixtures do not supply it. Theta is exactly defined by the analytic factors; the explicit expression Theta(h,0)=c_+(h)/a_C(h) is its leading coefficient-space value, not a universal conversion constant. These limitations are essential and are already correctly stated.

### RD04 — Generator versus finite step

Accepted. The in-phase generator G_r, additive step I+hG_r, and ordered native response differ by the displayed h^2 cross term. The normalized native cycle tends to cyc(G_r), whose exact value is -V_r/(900 r0 r1 r2).

For a *fixed* sufficiently small pairwise-distinct coefficient tuple, positivity makes the h^3 leading term of raw C and the h leading term of the per-update phase nonzero. At equality loci this nonzero-leading assertion does not apply. At h=0, raw C and omega vanish for all coefficient tuples; the nonzero normalized quantities describe the selected generator extension and do not make the identity map advance.

The cycle product is not a Bloch coefficient, a spectral phase, a physical current or a calibrated angular velocity. No physical interpretation follows from the numerical value of the limiting ratio.

### RD05 — What the diagnostic cannot select

Accepted with exactly the report's restriction. The assigned in-phase diagnostic is intentionally held fixed across a table containing three **different** full states. On a chosen D1 branch, nu_±=±Theta Cbar is valid. Without that choice, the same tuple permits zero and two opposite advances. The positive branch label names reference chirality, not an unconditionally positive phase rate; its sign follows A.

A sufficiently small common neighborhood also keeps the chosen unwrapped phase increments near zero, so the displayed distinction is not a branch-cut or 2pi wrapping artifact. This is a routine further shrinking available in the same proof, not a numerical radius claim.

This result does not invalidate deterministic full-state reconstruction or prove that every possible state-dependent diagnostic is insufficient. It supplies no branch-switching dynamics, attraction theorem or physical force law.

## 3. Nonduplication and inherited scope

The supplied prior-work comparison explicitly separates the older response formulas, D1 existence/coefficient and symmetry, native-potential descent, closed-coherence and phase reconstruction, update-50 capture, and M2–M3 alternating-branch connection. I inspected the main response and D1 passages and the comparison/ledger against them. The matched local comparison is supported as a distinct contribution within that bounded source set, not a worldwide novelty conclusion or an audit of the complete historical corpus.

The report's complete local comparison closes this commissioned question. It should not be recommissioned as 'discovering whether asymmetry causes phase motion'. The word causes would also exceed the cross-background theorem.

## 4. Artifact and execution review actually performed

The reviewer audit independently checked all 71 ZIP members, all 70 self-excluding manifest entries, safe case-unique paths, CRC, the external archive checksum, and equality of the extracted submission with the original bytes. Both separately uploaded final-audit JSON files are identical. Their 70 per-payload entries plus the separately recorded manifest hash account for all 71 members.

The preserved incoming packet matches the originally supplied packet byte-for-byte. Its 32 members and 31-entry manifest passed. All 18 inherited packet source copies matched, and all 29 consumed source records matched their recorded size/SHA-256. Eighteen supplied Git blob identifiers were checked against the corresponding local byte strings; this is not a fresh GitHub fetch or a new checkout audit. The five claim records and their evidence paths are present.

After inspecting the checker, I directly ran its unchanged portable `checks/exact_check.py` in the review environment with output redirected to a separate reviewer directory. No source modification or environment-guard adaptation was necessary. All 60 algebra/control predicates passed, and every check record and saved formula matched the submitted result. The replay used Linux Python 3.13.5 and SymPy 1.14.0; it is not a Windows rerun or a second independent symbolic backend. D1 numerical certificates, trajectories, branch fixtures, historical suites and repository programs were not run.

The analytic uniform-domain, divisibility and positivity arguments were reviewed as mathematical reasoning. A finite check count does not certify those arguments by itself. Historical environment, memory-monitor and repository-preservation claims remain Codex's recorded execution evidence; I cannot inspect the author's Windows machine from this artifact audit.

One reviewer-wrapper administrative assertion initially expected the external payload list itself to contain MANIFEST.json. The supplied format records that self-excluding manifest separately. The wrapper was corrected before the scientific replay; its initial version and correction note are preserved. This was not a defect in Codex's submission or mathematics. The original submission remained byte-unchanged throughout.

## 5. Carry-forward and next documentation

RD01–RD05 are accepted for a focused companion explaining the matched local correspondence and its state-selection limit. The paper must preserve the qualitative radius, the positive-label convention, actual native stage order, C versus Cbar, nu versus omega, and the h=0 distinction. Earlier D1/NRG results should be cited as inherited.

No new research, publication, Git operation or TORMENT production change is authorized by scientific acceptance alone. A separately supplied work order can authorize drafting and bounded read-only agenda consolidation; final physical/model-design choices and publication remain outside this acceptance.
