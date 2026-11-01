# NCM-Z-03 v0.1 — Native-source accounting of frozen Z displacement

Author: Hilmir Frímann Halldórsson / pzychozen. GPT supplied the work order and proposed mathematical brief; Codex independently checked definitions, identities and numerical accounting. This is a bounded research review package, not a manuscript or publication action.

## Finding

Every admitted adjacent pair is source-consistent under the stipulated numerical screen. All four frozen displacements close with the established intensity and area contributions, explicit model-to-data residuals, and a separate readout-roundoff residual. Small middle displacement reflects both smaller absolute terms than the first span and substantial cancellation. Native intensity growth does not imply outward placed movement: 2→3 is an explicit counterexample in this window. The 3→4 outward change has a positive macro-size balance exceeding two negative chiral/cross contributions.

## Identity, source authority and arithmetic

The exact unmodified input is `packet/NCM_Z_03_Packet_v0.1/inputs/SELECTED_HISTORY.json`: 8,871 bytes, SHA-256 `a294a4b0bf181adaa2054aa52379c1832a7833e3faa7614d0785aecd709ea09c`. Actual indices are 0,1,2,3,4, without exclusions or an index-4 successor. The selected file matches the original Windows Z-02 file and its unchanged 3,759,247-byte archive (SHA-256 `a0e26a24ce7511498d207bfac4a78da7ed4fa02605f92eed7b4a1a999a218518`). All 25 new packet payload hashes and all 98 prior archive payload hashes were checked; the prior archive has 99 members including its manifest. No old script was run.

Local dynamics/readouts match the supplied accepted snapshots. Local axial_observables.py and Paper G match the packet's two retained Git blob identities, calculated as header-plus-byte SHA-1 without any Git command. z_diagnostics.py has no baseline blob identity in the packet; its actual local SHA-256 is bound and its relevant definitions agree with the proposed formulas. Source authority is the read definitions, not an assumed checkout HEAD. All required originals were available; no fallback or new history search was needed. See SOURCE_CROSSWALK.md, SOURCE_EXCERPTS.txt, SOURCES.json and INPUT_VERIFICATION.json.

Native coefficients are exact rationals ε=1/10, g=1/5, λ_phase=17/100, k=(2,3,4). This is the constructed historical nominal example, distinct from the earlier two-state history and coherence-paper parameters. The historical producer used 120 working decimal digits and saved up to 100 significant digits. Its original radical entrance was not regenerated; enclosure flags were neither used as new certificates nor re-proved. Source identity does not authenticate the old producer.

Observer constants 0.618, 0.577 and 0.244 are exact lifts of the application binary64 values; hexadecimal encodings and integer ratios are retained. No golden-ratio substitution is made. α=1, β=1/2, μ=1, ψ=0, θ*=t*=0; E*=1. Pi/radicals/trigonometry use high precision. This is the first-sample freeze for every interval. It differs from Z-02's interval-native term at the previous scheduled setting after 0→1. No schedule is reconstructed here.

PLAN.json and the computation/checker source hashes were frozen at 2026-11-01T05:31:00.475390+00:00, before primary contributions. No post-freeze science/code correction or threshold change was needed. Primary arithmetic was 80 and 120 decimal digits; there were no binary64 shadow budgets. The residual screen is 10⁻⁶⁵ times max(1, sum of absolute contributing/compared scalar terms); each check stores its actual scale and raw residual. Existing Z-02 binary64 endpoint comparisons use the separately declared 5×10⁻¹² screen. Results remain NUMERICAL_CORROBORATION_ONLY.

## Inherited native identities

Write Ω=x+iy, s_i=|Ω_i|², D=diag(k−s), and L with diagonal −2 and off-diagonal 1. The simultaneous prestage uses u=εDΩ, v=gLΩ, Ω̃=Ω+u+v=MΩ, M=Id+εD+gL. These diagnostic intermediates are reconstructed, not stored observations. No sequential onsite/graph evolution is implied.

Expanding ||Ω+u+v||² proves the exact intensity identity

    ΔI_model = 2ε Σ(k_i s_i − s_i²) − 2g Σ_(i<j)|Ω_i−Ω_j|² + ||u+v||².
    ||u+v||² = ||u||² + 2 Re(u†v) + ||v||².

The three terms are onsite, coupling and finite_increment_square (the source API calls the last remainder). The five-term expansion is an alternative hierarchy, not five additional terms. Phase synchronization preserves each prestage modulus exactly, so its ideal intensity increment is zero. The source API's observed_delta compares its reconstructed prestage to its before-state; this study separately compares the saved after-state through R_I=ΔI_saved−ΔI_model.

For S=xxᵀ+yyᵀ and A=xyᵀ−yxᵀ, C=(A₂₃,A₃₁,A₁₂)=x×y. Thus ΩΩ†=S−iA, whereas the conjugate-pair matrix is S+iA. Direct expansion gives S̃=MSMᵀ, Ã=MAMᵀ, C̃=cof(M)C, and

    ΔA_amplitude = ε(DA+AD) + g(LA+AL) + ε²DAD
                   + εg(DAL+LAD) + g²LAL.

These are onsite_first, coupling_first, onsite_squared, mixed, coupling_squared. The cofactor statement follows from the bilinear cross-product/minor expansion, a polynomial identity valid at singular M. A generic symbolic three-component expansion was identically zero without using an inverse.

The simultaneous kicks are δ_i=λ_phase Σ_(j≠i)sin(3(Arg0 Ω̃_j−Arg0 Ω̃_i)); Arg0(0)=0, and λ_phase=0 bypasses phase extraction. For nonzero pairs, Im[((conj(Ω̃_i)Ω̃_j)/(|Ω̃_i||Ω̃_j|))³] agrees with the harmonic sine. The cube is inside Im. Zero-component tests use the source Arg0 convention, not division by zero.

With d_ij=δ_j−δ_i, conjugate-pair rotation gives A⁺_ij=Ã_ij cos d_ij+S̃_ij sin d_ij. The two increments are phase_existing_area=Ã_ij(cos d_ij−1) and phase_symmetric_pair=S̃_ij sin d_ij, entrywise. The seven C triples use the same cyclic extraction. R_C=ΔC_saved−Σc_t is retained componentwise. Each phase term depends on the actual mixed prestage, so these are algebraic source terms, not independent causal interventions. Both S and A are required; C, W and Γ are not claimed to be closed dynamical states. Raw C remains in Z; W is not substituted.

## Derived finite readout and radial bookkeeping

Let K(a)=λ_vp a/(1+a), H=cos(3 lock)(1,0,1), and r=X*−O=KH+C/2 with O=(0,√3/6,0). Subtracting two rational gains and using b²−a²=(b−a)(b+a) proves

    K(b)−K(a)=q ΔI,   q=λ_vp/[(a+b)(1+a)(1+b)],   a+b>0.

This is a finite divided difference, not a derivative. If a=b>0, the identity still holds; if both are zero, ΔK=0 and q is left undefined. For each parent intensity term B_l use d_l=HqB_l; each area triple contributes d_t=c_t/2. Add d_res=HqR_I+R_C/2 and the recorded arithmetic closure residual to reconstruct the actual saved displacement. The ledgers also retain the alternative intensity-child vectors without double counting them.

For nonzero H, Q=Id−HHᵀ/||H||² annihilates the macro direction, so QΔr=QΔC/2. In particular Δr_y=ΔC_y/2 and Δ(r_x−r_z)=Δ(C_x−C_z)/2. The work-order phrase about the frozen y coordinate means **centered** r_y; the absolute coordinate is X_y=√3/6+C_y/2. This notation clarification was frozen in the plan. At zero H the projector is undefined, not an invented axis.

The signed radial contribution of a displacement term is (r_j+r_i)·d_a, because ||r_j||²−||r_i||²=(r_j+r_i)·(r_j−r_i). The sum includes model-to-data and arithmetic residual contributions. Division by ||r_j||+||r_i|| gives an additive ordinary-radius ledger when the denominator is nonzero. Independently,

    ||r||² = K²||H||² + ||C||²/4 + K H·C.

Endpoint differences yield macro_magnitude, chiral_magnitude and cross_alignment. The last is a cross term involving both magnitude and alignment; it is not a pure angle measurement. These finite-gain, projection and radial compositions are elementary consequences of established definitions, not claims of new fundamental identities, forces or physical energies. Norms of contribution vectors are not additive percentages.

## Endpoints and all four displacement balances

The following tables round only for readability; JSON retains both precisions and residuals. Radius and displacement use placed width units, not native intensity units or a calibrated physical time.

| n | I | κ | C | Frozen radius |
| --- | --- | --- | --- | --- |
| 0 | +9 | +3 | (-0.6049879246, -0.3388966991, -0.08006320569) | +0.3512337119 |
| 1 | +0.2952967756 | +0.54341216 | (-0.02622837317, -0.08993836435, +0.06062000652) | +0.2471246826 |
| 2 | +0.2278934068 | +0.477381825 | (+0.002147278305, -0.05800994086, +0.04700079865) | +0.2298321538 |
| 3 | +0.2354425828 | +0.4852242603 | (+0.001824351502, -0.05167133393, +0.04054532001) | +0.2292416786 |
| 4 | +0.3173892611 | +0.5633731101 | (+0.0004842630967, -0.009365954067, +0.007194280747) | +0.2370425439 |

| Span | Δr=(Δx,Δy,Δz) | ||Δr|| | Δradius |
| --- | --- | --- | --- |
| 0→1 | (+0.1064611582, +0.1244791674, -0.1125770114) | +0.1987526725 | -0.1041090293 |
| 1→2 | (+0.0008760389611, +0.01596421174, -0.02012139071) | +0.02570007519 | -0.01729252877 |
| 2→3 | (+0.001481521907, +0.003169303464, -0.001584754012) | +0.003840681825 | -0.0005904752418 |
| 3→4 | (+0.0148015633, +0.02115268993, -0.00120391213) | +0.02584515374 | +0.007800865379 |

| Span | Onsite ΔI | Graph ΔI | Increment square | Actual ΔI |
| --- | --- | --- | --- | --- |
| 0→1 | -5.203523014 | -10.25785089 | +6.756670678 | -8.704703224 |
| 1→2 | +0.1691186807 | -0.2729609403 | +0.03643889084 | -0.0674033688 |
| 2→3 | +0.1468162741 | -0.1646281056 | +0.02536100744 | +0.007549175952 |
| 3→4 | +0.158907582 | -0.1007577497 | +0.02379684613 | +0.08194667837 |

| Span | Macro-size Δr² | Chiral-size Δr² | Cross-term Δr² | Total Δr² |
| --- | --- | --- | --- | --- |
| 0→1 | -0.1853405684 | -0.1187049641 | +0.2417510209 | -0.06229451162 |
| 1→2 | -0.008263688123 | -0.001718195754 | +0.001734094064 | -0.008247789813 |
| 2→3 | +0.0009815887265 | -0.0003154152833 | -0.0009372451754 | -0.0002710717322 |
| 3→4 | +0.009772971461 | -0.001044366176 | -0.005091184838 | +0.003637420448 |

### 0→1: large intensity decrease, partial spatial cancellation

The graph contribution −10.2578509 and onsite contribution −5.2035230 reinforce the native intensity decrease. The positive square +6.7566707 is material: its children are +0.9967298 onsite², +2.6825856 mixed and +3.0773553 graph². Dropping it would predict a negative final intensity from I₀≈9. The actual final intensity is about 0.2952968.

The macro displacement is (−0.1829186,0,−0.1829186); the chiral displacement is (+0.2893798,+0.1244792,+0.0703416). They oppose in x and z: the net x is positive, z negative. The y increase is wholly chiral. In its seven-term y ledger, coupling_first +0.2040638 and mixed +0.0495824 oppose onsite_first −0.0645448 and coupling_squared −0.0614369; the remaining three terms make smaller signed adjustments. The two phase terms together slightly reduce the y increase.

For squared radius, falling macro and chiral magnitudes give −0.1853406 and −0.1187050, but the cross term rises +0.2417510. Much of the decrease is canceled. In the source-resolved radial ledger the three intensity pathways sum to about −0.1258317; the seven chiral pathways sum to about +0.0635372. This alternate split has a different meaning from the three coarse endpoint terms and must not be mixed with them.

### 1→2: smaller sources, important coordinate cancellation

Onsite +0.1691187 and the square +0.0364389 oppose graph −0.2729609, leaving ΔI=−0.0674034. Inside the square, +0.0263927 onsite² and +0.0818883 graph² are opposed by mixed −0.0718421. The finite square remains relevant.

Macro x and z each decrease 0.0133118. Chiral x increases 0.0141878, almost canceling the macro x change; chiral z decreases 0.0068096, reinforcing the downward displacement. Chiral y increases 0.0159642: coupling_first +0.0325362 and mixed +0.0102830 oppose onsite_first −0.0260113 and two negative squared terms; the two phase terms add approximately +0.00579605. The raw signed components are retained rather than ranked by vector norm.

Macro-size squared radius falls 0.00826369. Chiral-size decrease −0.00171820 and cross increase +0.00173409 almost cancel each other. The net Δradius is −0.0172925. Sources are smaller than in 0→1, but small net x especially is a cancellation result.

### 2→3: increasing native norm, decreasing placed radius

Onsite +0.1468163 and graph −0.1646281 nearly balance. The +0.0253610 square makes ΔI positive, +0.00754918; ignoring this finite term would reverse the predicted intensity sign. Its children are +0.0248938, −0.0489212 and +0.0493884.

Macro x and z each rise 0.00164299. Chiral x falls 0.000161463 and chiral z falls 0.00322774. Thus x rises while z falls, despite a larger native norm. Chiral y rises only 0.00316930 after coupling_first +0.0182892, onsite_first −0.0169507, mixed +0.00577696, two negative square terms and phase terms +0.000858491 and −0.00206638 are combined. This is not inactivity.

Macro-size squared radius rises +0.000981589, but chiral-size −0.000315415 and cross −0.000937245 outweigh it. Δr²=−0.000271072 and Δradius=−0.000590475. The source-resolved radial sum has sum of absolute terms about 223.9 times its net magnitude: a strong cancellation measure, not percentages or an error bound. The sign is stable at both precisions and far above the declared screen.

### 3→4: outward radius, slightly decreasing height

Onsite +0.1589076 exceeds graph −0.1007577; the square adds +0.0237968, giving ΔI=+0.0819467. Its +0.0276978 onsite² and +0.0302273 graph² oppose mixed −0.0341282. The norm-dependent macro x/z rise +0.0154716 each.

The chiral displacement is (−0.000670044,+0.0211527,−0.0166755), so the net is (+0.0148016,+0.0211527,−0.00120391). The radius grows although height falls. In the y budget, coupling_first +0.0164316 and phase_symmetric_pair +0.0144813 are substantial positive terms; onsite_first −0.0151054 opposes them. The other four terms complete the +0.0211527 total. Both amplitude and phase contributions matter; phase still changes intensity by exactly zero in the ideal formula.

The coarse squared-radius balance is +0.00977297−0.00104437−0.00509118=+0.00363742. Macro growth exceeds the chiral-size and cross-term decreases. In the alternative source-resolved radial ledger, intensity pathways total about +0.0101601 and chiral pathways about −0.00652271. In particular phase_symmetric_pair gives +0.0144813 in y but −0.00478717 in radial balance. A contribution cannot be called simply “outward” from one positive coordinate. This explains the final reversal without an added force or clock.

## Verification, uncertainty and stopping boundary

Intensity sums were checked against directly computed prestage norms and independently evaluated inner products. Five-term area sums were checked against direct real cross products, matrix congruence and minor/cofactor evaluation. Phase predictions were checked using rotated conjugate pair products, without constructing a full post-sync complex vector. Pair magnitudes and phase diagonal intensities were checked independently. Arg0 sine kicks agreed with normalized-pair cubes where defined. The finite norm gain, full transverse projector, y and x−z identities, fine radial sum and coarse radial sum were checked for every pair.

There were exactly eight primary prestage/kick/budget evaluations: four at 80 digits and the same four at 120 digits. These are native-stage algebra evaluations and are reported as such. Each began afresh from an original saved row. Zero trajectory advances, full complex post-sync outputs, index-4 successors or new admitted states occurred. No project modules, old suites, producers, app workers or EMA were executed. Thirteen predeclared synthetic fixtures were evaluated at both precisions, with two full synthetic budgets per precision (four total, separate from the primary count). The other fixtures test zero/undefined cases, singularity, nontrivial phase cubing, cancellation and equal-norm/changing-C or equal-radius/nonzero-displacement cases. A generic cofactor polynomial proof was also checked symbolically.

All 1,851 logged assertions passed; many are individual scalar 80/120 comparisons, not independent experiments. Maximum absolute saved-after residual is 1.05422×10⁻⁸¹ at 80 digits and 1.27026×10⁻¹⁰⁰ at 120 digits. The 80-digit evaluation cannot resolve residuals at the finer stored-rounding scale. Maximum raw discrepancy across all compared 80/120 numerical fields is 2.65813×10⁻⁷⁷ (including cancellation ratios); all pass their explicit scaled screen. No historical transition failed, so none was excluded from attribution. Residual signs near rounding scale have no scientific interpretation. Material signs and comparisons discussed above are resolved; exact structural zero y macro and phase intensity increments follow algebraically, not from rounded zeros.

An independent portable checker used copies only, recomputed endpoint observables through conjugate pairs and verified ledger closure. All 80 checks passed. It did not rerun stage/kick budgets, so the primary count remains eight. This checks portability of the delivered data/accounting with the existing interpreter, not cross-platform byte reproducibility or an independently authenticated producer. The exact commands and environment are included.

The three figures use only existing ledger coordinates and signed terms. All four intervals are visible, with independent panel scales explicitly labeled. Intensity, placed squared radius and uncalibrated update spans are distinguished. All three original PNGs were visually inspected for clipping, signs and labels. No geometry scan, new opening classification, animation, invented intermediate state or generated illustration was used.

These are numerical corroborations on rounded nominal states, not interval enclosures, an exact trajectory proof or independent physical causes. The history is deliberately constructed and only four spans long. It supports no inference of acceleration, attraction, energy transfer, asymptotic equilibrium or general behavior beyond this window. Physical core motion, transport through openings, fields and fixed-support/two-arrangement interpretations remain unestablished. No new issue blocks this bounded source accounting; interpretation is left for GPT and the author before any further work order. No publication or successor investigation is started.

## Package index and preservation

STATE_SNAPSHOTS.json contains I, κ, S, A, C, K, centered/absolute frozen placement and radius at all five endpoints. NATIVE_INTENSITY_BUDGET.json contains parent/child terms and saved-after residuals. NATIVE_CHIRAL_BUDGET.json retains each signed A matrix and C vector, pair/congruence checks and saved-after residuals. FROZEN_Z_SOURCE_BUDGET.json carries all terms and residuals into the actual displacement. RADIAL_TRANSVERSE_ACCOUNTING.json contains fine radial contributions, the independent three-part coarse split and transverse accounting. PASSIVE_PRESTAGES.json is explicitly diagnostic, not a history extension. All use NUMERIC_POLICY.json and run keys 80/120.

The archive includes the exact input, packet context/evidence, actual source snapshots, standalone analysis and copy-only checker, frozen plan, commands, environment, checks, three figures and before/after hashes. Scratch copies and matplotlib caches are excluded. Preservation is a bounded audit of the 12 actual original input/source files listed in PRESERVATION_BEFORE.json, with results in PRESERVATION_AFTER.json; it is not a whole-checkout assertion. The external REVIEW_RECEIPT.json records the final ZIP bytes, SHA-256 and member verification. Every payload member is hashed; the internal manifest excludes itself.
