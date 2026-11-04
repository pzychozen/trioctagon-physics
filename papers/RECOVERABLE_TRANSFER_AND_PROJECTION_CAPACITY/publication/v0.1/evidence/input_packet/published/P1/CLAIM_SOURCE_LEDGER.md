# Manuscript fidelity and accepted-claim crosswalk

This fresh ledger maps final manuscript labels, numbers and pages to all accepted RX01-RX41. [Original ledger](evidence/accepted_claim_source_ledger.md) and [proof](evidence/accepted_proof.md) remain byte-identical. S/A/B/C/D labels in that evidence belong to the investigation, not automatically to this paper. Full active source identities are in [SOURCE_INVENTORY.json](SOURCE_INVENTORY.json).

| Accepted ID | Final labels (number, page) | Accepted claim/proof locator | Exact source or argument dependency | Status and domain |
|---|---|---|---|---|
| RX01 | sec:candidate (1, p. 2); tab:status (1, p. 2); eq:system (1.6, p. 3) | Candidate register and state system; S1–S4 | ORDER sections 2, 4.1–4.3, N1–N4; comparison with C1_FOUNDATIONS `eq:readouts`, `eq:sourcechain` | PROPOSED storage, feedback, receiver and timing; INHERITED chiral algebra/carrier. No adoption into existing model. |
| RX02 | sec:drive (1.1, p. 2); eq:registration (1.1, p. 2); eq:drive (1.2, p. 2) | Normals, yaw registration, gain, plus/minus ordering and dimensions of K/J; S2 | C1_FOUNDATIONS lines 9–29 (`eq:contacts`, `eq:arcs`, tangent-sign sentence) and 43–67 (`eq:readouts`, `eq:sourcechain`, `eq:sectors`); RAW_CHIRAL `z_chiral` | INHERITED plus direct dimension/rank check. No sign added from contact tangents; raw C retained, not ambient attachment. |
| RX03 | sec:ports (1.2, p. 2); eq:tents (1.3, p. 2); eq:ports (1.4, p. 3) | Circle, periodic state, finite disjoint normalized profiles; S2, A9 | C1_CARRIER lines 1–24, `eq:tent`, `eq:C1`, `prop:tent`, `eq:tentnorm`; C1_FOUNDATIONS 24–29 | INHERITED finite-width adoption. epsilon_c strictly between zero and eta_geom; disjointness is geometric input. |
| RX04 | sec:exchange (1.3, p. 3); tab:units (2, p. 3) | Dimension audit including new scales; S3 | C1_FOUNDATIONS lines 69–90, `tab:units`; ORDER section 4.2; direct unit multiplication in S3 | VERIFIED conditional dimensional consistency. alphaN, betaR and h_ex remain new choices; no SI calibration. Native fixed tuple retains normalized convention. |
| RX05 | prop:euler (2.1, p. 4); eq:jacobian (2.1, p. 4); eq:core (2.2, p. 4) | Exact Jacobian, Euler identity and transpose signs; A1–A2 | Differentiate K(a cross b); scalar triple product; exact helper `chiral_jacobian`, `degree_two_euler`, `transpose_signs`, `core_vector_form` | VERIFIED for all real x,y and constant K, including zero states. T1 confirmed. |
| RX06 | eq:powers (2.3, p. 4); eq:localwork (2.4, p. 4); eq:balances (2.5, p. 4) | Matched native/carrier/receiver powers and total conservation; A3–A6 | RX05; S4; C1_CARRIER lines 50–70, `thm:work`, `eq:balance` for carrier product rule; A3 proof justifies closed-solution use | VERIFIED for candidate. T2 confirmed. Carrier work includes the negative receiver load; periodic derivative integrates to zero. |
| RX07 | eq:integrated (2.6, p. 4); thm:global (3.1, p. 5) | Integrated energy account for mild feedback solutions; A6, A3 theorem | Common local existence interval, H1 approximation, A13 continuous dependence, uniform convergence of port work integrands | VERIFIED on full energy space. Does not infer unrestricted point traces from L2. |
| RX08 | eq:profilenorms (3.3, p. 5) | B/B* bounded, Gram matrix and H1 profile bound; A9 | C1_CARRIER `prop:tent`; direct integral and disjointness; exact helper tent identities | VERIFIED/inherited ingredients. M_B = 2/(3 epsilon_c) times I2. No shrinking-width limit; H1 bound is not a new storage metric. |
| RX09 | eq:lipschitzbounds (3.5, p. 5); eq:duhamel (3.6, p. 5); eq:dependence (3.7, p. 5) | Closed nonlinear local existence, uniqueness and dependence; A11–A13 | Periodic translation group from C1_CARRIER lines 27–45, `eq:characteristics`; explicit local polynomial Lipschitz bounds; contraction on C([0,T];H) | VERIFIED for this coupled system, not inherited from exogenous C1. Complete-space contraction hypotheses and constants are stated. |
| RX10 | eq:strong (3.2, p. 5); eq:H1estimate (3.8, p. 6) | H1 regularity and legitimate strong energy calculation; A8, A14 | B maps R2 to H1, continuous finite-dimensional forcing, translation generator H1 to L2; periodic H1 weak product rule | VERIFIED for periodic H1 preparation on finite intervals; continuous spatial representatives. No H2 assertion at corners. |
| RX11 | eq:coercive (3.9, p. 6); eq:forcingbound (3.10, p. 6) | Global exchange continuation and finite-time H1 estimate; A15–A16 | RX06–RX10; coercive positive storage bounds energy norm; local restart time depends only on bounded energy norm; separate Duhamel H1 estimate | VERIFIED for all finite positive/negative exchange times. No infinite-hybrid-index bound follows. |
| RX12 | sec:power (2, p. 4) | Zero-state regularity and nonunique power completion; A1–A2 | Polynomial S4, f(0) = J(0) = 0; x dot h = 0 leaves HNdot unchanged | VERIFIED. No singular normalization or additional orthogonal term introduced; no classification of completions. |
| RX13 | eq:nonzero (4.6, p. 7) | Nonzero chiral drive exists inside coherent domain for arbitrary fixed yaw; B1 | RAW_CHIRAL formula; C1_FOUNDATIONS source chain; NATIVE_INTENSITY lines 95–108 for D; explicit Omega = (1, exp(i phi), 1) and nonzero port difference | VERIFIED for 0 < phi < pi/12 and inherited positive gains. No selected numerical phi/yaw/gain. |
| RX14 | prop:launch (4.1, p. 7); eq:initialcarrier (4.1, p. 7); eq:initialports (4.2, p. 7); eq:nativedebit (4.3, p. 7); eq:receiverstate (4.4, p. 7); eq:receivergain (4.5, p. 7) | Empty-carrier/receiver short-time supply and reception; B2–B4 | RX10, p'(0) = etaN B f0; x'(0) = 0; bounded B*; integrate A6 and receiver ODE | VERIFIED asymptotic T3 with remainders in stated norms. Strict positive storage transfer for small positive time when etaN,etaR > 0 and f0 != 0. Helper checks coefficients only. |
| RX15 | prop:credit (4.2, p. 7); eq:prepared (4.8, p. 7); eq:creditsign (4.9, p. 7) | Prepared native debit and credit; B5–B6 | y0 = ±T_star M_B f0, A5, continuity; C1_CARRIER lines 77–84 is historical signed-work comparison | VERIFIED for candidate H1 preparation and etaN > 0. Native credit is actual feedback, not a demonstrated delayed-return orbit. T_star has time units. |
| RX16 | eq:reverser (4.10, p. 7); prop:credit (4.2, p. 7) | Receiver discharge/charge and reversing involution; B2 | Any y0 realized by B M_B^(-1)y0; sign of z0 dot y0; substitute R(x,p,rc,z) = (x,−p,rc,z) in S4 and use uniqueness | VERIFIED reversible store and mathematical reversal symmetry. No physical parity, damping, absorption or irreversible disposal asserted. |
| RX17 | sec:capacity (5, p. 8); sec:power (2, p. 4) | Dark preparations and inability to charge native zero; A2, B3 | S4 and uniqueness; f(x0) = 0 with p0 = rc0 = z0 = 0 is stationary; J(0) = 0 | VERIFIED. Nonzero carrier may activate a nonzero zero-drive core; zero drive at one instant alone is not a persistent dark condition. |
| RX18 | eq:Z2 (5.1, p. 8); eq:invariantderivatives (5.6, p. 8) | Complex bilinear exchange invariant; B7–B8 | Direct derivatives using A2; exact helper `Z2_real_invariant`, `Z2_imaginary_invariant` | VERIFIED T4, independently of carrier/receiver preparation. Exchange-only; not claimed a canonical Casimir or native-F invariant. |
| RX19 | thm:capacity (5.1, p. 8); eq:chiralityidentity (5.2, p. 8); eq:floor (5.3, p. 8); eq:netcapacity (5.4, p. 8) | Lower native-storage bound and net extraction limit; B9–B10 | Triangle inequality or exact I² − abs(Z2)² = 4 norm(Cch)²; RX18 | VERIFIED T5. Net extraction only, not gross repeated work or attainability. At I0 = 0 use unnormalized statement. |
| RX20 | eq:coherentcapacity (5.5, p. 8); eq:phasebound (5.7, p. 8) | Coherent initial phase-span capacity; B11–B12 | Rotate doubled phases to midpoint and bound each cosine below by cos(Delta0) | VERIFIED for ordinary initial span <= pi/12. Later domain invariance is unnecessary. Denominator is initial native trial storage, not a diverted-work fraction. |
| RX21 | prop:phase (5.2, p. 9) | Common-phase equivariance, information limitation; B4 | Orthogonal Q_theta action, f(Q_theta x) = f(x), chain rule for J; RECIRC_INTERPRETATION lines 55–64 for inherited phase/decoder distinction | VERIFIED exchange equivariance. Phase-sensitive outlet selector is NOT ESTABLISHED. No transfer of whole-hybrid equivariance through native zero strata. |
| RX22 | eq:tuple (6.1, p. 9); eq:prestage (6.2, p. 9); eq:nativemap (6.3, p. 9) | Exact F, tuple and zero convention; C1–C3 | DYNAMICS `arg0`, `phase_sync`, `_advance`, `step3`; NATIVE_INTENSITY 6–20, 95–108, `eq:pre`, `eq:map`, `eq:tuple` | INHERITED unchanged ideal map. Simultaneous kicks and synchronization retained; no continuous-flow replacement. |
| RX23 | eq:nativeintensity (6.4, p. 9); eq:fullsquare (6.5, p. 10); eq:graphsquare (6.6, p. 10) | Exact intensity change and full finite square; C4–C5 | NATIVE_INTENSITY 36–61, `prop:intensity`, `eq:total`, `eq:square`; DIAGNOSTICS 256–287; direct symbolic expansion | INHERITED and independently VERIFIED algebra. T7 confirmed at all finite ideal states. Every edge once, full mixed term retained, d_pre not full displacement. |
| RX24 | prop:hybrid (6.1, p. 10); eq:hybrid (6.7, p. 10); eq:hybridbalance (6.8, p. 10) | Ordered split and full-step storage increment; C6–C7 | ORDER section 7 N5; native jump changes only x; RX06 exchange conservation | PROPOSED split; VERIFIED T6. Exact flow, no prescribed numerical integrator. Baseline native change is not assigned source/receiver work. |
| RX25 | eq:potential (6.9, p. 10); eq:domain (6.10, p. 10); eq:positivebaseline (6.11, p. 10) | Native HN need not descend and Z2 need not survive jumps; C8 | Exact rational evaluation of C2 at aligned unit input, synchronization zero; NATIVE_INTENSITY 69–110 for distinct V and inherited descent theorem | VERIFIED counterexample to conflating V with HN. No native trajectory experiment or domain enlargement. |
| RX26 | prop:hybrid (6.1, p. 10); sec:limits (6.1, p. 11) | Zero and individual coupling limits; C3 table | Direct substitution into S4 and C6 | VERIFIED: both zero gives sampled F exactly, source-off carrier and fixed receiver. Individual zero cases retain the other interaction. |
| RX27 | sec:limits (6.1, p. 11) | Exogenous clamping comparison and changed timing; C3 | C1_NATIVE lines 4–10, `eq:hold`; C1_FOUNDATIONS 88–90; S4 and C6 | VERIFIED comparison. Clamped drive with debit suppressed is external work, not closed exchange. etaN = 1 recovers unchanged drive amplitude. |
| RX28 | sec:limits (6.1, p. 11) | Old loop period not automatically inherited under active coupling; C3 | RECIRC_RETURN `thm:return`, `eq:translation`, source-off hypothesis; S4 complete internal forcing | VERIFIED limit on theorem transfer. Coupled system may have nonzero internal forcing despite no external source. No general coupled-period classification. |
| RX29 | sec:limits (6.1, p. 11) | Every finite hybrid step exists; regular dependence qualified; C3 | C2 polynomial prestage, C3 exact zero convention, RX11; smooth phase differences where each prestage component nonzero | VERIFIED finite-index existence; local regular dependence on nonzero-prestage neighborhoods. No general smoothness through zeros or uniform infinite-step bound. |
| RX30 | prop:domainexchange (A.1, p. 13); eq:boundaryprep (A.1, p. 14); eq:boundaryderivative (A.2, p. 14) | Exchange exits old coherent domain for admissible preparation; C9–C11 | Accessible w = −W e_z, p0 = B M_B^(-1)y0, phase derivative from A2 | VERIFIED analytic outward witness for etaN > 0; no noise, clamps or normalization. Does not claim every preparation exits. |
| RX31 | prop:domainhybrid (A.2, p. 14); eq:fastports (A.3, p. 14); eq:fastcore (A.4, p. 14); eq:fastspan (A.5, p. 14) | Sampled hybrid has no universal D-invariance over allowed cadences; C12–C14 | Exact native q from C8; large finite carrier preparation; fast-time Duhamel limit with uniform bounds; explicit hyperbolic-function limit solution | VERIFIED existential analytic witness. No simulation, finite R sampling or parameter scan. Does not prove failure for every fixed cadence. |
| RX32 | eq:perport (7.1, p. 11); eq:Qdefinitions (7.2, p. 11) | Per-port directional work convention; D1–D2 | ORDER section 8; positive/negative part identity; equal and opposite simultaneous port example | PROPOSED explicit counting convention; VERIFIED cancellation warning. These are work integrals, not tagged cohorts or per-pass section amounts. |
| RX33 | eq:baselinewindow (7.3, p. 12); eq:windowbalances (7.4, p. 12) | Window accounts including native jumps; D3–D4 | Integrate A5 separately between jumps; add C7; carrier and receiver have no jump | VERIFIED with declared endpoints/windows and finite jumps. Receiver signed storage change exactly Q_CtoR − Q_RtoC. |
| RX34 | prop:ratio (7.1, p. 12); eq:retainedratio (7.5, p. 12); eq:ratioidentity (7.6, p. 12) | Restricted retained-ratio bound; D5 and subsequent paragraph | D4, HC/HR initially zero, nonnegative stocks and Q_CtoN | VERIFIED retained ratio in [0,1] when denominator positive. Same bound also survives counted native jumps under these start conditions; baseline increments affect initial-core attribution, not this inequality. |
| RX35 | sec:accounts (7, p. 11); prop:ratio (7.1, p. 12) | Gross receiving and arbitrary-history ratios; D2 | D3, possible backflow, admissible prepared y0 = T_star M_B f0 and z0 = A f0 | VERIFIED absence of universal [0,1] bound for arbitrary preparation; actual small-window examples. Gross ratio inherits restricted bound if also receiver backflow is zero. No fitted fraction. |
| RX36 | sec:accounts (7, p. 11); sec:interpretation (8, p. 12) | Receiver storage is not C6 observation or permanent siphoning; D2, E | C6_EXTERIOR lines 1–10, `eq:C6`; C1_LIMITS line 14; RECIRC_INTERPRETATION 1–19; candidate receiver ODE | INHERITED distinction and VERIFIED candidate interpretation. Irreversibility would need further separately authorized constitutive choices. |
| RX37 | sec:interpretation (8, p. 12) | Geometry limits and exact O versus finite region; E | RECIRC_INTERPRETATION 21–45, `eq:circle`, `eq:patchdictionary`, `eq:G`; ACCEPTED_PROOF C.1; ORDER sections 2 and 9 | INHERITED registered distinctions plus controlling interpretation. No new geometry construction, central region, six-opening route, toroidal field or EM law selected. |
| RX38 | prop:phase (5.2, p. 9); sec:interpretation (8, p. 12) | Based decoder, raw versus ambient chirality and stationary supports; B4, E | FACE_DECODER lines 66–101, 123–134; RECIRC_INTERPRETATION 55–64 | INHERITED as comparison only. No decoder/project code executed; vectors are not transport trajectories. |
| RX39 | sec:candidate (1, p. 2); sec:conclusion (8.1, p. 13) | New contribution compared with accepted missing-interface inventory; verdict, E | RECIRC_FOUNDATIONS 44–53; RECIRC_DIVERSION 45–71; RECIRC_INTERPRETATION 66–81; ACCEPTED_PROOF B.2 and C.3; RX05–RX16 | VERIFIED candidate supplies explicit debit/credit and dynamic receiver; physical route and energy interpretation remain NOT ESTABLISHED. Old source-off recurrence is not presented as the new result. |
| RX40 | sec:candidate (1, p. 2) | External methodological context only; S1 | A. van der Schaft, arXiv:2412.19673v1, sections 1.1–1.2, equations (5)–(6), interconnection paragraphs | CONTEXT. No canonical Poisson claim, physical validation, or candidate existence theorem imported. All required coupled analysis is written in A3. |
| RX41 | sec:conclusion (8.1, p. 13) | Evidence availability and preservation limits; verdict, E | Supplied order expected identities; SOURCE_IDENTITIES.json; AGENTS_CHECK.json; final PRESERVATION_CHECK.json | FILE EVIDENCE. Full defining sources available; separate historical GPT review/packet unavailable in the disclosed scope. No claim of whole-machine/repository audit or scientific peer review. |

## Final editable-source locations

- sec:accounts: [manuscript/accounts.tex:1](manuscript/accounts.tex#L1); printed 7, page 11.
- eq:perport: [manuscript/accounts.tex:3](manuscript/accounts.tex#L3); printed 7.1, page 11.
- eq:Qdefinitions: [manuscript/accounts.tex:8](manuscript/accounts.tex#L8); printed 7.2, page 11.
- eq:baselinewindow: [manuscript/accounts.tex:19](manuscript/accounts.tex#L19); printed 7.3, page 12.
- eq:windowbalances: [manuscript/accounts.tex:24](manuscript/accounts.tex#L24); printed 7.4, page 12.
- prop:ratio: [manuscript/accounts.tex:34](manuscript/accounts.tex#L34); printed 7.1, page 12.
- eq:retainedratio: [manuscript/accounts.tex:36](manuscript/accounts.tex#L36); printed 7.5, page 12.
- eq:ratioidentity: [manuscript/accounts.tex:43](manuscript/accounts.tex#L43); printed 7.6, page 12.
- sec:activity: [manuscript/activity.tex:1](manuscript/activity.tex#L1); printed 4, page 7.
- prop:launch: [manuscript/activity.tex:2](manuscript/activity.tex#L2); printed 4.1, page 7.
- eq:initialcarrier: [manuscript/activity.tex:6](manuscript/activity.tex#L6); printed 4.1, page 7.
- eq:initialports: [manuscript/activity.tex:8](manuscript/activity.tex#L8); printed 4.2, page 7.
- eq:nativedebit: [manuscript/activity.tex:9](manuscript/activity.tex#L9); printed 4.3, page 7.
- eq:receiverstate: [manuscript/activity.tex:10](manuscript/activity.tex#L10); printed 4.4, page 7.
- eq:receivergain: [manuscript/activity.tex:11](manuscript/activity.tex#L11); printed 4.5, page 7.
- eq:nonzero: [manuscript/activity.tex:18](manuscript/activity.tex#L18); printed 4.6, page 7.
- eq:initialreceiverpower: [manuscript/activity.tex:27](manuscript/activity.tex#L27); printed 4.7, page 7.
- prop:credit: [manuscript/activity.tex:34](manuscript/activity.tex#L34); printed 4.2, page 7.
- eq:prepared: [manuscript/activity.tex:36](manuscript/activity.tex#L36); printed 4.8, page 7.
- eq:creditsign: [manuscript/activity.tex:40](manuscript/activity.tex#L40); printed 4.9, page 7.
- eq:reverser: [manuscript/activity.tex:44](manuscript/activity.tex#L44); printed 4.10, page 7.
- sec:candidate: [manuscript/candidate.tex:1](manuscript/candidate.tex#L1); printed 1, page 2.
- tab:status: [manuscript/candidate.tex:14](manuscript/candidate.tex#L14); printed 1, page 2.
- sec:drive: [manuscript/candidate.tex:20](manuscript/candidate.tex#L20); printed 1.1, page 2.
- eq:registration: [manuscript/candidate.tex:22](manuscript/candidate.tex#L22); printed 1.1, page 2.
- eq:drive: [manuscript/candidate.tex:28](manuscript/candidate.tex#L28); printed 1.2, page 2.
- sec:ports: [manuscript/candidate.tex:35](manuscript/candidate.tex#L35); printed 1.2, page 2.
- eq:tents: [manuscript/candidate.tex:37](manuscript/candidate.tex#L37); printed 1.3, page 2.
- eq:ports: [manuscript/candidate.tex:43](manuscript/candidate.tex#L43); printed 1.4, page 3.
- eq:storages: [manuscript/candidate.tex:48](manuscript/candidate.tex#L48); printed 1.5, page 3.
- sec:exchange: [manuscript/candidate.tex:55](manuscript/candidate.tex#L55); printed 1.3, page 3.
- eq:system: [manuscript/candidate.tex:57](manuscript/candidate.tex#L57); printed 1.6, page 3.
- tab:units: [manuscript/candidate.tex:78](manuscript/candidate.tex#L78); printed 2, page 3.
- sec:capacity: [manuscript/capacity.tex:1](manuscript/capacity.tex#L1); printed 5, page 8.
- thm:capacity: [manuscript/capacity.tex:4](manuscript/capacity.tex#L4); printed 5.1, page 8.
- eq:Z2: [manuscript/capacity.tex:6](manuscript/capacity.tex#L6); printed 5.1, page 8.
- eq:chiralityidentity: [manuscript/capacity.tex:12](manuscript/capacity.tex#L12); printed 5.2, page 8.
- eq:floor: [manuscript/capacity.tex:13](manuscript/capacity.tex#L13); printed 5.3, page 8.
- eq:netcapacity: [manuscript/capacity.tex:14](manuscript/capacity.tex#L14); printed 5.4, page 8.
- eq:coherentcapacity: [manuscript/capacity.tex:17](manuscript/capacity.tex#L17); printed 5.5, page 8.
- eq:invariantderivatives: [manuscript/capacity.tex:25](manuscript/capacity.tex#L25); printed 5.6, page 8.
- eq:phasebound: [manuscript/capacity.tex:34](manuscript/capacity.tex#L34); printed 5.7, page 8.
- prop:phase: [manuscript/capacity.tex:46](manuscript/capacity.tex#L46); printed 5.2, page 9.
- sec:domainfailures: [manuscript/domain.tex:1](manuscript/domain.tex#L1); printed A, page 13.
- prop:domainexchange: [manuscript/domain.tex:4](manuscript/domain.tex#L4); printed A.1, page 13.
- eq:boundaryprep: [manuscript/domain.tex:9](manuscript/domain.tex#L9); printed A.1, page 14.
- eq:boundaryderivative: [manuscript/domain.tex:14](manuscript/domain.tex#L14); printed A.2, page 14.
- prop:domainhybrid: [manuscript/domain.tex:21](manuscript/domain.tex#L21); printed A.2, page 14.
- eq:fastports: [manuscript/domain.tex:28](manuscript/domain.tex#L28); printed A.3, page 14.
- eq:fastcore: [manuscript/domain.tex:33](manuscript/domain.tex#L33); printed A.4, page 14.
- eq:fastspan: [manuscript/domain.tex:42](manuscript/domain.tex#L42); printed A.5, page 14.
- sec:hybrid: [manuscript/hybrid.tex:1](manuscript/hybrid.tex#L1); printed 6, page 9.
- eq:tuple: [manuscript/hybrid.tex:3](manuscript/hybrid.tex#L3); printed 6.1, page 9.
- eq:prestage: [manuscript/hybrid.tex:10](manuscript/hybrid.tex#L10); printed 6.2, page 9.
- eq:nativemap: [manuscript/hybrid.tex:12](manuscript/hybrid.tex#L12); printed 6.3, page 9.
- eq:nativeintensity: [manuscript/hybrid.tex:17](manuscript/hybrid.tex#L17); printed 6.4, page 9.
- eq:fullsquare: [manuscript/hybrid.tex:25](manuscript/hybrid.tex#L25); printed 6.5, page 10.
- eq:graphsquare: [manuscript/hybrid.tex:26](manuscript/hybrid.tex#L26); printed 6.6, page 10.
- prop:hybrid: [manuscript/hybrid.tex:30](manuscript/hybrid.tex#L30); printed 6.1, page 10.
- eq:hybrid: [manuscript/hybrid.tex:32](manuscript/hybrid.tex#L32); printed 6.7, page 10.
- eq:hybridbalance: [manuscript/hybrid.tex:36](manuscript/hybrid.tex#L36); printed 6.8, page 10.
- eq:potential: [manuscript/hybrid.tex:48](manuscript/hybrid.tex#L48); printed 6.9, page 10.
- eq:domain: [manuscript/hybrid.tex:53](manuscript/hybrid.tex#L53); printed 6.10, page 10.
- eq:positivebaseline: [manuscript/hybrid.tex:59](manuscript/hybrid.tex#L59); printed 6.11, page 10.
- sec:limits: [manuscript/hybrid.tex:65](manuscript/hybrid.tex#L65); printed 6.1, page 11.
- sec:interpretation: [manuscript/interpretation.tex:1](manuscript/interpretation.tex#L1); printed 8, page 12.
- sec:conclusion: [manuscript/interpretation.tex:12](manuscript/interpretation.tex#L12); printed 8.1, page 13.
- sec:power: [manuscript/power.tex:1](manuscript/power.tex#L1); printed 2, page 4.
- prop:euler: [manuscript/power.tex:2](manuscript/power.tex#L2); printed 2.1, page 4.
- eq:jacobian: [manuscript/power.tex:4](manuscript/power.tex#L4); printed 2.1, page 4.
- eq:core: [manuscript/power.tex:8](manuscript/power.tex#L8); printed 2.2, page 4.
- eq:powers: [manuscript/power.tex:19](manuscript/power.tex#L19); printed 2.3, page 4.
- eq:localwork: [manuscript/power.tex:24](manuscript/power.tex#L24); printed 2.4, page 4.
- eq:balances: [manuscript/power.tex:28](manuscript/power.tex#L28); printed 2.5, page 4.
- eq:integrated: [manuscript/power.tex:33](manuscript/power.tex#L33); printed 2.6, page 4.
- sec:wellposed: [manuscript/wellposed.tex:1](manuscript/wellposed.tex#L1); printed 3, page 5.
- thm:global: [manuscript/wellposed.tex:4](manuscript/wellposed.tex#L4); printed 3.1, page 5.
- eq:space: [manuscript/wellposed.tex:6](manuscript/wellposed.tex#L6); printed 3.1, page 5.
- eq:strong: [manuscript/wellposed.tex:10](manuscript/wellposed.tex#L10); printed 3.2, page 5.
- eq:profilenorms: [manuscript/wellposed.tex:19](manuscript/wellposed.tex#L19); printed 3.3, page 5.
- eq:energynorm: [manuscript/wellposed.tex:28](manuscript/wellposed.tex#L28); printed 3.4, page 5.
- eq:lipschitzbounds: [manuscript/wellposed.tex:35](manuscript/wellposed.tex#L35); printed 3.5, page 5.
- eq:duhamel: [manuscript/wellposed.tex:40](manuscript/wellposed.tex#L40); printed 3.6, page 5.
- eq:dependence: [manuscript/wellposed.tex:46](manuscript/wellposed.tex#L46); printed 3.7, page 5.
- eq:H1estimate: [manuscript/wellposed.tex:56](manuscript/wellposed.tex#L56); printed 3.8, page 6.
- eq:coercive: [manuscript/wellposed.tex:67](manuscript/wellposed.tex#L67); printed 3.9, page 6.
- eq:forcingbound: [manuscript/wellposed.tex:75](manuscript/wellposed.tex#L75); printed 3.10, page 6.

## Source/provenance scope

The current publication order adds its recorded acceptance and the reviewed decimal evaluation of the exact capacity expression; no new theorem, model choice or scientific rerun was added. The old absence of feedback describes the earlier model, while this paper explicitly investigates the new proposal. Current GPT review/bundle and older supporting review were unavailable; see [disposition](evidence/current_review_disposition.md). The external reference supplies methodology only.
