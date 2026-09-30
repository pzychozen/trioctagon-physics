"""Detached analysis contracts. No kernel import or execution at package import."""
__version__ = "0.1.1"

from .envelope import (ArtifactEnvelopeHint, ArtifactFamilyHint, CanonicalParseState,
                       probe_artifact_envelope)

__all__ = ("ArtifactEnvelopeHint", "ArtifactFamilyHint", "CanonicalParseState",
           "probe_artifact_envelope")
