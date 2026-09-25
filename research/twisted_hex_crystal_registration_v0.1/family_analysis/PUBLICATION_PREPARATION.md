# Crystal-lane publication preparation

This is a pre-staging package record, not a Git commit or publication receipt.
The controlling work order authorizes publication only after exact staging
and preservation checks, with **no whitespace exceptions**. An actual
failure requires stopping without normalizing the preserved sources.

Starting main and expected origin/main:
`1dca474e09b180664a17f85a0bb2f92967dd18f1`.

The explicit path list is `PUBLICATION_ALLOWLIST.txt`; it contains only this
crystal research lane and includes itself. `PUBLICATION_CENSUS.json` lists
every path and its class. `PUBLICATION_SHA256SUMS.txt` pins every allowlisted
file other than itself, using repository-relative paths. The execution
receipt pins that manifest too, avoiding a self-hash cycle.

All 60 original lane files are retained, including historical source copies,
the original verifiers and execution evidence, source/host/candidate JSON,
the complete atlas, both hands, the viewer and its existing QA. The small
font-cache JSON is retained as a previously manifested render artifact;
no Python/Node environment or large archive is copied. Pre-existing hash
manifests remain unchanged. The new report supplements their findings;
it does not relabel old logs as new execution.

`family_validation.json` contains the final 73/73 passing predicates.
They include direct coordinate identities and metrics, exact root isolation,
convexity/sign certificates, zero symmetries and surface separation. The
numerical zero intersection cross-check is identified separately. Counts
are evidence bookkeeping, not a count of independent theorems.

For reproduction, use a separate copy of this lane, with Python 3.12,
SymPy 1.14 and NumPy available, and run `family_exact_checks.py`. It imports
the preserved coordinate and face functions without invoking their builds.
It writes only the six generated JSON companions in its own analysis
directory. Their timestamps identify the new execution; do not overwrite
the frozen submitted evidence to make a new run look original.

`prepare_publication.py` checks the unchanged checkout and original file
identities, then writes the explicit census, allowlist, preservation check
and publication manifest. It does not stage, commit or push. It is a
pre-publication tool tied to the declared starting HEAD, not a general
post-publication maintenance command.

The final stage/commit/push receipt is saved outside this frozen lane under
`C:/TORMENT/TRIOCTAGON_new/publication_workspaces/twisted_hex_crystal_closeout_20260925/`.
It reports the actual Git result, including any required whitespace stop.
No successful publication is claimed here in advance of those gates.
