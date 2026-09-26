# K2c — Paper F analytic parity P7/P8

K2C_STATUS = PASS. Exactly five new files; existing sources, tests, fixtures, papers and research are unchanged.

Starting HEAD: `22b3009d51e4e47efda48acf52d234d00907fe2c`. The final commit is the commit introducing this receipt; resolve it with:

```text
git log --diff-filter=A --format=%H -- kernel_physics/K2C_PAPER_F_ANALYTIC_PARITY_VALIDATION.json
```

The published closeout supplies literal final HEAD and verified origin/main. A commit cannot contain its own literal hash.

## Status

```text
STARTING_HEAD = 22b3009d51e4e47efda48acf52d234d00907fe2c
K2C_STATUS = PASS
P7 = PASS
P8 = PASS
P7_EXACT_ONE_STEP = PASS
P7_FINITE_N_COEFFICIENTS = PASS
P7_KAPPA_INFINITY_ORACLE_PAPER = PASS
P7_KAPPA_INFINITY_ORACLE_PAPER_CHECK = PASS
P7_KAPPA_INFINITY_RUNTIME_TESTED = NO
P7_FULL_MAP_ORACLE = PASS
P7_RUNTIME_C = PASS
P7_RUNTIME_ANGLE = PASS
P7_SIGN_PREDICTIONS = PASS
P7_REMAINDER_QUALIFICATION = PASS
P8_EXACT_ONE_STEP_DERIVATIVE = PASS
P8_99_OVER_2500 = PASS
P8_243_OVER_160_FALSIFIER = PASS
P8_HIGH_PRECISION_DERIVATIVE = PASS
P8_RUNTIME_FINITE_DIFFERENCES = PASS
P8_LIMITING_DERIVATIVE_ORACLE_PAPER = PASS
P8_LIMITING_DERIVATIVE_RUNTIME_TESTED = NO
ORACLE_IMPORT_BOUNDARY_K2C = PASS
PRODUCTION_SOURCE_CHANGED = 0
EXISTING_TEST_CHANGED = 0
PAPERS_CHANGED = 0
PAPER_CHANGED = 0
RESEARCH_CHANGED = 0
K0_CHANGED = 0
K1_CHANGED = 0
K2A_CHANGED = 0
K2B_CHANGED = 0
FIXTURE_CHANGED = 0
OPTION_B_MODULE_CHANGED = 0
NEW_K2C_TEST_COUNT = 10
TOTAL_TRACKED_TESTS = 298
TRACKED_TEST_RESULT = PASS
OPTIONAL_LOCAL_TEST_RESULT = PASS
FILES_CREATED = 5
FILES_MODIFIED = 0
K2_READY_FOR_FINAL_CLOSEOUT = YES
EXACT_SYMBOLIC_CHECKS = 85
ORACLE_PAPER_ONLY_CHECKS = 2
NEGATIVE_FALSIFIER_CHECKS = 13
HIGH_PRECISION_FULL_MAP_CHECKS = 204
ASYMPTOTIC_QUALIFICATION_CHECKS = 36
BINARY64_RUNTIME_COMPARISONS = 250
MAX_P7_STATE_ERROR = 1.160078056092935751714616853602483370233e-16
MAX_P7_C_ERROR = 3.866566180452417710414388602301928318019e-18
MAX_P7_ANGLE_ERROR = 3.964411138584479236381405355893590419858e-16
MAX_P7_ANGLE_BOUND_FRACTION = 0.006974265830653322057092787972539273916132
MAX_P8_FD_ENVELOPE_FRACTION = 0.8129333720104450265080969613752843440938
```

## Environment and authority

```json
{
  "conda": "torment",
  "python": "3.11.15 | packaged by Anaconda, Inc. | (main, Mar 11 2026, 17:12:15) [MSC v.1942 64 bit (AMD64)]",
  "executable": "C:\\Users\\Notandi\\miniconda3\\envs\\torment\\python.exe",
  "platform": "Windows-10-10.0.26200-SP0",
  "numpy": "2.4.4",
  "sympy": "1.14.0",
  "mpmath": "1.3.0",
  "oracle_decimal_digits": 80,
  "independent_precision_crosscheck_digits": 100
}
```

The publication and accepted draft contain 106 identical display equations. The publication controls orientation and corrected full-composition coefficients. The earlier review supplies the bounded update-4 sign-change locator; its superseded isolated-phase interpretation is not adopted. No verifier was executed or used as an expected-value generator.

| Source | SHA-256 |
| --- | --- |
| papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md | `8c9419b20a0899857e68f4b191e7321cfc99f5286f149504f5d82a3e75db4fd5` |
| papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/PAPER_F_DRAFT_v0.2.md | `bcb08b70804051861094142f80d6b057542f22848850cdc3458816ed97ae54a3` |
| papers/PAPER_F/support/repository/research/paper_F_transverse_normal_form/paper_f_exact_checks_v0_2.py | `e661af6536e9ec37c09c8126574e775f262e03c8ed49ca0e02b0d13cb010ff4d` |
| papers/PAPER_F/support/repository/research/GATE_TORUS_INVESTIGATION_v0.1/CLAUDE_GENERIC_TRANSVERSE_HARMONICS_REVIEW.md | `a7114abb47bf61829cc901876a04be88e3438bbe55d529d6118483b152de619d` |
| kernel_physics/tests/parity_oracles/paper_f_oracle.py | `b702de1145741da814bf88b1e3b99a76701d9170eedabfdb60edd42a89b4e9f7` |
| kernel_physics/tests/test_parity_p07_p08.py | `7e958943f73cb4358f0094c1972303c9a91ed44bb99527b73557783ea896fec4` |
| kernel_physics/tests/test_parity_oracle_boundaries_k2c.py | `2180702923028ece9fee10d31ca39d7d2d84ddfe336060f6fd2b2928f15b2484` |

Oracle dependency graph: `paper_f_oracle.py → sympy, mpmath`. No project-local oracle is reused; the Paper-A full map is independently reconstructed locally. The new AST audit bans dynamic execution and file-loading escape routes. Every P7/P8 test runs under a guard rejecting paper/research/verifier reads.

## Exact coefficient reconstruction

The basis is e=(1,1,1), u=(1,-1,0)/sqrt(2), v=(1,1,-2)/sqrt(6), with u×v=e/sqrt(3). Set q=u cos(phi)+v sin(phi), q_perp=-u sin(phi)+v cos(phi), and Omega_0=e+i h q. The signed local angle is atan2(-C·q, C·q_perp); its denominator stays positive for the tested chart.

Direct polynomial cross products reproduce all three exact one-step projections (23). The leading signed coefficient is -eps^2/(36a), becoming -1/5760. The independent three-root quotient algebra t^3=t/2+S/(3 sqrt(6)) expands the defining amplitude cubic and the atan/sine phase series. Common modes are retained. It reconstructs (31), (33), (34), (49), (50), T0, Ps and both angular rows. Denominator differentiation is included.

The resulting coefficients agree exactly through three routes: reconstructed matrix lift, scalar recurrence (35–36), and finite geometric closed form (39).

| n | Exact kappa_n |
| --- | --- |
| 1 | -1/5760 |
| 2 | -347/7200000 |
| 3 | -59629/9000000000 |
| 4 | 71745997/11250000000000 |
| 5 | 145603166279/14062500000000000 |
| 6 | 203126174530303/17578125000000000000 |
| 7 | 32730981759886837/2746582031250000000000 |
| 8 | 660579363515112919919/54931640625000000000000000 |

`kappa_infinity = 13375/1107936648`. The parameter-general scalar geometric sum is checked against (40), and the exact resolvent independently agrees. This is ORACLE_VERSUS_PAPER_ONLY; no runtime limit is tested.

The full one-step lambda coefficient is `eps*a^2/4 + 47*a^4/32`, exactly `99/2500` at the historical point. The independent phase-only polynomial calculation gives `243/160` for its different observable. The differentiated exact resolvent gives `34494041501/849664304944` for the limiting lambda derivative, again ORACLE_VERSUS_PAPER_ONLY.

## P7 bounded full-map parity

Use eps=1/20, g=1/5, k=(1,1,1), lambda=0; h=0.02 and 0.01; phi=±pi/12; exactly eight updates. The ideal full map is evaluated at 80 digits and cross-checked at 100 digits. Runtime starts from a once-rounded seed and uses step3 and z_chiral. State and C component bounds are 1e-13; the frozen angular bound is 256×2^-52 = 5.6843418860808015e-14 radians. Signs are enforced only above four times that bound.

| phi/pi | h | n | Oracle angle | Runtime angle | max |state error| | max |C error| | |angle error| | Sign status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1/12 | .02 | 1 | -2.777865743140e-11 | -2.777855138804e-11 | 4.372696660226e-17 | 3.866566180452e-18 | 1.060433689431e-16 | RESOLVED_PASS |
| 1/12 | .02 | 2 | -7.712376199479e-12 | -7.712257846431e-12 | 2.499403200073e-17 | 2.125547965801e-18 | 1.183530479157e-16 | RESOLVED_PASS |
| 1/12 | .02 | 3 | -1.061514753964e-12 | -1.061385464798e-12 | 3.619804535884e-17 | 4.389301066452e-19 | 1.292891658350e-16 | RESOLVED_PASS |
| 1/12 | .02 | 4 | 1.018901250891e-12 | 1.019116972438e-12 | 8.412967634161e-17 | 2.740802912311e-19 | 2.157215466245e-16 | RESOLVED_PASS |
| 1/12 | .02 | 5 | 1.655145564030e-12 | 1.655542005144e-12 | 1.008316967242e-16 | 1.600981114711e-19 | 3.964411138584e-16 | RESOLVED_PASS |
| 1/12 | .02 | 6 | 1.847403313873e-12 | 1.847704788684e-12 | 6.019055308508e-17 | 8.599082543286e-20 | 3.014748105047e-16 | RESOLVED_PASS |
| 1/12 | .02 | 7 | 1.905221554108e-12 | 1.905561013238e-12 | 6.851135324035e-17 | 3.499171660619e-20 | 3.394591303226e-16 | RESOLVED_PASS |
| 1/12 | .02 | 8 | 1.922580594847e-12 | 1.922963816776e-12 | 3.528549766977e-17 | 2.104308693318e-20 | 3.832219289114e-16 | RESOLVED_PASS |
| 1/12 | .01 | 1 | -1.736124855418e-12 | -1.736063455545e-12 | 1.945565844429e-17 | 1.907127061894e-18 | 6.139987317642e-17 | RESOLVED_PASS |
| 1/12 | .01 | 2 | -4.819642111004e-13 | -4.819575220652e-13 | 1.011049585397e-16 | 7.393770447540e-19 | 6.689035169644e-18 | RESOLVED_PASS |
| 1/12 | .01 | 3 | -6.627700107412e-14 | -6.616691632951e-14 | 6.995282487108e-18 | 3.864900305866e-19 | 1.100847446022e-16 | SIGN_NOT_NUMERICALLY_RESOLVED |
| 1/12 | .01 | 4 | 6.375099698726e-14 | 6.385005958912e-14 | 7.211017383722e-17 | 2.042163557327e-19 | 9.906260185999e-17 | SIGN_NOT_NUMERICALLY_RESOLVED |
| 1/12 | .01 | 5 | 1.035166717260e-13 | 1.035385178702e-13 | 7.124440144942e-17 | 4.609618769832e-20 | 2.184614422244e-17 | SIGN_NOT_NUMERICALLY_RESOLVED |
| 1/12 | .01 | 6 | 1.155328448509e-13 | 1.156211413497e-13 | 5.306488895745e-17 | 1.738735781716e-20 | 8.829649880979e-17 | SIGN_NOT_NUMERICALLY_RESOLVED |
| 1/12 | .01 | 7 | 1.191464879138e-13 | 1.191253049858e-13 | 7.932833712336e-17 | 9.998437086142e-21 | 2.118292798514e-17 | SIGN_NOT_NUMERICALLY_RESOLVED |
| 1/12 | .01 | 8 | 1.202314244983e-13 | 1.201027975619e-13 | 1.160078056093e-16 | 5.223469720181e-21 | 1.286269364132e-16 | SIGN_NOT_NUMERICALLY_RESOLVED |
| -1/12 | .02 | 1 | 2.777865743140e-11 | 2.777855138804e-11 | 4.372696660226e-17 | 3.866566180452e-18 | 1.060433689431e-16 | RESOLVED_PASS |
| -1/12 | .02 | 2 | 7.712376199479e-12 | 7.712257846431e-12 | 2.499403200073e-17 | 2.125547965801e-18 | 1.183530479157e-16 | RESOLVED_PASS |
| -1/12 | .02 | 3 | 1.061514753964e-12 | 1.061385464798e-12 | 3.619804535884e-17 | 4.389301066452e-19 | 1.292891658350e-16 | RESOLVED_PASS |
| -1/12 | .02 | 4 | -1.018901250891e-12 | -1.019116972438e-12 | 8.412967634161e-17 | 2.740802912311e-19 | 2.157215466245e-16 | RESOLVED_PASS |
| -1/12 | .02 | 5 | -1.655145564030e-12 | -1.655542005144e-12 | 1.008316967242e-16 | 1.600981114711e-19 | 3.964411138584e-16 | RESOLVED_PASS |
| -1/12 | .02 | 6 | -1.847403313873e-12 | -1.847704788684e-12 | 6.019055308508e-17 | 8.599082543286e-20 | 3.014748105047e-16 | RESOLVED_PASS |
| -1/12 | .02 | 7 | -1.905221554108e-12 | -1.905561013238e-12 | 6.851135324035e-17 | 3.499171660619e-20 | 3.394591303226e-16 | RESOLVED_PASS |
| -1/12 | .02 | 8 | -1.922580594847e-12 | -1.922963816776e-12 | 3.528549766977e-17 | 2.104308693318e-20 | 3.832219289114e-16 | RESOLVED_PASS |
| -1/12 | .01 | 1 | 1.736124855418e-12 | 1.736063455545e-12 | 1.945565844429e-17 | 1.907127061894e-18 | 6.139987317642e-17 | RESOLVED_PASS |
| -1/12 | .01 | 2 | 4.819642111004e-13 | 4.819575220652e-13 | 1.011049585397e-16 | 7.393770447540e-19 | 6.689035169644e-18 | RESOLVED_PASS |
| -1/12 | .01 | 3 | 6.627700107412e-14 | 6.616691632951e-14 | 6.995282487108e-18 | 3.864900305866e-19 | 1.100847446022e-16 | SIGN_NOT_NUMERICALLY_RESOLVED |
| -1/12 | .01 | 4 | -6.375099698726e-14 | -6.385005958912e-14 | 7.211017383722e-17 | 2.042163557327e-19 | 9.906260185999e-17 | SIGN_NOT_NUMERICALLY_RESOLVED |
| -1/12 | .01 | 5 | -1.035166717260e-13 | -1.035385178702e-13 | 7.124440144942e-17 | 4.609618769832e-20 | 2.184614422244e-17 | SIGN_NOT_NUMERICALLY_RESOLVED |
| -1/12 | .01 | 6 | -1.155328448509e-13 | -1.156211413497e-13 | 5.306488895745e-17 | 1.738735781716e-20 | 8.829649880979e-17 | SIGN_NOT_NUMERICALLY_RESOLVED |
| -1/12 | .01 | 7 | -1.191464879138e-13 | -1.191253049858e-13 | 7.932833712336e-17 | 9.998437086142e-21 | 2.118292798514e-17 | SIGN_NOT_NUMERICALLY_RESOLVED |
| -1/12 | .01 | 8 | -1.202314244983e-13 | -1.201027975619e-13 | 1.160078056093e-16 | 5.223469720181e-21 | 1.286269364132e-16 | SIGN_NOT_NUMERICALLY_RESOLVED |

For h=.02, both orientations have resolved opposite signs: updates 1–3 carry the first-step sign, and updates 4–8 carry the reversed sign. For h=.01, only updates 1–2 are resolved; all twelve later orientation/update cases are explicitly SIGN_NOT_NUMERICALLY_RESOLVED. No long-run interpretation follows.

## P7 finite-amplitude remainder qualification

Each row retains remainder = full_oracle_angle − kappa_n h^4 sin(6phi). The normalized quantity is remainder/h^6. Values below are for +pi/12; -pi/12 has exactly opposite signs to the verified precision. The JSON contains all 32 individual cases. No universal ratio, empirical envelope or equality between jet and finite-amplitude map is imposed.

| n | Remainder, h=.02 | R/h^6, h=.02 | Remainder, h=.01 | R/h^6, h=.01 |
| --- | --- | --- | --- | --- |
| 1 | -8.796536271810e-16 | -1.374458792470e-05 | -1.374430670153e-17 | -1.374430670153e-05 |
| 2 | -1.265088367564e-15 | -1.976700574318e-05 | -1.976665594855e-17 | -1.976665594855e-05 |
| 3 | -1.443642853200e-15 | -2.255691958125e-05 | -2.255662967141e-17 | -2.255662967141e-05 |
| 4 | -1.486261997752e-15 | -2.322284371488e-05 | -2.322256829612e-17 | -2.322256829612e-05 |
| 5 | -1.494905632979e-15 | -2.335790051529e-05 | -2.335762798359e-17 | -2.335762798359e-05 |
| 6 | -1.496265851662e-15 | -2.337915393222e-05 | -2.337888193730e-17 | -2.337888193730e-05 |
| 7 | -1.496330884398e-15 | -2.338017006872e-05 | -2.337989817344e-17 | -2.337989817344e-05 |
| 8 | -1.496257033760e-15 | -2.337901615251e-05 | -2.337874427806e-17 | -2.337874427806e-05 |

The paired normalized values remain close for each fixed n. This is consistent with the accepted fixed-n O(h^6) qualification, without certifying a uniform-in-n remainder or a finite-amplitude equality.

## P8 finite-amplitude derivative and error budget

The exact finite-amplitude derivative differentiates w_j(lambda)=v_j exp(i lambda H_j), then C and atan2. It agrees with independent mpmath differentiation at 80 digits. All targets and complete FD envelopes are computed before runtime evolution and checked at 100 digits. The pre-runtime oracle capture SHA-256 is `6c49777f94eaed77e091ee4720a658354be2704903414732d95c965eaa3c8f0f`.

| phi/pi | h | Oracle derivative | Derivative/[h^4 sin(6phi)] | Higher-order remainder/h^6 |
| --- | --- | --- | --- | --- |
| 1/12 | .02 | 6.335085784049e-09 | 3.959428615031e-02 | -1.428462423192e-02 |
| 1/12 | .01 | 3.959857143440e-10 | 3.959857143440e-02 | -1.428565603656e-02 |
| -1/12 | .02 | -6.335085784049e-09 | 3.959428615031e-02 | 1.428462423192e-02 |
| -1/12 | .01 | -3.959857143440e-10 | 3.959857143440e-02 | 1.428565603656e-02 |

The finite-h target remains distinct from `(99/2500) h^4 sin(6phi)`. The displayed coefficient approaches 0.0396 as h decreases.

For every delta, truncation is the high-precision centered-difference bias. Input quantization, componentwise binary64 evaluation, FD arithmetic, and angle evaluation are kept separately. The sum gives the acceptance envelope, without post-hoc widening. The conservative error model uses u=2^-52, gamma_n=n*u/(1-n*u), gamma_32 for expanded amplitude arithmetic, gamma_8 for phase/polar/dot operations, and two-u elementary-function allowances. Rectangular state errors propagate through the cross product. Angular perturbations use the atan2 differential and asin(distance/radius). This is a bounded numerical model, not a general vendor-libm theorem. Full formulas are in the independent oracle.

| phi/pi | delta | Oracle derivative | Runtime FD | Absolute discrepancy | Truncation | Roundoff | Angle uncertainty | Total envelope | Fraction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1/12 | .01 | 6.335085784049e-09 | 6.388343459014e-09 | 5.325767496456e-11 | 5.326480418948e-11 | 1.200798188092e-11 | 2.401782120828e-13 | 6.551296428248e-11 | 8.129333720104e-01 |
| 1/12 | .001 | 6.335085784049e-09 | 6.335631349493e-09 | 5.455654434334e-13 | 5.285770170244e-13 | 1.118326162639e-10 | 2.401782089217e-12 | 1.147629753702e-10 | 4.753845407665e-03 |
| 1/12 | .0001 | 6.335085784049e-09 | 6.335083364474e-09 | 2.419575175211e-15 | 5.285366364008e-15 | 1.110637056533e-09 | 2.401782088901e-11 | 1.134660162789e-09 | 2.132422776935e-06 |
| -1/12 | .01 | -6.335085784049e-09 | -6.388343459014e-09 | 5.325767496456e-11 | 5.326480418948e-11 | 1.200798188092e-11 | 2.401782120828e-13 | 6.551296428248e-11 | 8.129333720104e-01 |
| -1/12 | .001 | -6.335085784049e-09 | -6.335631349493e-09 | 5.455654434334e-13 | 5.285770170244e-13 | 1.118326162639e-10 | 2.401782089217e-12 | 1.147629753702e-10 | 4.753845407665e-03 |
| -1/12 | .0001 | -6.335085784049e-09 | -6.335083364474e-09 | 2.419575175211e-15 | 5.285366364008e-15 | 1.110637056533e-09 | 2.401782088901e-11 | 1.134660162789e-09 | 2.132422776935e-06 |

The roundoff column includes input quantization and centered subtraction/division. The JSON separately retains those contributions, both observed endpoint angles, all exact targets, and the 1e-60/delta oracle precision guard.

The wrong-law envelope is centered at `(243/160) h^4 sin(6phi)` and includes its own independently computed phase-only finite-h correction plus the full FD uncertainty. Both the full-map oracle and actual runtime FD lie outside that envelope. This falsifies the wrong coefficient through the observable, not merely through rational inequality.

| phi/pi | delta | Runtime distance beyond isolated envelope | Margin / complete FD envelope |
| --- | --- | --- | --- |
| 1/12 | .01 | 2.364836648916e-07 | 3.609723166729e+03 |
| 1/12 | .001 | 2.364871269900e-07 | 2.060656986517e+03 |
| 1/12 | .0001 | 2.354677777876e-07 | 2.075227328057e+02 |
| -1/12 | .01 | 2.364836648916e-07 | 3.609723166729e+03 |
| -1/12 | .001 | 2.364871269900e-07 | 2.060656986517e+03 |
| -1/12 | .0001 | 2.354677777876e-07 | 2.075227328057e+02 |

## Evidence counts and claim boundaries

| Evidence class | Predicates | Role |
| --- | --- | --- |
| EXACT_SYMBOLIC_CHECKS | 85 | Exact scalar identities, including matrix entries; not theorem count. |
| ORACLE_PAPER_ONLY_CHECKS | 2 | Two exact limiting constants; no runtime infinity comparison. |
| NEGATIVE_FALSIFIER_CHECKS | 13 | One exact distinct-coefficient predicate, six oracle separations, six runtime exclusions. |
| HIGH_PRECISION_FULL_MAP_CHECKS | 204 | 80/100-digit agreement, differentiated observable and source-defined sign/mirror checks. |
| ASYMPTOTIC_QUALIFICATION_CHECKS | 36 | Distinct finite-h/jet values and recorded normalized remainders; no ratio threshold. |
| BINARY64_RUNTIME_COMPARISONS | 250 | State/C/angle values, resolved signs and six runtime centered differences. |

The two import/file-boundary test methods are reported separately from these mathematical predicates. PASS supports exact coefficient algebra, bounded full-map/runtime parity and the one-step local finite-amplitude lambda sensitivity. It does not support:

- GLOBAL ATTRACTOR CLAIM
- SIX-AXIS PHYSICAL SELECTOR
- INFINITE-TIME CERTIFICATION FROM EIGHT STEPS
- JET == FINITE AMPLITUDE
- FLOAT64 CERTIFICATION OF KAPPA_INFINITY
- FLOAT64 CERTIFICATION OF LIMITING LAMBDA DERIVATIVE
- 243/160 AS FULL-COMPOSITION COEFFICIENT
- LARGE-LAMBDA EXTRAPOLATION
- uniform-in-n remainder from fixed-n expansion
- geometry/dynamics coupling
- arbitrary-amplitude or higher-order lambda differentiation

Limiting coefficient sums use |a|<1, |r|<1 and a!=0. Limiting observed-angle interpretation additionally retains Paper F's local nonzero chart, 0<r<a<1, nonresonance and parametric hypotheses.

## Test execution and preservation

Environment activation: conda activate torment.

```text
python -B -m unittest kernel_physics.tests.test_parity_oracle_boundaries_k2c kernel_physics.tests.test_parity_p07_p08 -v -f
```

10 tests PASS in 2.970 seconds.

```text
python -B -m unittest discover -s kernel_physics/tests -t . -p "test_*.py" -v
```

298 tests PASS in 352.351 seconds.

```text
python -B -m unittest kernel_physics.tests.test_boundary_response kernel_physics.tests.test_srg kernel_physics.tests.test_operating_region kernel_physics.tests.test_boundary_pipeline -v
```

30 tests PASS in 0.658 seconds.

The tracked suite ran in clean detached snapshot `c0d03d3af404d219ff30b207e58c9a386e179ef2`. Its three new executable sources are byte-identical to the final files. The checkout was clean before and after. These receipts were written after test completion.

The 30 preserved Option-B local-only tests ran separately after the tracked suite. They do not change public support status. All 699 starting tracked files and four local-only test files retain their starting SHA-256 hashes. Existing untracked material remains untouched.

Exactly these five new paths comprise K2c:

- `kernel_physics/tests/parity_oracles/paper_f_oracle.py`
- `kernel_physics/tests/test_parity_p07_p08.py`
- `kernel_physics/tests/test_parity_oracle_boundaries_k2c.py`
- `kernel_physics/K2C_PAPER_F_ANALYTIC_PARITY_VALIDATION.md`
- `kernel_physics/K2C_PAPER_F_ANALYTIC_PARITY_VALIDATION.json`

K2 is ready for final closeout at the commit introducing this receipt. No further phase is implemented by K2c.
