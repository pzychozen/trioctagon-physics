"""Exact generic codec reuse. No copy, fork, registry mutation or scientific import."""
from trioctagon_analysis.codec import (CODEC, ParseLimits, canonical_bytes, decode,
                                      validate_f64)

__all__ = ("CODEC", "ParseLimits", "canonical_bytes", "decode", "validate_f64")
