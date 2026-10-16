# BOUNDARY-12 observation interface proposal

This is a design note accompanying the isolated prototype. No existing application architecture was inspected or changed. Integration is deferred until separate acceptance and authorization.

## Inputs and provenance

- Immutable accepted Paper C / BOUNDARY-11 geometry inventory, with SHA-256 identities, original vertex/edge IDs and directions.
- Positive panel width w, interpreted only as a geometric similarity scale.
- One active input: R/w, C/w or per-end ℓ/w. Convert to the shared t/w and validate R≥ρ. Explicit original/A/B presets carry exact event identities. Seven fixed comparisons remain separately named.
- Display unit: w, s, C or ℓ; the last requires ℓ>0. Changing a unit does not change R/w or the mathematical configuration.
- Layer visibility, camera and selected edge. These are presentation state only.

## Outputs

- All 42 branch records with original edge, sign, original endpoint, outward ray, normalized point, scaled point and displayed point.
- Exact-event token and its provenance (preset or exact length identity), kept separate from floating coordinates and visual overlap.
- Unique-dot IDs only from the accepted exact event incidence groups. Other numeric states retain one marker per branch and make no tolerance-based coincidence certification.
- Precomputed exact graphs and maximal-face hulls for the three events, with source-linked inventories. Generic radii do not cause additional graph/hull investigations.
- Readouts R/w, t/w, C/w, ℓ/w, and conversions into the selected unit. Export all original branch labels even when dots coincide.

## Role and defaults

Default to A for this investigation: first strictly later meeting on every outward ray, with whole chord equal to panel width. Treat it as an observation preset. Keep original and B directly available. Start with original panels, edges, reference spheres and split graph visible; the separate filled convex envelope is opt-in.

The observer is a pure map from explicit geometric input plus immutable data to a static observation. It has no time-step interface, random generator, mutable kernel-state handle, z/Omega access, trajectory storage or mechanism to choose a physical wall. The current loopback preview server only serves files from the isolated research directory.

## Proposed later integration tests — not executed or authorized here

1. Snapshot a live model's state and RNG state before and after observation; require byte identity and zero clock advancement.
2. Require explicit provenance/version matching for geometry and exact event inventories.
3. Validate all seven fixed presets against this accepted standalone reference once accepted.
4. Verify input failures preserve the model and cannot silently clamp to another event.
5. Test display-unit and global-similarity changes independently of observer-radius changes.
6. Preserve 42 branch labels through dot grouping, selection and export round trips.
7. Keep graph, filled hull and original panels distinct in UI wording and data types.
8. Check event metadata at near-event values, invalid widths and ℓ=0 unit singularity.
9. Check that observation cannot supply a new boundary condition or coefficient to an evolution step.

Any physical interpretation, tensor norm, reflection/stopping rule, kernel rescaling or production wiring is a later modeling/engineering decision.
