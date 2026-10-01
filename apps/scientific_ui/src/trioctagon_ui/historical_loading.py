"""Inert Historical ownership boundary. Only public protocol parsers are used."""
from dataclasses import dataclass
import sys

from .historical_identity import verify_installed_historical

RESULT_FAMILY = "TRIOCTAGON_HISTORICAL_DERIVED_ANALYSIS_RECORD"
RECEIPT_FAMILY = "TRIOCTAGON_HISTORICAL_ANALYSIS_ATTEMPT_RECEIPT"


@dataclass(frozen=True, slots=True)
class LoadedHistoricalResult:
    document: object
    source: object
    sha256: str
    loader: object
    external_expected_sha256: str | None = None
    external_identity_source: str | None = None

    @property
    def raw(self):
        return self.document.to_bytes()


@dataclass(frozen=True, slots=True)
class LoadedHistoricalReceipt(LoadedHistoricalResult):
    pass


def parse_historical(raw, family, schema, limits):
    """A family hint is never authority; the owning parser validates it again."""
    loader = verify_installed_historical()
    if family not in (RESULT_FAMILY, RECEIPT_FAMILY) or schema != "1.0.0":
        raise ValueError("UNKNOWN / UNSUPPORTED Historical family or schema")
    previous = sys.dont_write_bytecode
    try:
        sys.dont_write_bytecode = True
        from trioctagon_historical_protocol.records import DerivedRecord, AttemptReceipt
    finally:
        sys.dont_write_bytecode = previous
    verify_installed_historical()
    owner, handle = ((DerivedRecord, LoadedHistoricalResult) if family == RESULT_FAMILY
                     else (AttemptReceipt, LoadedHistoricalReceipt))
    document = owner.from_bytes(raw, limits)
    if raw != document.to_bytes():
        raise ValueError("NONCANONICAL_INPUT: Historical bytes must already be canonical")
    return document, handle, loader
