# Exact supporting-plane orbit representatives

These are readouts of the checked certificate, not new nominated faces. Coordinates are `X=physical_x/w`, `Y=physical_y/(sqrt(3)*w)`, `Z=physical_z/w`. Each row means `n_X X + n_Y Y + n_Z Z <= d`. Coefficients are exact over Q(sqrt(2)); polynomial formulas use the observation parameter x. The positive common-factor normalization preserves outward inequality direction throughout the stated domain. The full zero set equals the listed cycle. Apply the 12 coefficient-verified D3h actions in `exact_certificate.json` to recover every face; face IDs are local to each domain.

## C1

| Representative | Orbit size | Full zero-set cyclic order | n_X | n_Y | n_Z | d |
|---|---:|---|---|---|---|---|
| F01 | 2 | E01+, E05-, E16+, E03+, E07+, E14- | `0` | `0` | `-1` | `sqrt(2)*(x + 1/2)/2` |
| F02 | 6 | E01+, E09-, E12-, E05- | `-1` | `1` | `-x - 1/2 + sqrt(2)/2` | `sqrt(2)*(x**2 + x*(1 - sqrt(2)/2) + sqrt(2)/12 + 1/4)/2` |
| F03 | 12 | E01+, E06-, E13- | `-1` | `3 - 2*sqrt(2)` | `-1` | `x + sqrt(2)/3` |
| F04 | 6 | E01+, E14-, E06- | `-1` | `-1` | `-sqrt(2) - 1` | `(1 + sqrt(2))*(x - 2/3 + 2*sqrt(2)/3)` |
| F05 | 12 | E01+, E13-, E09- | `x - sqrt(2)/2 - 1/2` | `x - 5*sqrt(2)/2 + 7/2` | `(-1 + sqrt(2))*(x - sqrt(2)/2 - 1/2)` | `-x**2 + 5*x/6 - 1/3 + 5*sqrt(2)/12` |
| F06 | 6 | E01-, E03-, E21-, E10+ | `0` | `1` | `(-1 + sqrt(2))/2` | `(x - 1/3 + sqrt(2)/2)/2` |
| F07 | 3 | E01-, E11+, E12-, E03- | `0` | `1` | `0` | `sqrt(2)*(x + sqrt(2)/6 + 1/2)/4` |
| F09 | 3 | E01-, E14+, E17-, E11+ | `1` | `1` | `0` | `sqrt(2)*(x - sqrt(2)/6 + 1/2)/2` |
| F14 | 6 | E02+, E10+, E21- | `0` | `1` | `1/2` | `(x + 2/3)/2` |

## T

| Representative | Orbit size | Full zero-set cyclic order | n_X | n_Y | n_Z | d |
|---|---:|---|---|---|---|---|
| F01 | 2 | E01+, E05-, E16+, E03+, E07+, E14- | `0` | `0` | `-1` | `(3 - sqrt(2))/2` |
| F02 | 6 | E01+, E13-, E09-, E12-, E20+, E05- | `-1` | `1` | `1 - sqrt(2)` | `(-13 + 12*sqrt(2))/6` |
| F03 | 12 | E01+, E06-, E13- | `-1` | `3 - 2*sqrt(2)` | `-1` | `(-9 + 11*sqrt(2))/6` |
| F04 | 6 | E01+, E14-, E06- | `-1` | `-1` | `-sqrt(2) - 1` | `13/6` |
| F05 | 6 | E01-, E03-, E21-, E10+ | `0` | `1` | `(-1 + sqrt(2))/2` | `(-11 + 12*sqrt(2))/12` |
| F06 | 3 | E01-, E11+, E12-, E03- | `0` | `1` | `0` | `(10 - 3*sqrt(2))/12` |
| F08 | 3 | E01-, E14+, E17-, E11+ | `1` | `1` | `0` | `(8 - 3*sqrt(2))/6` |
| F12 | 6 | E02+, E10+, E21- | `0` | `1` | `1/2` | `(-5 + 9*sqrt(2))/12` |

## C2

| Representative | Orbit size | Full zero-set cyclic order | n_X | n_Y | n_Z | d |
|---|---:|---|---|---|---|---|
| F01 | 2 | E01+, E05-, E16+, E03+, E07+, E14- | `0` | `0` | `-1` | `sqrt(2)*(x + 1/2)/2` |
| F02 | 6 | E01+, E13-, E20+, E05- | `-x - 1/2 + sqrt(2)/2` | `x - sqrt(2)/2 + 1/2` | `-sqrt(2)*(x - 1/2)` | `x**2 + x/3 - sqrt(2)/6 - 1/12` |
| F03 | 12 | E01+, E06-, E13- | `-1` | `3 - 2*sqrt(2)` | `-1` | `x + sqrt(2)/3` |
| F04 | 6 | E01+, E14-, E06- | `-1` | `-1` | `-sqrt(2) - 1` | `(1 + sqrt(2))*(x - 2/3 + 2*sqrt(2)/3)` |
| F05 | 6 | E01-, E03-, E21-, E10+ | `0` | `1` | `(-1 + sqrt(2))/2` | `(x - 1/3 + sqrt(2)/2)/2` |
| F06 | 3 | E01-, E11+, E12-, E03- | `0` | `1` | `0` | `sqrt(2)*(x + sqrt(2)/6 + 1/2)/4` |
| F07 | 6 | E01-, E10+, E19-, E14+ | `1` | `1` | `-1 + sqrt(2)` | `x - 2/3 + sqrt(2)/2` |
| F08 | 3 | E01-, E14+, E17-, E11+ | `1` | `1` | `0` | `sqrt(2)*(x - sqrt(2)/6 + 1/2)/2` |
| F12 | 6 | E02+, E10+, E21- | `0` | `1` | `1/2` | `(x + 2/3)/2` |

