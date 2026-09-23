# Paper B: symbols and theorem correspondence v0.1.1

Companion to the complete manuscript. This sheet does not replace the proofs.

| Symbol | Meaning and domain |
|---|---|
| A, B, C | Face/channel labels in the accepted order P1, P2, P3 |
| s | Width-one octagon side, sqrt(2)-1 |
| c_i, n_i, t_i, e_z | Face centre, outward normal, horizontal tangent, common positive vertical |
| o, R | Centroid-axis point and linear +120-degree spatial rotation |
| P | Active cyclic channel permutation A to B to C to A |
| H, V | Spatial mirrors z to -z and x to -x |
| S | Channel swap A/C induced by V |
| G, Q, pi | General shell symmetry's linear part, channel matrix, face permutation |
| W_i, W_tan | One face's free tangent-vector plane; direct sum of all three planes |
| Omega_i = q_i + i p_i | Raw complex channel component, with no normalization |
| D, E | Decoding C^3 to W_tan and encoding back |
| J_i | n_i cross, restricted to W_i |
| g_i, omega_i | Euclidean metric and dq_i wedge dp_i, with omega_i(v,w)=g_i(J_i v,w) |
| Pi_i | Ambient rank-two tangent projector |
| T_ij | Zero-relative-phase transport from j to i |
| R_ij | Linear cyclic rotation matching source j to destination i |
| mathcal A_ij | Signed transported state-vector parallelogram area |
| Z | (A_BC,A_CA,A_AB), the channel-pair triple; not Cartesian components |
| L3 | Negative K3 graph Laplacian; -3(I-p0) |
| eps, g, lambda, k | Existing recurrence's real parameters |
| F_TO, F_face | Same map in complex and tangent coordinates |
| Arg0 | Argument for nonzero entries; exactly zero at every complex zero |

| Statement | Equations | Provenance and exact scope |
|---|---|---|
| Geometry used in §2 | 1-5 | Reused Paper C §§4,5,7,9; actual width-one placement, no new geometry theorem |
| Adoption 1 | 6 | Folded-face attachment §§3,10; choosing tangent vectors as an observable, not recovering a field |
| Proposition 1 | 6-8 | Bridge I oriented-plane construction and corrected Bridge II compatible form; proof supplied. ED=I, DE=Pi ambiently |
| Adoption 2 | 9 | Folded-face attachment §§4,10; no adjustable relative phase or seam transport |
| Proposition 2 | 9-10 | Corrected attachment §10; rank-two ambient maps compose on all ambient inputs; matched rotation only on tangent domain |
| Theorem 3 | 11-14 | Paper A §6.1 plus attachment §§4,10; same Arg0 and real parameters; exact coordinate conjugacy |
| Theorem 4 | 15-16 | Corrected Bridge II and attachment §§5,10; transported symplectic form, signed parallelogram area, raw scale |
| Proposition 5 | 17 | Existing channel/orientation identities; elementary proof written in manuscript; arbitrary channel permutations |
| Theorem 6 | 18-21 | Corrected attachment §10; two determinant factors; shell symmetry and induced permutation, not arbitrary unrelated G and Q |
| Passive frame calculation | 22-23 | Attachment §4.5 and §10; derived with the physical transport held fixed |
| Proposition 7 | 24 | Existing C3 representation witness in test_face_state.py; exact squared-distance evaluation included here |
| Dynamics qualifications | 25-26 | Paper A and attachment §10; unequal k joint covariance, eps=0 exception, common-phase limitation at zero |

The self-contained proofs reconstruct accepted mathematics. The user-relayed GPT review accepts the identified v0.1 PDF within its stated scope; this publication revision preserves those mathematical statements. The 25 check groups in evidence/v0.1.1/manuscript_algebra.json are attributed Codex checks of displayed algebra. They do not establish new trajectory, stability, or physical claims.

The original synthesis used during drafting is identified by its preserved hash in reviewed_v0.1/evidence/source_inputs.json. It is not a public runtime or paper-build input; the specific underlying sources are available through the current reference ledger. The scoped GPT acceptance of the reviewed v0.1 PDF is recorded with that exact identity in the appended publication validation report.

Implementation links: [geometry](../../kernel_physics/geometry.py), [face-state view](../../kernel_physics/face_state.py), [recurrence](../../kernel_physics/dynamics.py), [readout](../../kernel_physics/readouts.py), [face tests](../../kernel_physics/tests/test_face_state.py), [dynamics tests](../../kernel_physics/tests/test_dynamics.py), [readout tests](../../kernel_physics/tests/test_readouts.py).

The tests named in Appendix A exist in the current tree. No existing suite is rerun as a claimed proof of this publication. The package's small algebra checker is separate from that suite.
