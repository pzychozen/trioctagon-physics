"""Stable refusal categories; messages are diagnostics, never executable data."""

CATEGORIES = frozenset({
    "INVALID_CODEC", "INVALID_SCHEMA", "WRONG_PARENT_FAMILY", "PARENT_VALIDATION",
    "INPUT_BYTE_MISMATCH", "PARENT_CANONICAL_MISMATCH", "PARENT_SEMANTIC_MISMATCH",
    "WRONG_PRODUCER", "UNVERIFIED_PRODUCER", "UNSUPPORTED_OPERATION",
    "UNSUPPORTED_PROVIDER", "AUTHORITY_MISMATCH", "UNSUPPORTED_EXTERNAL_DATA",
    "SAMPLE_INDEX_MISMATCH", "MISSING_RECORDED_FIELD", "FORBIDDEN_SELECTION",
    "DOMAIN_MISMATCH", "PARENT_MUTATION", "IMPLICIT_RECOMPUTATION",
    "UNSUPPORTED_RESUME", "UNSUPPORTED_CONVERSION", "KERNEL_MISMATCH",
    "RESULT_BINDING_MISMATCH", "COPIED_VALUE_MISMATCH", "RESOURCE_LIMIT",
    "FORBIDDEN_EFFECT", "CANCELLED", "PERSISTENCE_FAILURE", "LEGACY_ARTIFACT",
    "SCIENTIFIC_OVERCLAIM", "B1_VERIFIED_LANE_DISABLED", "RESOURCE_POLICY_UNAPPROVED", "PROVIDER_FAILURE",
})

class ProtocolError(ValueError):
    def __init__(self, category, message):
        if category not in CATEGORIES:
            raise ValueError("unknown error category")
        self.category = category
        super().__init__(message)

def require(condition, category, message):
    if not condition:
        raise ProtocolError(category, message)
