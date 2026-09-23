from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib
import json

@dataclass(frozen=True)
class RunMeta:
    """Minimal provenance bundle to make runs reproducible + traceable."""
    version: str
    seed: int
    params_hash: str
    run_id: str
    timestamp_utc: str

def _stable_hash_dict(d: dict) -> str:
    blob = json.dumps(d, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
    return hashlib.sha1(blob).hexdigest()[:10]

def make_run_meta(version: str, seed: int, params_dict: dict) -> RunMeta:
    h = _stable_hash_dict(params_dict)
    run_id = f"v{version}_p{h}_s{int(seed)}"
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return RunMeta(
        version=str(version),
        seed=int(seed),
        params_hash=h,
        run_id=run_id,
        timestamp_utc=ts,
    )

def meta_dict(meta: RunMeta) -> dict:
    return asdict(meta)

def stamp_run_meta(fig, meta: RunMeta | None):
    """Stamp RunID + timestamp into the lower-left corner of a matplotlib figure."""
    if meta is None:
        return
    txt = f"{meta.run_id} | {meta.timestamp_utc}"
    fig.text(0.01, 0.01, txt, fontsize=8, alpha=0.8)
