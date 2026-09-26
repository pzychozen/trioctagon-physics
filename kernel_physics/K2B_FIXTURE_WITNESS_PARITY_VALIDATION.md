# K2b fixture / witness parity validation

**K2B_STATUS = PASS. O03 = CLOSED. P5 = PASS. P6 = PASS.**

Starting HEAD: `24b62db7ff1960ac485789ff235d01a63f94e65a`. Final HEAD is the creation commit of this receipt, resolved by `git log --diff-filter=A --format=%H -- kernel_physics/K2B_FIXTURE_WITNESS_PARITY_VALIDATION.json`; its literal identity is reported after publication. This avoids a circular embedded commit hash.

## Validation and preservation

- K2b: 9 tests PASS.
- Clean isolated tracked checkout: 288 tests PASS in 397.482 seconds.
- Preserved local-only Option-B tests, run afterward: 30 PASS in 1.18 seconds. No supported-v1 status is inferred.
- All 692 starting tracked files, four local-only tests, local original golden CSV and all three provenance sources retain starting SHA-256 hashes.
- Production, existing tests, K0, K1, K2a, papers, research and Option-B changes: **0**. P6 source bytes are unchanged. No P7/P8 work.

```powershell
& 'C:\Users\Notandi\miniconda3\shell\condabin\conda-hook.ps1'
conda activate torment
python -B -m unittest kernel_physics.tests.test_parity_oracle_boundaries_k2b kernel_physics.tests.test_parity_p05_p06 -v -f
python -B -m unittest discover -s kernel_physics/tests -t . -p "test_*.py" -v
python -B -m unittest kernel_physics.tests.test_boundary_response kernel_physics.tests.test_srg kernel_physics.tests.test_operating_region kernel_physics.tests.test_boundary_pipeline -v
```

The full tracked command ran only in the clean detached snapshot `2f4f6d13bd801f1b6efdc55295acf36bab20526b`; the local-only command ran subsequently in the original workspace. The five executable/fixture files match the tested snapshot byte for byte. Validation receipts were added afterward.

## O03 packet and provenance

Golden identity: SHA-256 `eeed672b1cb20321dfc85a2f4753c93d4fe1b9345a5cede4f5e12532537a4a38`; 282427 bytes; 388 rows; 50 columns. P6 identity: SHA-256 `fb2b2a71fd99c536dc7e490c6a2e201b2a0b22ee533820870dff5ee516c468dc`; 10345 bytes; 18 rows; 32 columns.

The two-file golden packet contains only the unchanged CSV and [GOLDEN_388_RECEIPT.md](tests/fixtures/golden_388/GOLDEN_388_RECEIPT.md). That receipt transcribes the full protocol, all 50 column meanings, source hashes, environment, baseline IDs and attributed Linux comparison evidence. No generator or research directory is published.

| Source | Actual SHA-256 |
|---|---|
| `investigate.py` | `bf8c5b95296a4401e21fc1702af4b81113d264197855f48188a24e47597304a1` |
| `REPORT.md` | `29ba7dc8d233c00c091c4ce809772d09c5537e53f854ff122147c3eedbe51709` |
| `RESULTS.json` | `e73fbb0e569f8d2af705fec30c89bea537956de6737be4aeeba4cf79adfb7ebc` |

Repository baseline `d0aa8d1cb19421ff441eacda0f83ec89fc3160b3`; implementation checkpoint `d2b1cbeca807ae33117f02f697e5eff0b4b1ca96`; baseline tree `e9e7501fdb8c2942862943fc6cc529c12a5b4fa2`. Both original history hashes are preserved in the golden receipt and JSON.

## P5 comparison mode and claims

**P5 IS A HISTORICAL REGRESSION / SCHEDULE WITNESS.** P5_EQUATION_ORACLE = NO; P5_HISTORICAL_REGRESSION_WITNESS = YES; P5_SCHEDULE_WITNESS = YES; P5_INDEPENDENT_CHIRALITY_ORACLE = YES.

**CROSS_ENVIRONMENT.** Recorded-environment bitwise certification: **NOT_APPLICABLE**. Recorded Python 3.12.14 / NumPy 2.3.5 differ from current torment Python 3.11.15 / NumPy 2.4.4. The exact environment dictionaries appear in JSON. The mode was selected before comparison and remains unchanged despite zero numerical differences in the ordinary saved-versus-Runner comparisons.

All 97 rows per run agree bitwise with the direct public-operation control for Omega, clock, memory, results and diagnostics. Row zero has no advancement or initial EMA innovation. This is an orchestration check, not an independent equation oracle. Independent high-precision cross products cover all 388 saved rows and all matching replay rows.

Ordinary quantities use `1e-12 + 1e-12*abs(reference)`. C uses the frozen `64u` component term scale, plus the exact high-precision trajectory-difference term when needed; `u=2^-52`. Accounting values at saved/replayed inputs use independent P10 expressions and `256u` defining-term scales, without the historical allowance. Resolution flags remain exact. Global CSV row labels in numerical receipts are zero-based positions, not per-run update indices.

PASS SUPPORTS: preserved historical samples, schedule, row-zero behavior, clock/EMA ordering, stored relationships and independent chirality from saved Omega.

PASS DOES NOT SUPPORT: Paper A/E equations (owned by P1/P9), physical interpretation, spatial registration, gate assignment or display mappings.

## All 50 columns, exactly one classification each

| # | Column | Classification | P5 disposition |
|---:|---|---|---|
| 1 | `phase_strength` | RUN_KEY | Parity / exact protocol check |
| 2 | `variant` | RUN_KEY | Parity / exact protocol check |
| 3 | `row` | RUN_KEY | Parity / exact protocol check |
| 4 | `q` | OBSERVER_STATE | Parity / exact protocol check |
| 5 | `t` | OBSERVER_STATE | Parity / exact protocol check |
| 6 | `theta` | OBSERVER_STATE | Parity / exact protocol check |
| 7 | `initialization` | OBSERVER_STATE | Parity / exact protocol check |
| 8 | `z` | OBSERVER_RESULT | Parity / exact protocol check |
| 9 | `I` | RAW_READOUT | Parity / exact protocol check |
| 10 | `harmonic_amplitude` | EXCLUDED_RESEARCH | Excluded; preserved bytes only |
| 11 | `ema_memory` | OBSERVER_STATE | Parity / exact protocol check |
| 12 | `gate_assignment` | EXCLUDED_RESEARCH | Excluded; preserved bytes only |
| 13 | `map_lambda` | EXCLUDED_RESEARCH | Excluded; preserved bytes only |
| 14 | `map_delta0` | EXCLUDED_RESEARCH | Excluded; preserved bytes only |
| 15 | `M_x` | OBSERVER_RESULT | Parity / exact protocol check |
| 16 | `M_y` | OBSERVER_RESULT | Parity / exact protocol check |
| 17 | `M_z` | OBSERVER_RESULT | Parity / exact protocol check |
| 18 | `C_x` | OBSERVER_RESULT | Parity / exact protocol check |
| 19 | `C_y` | OBSERVER_RESULT | Parity / exact protocol check |
| 20 | `C_z` | OBSERVER_RESULT | Parity / exact protocol check |
| 21 | `T_x` | OBSERVER_RESULT | Parity / exact protocol check |
| 22 | `T_y` | OBSERVER_RESULT | Parity / exact protocol check |
| 23 | `T_z` | OBSERVER_RESULT | Parity / exact protocol check |
| 24 | `display_M_x` | EXCLUDED_RESEARCH | Excluded; preserved bytes only |
| 25 | `display_M_y` | EXCLUDED_RESEARCH | Excluded; preserved bytes only |
| 26 | `display_M_z` | EXCLUDED_RESEARCH | Excluded; preserved bytes only |
| 27 | `Omega0_real` | KERNEL_STATE | Parity / exact protocol check |
| 28 | `Omega0_imag` | KERNEL_STATE | Parity / exact protocol check |
| 29 | `Omega1_real` | KERNEL_STATE | Parity / exact protocol check |
| 30 | `Omega1_imag` | KERNEL_STATE | Parity / exact protocol check |
| 31 | `Omega2_real` | KERNEL_STATE | Parity / exact protocol check |
| 32 | `Omega2_imag` | KERNEL_STATE | Parity / exact protocol check |
| 33 | `norm_residual` | DIAGNOSTIC | Parity / exact protocol check |
| 34 | `q_residual` | DIAGNOSTIC | Parity / exact protocol check |
| 35 | `macro_relation_residual` | DIAGNOSTIC | Parity / exact protocol check |
| 36 | `q_macro` | DIAGNOSTIC | Parity / exact protocol check |
| 37 | `q_total` | DIAGNOSTIC | Parity / exact protocol check |
| 38 | `d_TM` | DIAGNOSTIC | Parity / exact protocol check |
| 39 | `d_CM` | DIAGNOSTIC | Parity / exact protocol check |
| 40 | `d_TC` | DIAGNOSTIC | Parity / exact protocol check |
| 41 | `macro_resolved` | DIAGNOSTIC | Parity / exact protocol check |
| 42 | `chiral_resolved` | DIAGNOSTIC | Parity / exact protocol check |
| 43 | `total_resolved` | DIAGNOSTIC | Parity / exact protocol check |
| 44 | `TM_resolved` | DIAGNOSTIC | Parity / exact protocol check |
| 45 | `CM_resolved` | DIAGNOSTIC | Parity / exact protocol check |
| 46 | `TC_resolved` | DIAGNOSTIC | Parity / exact protocol check |
| 47 | `threshold` | HISTORICAL_CONVENTION | Excluded; preserved bytes only |
| 48 | `gram_residual` | DIAGNOSTIC | Parity / exact protocol check |
| 49 | `slack_residual` | DIAGNOSTIC | Parity / exact protocol check |
| 50 | `polynomial_residual_allowance` | HISTORICAL_CONVENTION | Excluded; preserved bytes only |

`HISTORICAL_CONVENTION` remains distinct from `EXCLUDED_RESEARCH`; both are excluded from kernel parity claims. The two convention fields are not new laws/controllers or recurrence acceptance criteria. No column was reclassified after discrepancies.

## P6 exact mathematics and falsifiers

For A, `Omega=(x+iy,x-iy,z)` and `C=y*(z,z,-2x)`. For B, `Omega=(b+ic,b+ic,d+if)` and `C=(bf-dc)*(1,-1,0)`. Exact symbolic substitution verifies invariance of both forms and `C_A dot C_B=0` for arbitrary permitted real subspace amplitudes.

At `h=1/1000`, A has `x1=1-h^2/40`, `Y=h*(2/5-h^2/40)/sqrt(2)`, `Omega1=(x1+iY,x1-iY,1)` and `C1=Y*(1,1,-2+h^2/20)`. Its positive local signed elevation and acute projective angle are

```text
atan(sqrt(2)*h^2 / (20*(6-h^2/10)))
```

The tangent identity is symbolic. The chosen positive branch agrees with the AX report and Paper F (26)-(27). Projective comparisons use `atan2(cross_norm, abs(dot))`, never acos. Signed elevation uses the longitudinal projection and transverse norm. The historical direction-validity proxy is transcribed explicitly; a zero vector receives no direction.

All nine rows per seed satisfy exact floating `A: Cx=Cy`, `B: Cx=-Cy, Cz=+0.0`, and the state subspace relations. Signed-zero inputs are tested deliberately without another trajectory. The 18 nonzero-valid flags are preserved. Own/other axes, plane angles and mutual pi/2 separation pass the frozen 1e-12 rad bound. State and chirality use the frozen 1e-13 absolute plus 1e-12 relative bound.

PASS SUPPORTS: these two special invariant subspaces over eight updates, chirality orientation, their transverse relationship, and accepted exact one-step formulas.

PASS DOES NOT SUPPORT: universal axis, attraction, physical selector, generic-seed behavior, or a global theorem inferred from floating zeros.

## Worst normalized comparisons

| Check | Quantity | Absolute error | Bound | Fraction |
|---|---|---:|---:|---:|
| P5_ordinary | lambda=0.0 staged row=0 Omega0_real | 0.0 | 1.2000000000000000111022302462515654e-12 | 0.0 |
| P5_saved_C | saved row=95 C_z | 2.6135784103582642379053253188667962e-17 | 4.0102381615389727642125952206817968e-15 | 0.0065172648233821477871297594023901448 |
| P5_replayed_C | replayed row=95 C_z | 2.6135784103582642379053253188667962e-17 | 4.0102381615389727642125952206817968e-15 | 0.0065172648233821477871297594023901448 |
| P5_cross_trajectory_C | cross trajectory row=0 C_x | 0.0 | 1.2789769243681804765629866214227539e-15 | 0.0 |
| P5_accounting | replayed row=349 gram_residual | 6.6613381477509392425417900085449219e-16 | 1.3827396512311506302934279591659309e-13 | 0.0048174926797100814267405639213121841 |
| P6_state | A row=0 Omega0 | 0.0 | 1.1000002499999687500078043577056174e-12 | 0.0 |
| P6_C | A row=0 C_norm | 9.1235515559232712452363058739648781e-20 | 1.0173205080756887717409464588769197e-13 | 0.00000089682174727617678970620660162372801 |
| P6_unit_C | A row=3 unit_C_y | 4.3134308887830166595571736537304915e-17 | 5.0824829157702002824237297318177298e-13 | 0.00008486857625038093503532694660265084 |
| P6_plane | A row=1 signed plane residual | 8.9841275123747052116779093137967297e-25 | 1.0000001178511320707424447497642703e-13 | 8.9841264535852319899537915474808797e-12 |
| P6_angles | A row=0 projective_angle_other_initial_rad | 6.1232339957367658861303296613750053e-17 | 1.0e-12 | 0.000061232339957367658861303296613750053 |
| P6_orthogonality | row=0 mutual angle | 0.0 | 1.0e-12 | 0.0 |
| P6_one_step_angle | A projective own-axis row=1 | 9.1200994847866557130559565362134973e-18 | 1.0e-12 | 0.0000091200994847866557130559565362134973 |
| P6_one_step | A exact state 1 | 4.0914474084299324723872892072105049e-17 | 1.1000000149999952000002282499850563e-12 | 0.000037194975933068058421570913384109892 |

The JSON also records the maximum absolute error separately, reference/actual values and all independent term scales. Ordinary P5 saved-versus-Runner maximum error is **0.0**. The largest saved-C independent absolute error is **4.228198086608143e-17**, and the largest normalized fraction is **0.006517264823382148**. These are independent cross-product roundoff comparisons, not cross-environment trajectory error.

P6 one-step angle discrepancy is **9.120099484786656e-18 rad**, below **1e-12 rad**. Exact floating symmetry falsifiers and zero-direction rejection all pass. No tolerance was widened and no runtime repair was performed.

## Counts and import boundary

```json
{
  "EXACT_DISCRETE": 22413,
  "HISTORICAL_FIXTURE_TOLERANCE": 7862,
  "HIGH_PRECISION_REFERENCE": 2328,
  "BINARY64_TERM_SCALE": 6596,
  "EXACT_SYMBOLIC": 11
}
```

The new oracle imports only mpmath and SymPy. The new static boundary test rejects runtime/research/paper imports and obvious dynamic import/exec escapes. P5 accounting reuses the unchanged independently reconstructed K2a Paper E oracle from the test module; the new oracle does not import it or any kernel module. Counts are comparison assertions, not unittest method counts.

## Exact new-file list

- `kernel_physics/K2B_FIXTURE_WITNESS_PARITY_VALIDATION.json`
- `kernel_physics/K2B_FIXTURE_WITNESS_PARITY_VALIDATION.md`
- `kernel_physics/tests/fixtures/golden_388/GOLDEN_388_RECEIPT.md`
- `kernel_physics/tests/fixtures/golden_388/TRAJECTORIES.csv`
- `kernel_physics/tests/parity_oracles/transverse_axis_oracle.py`
- `kernel_physics/tests/test_parity_oracle_boundaries_k2b.py`
- `kernel_physics/tests/test_parity_p05_p06.py`

K2c is ready for separate authorization, starting from the publication commit containing these receipts. P7/P8 have not begun.
