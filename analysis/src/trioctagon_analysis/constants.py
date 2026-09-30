"""Frozen B1 identities and the only admitted stored-data selection."""
PROTOCOL_FAMILY = "TRIOCTAGON_ANALYSIS_PROTOCOL"
PROTOCOL_VERSION = 1
SCHEMA = "1.0.0"
OPERATION = "core.app04.recorded_chirality_accounting.inspect"
PROVIDER = "core.app04.recorded_copy"
REVISION = 1
FIELDS = ("S.raw_readouts.z_chiral", "D.chiral", "D.A", "D.B", "D.h",
          "D.intensity", "D.chiral_norm", "D.chiral_norm_squared", "D.gram_product",
          "D.h_squared", "D.gram_rhs", "D.gram_residual", "D.amplitude_bound",
          "D.slack_sum_of_squares", "D.observed_slack", "D.slack_residual")
VECTOR_FIELDS = frozenset(FIELDS[:2])
QUALIFICATION = (
    "Recorded selected-sample Core data, copied without scientific recomputation. "
    "Parent structure and digests validated; original scientific execution and "
    "accounting equations were not replayed. Floating residuals are retained as "
    "recorded and are not exact equality certificates. Channel chirality is not "
    "a physical placement or calibrated energy claim.")
REPRODUCIBILITY = "EXACT_STORED_TOKEN_COPY_NOT_SCIENTIFIC_REPLAY"
NUMERICAL = "CANONICAL_F64_TOKEN_COPY_TOLERANCE_NOT_APPLICABLE"
EFFECTS = ["READ_IMMUTABLE_PARENT", "PUBLIC_RUNRECORD_LOAD", "RETURN_DETACHED_PAYLOAD"]
STATUS_ASSERTIONS = [
    {"subject": "recorded_field_semantics", "status": "CURRENT_ACCEPTED_MATH"},
    {"subject": "copy_operation", "status": "INFRASTRUCTURE"},
]
AUTHORITY_REFERENCES = [
    {"id": "ATLAS07", "edition": "0.1", "locator": "Atlas07 section 3 and runtime caveat",
     "sha256": "5ffea5412d7ce70490e1d32bbbe797168394e3df518074f2cf4979a1d71e60e2",
     "qualification": "Prior passing assertions/zero exit accompanied Windows access violations; not resolved by B1."},
    {"id": "CORE_DIAGNOSTICS", "edition": "491f8817afe49204c9fdd52fadafe99217f4aea9",
     "locator": "kernel_physics/z_diagnostics.py:144",
     "sha256": "db6c5d87fcecd492ac76fbc3cbcd6b71520d2ab4c9bbe4b1686c138aa0549d09",
     "qualification": "Stored field semantics only; no call to scientific diagnostics by this provider."},
]
