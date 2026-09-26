"""The three named K0 presets. Original selection motivation remains unknown."""
from ._contract_types import Clock, EMAConfig, EMAState, ObserverRequest, Provenance, Seed, StagedConfig, _text

_K0 = "3d9e2c24f2cd9207242e16559558c6adabb21c04"
_LOCATOR = "kernel_physics/K0_KERNEL_AUTHORITY_PUBLIC_CONTRACT_FREEZE_v0.1.md#2-supported-v1-surface-for-k1"


def historical_seed(name: str) -> Seed:
    _text(name, "name")
    if name != "gate_torus_seed_v1":
        raise ValueError("unknown historical seed")
    return Seed(name=name, omega=(0.2+0.3j, -0.4+0.1j, 0.1-0.2j), provenance=Provenance(
        kind="historical_preset", source_id=name, source_revision=_K0, locator=_LOCATOR,
        literal_values={"omega": "(0.2+0.3j,-0.4+0.1j,0.1-0.2j)"},
        notes="Saved gate/torus seed; original selection rationale is OPEN_NONBLOCKING (O02)."))


def historical_observer(name: str) -> ObserverRequest:
    _text(name, "name")
    if name not in ("paper_e_staged_v1", "paper_e_ema_v1"):
        raise ValueError("unknown historical observer")
    literal = {"lambda_vp": ".618", "theta_lock": ".244", "alpha": "1", "beta": ".5",
               "N": "12", "q": "0", "t": "0", "q_step": "1", "dt": ".1",
               "initialization": "recomputed"}
    if name == "paper_e_staged_v1":
        config = StagedConfig(lambda_vp=.618, gamma=.577, theta_lock=.244, alpha=1, beta=.5)
        memory = None
        literal["gamma"] = ".577"
    else:
        config = EMAConfig(lambda_vp=.618, theta_lock=.244, alpha=1, beta=.5)
        memory = EMAState(m=0)
        literal["m"] = "0"
    return ObserverRequest(observer_id=name, config=config, clock=Clock(q=0, N=12, t=0, q_step=1),
                           memory=memory, dt=.1, initialization="recomputed", provenance=Provenance(
                               kind="historical_preset", source_id=name, source_revision=_K0,
                               locator=_LOCATOR, literal_values=literal,
                               notes="Named K0 run preset, not constructor-zero replay. Original lock rationale remains OPEN (O02)."))
