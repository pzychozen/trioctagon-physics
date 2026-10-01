"""Historical failure vocabulary, independent of frozen Core error registries."""
CATEGORIES = frozenset({
    "MALFORMED_REQUEST", "UNSUPPORTED_SCHEMA", "WRONG_HISTORICAL_PROFILE",
    "UNKNOWN_OPERATION", "WRONG_K_PROFILE", "CONSTANT_MISMATCH", "INVALID_OMEGA",
    "INVALID_DOMAIN_ARGUMENT", "UNSUPPORTED_READOUT", "AUTHORITY_MISMATCH",
    "PROVIDER_IDENTITY_MISMATCH", "NUMERICAL_DOMAIN_FAILURE", "PROVIDER_FAILURE",
    "FORBIDDEN_SCIENTIFIC_DELEGATION", "RESOURCE_POLICY_NOT_ADMITTED", "RESOURCE_LIMIT",
    "FORBIDDEN_SOURCE_IMPORT", "FORBIDDEN_CURRENT_SCIENCE_IMPORT",
    "FORBIDDEN_PRODUCTION_SERVICE", "UNSUPPORTED_PARENT_INPUT", "RESULT_BINDING_FAILURE",
    "PERSISTENCE_FAILURE", "CANCELLED",
})


class ProtocolError(ValueError):
    def __init__(self, category, message):
        if category not in CATEGORIES | {"INVALID_SCHEMA", "INVALID_CODEC"}:
            raise ValueError("unknown Historical error category")
        self.category = category
        super().__init__(message)


def require(condition, category="INVALID_SCHEMA", message="Historical contract mismatch"):
    if not condition:
        raise ProtocolError(category, message)
