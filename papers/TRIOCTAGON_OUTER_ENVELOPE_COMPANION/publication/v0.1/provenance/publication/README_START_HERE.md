# Start here — outer-envelope manuscript acceptance and publication handoff

The actual 12-page manuscript has passed GPT manuscript review. No scientific, interpretive, documentary or layout correction is required.

Read `TRIOCTAGON_OUTER_ENVELOPE_PAPER_01_GPT_REVIEW.md`, `GPT_MANUSCRIPT_ACCEPTANCE.json`, then `TRIOCTAGON_OUTER_ENVELOPE_PUBLISH_01_CODEX_WORK_ORDER.md`.

**Author activation is still required.** The order becomes active when the author approves publication or explicitly instructs Codex to publish this packet. This package is not evidence of a completed commit or push.

The whole original review submission is preserved under `received/`; extract it into new external staging. It contains editable LaTeX, accepted science and all original evidence. `reviewed/` contains an unchanged reviewed PDF, with its historical pending-review label. `reviewer/` contains this manuscript-review audit and 12 page renders. `ADMINISTRATIVE_SOURCE_EDITS.json` supplies exact conditional status replacements, not silently modified source files.

After activation: status-only finalization, final Windows build and all-page inspection, scoped ordinary commit/normal push, fresh remote-byte and actual CI verification. Earlier papers and all inherited inputs stay unchanged. No scientific rerun or successor research.

`PACKET_MANIFEST.json` covers every other packet member. The external checksum binds the finished ZIP. Run `python tools/verify_packet.py` in the extracted packet to verify those local bytes; it runs no scientific or repository code.
