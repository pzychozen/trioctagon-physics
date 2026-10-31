# Numerical lower-period groups and readouts

These seven groups summarize 42 nominal lower-period solutions. They are not interval-validated roots or a complete branch classification. All H matrices and raw transitions remain in numerical_groups.json and attempts/*.json. Readout stages below are from the actual three native updates evaluated by the solver, not from a formula-generated continuation.

| Group / representative | Seed members | Three-step fitted phase (rad) | Largest relative H separation | Minimum prestage modulus |
|---|---|---:|---:|---:|
| G01 / S02 | S02, S03, S06, S21, S38, S39, S42, S55, S56, S59, S60 | 2.0979284110947e-53 | 2.054720382e-51 | 0.9995999627 |
| G02 / S04 | S04, S05, S07, S08, S23, S26, S27, S41, S44, S45 | 3.3653148927493e-7 | 8.310896611e-78 | 0.7045181018 |
| G03 / S10 | S10, S11, S29, S30, S47, S48 | -3.3653148927493e-7 | 5.403781752e-81 | 0.7045181018 |
| G04 / S13 | S13, S40, S43, S46, S49, S57, S58 | 0.0 | 9.916704533e-65 | 0.1591430398 |
| G05 / S16 | S16, S22, S25, S28, S31, S34 | 0.0 | 2.676097262e-64 | 0.1595711585 |
| G06 / S19 | S19 | -6.9937464264523e-5 | 1.069066457e-61 | 0.0009279117082 |
| G07 / S52 | S52 | 0.0 | 0.0 | 0.1590908914 |

| Group | j(z0) | j(z1) | j(z2) | j(z3) |
|---|---:|---:|---:|---:|
| G01 | 1.14345839206546e-50 | 1.054305901222116e-50 | 9.721512894084512e-51 | 8.964452695423285e-51 |
| G02 | 0.3020991585858716 | 0.3020991379763302 | 0.302099117366785 | 0.302099096757236 |
| G03 | -0.3020991585858716 | -0.3020991379763302 | -0.302099117366785 | -0.302099096757236 |
| G04 | 0.0 | 0.0 | 0.0 | 0.0 |
| G05 | 0.0 | 0.0 | 0.0 | 0.0 |
| G06 | -0.0003999377528482098 | -0.0003999432350928106 | -0.0003999487171200534 | -0.0003999541989299353 |
| G07 | 0.0 | 0.0 | 0.0 | 0.0 |

H0,H1,H2 are numerically identical at the stated tolerance in every group. The fitted three-step phase is not a minimal coherence period. In an exact relative return, K(mu z)=mu K(z) implies j(F^(3m)z)=Im(mu^m K(z)); no extra native blocks were run and no EMA memory or clock was advanced. No exact finite order of these numerical multipliers is inferred.
