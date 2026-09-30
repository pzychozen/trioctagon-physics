from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
from unittest.mock import patch

import pytest

from trioctagon_analysis.codec import ParseLimits
from trioctagon_analysis.digests import FullArtifactDigest, InputByteDigest, byte_digest
from trioctagon_analysis.errors import ProtocolError
from trioctagon_analysis.persistence import persist_record, load_record
from support import PARSING, record_claim

pytestmark = pytest.mark.skipif(os.name != "nt", reason="qualified publication lane is Windows NTFS only")

def test_N28_one_file_commit_full_digest_external_and_idempotent_collision(tmp_path):
    record, parent = record_claim()
    stored = persist_record(record, tmp_path)
    raw = stored.path.read_bytes()
    assert raw == record.to_bytes()
    assert stored.digest == byte_digest(FullArtifactDigest, raw)
    assert stored.path.name == "sha256-" + stored.digest.sha256 + ".json"
    assert not stored.reused and list(tmp_path.iterdir()) == [stored.path]
    assert stored.digest.sha256.encode() not in raw  # no self-referential full digest slot
    loaded = load_record(stored.path, stored.digest, PARSING)
    loaded.verify_parent_copy(parent)
    assert persist_record(record, tmp_path).reused
    assert list(tmp_path.iterdir()) == [stored.path]

def test_N28_preexisting_corrupt_destination_is_never_overwritten(tmp_path):
    record, _ = record_claim()
    identity = byte_digest(FullArtifactDigest, record.to_bytes())
    path = tmp_path / ("sha256-" + identity.sha256 + ".json")
    path.write_bytes(b"preexisting-different-artifact")
    with pytest.raises(ProtocolError) as caught:
        persist_record(record, tmp_path)
    assert caught.value.category == "PERSISTENCE_FAILURE"
    assert path.read_bytes() == b"preexisting-different-artifact"
    assert list(tmp_path.iterdir()) == [path]

def test_N28_failure_before_rename_exposes_no_final_file(tmp_path):
    record, _ = record_claim()
    with patch("trioctagon_analysis.persistence._rename_noreplace", side_effect=PermissionError("injected")):
        with pytest.raises(ProtocolError):
            persist_record(record, tmp_path)
    assert not list(tmp_path.iterdir())

def test_N28_fsync_failure_exposes_no_partial_success(tmp_path):
    record, _ = record_claim()
    with patch("trioctagon_analysis.persistence.os.fsync", side_effect=OSError("injected")):
        with pytest.raises(ProtocolError):
            persist_record(record, tmp_path)
    assert not list(tmp_path.iterdir())

def test_N28_concurrent_identical_writers_one_commit_no_overwrite(tmp_path):
    record, _ = record_claim()
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(lambda _: persist_record(record, tmp_path), range(16)))
    assert sum(not result.reused for result in results) == 1
    assert len({result.path for result in results}) == 1
    assert len(list(tmp_path.iterdir())) == 1
    assert results[0].path.read_bytes() == record.to_bytes()

def test_N28_corrupt_and_noncanonical_load_rejected(tmp_path):
    record, _ = record_claim()
    stored = persist_record(record, tmp_path)
    stored.path.write_bytes(b"partial")
    with pytest.raises(ProtocolError):
        load_record(stored.path, stored.digest, PARSING)
    pretty = json.dumps(record.to_dict(), indent=2).encode()
    identity = byte_digest(FullArtifactDigest, pretty)
    path = tmp_path / ("sha256-" + identity.sha256 + ".json")
    path.write_bytes(pretty)
    with pytest.raises(ProtocolError, match="canonical"):
        load_record(path, identity, PARSING)

def test_N28_load_requires_full_scope_and_bounded_bytes(tmp_path):
    record, _ = record_claim()
    stored = persist_record(record, tmp_path)
    with pytest.raises(ProtocolError):
        load_record(stored.path, InputByteDigest(stored.digest.sha256), PARSING)
    with pytest.raises(ProtocolError):
        load_record(stored.path, stored.digest, ParseLimits(1, 64))
