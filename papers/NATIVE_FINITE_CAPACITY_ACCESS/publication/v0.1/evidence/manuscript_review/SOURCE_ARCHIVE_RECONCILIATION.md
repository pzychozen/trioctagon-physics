# Source-archive reconciliation — finite-capacity-access manuscript

**Date:** 4 November 2026. **Reviewer:** GPT, project-internal manuscript review.

## Finding

The checksum exception reported by Codex does **not** prevent use of the manuscript's scientific sources. The exact originally issued packet is independently available in the continuing conversation. Its outer checksum is correct, and all 74 of its members are byte-identical to their returned copies under `evidence/issued_packet/`.

| Object | Bytes | SHA-256 | Status |
|---|---:|---|---|
| Original issued packet, independently available here | 878459 | `2eab77538e18e5146dd123446535456ee2a46d0c3f4eb37269447d6470774668` | Recomputed; matches its original external sidecar |
| Different packet reported as received by Codex | 878805 | `d922e3c66848f1796b8a04b002f3b8aab4d4df2ecc163649186d048d0458422e` | Codex's recorded container identity; those raw container bytes were not delivered for this review |
| New Stage A review ZIP | 3560096 | `53fee5678e508d8ff07e36e48109b423dace9a1a08350338e45969476d3717d3` | Independently verified with its adjacent sidecar and exhaustive manifest |

The original packet has 74 members: 73 manifest-covered payloads plus its self-excluded manifest. Its paths are safe and unique and its CRC check passes. The returned issued-packet directory contains those same 74 files, exactly, and one extra file: `NATIVE_FINITE_CAPACITY_ACCESS_PAPER_AND_PUBLISH_01_CODEX_PACKET.zip.sha256`. That extra is byte-identical to the original external sidecar.

Thus the source membership difference is fully accounted for. The different outer ZIP's complete serialization, creation process and cause are not independently established here. A manifest verifies members, not an arbitrary enclosing archive; a sidecar identifying the original packet must not be described as identifying the changed received container. Recreating a ZIP after removing an entry also need not reproduce its earlier container bytes.

All 67 convenience-registry records and all 75 delivered-member registry records pass. The accepted proof, current scientific review and complete scientific-review archive additionally match separately mounted prior attachments. The nested original scientific submission matches its separately supplied archive. None of these originals has been edited.

## Disposition and preservation

**Source ambiguity resolved; no manuscript or mathematical change is required because of the container discrepancy.** This finding does not retroactively make Codex's received-container checksum match. Preserve its forensic record and later input-verification record as historical records; add this reconciliation as the subsequent resolution. The early forensic `do not use` disposition was followed by the recorded payload/anchor assessment and is now superseded for source-use purposes by this direct original-byte comparison.

The original issued packet and its matching sidecar are included in the GPT review package. This receipt does not authorize Stage B or assert a fresh remote repository check.
