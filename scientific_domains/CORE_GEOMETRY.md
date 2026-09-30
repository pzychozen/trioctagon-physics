# Scientific Core / Core Geometry

[Scientific ownership index](README.md) · Navigation v0.1, 30 September 2026.

The current scientific kernel is **`kernel_physics` in this repository**. It owns
the accepted toy-model dynamics, exact geometry and passive readouts within the
domains recorded by its papers and contracts. It is distinct from historical
TORMENT. Accepted historical observer mathematics has a current implementation;
this does not make the whole historical model current.

## Support and authority layers

| Layer | Existing authority and implementation | Boundary |
|---|---|---|
| **PUBLIC/SUPPORTED** | The 34 exports in [kernel_physics.api](../kernel_physics/api.py), documented by the [kernel guide](../kernel_physics/README.md). | Explicit parameters, state and provenance; step/run/resume; exact geometry records; passive observer, diagnostic, accounting and display operations. Only declared public names and workflows carry this support contract. |
| **INTERNAL ACCEPTED** | [Cycle-covering mathematics](../kernel_physics/covering.py); [FaceState](../kernel_physics/face_state.py) and its [kinematic attachment scope](../research/folded_face_state/FOLDED_FACE_STATE_ATTACHMENT_v0.1.md). | Accepted internal mathematics/representation within scope; neither module is a facade export. FaceState is a kinematic view, not a physical point-position law or an independently supported application model. |
| **QUARANTINED / OPTION-B** | [Boundary response](../kernel_physics/boundary_response.py), [SRG](../kernel_physics/srg.py), [operating region](../kernel_physics/operating_region.py); resolved support status in the [K2 final closeout](../kernel_physics/K2_PARITY_FINAL_CLOSEOUT.md). | Shipped preparation modules with model choices and scoped mathematical results; excluded from public facade/Runner reachability. Atlas coverage, internal imports and local tests do not promote them to public support. |
| **DOCUMENTARY / PROVENANCE** | [Definition ledger](../kernel_physics/K0_KERNEL_DEFINITION_LEDGER_v0.1.md), [contract freeze](../kernel_physics/K0_KERNEL_AUTHORITY_PUBLIC_CONTRACT_FREEZE_v0.1.md), [parity closeout](../kernel_physics/K2_PARITY_FINAL_CLOSEOUT.md), papers and Atlas below. | Evidence, authority and historical engineering decisions. Read recorded dates and later dispositions; earlier pending wording is not a new stop or admission decision. |

Package membership is broader than the supported API: nineteen top-level Python
files ship, while fourteen module paths participate in record implementation
identity. Nonpublic files remain part of that package and preservation boundary.

## Current mathematics and contracts

[Dynamics](../kernel_physics/dynamics.py) owns triad/ring state advancement;
[readouts](../kernel_physics/readouts.py), [Z observers](../kernel_physics/z_manifold.py)
and [diagnostics](../kernel_physics/z_diagnostics.py) observe or account for it.
Readout accounting does not become a second evolution law. Observer and display
operations remain passive; finite-history displays retain their finite domain.
Named historical presets are explicit model choices, not derived physical laws.

[Exact folded geometry](../kernel_physics/geometry.py) and the
[reference scaffold](../kernel_physics/reference_scaffold.py) are distinct
mathematical objects (C01 and D03). A scaffold gap is not recurrence coupling;
neither a geometry record nor a tangent representation establishes physical
attachment of amplitudes to the shell. Geometry-to-dynamics physical coupling,
Z-to-six-opening registration and physical units/calibration remain open.

The [public types](../kernel_physics/_contract_types.py),
[run records](../kernel_physics/_records.py) and
[geometry records](../kernel_physics/_geometry_records.py) bind inputs,
implementation and provenance. Public API and both record schemas are `1.0.0`;
ledger `0.1`, exact geometry codec `1` and package `0.1.0` have distinct roles.
The [scientific UI surface contract](../kernel_physics/K4A_SCIENTIFIC_UI_SURFACE_CONTRACT.md)
describes delegated application access. Record loading is not scientific execution
or automatic permission to resume under a different artifact identity.

## Papers A-F and Mathematical Atlas

The [root publication index](../README.md#papers-a-f) links the authoritative
PDFs and edition records. These are the current scientific source editions:

| Paper | Subject and current source | Recorded qualification |
|---|---|---|
| A | [Cycle-covering dynamics](../papers/PAPER_A/publication/paper_A_publication.md), publication v1.0 | Scientific source v0.5.1; recurrence, symmetries and covering claims retain their domains. |
| B | [Triadic chirality and orientation geometry](../papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md), v0.1.2 | Scope/citation revision; optional kinematic representation supplies no physical shell attachment. |
| C | [Exact folded Tri-Octagon geometry](../papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md), v1.0.1 | Scientific source v0.3.1; exact material geometry remains distinct from the reference scaffold. |
| D | [Reference-scaffold geometry](../papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md), v0.1.1 | Acceptance is limited to the stated mathematical scope. |
| E | [Z manifold](../papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md), v0.1.1 | Recorded review/revision status is retained; observer parity does not assert historical trajectory equivalence. |
| F | [Transverse chirality and local linearization](../papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md), v0.2 | Accepted source and publication-build status; local analytic results retain their written hypotheses. |

The [owner publication disposition](../PUBLIC_RELEASE_CONTENT_DISPOSITION_v0.1.md)
authorizes E/F visibility at their recorded statuses, without inventing a further
review round. Predecessors and frozen publication wording retain their identities.
No external peer review or experimentally validated physical theory is implied.

The [Mathematical Atlas](../research/mathematical_atlas/README.md) is the current
core's derivation and evidence layer: entries 01-09, Supplements A/F and the
75-row completeness crosswalk. It adds explanations, exact checks,
counterexamples and boundaries without silently revising papers or public APIs.
Entries 07/08 retain unresolved runtime caveats despite their mathematical
results. Preserved checkers have original source/HEAD/layout assumptions; they
are evidence artifacts, not a portable installed-package test suite.

Use the [P1-P12 parity record](../kernel_physics/K2_PARITY_FINAL_CLOSEOUT.md) and
existing [distribution verifier](../tools/verify_distribution.py) for their
respective mathematical and artifact scopes. This navigation performs no new
scientific execution, certification or package change.
