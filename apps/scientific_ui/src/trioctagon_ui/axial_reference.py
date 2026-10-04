"""Inert, hash-bound Paper G excerpt. No proof or model matching is executed."""
import hashlib
from importlib import resources
import json
from trioctagon_ui.record_views import freeze

RESOURCE_SHA256 = 'bfacc19fbeddaebe6186c95ed09466f18291cf47aa22c5146573202cb18d46b0'


def load_reference(raw=None):
    if raw is None: raw = resources.files('trioctagon_ui').joinpath('axial_reference_v0_1.json').read_bytes()
    if hashlib.sha256(raw).hexdigest() != RESOURCE_SHA256:
        raise ValueError('Paper G reference resource identity mismatch; reference unavailable')
    return freeze(json.loads(raw))
