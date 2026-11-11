# Manuscript blueprint — companion note

**Title:** Certified Capture of the Collective-Turning Trajectory in the Native Triad  
**Parent:** Transient Collective Turning and Coherent Relaxation in the Native Triad, research edition v0.1.  
**Task:** NATIVE_TURNING_CAPTURE_PAPER_01.

This outline is editorial guidance, not additional mathematics. The controlling claims are the accepted proof and GPT review in `inputs/accepted_capture/`.

## 1. Question and contribution (about half a page)

Explain that the parent paper certified an early turn and separately proved convergence on a specified invariant domain, but did not connect its original entrance to that domain. This note supplies that finite connection for the original coefficients and seed. Summarize the bounded source comparison without reciting the full historical catalog. Distinguish new capture from inherited methods/results.

A suitable abstract should cover four points in roughly 120–170 words: unchanged native map/seed, certified strict inclusion at update 50, application of the inherited convergence theorem, and qualitative initial-state robustness. State that 50 is sufficient rather than earliest, and that no physical identification is claimed. Do not imply parameter robustness or a global basin.

## 2. Frozen recurrence and inherited theorem (about one page)

Give the exact simultaneous prestage and harmonic-three synchronization, fixed rational coefficients, original seed and coherent-domain definition. State the needed inherited theorem with its domain and cube-qualified uniqueness. Define the early turn statistic only as needed to formulate the same-trajectory result; cite its existing strict sign. Avoid reproducing the parent's long domain/contraction proofs.

## 3. Certified finite entry (about two pages)

State the central theorem: F^50 of the exact seed is strictly inside the inherited domain. Explain the induction from the exact singleton through 50 linked enclosures, the positive-prestage checks and the branch-independent sine identity. Describe the two arithmetic implementations and justified remainder bounds. Give the terminal amplitude/cone table and the common-phase-width inequality. This is the note's main proof, not a reference to a PASS count alone.

The cone test uses w_i=(987395−158274i)Omega_{i,50}; Re(w_i)>8|Im(w_i)|. Positive common scaling and rotation here are diagnostic only. Ordinary width <2 arctan(1/8)<1/4<pi/12 is a strict sufficient admission test, not a computed minimum width.

## 4. Same-trajectory relaxation and nearby entrances (about one to two pages)

Apply the parent theorem starting at index 50. With j=n−50 an integer, c=1−3sqrt(2)/200 and beta=8571/10000, the accepted explicit bound is

\[
\|\Omega_{50+j}-e^{i\theta_\infty}r_*\|_\infty
\le \frac15\beta^j+
\frac{107701}{12800000}\frac{c^{2j}-\beta^j}{c^2-\beta}
+\frac{11}{40}c^j.
\]

This is an inherited estimate with the new admission index and the accepted bounds e_0<=1/5, Delta_50<1/4. Do not call the constants a new rate theorem. Explain the limit of the mean, positive residual amplitude spread and decay of the inherited area observables only with their proper definitions and citations.

Then give the short open-neighborhood proof at the same coefficients. Preserve all three ingredients in one neighborhood: regular finite path, strict positive early turn, strict terminal inclusion. An explicit numerical radius is neither available nor needed for this result.

## 5. Reproducibility and scope (about half a page, plus references)

Identify the archived certificate, generator, independent checker, recorded runs and later reviewer replay without blending their roles or platforms. Explain that the present manuscript is a document build, not a new replay. Include only essential hashes/identifiers in print; keep full manifests in the evidence.

Close with the actual finding: a known transient turning example and a qualitative neighborhood converge under the unchanged native recurrence. Do not infer gravity, magnetism, a physical circuit, global attraction, a unique global equilibrium, or finitely many remaining diminishing turns. Do not automatically launch earliest-entry optimization, a parameter scan or a new receiver project.

## References and visual economy

The parent paper and accepted capture investigation are the essential primary references, with the native implementation/source cited where it is used. Preserve exact editions and repository locators. Add other earlier papers only where their content is materially used. No fresh external literature survey is required for this source-based note.

A terminal-certificate table is sufficient. One optional retained-data figure may help; no new trajectory is permitted. No decorative cover, broad project history, separate table of contents, or extensive appendices are needed to reach a page target.
