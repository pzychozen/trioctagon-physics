# Codex work order — NATIVE_FINITE_CAPACITY_ACCESS_PAPER_AND_PUBLISH_01

**Prepared:** 4 November 2026, Atlantic/Reykjavik  
**Research author:** Hilmir Frímann Halldórsson (pzychozen)  
**Current executable stage:** A — prepare the manuscript and exact candidate for GPT/author review.  
**Publication stage:** B — specified below, but locked until explicit manuscript-and-payload publication GO.

## 1. Purpose and the remaining gate

Prepare a focused companion paper presenting the accepted `NATIVE_FINITE_CAPACITY_ACCESS_01` theorem, its complete proof and evidence. Then, only after review of the actual finished manuscript and exact publication payload, publish that accepted edition in one ordinary scoped commit and normal push.

The author asks: **“ready to give codex the push order?”** This order prepares the requested publication path. The mathematical investigation is already accepted unchanged; a manuscript and its final PDF have not yet been prepared or accepted. Do not describe the mathematical acceptance as an inspection of a nonexistent final PDF. Do not push a newly written paper on the strength of proof acceptance alone.

**Execute Stage A now without another preliminary approval request. Return the finished manuscript package and stop. Stage B activates only when the continuing author conversation supplies an explicit publication GO identifying the accepted artifact and scope.** The GO may accompany manuscript acceptance; it is not a request to repeat the scientific investigation. Codex's own successful checks do not unlock Stage B.

Earlier paper-specific commit/push permissions do not authorize this new payload. This is not an instruction to reopen prior publications or start successor research.

## 2. Identity, destination and source authority

**Paper title:** *Finite-Time Access to Native Projection Capacity in the Reciprocal Chiral Exchange Candidate*  
**Subtitle:** *An explicit quarter-capacity certificate for coherent empty launches*  
**Edition:** v0.1; use the actual manuscript preparation date, without backdating final review or publication.

Stage-A working directory:

    C:\TORMENT\TRIOCTAGON_new\research\NATIVE_FINITE_CAPACITY_ACCESS_PAPER_01\

Prepare the intended repository structure beneath `candidate_edition/`, not in an existing accepted publication:

    papers/NATIVE_FINITE_CAPACITY_ACCESS/README.md
    papers/NATIVE_FINITE_CAPACITY_ACCESS/publication/v0.1/
        NATIVE_FINITE_CAPACITY_ACCESS_v0.1.pdf
        manuscript/
        evidence/
        verification/
        README.md
        BUILD.md
        PROVENANCE.md
        CLAIM_SOURCE_LEDGER.md
        SOURCE_IDENTITIES.json
        CANDIDATE_MANIFEST.json

These are proposed new paths. Check for collisions before any publication; never overwrite an existing edition. Keep the prospective root README addition as a separate reviewable patch in Stage A.

Read in this order:

1. `accepted/NATIVE_FINITE_CAPACITY_ACCESS_01_GPT_REVIEW.md` — current internal scientific acceptance and its exact scope.
2. `accepted/NATIVE_FINITE_CAPACITY_ACCESS_01_PROOF.md` — the accepted theorem and full argument, FA01–FA26.
3. `accepted/NATIVE_FINITE_CAPACITY_ACCESS_01_CLAIM_SOURCE_LEDGER.md` and `CLAIM_CROSSWALK.json` — 15 inherited groups, seven new steps, 26 displayed groups, and unnumbered analytical obligations.
4. Selected exact P1/P2/P3 source files under `inputs/published/`; use the original eight-group results only at their recorded scope.
5. `CURRENT_CONTINUITY.md` and preserved historical author/context documents.

The unchanged GPT review ZIP includes the complete original Codex submission ZIP, original exact checks, recorded execution evidence, all 74 carried input members, and the selected predecessor PDFs. It is included once, without recursively repackaging the new order into its own evidence. Convenience copies in this packet have exact byte identities listed in `INPUT_IDENTITIES.json`.

Published foundations:

- **P1:** *A Reciprocal Chiral Exchange Extension of the Tri-Octagon Model*, v0.1, commit `273b1a6faaab19ea58748d00576439166eeef9ab`.
- **P2:** *Same-Trajectory Native Credit in the Reciprocal Chiral Exchange Candidate*, v0.1, commit `28e8a85c8fe1e6321328d4d7285b2560d1f98aa9`.
- **P3:** *Recoverable Transfer and Projection Capacity in the Reciprocal Chiral Exchange Candidate*, v0.1, commit `54c0f6c419fa681e2c1e74a5ad2bb46df787bb93`.

P1 Theorem 3.1 is global well-posedness; P2 Theorem 3.1 is native credit; P3 Theorem 3.1 is the projection ceiling. Preserve these distinctions and the already corrected printed source locators. The three papers are fixed foundations, not the new paper's title or current repository HEAD.

Accepted identity anchors:

| Artifact | SHA-256 |
| --- | --- |
| Original Codex proof | `05d962af8be00377212c96c63a2ae498e57b4912192dfad87e705b4aadd56cb7` |
| Original Codex review ZIP | `e554415e2dd874d956924737fdcb95422583bf281a18554d94e3f72873abe905` |
| GPT scientific review | `832782627a5ec831e16673b544566b596ca2fe6a3d15d546078b3c762facdaaf` |
| GPT scientific-review ZIP | `f324f81c98603def0c3c8d579d0ab99af03eab0d2554a917aca8edc5db601888` |
| Original investigation work order | `cff35558c510a368c41258d77d1b451539730636aed8cae8598be4bc44798b36` |

Verify the packet and these bindings before use. Preserve every accepted original, including historical pending-review wording; explain later acceptance in new provenance rather than rewriting history.

## 3. Exact scientific content to present

Use the original, unscaled exchange equations and raw two-port order:

\[
\dot x=-\frac{\eta_N}{2\alpha_N}J(x)^Ty,\qquad
p_t+c(r_c)_s=\mathcal B\{\eta_Nf(x)-\kappa z\},\qquad
(r_c)_t+cp_s=0,\qquad
\dot z=\frac\kappa{\beta_R}y,\quad y=\mathcal B^*p.
\]

Retain the fixed rank-two registration at yaw \(\delta_g=\pi/4\), finite positive propagation and receiver coupling, the admitted periodic circle and disjoint finite-width tents, and positive storage scales. Preserve the whole-circle shortest-separation condition, including the coordinate seam. The declared launch is

\[
\Omega_0=(1,e^{i\phi},1),\qquad0<\phi<\pi/12,\qquad
p(0)=r_c(0)=z(0)=0.
\]

With \(R=\sqrt3\), \(k=G\sqrt{8/7}\), \(m=2/(3\epsilon_c)\), \(d=2/\epsilon_c^3\) in the normalized convention, set

\[
\nu^2=\frac{\eta_N^2mk^2R^2}{2\alpha_N},\qquad
\sigma_{\rm ext}^2=\frac{c^2d}{m}+\frac{\kappa^2m}{\beta_R},\qquad
C_{\rm joint}=\alpha_N(1-\cos\phi)>0.
\]

The main theorem must retain the exact quantifiers:

> Fix the admitted geometry and all positive finite coefficients satisfying \(\sigma_{\rm ext}\le\nu/2\), before choosing the phase. For every \(0<\phi<\pi/12\), its unique unchanged empty-launch solution satisfies at the same phase-independent time \(t_*=1/\nu\)
>
> \[
> H_C(t_*)+H_R(t_*)>\frac{1053}{4096}C_{\rm joint}>\frac14C_{\rm joint}>0.
> \]

Equality in the rate condition is allowed. The sufficient regime is nonempty because, with the other admitted parameters fixed, one finite positive constant \(\eta_N\) may be selected to satisfy

\[
\eta_N^2\ge\frac{8\alpha_N}{mk^2R^2}
\left(\frac{c^2d}{m}+\frac{\kappa^2m}{\beta_R}\right).
\]

Do not turn a sufficient condition into a necessary, optimal or universal one. No state reset, native F jump, changing coefficient, limit construction or altered feedback enters the theorem.

The complete new proof must include:

- Inherited existence and strong regularity before the original-variable weighted energy estimate; receiver cancellation and zero-norm regularization.
- The exact evolving-drive equation \(\dot f=-\eta_N JJ^Ty/(2\alpha_N)\); the positive Volterra-kernel comparison and the finite-interval factorial remainder tending to zero.
- The drive-dependent bounds preserving the factor \(|f_0|\), rather than replacing it by a generic maximum.
- The strong reference curve \(U_{\rm ref}=(\eta_N t\mathcal Bf_0,0,0)\), with both residual components: negative propagation in the second carrier coordinate and positive receiver feedback. Its weighted norm defines \(\sigma_{\rm ext}\).
- The full finite error, the reverse-triangle bracket \(B(u,\rho)=2u-\sinh u-\rho u^2/2\), and proof of its positivity before squaring.
- The exact inequalities \(\sinh1<67/57<19/16\), \(\cos(\pi/12)>19/20\), bracket \(>9/16\), normalization factor \(>13/16\), and \(1053/4096=1/4+29/4096\).
- Nonempty finite regime, phase independence, units with \(R^2\) retained, and the precise storage interpretation.

Use the accepted report, not this shorter order, as the authority for full derivations. No theorem strengthening, optimization, new numerical evidence or new literature-priority claim is commissioned. A genuine contradiction must be reported, not silently repaired.

## 4. Manuscript scope and attribution

Present one connected paper: motivation and prior gap; fixed model and hypotheses; main theorem; full new proof; admissible parameter regime and dimensions; interpretation, evidence and continuing geometric questions. Cite P1/P3 for inherited foundations rather than reproducing entire predecessor papers. Keep enough definitions to make the new argument independently readable.

Use the predecessor LaTeX appearance as a style reference, with properly sized equations, readable tables, complete references, navigation and normal page numbering. No artificial page count is required. Do not add illustrative trajectories or geometry figures that could imply new calculations or a newly established spatial route. No new figures are necessary.

Research author: **Hilmir Frímann Halldórsson (pzychozen)**. Describe GPT's formulation/internal scientific review and Codex's independent investigation/manuscript preparation accurately. This is project-internal review, not external peer review or Lean formalization.

For the review candidate, distinguish **accepted mathematics** from **manuscript review pending** in title-page status, metadata, contribution statement and conclusion. Never inherit P3's statement that GPT already accepted this new manuscript. Later publication wrappers may record completed acceptance without altering the frozen accepted PDF unless an explicit editorial change is approved.

The abstract must state the specified coherent family and nonzero drive, the initially empty external states, the sufficient condition, the combined-stock numerator and joint-capacity denominator. The central distinction is actual finite-time access to a definite fraction of a structural ceiling.

Keep the following limitations in the manuscript, not only the evidence package:

- This is more than one quarter of **joint capacity**, not one quarter of initial native stock. Here \(C_{\rm joint}/H_N(0)=\tfrac23(1-\cos\phi)\).
- The absolute stock tends to zero toward the excluded zero-phase endpoint; the normalized guarantee is uniform over the open phase range.
- Neither receiver allocation nor later recovery of this particular amount on these same coefficients is established. Do not splice the earlier \(80/81\) or native-credit guarantees onto this regime without a new argument, which this order does not authorize.
- No saturation, maximizing time, monotonic extraction, physical-energy calibration or completed spatial circuit is claimed.
- \(\nu\) and \(\sigma_{\rm ext}\) are estimate rates, not native frequencies, an F cadence or a new physical clock. Keep P3's original accessibility statistic and denominator unchanged.

## 5. Stage A — prepare, build, verify and return

Work outside the repository publication tree. Use the existing environment and known build tools. Do not install packages, invoke historical simulations, run parameter scans or change accepted evidence. Existing scientific checks are eight distinct groups with an independent replay; they are not sixteen distinct discoveries. No scientific rerun is required merely to typeset the proof.

Create a fresh manuscript-to-source crosswalk that covers **I01–I15, N01–N07 and FA01–FA26**, including unnumbered regularity, factorial-remainder, strictness and unit arguments. Map each to new TeX labels and actual printed equation/page locators after the final build. These sets overlap; do not sum them into a count of independent theorems.

Perform the build/fidelity gates on the exact candidate:

1. Compile complete editable LaTeX to PDF; retain engine/version, invocation, actual logs, source hashes and PDF hash. Confirm resolved citations, labels and bookmarks; fix missing glyphs, clipping, material overfull boxes and inconsistent status. Record any benign remaining warning explicitly.
2. Extract text and inspect equation/theorem ordering, positive/strict signs, factors, quantifiers, date, author, metadata and bibliography against the accepted report. Review every crosswalk row.
3. Render **every final page** and visually inspect it. Repeat affected checks after edits. Bind the visual record and page-image identities to the final PDF hash; do not claim inspection of an earlier PDF as inspection of a rebuilt one. Do not distribute standalone font files.
4. Hash-check the protected originals before and after. Scope preservation honestly to inventoried files; do not claim a machine-wide audit.
5. Freeze the complete candidate and manifest, prospective new-path allowlist, and minimal root README addition. Manifests must explicitly exclude themselves; avoid circular hash requirements.
6. Build the review ZIP, check unique safe paths, exhaustive member coverage, CRC, sizes and hashes after writing, and create an adjacent whole-archive SHA-256 checksum. The standalone PDF must match the archived copy.

Return:

- The PDF and complete editable LaTeX/build sources.
- A complete review ZIP and SHA-256 checksum.
- Source identities, claim crosswalk/ledger, fidelity checks, build logs/receipt, all-page visual record and render images, preservation record, package verification and a short completion report.
- A proposed publication tree/allowlist and README patch for the next review.

**STOP HERE FOR GPT/AUTHOR MANUSCRIPT-AND-PAYLOAD REVIEW. No git add, commit, push, tag, release, DOI, announcement or successor research is authorized in Stage A.**

## 6. Stage B — publish only after explicit GO

This section specifies the eventual requested push order. It is dormant until a subsequent manuscript-and-payload publication GO identifies the accepted PDF/hash and scope. If corrections are requested, apply only their approved scope and perform the corresponding artifact checks before the gate is closed.

After GO, use:

    C:\TORMENT\TRIOCTAGON_new\research\NATIVE_FINITE_CAPACITY_ACCESS_PUBLISH_01\

Target repository: `pzychozen/trioctagon-physics`; remote `origin`; branch `main`.

The last supplied publication anchor is `54c0f6c419fa681e2c1e74a5ad2bb46df787bb93`. **Do not assume it is still the remote tip.** Fetch and record the actual current target at execution. Verify the origin resolves to the intended repository, the foundation commits remain available, and the intended new destination does not conflict with existing work.

Use an isolated temporary/detached worktree from the verified remote base. Preserve the original checkout's branch, HEAD, index, tracked modifications and unrelated untracked work. No destructive clean/reset, automatic stashing, force push, history rewrite, global configuration change or unsolicited branch movement. Use command-local Windows long-path handling if needed. If branch movement or a collision prevents the approved ordinary push, report it rather than overwrite other work.

Freeze and validate an explicit allowlist containing only:

- The accepted new `papers/NATIVE_FINITE_CAPACITY_ACCESS/` publication subtree and landing page.
- One minimal appended root README catalog entry.

No predecessor paper, kernel/runtime, other research directory, licence or global repository policy may be altered. Preserve the accepted PDF, manuscript sources and evidence byte-for-byte. Do not rebuild a frozen accepted PDF merely to change status text; a dated publication disposition may explain historical draft wording. Any approved final rebuild must have its own reviewed/authorized identity and fresh checks, not an invented earlier GPT inspection.

Write an accurate publication README/disposition/provenance and a new exhaustive publication manifest for this edition. Preserve nested historical manifests and their scopes. Final wrappers must separate scientific acceptance, manuscript acceptance, build/visual checks and publication authorization, with actual dates and hashes. Do not include credentials, caches or unrelated files. Keep large render/build support and post-push receipts in the external closeout unless part of the accepted payload.

Stage **only the explicit allowlist**. Verify the staged path set, statuses and bytes against the frozen intended payload. Confirm no deletion or unrelated edit. Make **one ordinary scoped non-merge commit**, with a message such as:

    Publish finite-time native capacity access v0.1

Then perform **one normal push**:

    git push origin HEAD:refs/heads/main

Do not amend a published commit or make an extra receipt commit. No release, tag, DOI or announcement is included. If there is a genuine authorization, source, access or remote-base conflict, stop and report it; no generic confirmation is required after a valid scoped GO.

## 7. Fresh remote-byte verification and closeout

After the push:

- Retrieve the actual commit metadata and complete changed-path set, including pagination if needed. Confirm the intended parent and exact allowlist/status match.
- Fetch every added/modified file afresh at its full immutable commit-pinned URL. Compare content bytes, lengths and SHA-256 with both the committed blob bytes and frozen intended bytes. Record fetch time, resolved URL, HTTP status, expected/actual sizes/hashes and failures. A matching URL or stored historical record is not a new download.
- Check remote `main` and document its relationship to the publication commit. Do not claim it still points to that commit if another commit has arrived; establish reachability and disclose the movement instead.
- Recheck the inventoried original checkout and protected inputs. Distinguish recorded Windows checks from any independent review performed elsewhere.
- Return `PUBLICATION_RECEIPT.md`, machine-readable remote comparison, immutable PDF and edition links, exact publication payload and a complete closeout ZIP with exhaustive manifest, CRC/hash verification and adjacent SHA-256 checksum.

Use the actual computed changed-file count, PDF page count and hashes. No such final numbers are predetermined by this order. Keep post-push receipts outside the publication commit to avoid self-reference and an unnecessary second commit.

## 8. Continuing research and stopping point

Carry the central starting/meeting region, opposed cones, outward spreading and curved around–inward return, stationary supports and possible transfer elsewhere in the motivation and outlook. The carrier circle is not the intended tight toroid; the close original and extended-line spheres are distinct; finite host-notch N regions and central broken G boundaries are not interchangeable. The author's tentative 15–20%, possibly more, is intuition, not a calibrated fraction or this certificate's denominator.

After this publication, the next substantive question remains receiving and recovering the capacity-sized transferred amount on the same fixed-parameter trajectory. It precedes the standing native F/exchange-cadence, intended-route and six-opening work, with linked gravity–magnetism and later outer-geometry/justified SRG integration. Three-Way stays parked.

The pi material remains brainstorming only. Do not add a Pi theorem citation, Lean claim or new research branch to this paper. No new author geometric choice is needed for typesetting the accepted theorem; escalate only a concrete contradiction or a new assumption that changes the construction.

**This order ends with Stage A review delivery, and—only after its gate is explicitly opened—Stage B publication and closeout. Do not begin a successor investigation.**
