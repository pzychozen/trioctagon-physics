# Same-trajectory native return — review package

**Established for the declared finite fast-receiver regime.** The unchanged exchange candidate has an initially empty launch that first supplies native trial storage and later has strictly negative total native-to-carrier power on the same solution. The explicit sufficient threshold, witness time and strict margin are in the theorem.

Read:

1. [Proof report](NATIVE_SAME_TRAJECTORY_RETURN_01_PROOF.md).
2. [Claim/source ledger](NATIVE_SAME_TRAJECTORY_RETURN_01_CLAIM_SOURCE_LEDGER.md).
3. [Source identities](SOURCE_IDENTITIES.json), [execution record](EXECUTION_RECORD.md) and [review checks](REVIEW_CHECKS.json).
4. [Exact algebra results](EXACT_CERTIFICATE_RESULTS.json), with the [optional helper](exact_certificate_checks.py). These are supplementary, not the analytical PDE proof.

The seven defining source files are retained unchanged under sources/. The current order and standalone START_HERE context are included. No full handoff ZIP or its separate review text was available in the focused local search; all required hash-pinned defining texts were available.

The result establishes a sufficient finite-parameter existence regime. It does not cover every positive receiver coupling, identify a physical spatial circuit, establish a substantial return fraction or assert the exact receiver-power sign at the witness. The native store never exceeds its initial stock.

The review archive includes MEMBER_MANIFEST.json, which intentionally excludes its own hash. The adjacent archive SHA-256 and PACKAGE_VERIFICATION.json are external to avoid circular identities. Verify member set, sizes and hashes against the manifest. Supporting scripts preserve the process record; prepare_sources.py and finish_report.py are one-time preparation utilities, not instructions to rerun against the final package. The exact algebra helper can be run separately with existing SymPy:

    call conda activate torment
    python -I -B exact_certificate_checks.py

This is a local investigation for GPT/author review. No Git operation, publication, model change, numerical trajectory, native hybrid step or subsequent research phase was performed.
