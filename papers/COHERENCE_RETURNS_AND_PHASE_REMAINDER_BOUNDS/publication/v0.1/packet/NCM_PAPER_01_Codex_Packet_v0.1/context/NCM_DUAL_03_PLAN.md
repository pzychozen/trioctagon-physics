# Frozen discovery plan — NCM-DUAL-03 v0.1

Amendment 01 to the preserved Stage A missing-input status: the author supplied the packet. No earlier discovery attempt exists. The work order and prior report/manifest match byte-for-byte. The independently proved amplitude bound agrees with the brief; its looser rational envelope and all printed fractions were separately checked. The new Stage A sector and phase-chord bounds remain scoped necessary conditions, not a global exclusion. Proceed with all 60 supplied starts; none are added, removed, permuted, or selected by phase remainder.

## Immutable inputs and resolution

DISCOVERY_PLAN.json SHA-256: e6a3de2535871182a4b0cd078695a42180860972f914c5a019657f41b9af3cf6.

Resolve its 54 polar seeds using exact rational amplitudes and pi multiples, with exact canonical zeros/signs for the prescribed integer/half-integer phases and explicit sqrt(3) values for sixths/thirds. Resolve six Cartesian seeds from their exact rational real/imaginary components. Original formulas, 80-digit working representations and exact squared-modulus pivot decisions are all retained in resolved_plan.json. Printed representations have 90 digits to preserve the 80-digit working values on serialization, not to assert 90-digit accuracy. No F is evaluated during this resolution.

All fixed coefficients are parsed from their exact rational strings. Pivot is the seed's exact largest modulus, lowest index on an exact tie; no roundoff-dependent tie breaking. One initial common rephasing makes the pivot positive real, retaining norm. The pivot is fixed for the entire solve, with no chart restart. Initial mu is the unit phase of z†F³z, or 1 only if that correlation is exactly zero. An exact zero prestage refuses the regular initial block. No preferred phase penalty or initialization is used.

## Solver frozen before search

- mpmath at 80 decimal digits. Eight real unknowns: Re/Im z, Re mu, Im mu. All six return equations, the unit circle equation and Im z_pivot=0 are retained.
- Analytic real Jacobian through all three updates, as independently checked in Stage A. No complex-step derivatives and no project imports.
- Newton direction solves the full square Jacobian with LU. Singular linear systems stop that start; no hidden fallback, random perturbation, continuation or retry.
- Fixed per-start residual scaling: divide the six return rows and gauge row by s=max(1,||initial gauged z||_2); leave the circle row unchanged. Solve with correspondingly scaled Jacobian. This is numerical residual scaling, not state normalization.
- Merit is the Euclidean norm of that scaled residual. Try t=1,1/2,...,2^-20, accepting the first trial with merit <=(1−10^-4 t) times the current merit. Record every trial and rejection reason. Nonfinite states, max component modulus >3, or nonpositive real pivot are rejected before F evaluation. Exact-zero prestages are rejected without repair. Insufficient decrease at all 21 trial lengths stops the start.
- At most 80 iteration passes per start. Every F call attempted by initial correlation, residual/Jacobian or line search is charged. A three-step residual normally charges three calls, and an earlier singular refusal charges only the calls actually attempted. Analytic Jacobian propagation adds no hidden F stencil. The global cap is 120,000 attempted calls, conservatively including singular refusals.
- Numerical convergence requires absolute return norm <=1e-45, return norm divided by ||z|| <=1e-40, circle error <=1e-45 and gauge error <=1e-45. A state norm <1e-25 stops as zero/near-zero, not a return candidate. No objective forces a phase value.

## Screening and retained evidence

Every attempt keeps its exact seed provenance, gauged start, initial correlation block, fixed pivot, iteration coordinates/residuals/Newton directions, all trial scales and rejection reasons, final raw z0..z3, nine prestage components, kicks, raw H0..H3, j values, fitted/correlated mu, return errors and pairwise H separations. Trial coordinates can be reconstructed from the retained current point, Newton direction and scale.

After convergence require max |z_i|<=sqrt(1.001)+1e-35, pivot real part >1e-25, and every prestage modulus >1e-20 as numerical screens. These are not certifications. H separations are Frobenius norms divided by ||z0||². If all three separations and the one-step phase-proportionality residual are <1e-25, classify as numerical lower period one. If every pair separation is >1e-12, classify as an unvalidated period-three candidate. The gap and near-singular cases remain unresolved.

Potential duplicate groups compare only common-phase-equivalent states and cyclic starts, with relative state discrepancy <1e-25; no channel permutation or conjugation identification is used. Retain all original attempts and explicit conjugate seeds. Numerical grouping is not a uniqueness theorem.

## Independent checking and validation boundary

After discovery, independently evaluate the direct Arg0 formula for each numerically converged attempt's three-step block at 80 digits. This is charged to the packet's separate regression ceiling of 384 F calls, including the 25 Stage A attempts. It is a regression check, not another root solve. Preserve discrepant outcomes.

Select at most eight distinct genuine-period-three candidates, sorted by return residual then seed order, never by phase. Reevaluate those once at 120 digits with the independent direct formula. Only then consider an existence certificate for the complete phase-fixed eight-equation system. At most 64 local boxes per candidate and one escalation to at most 160 digits are permitted. No certificate is claimed from a point residual or a scalar circle test. If no genuine candidate exists, no certificate is attempted and this is explicitly reported. No optional twelve-update trace is planned; its 96-call allowance remains unused unless an actual finding later justifies a documented amendment.

All source coefficients remain fixed. No amplitude normalization occurs inside F, no clock/memory is advanced, and no cone-pose construction is performed. Lower-period outcomes and numerical failures are valid outcomes. There are no automatic extra starts or budget extensions.

The previous Stage A snapshot remains unchanged. PLAN_FREEZE.json binds this plan, the resolved seeds and executable research files before the first discovery seed is evaluated. Changes after freezing require an append-only amendment and preservation of prior outcomes.
