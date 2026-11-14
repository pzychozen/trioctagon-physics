# Reproduction and verification boundary

The result uses Python 3.11.15 in the existing Windows `torment` Conda environment. Exact arithmetic is Python integer/Fraction arithmetic over Q(sqrt(2)), with an explicit ordered-field sign algorithm and Sturm polynomial root counting. SymPy 1.14.0 parses exact source expressions and formats representative planes. SciPy 1.17.1 and NumPy 2.4.4 were used only to nominate three candidate hulls. Matplotlib 3.10.9 produced the optional illustrative figure. No dependencies were installed or updated.

Extract the review ZIP into a **new external folder**, preserving the relative `sources/`, `data/` and `scripts/` paths. In Windows Command Prompt:

```bat
conda activate torment
set PYTHONDONTWRITEBYTECODE=1
set PYTHONUTF8=1
python -B scripts\check_certificate.py --certificate data\exact_certificate.json --output data\CHECKER_RECHECK.json
```

The checker needs the copied sources, Python and existing SymPy; it does not need SciPy, Matplotlib, the live repository, internet, native kernel or application. It reconstructs folds, reads the candidate, and writes the separately named result. It never changes certificate/source inputs. For the same Windows resource wrapper used in this task, use a fresh log tag:

```bat
python -B scripts\bounded.py check_certificate.py review_recheck --certificate data\exact_certificate.json --output data\CHECKER_RECHECK.json
```

The resource wrapper assigns the worker to a Windows Job Object with a 2 GiB process committed-memory ceiling and kill-on-close behavior. Its parent uses a 900-second wall timeout. The exact checker completed in about 3.22 seconds with approximately 76.59 MiB peak committed memory on the recorded run. These timings are observations, not promised runtimes.

`scripts/negative_controls.py` creates only in-memory damaged copies, checks the expected failure reason, and leaves the original certificate untouched. It also tests an even-multiplicity interior root and a valid polynomial with endpoint-only zeros. Its output is retained in `data/NEGATIVE_CONTROL_RESULTS.json` and `logs/controls_01.stdout`. Running it in a fresh extracted copy reproduces the controls without changing the repository or original sources.

The saved candidate's generation-time status says that it awaited the independent checker. That historical generation label was not overwritten to fabricate prior acceptance. `data/CHECKER_RESULT.json` binds the exact candidate hash and reports the subsequent result; `data/CURRENT_DISPOSITION.json` records the current return status. The checker ignores status fields and recomputes all decisive predicates.

## Files and exact conventions

- `data/exact_certificate.json`: field encoding, 42 affine points, exact transition, all maximal face cycles/planes/residuals, 12 group actions, face orbits and inherited endpoint mappings.
- `data/CHECKER_RESULT.json`: independently reconstructed support/order/topology/coverage decisions, endpoint correspondence and limit maps.
- `data/FACE_INCIDENCE_RECORDS.json`: complete consolidated face/edge/vertex data; each chamber's labels and IDs are distinct namespaces.
- `data/FACE_REPRESENTATIVES.md` and JSON: all 26 exact new-domain orbit representatives. These are equivalent outward plane equations after positive normalization.
- `data/CANDIDATE_RESIDUAL_TABLE.md`: the complete sign table for the nominated six-point plane, with no tolerance.
- `data/TRANSITION_READOUT.json`: all six local regroupings, disappearing/appearing edges and endpoint collapse accounting.
- `data/EXPLORATORY_NOMINATION.json`: three floating nominations, explicitly outside the proof basis. No additional bisection evaluations occurred.
- `sources/`: authenticated originals plus explicitly distinguished local context. `packet/` preserves the unchanged incoming GPT proposal and pilot evidence; those proposals do not replace the original geometry or the new checker.
- `logs/`: actual bounded-worker stdout/stderr and resource records. Raw whole-repository snapshots/path dumps are excluded from the review payload; the compact preservation record retains the relevant identities and comparison outcomes.

No old 816-triple hull enumeration, 861-branch-pair catalogue, historical scientific suite, production kernel, TORMENT simulation, UI or PDF build was run. No Git operation other than read-only inspection/retrieval occurred. No manuscript or application viewer is part of this return.

## Shared implementation and limits

The generator and checker share `exact.py` and the disclosed source parser. The generator reads the inventory; the checker rebuilds the original folds and recomputes all support, complete-zero-set, order, ridge-closure, endpoint and group predicates. This is separately organized checking, not two independent algebra engines. The proof report supplies the mathematical completeness argument. Hashes bind data and code but do not prove theorems. No proof-assistant verification or external peer review is claimed.

`METHOD_AND_RESOURCE_PLAN.md` was written before the scientific workers and fixes the method and ceilings. Actual execution used six bounded workers: one nomination/generation, one decisive checker, one rejection-control run, one exact readout, and two figure renders. The second render corrected overlapping labels in the illustration; it made no new geometry decision or hull evaluation. All workers completed within the stated time and memory ceilings. There were no scientific worker failures or automatic scope expansions.

The self-excluding payload manifest is checked before packaging. The external archive audit reopens every member, checks sizes/hashes/CRC/safe unique paths, and binds the finished review ZIP. The archive hash and audit remain outside the archive to avoid circular identities.
