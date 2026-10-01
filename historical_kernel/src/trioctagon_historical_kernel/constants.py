"""H4/H5 binary64 literals. No selector, coefficient overrides or scientific imports."""
from enum import Enum
from types import MappingProxyType


class KProfile(str, Enum):
    SCALED = "HISTORICAL_THETA_SCALED"
    SOFT = "HISTORICAL_THETA_SOFT"
    SIMPLE = "HISTORICAL_SIMPLE"


class Readout(str, Enum):
    NONE = "NONE"
    STAGED = "HISTORICAL_STAGED_Z_K"
    EMA = "HISTORICAL_COGNITIVE_EMA_Z_H"


K = MappingProxyType({
    KProfile.SCALED: tuple(map(float.fromhex, ("0x1.0000000000000p+0", "0x1.388cabcc6de5fp+0", "0x1.96993f4199da1p+2"))),
    KProfile.SOFT: tuple(map(float.fromhex, ("0x1.0000000000000p+0", "0x1.1add77ec19748p+0", "0x1.42a0ef567b39dp+1"))),
    KProfile.SIMPLE: tuple(map(float.fromhex, ("0x1.6666666666666p-1", "0x1.0000000000000p+0", "0x1.4cccccccccccdp+0"))),
})
EPSILON = float.fromhex("0x1.999999999999ap-5")
COUPLING = float.fromhex("0x1.999999999999ap-3")
PHASE_STRENGTH = float.fromhex("0x1.0624dd2f1a9fcp-10")
DT = float.fromhex("0x1.999999999999ap-4")
LAMBDA_VP = float.fromhex("0x1.3c6a7ef9db22dp-1")
GAMMA = float.fromhex("0x1.276c8b4395810p-1")
THETA_LOCK = float.fromhex("0x1.f3b645a1cac08p-3")
BETA = float.fromhex("0x1.0000000000000p-1")
INNOVATION = float.fromhex("0x1.47ae147ae147bp-7")
RETENTION = float.fromhex("0x1.fae147ae147aep-1")
PI = float.fromhex("0x1.921fb54442d18p+1")
HARMONIC = 3
SECTORS = 12
BASIS = tuple(tuple(map(float.fromhex, row)) for row in (
    ("0x1.279a74590331dp-1", "0x1.6a09e667f3bccp-1", "0x1.a20bd700c2c3fp-2"),
    ("0x1.279a74590331dp-1", "-0x1.6a09e667f3bccp-1", "0x1.a20bd700c2c3fp-2"),
    ("0x1.279a74590331dp-1", "0x0.0p+0", "-0x1.a20bd700c2c3fp-1"),
))
