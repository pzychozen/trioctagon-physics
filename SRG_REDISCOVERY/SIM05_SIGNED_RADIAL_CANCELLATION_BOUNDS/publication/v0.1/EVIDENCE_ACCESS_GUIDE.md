# SIM05 evidence and access guide

Read [SIM05_REPORT.md](SIM05_REPORT.md) for the scientific answer, [MATHEMATICAL_RESULTS.md](MATHEMATICAL_RESULTS.md) for the pre-evaluation proofs, and [OUTPUT_FIELD_GUIDE.md](OUTPUT_FIELD_GUIDE.md) for exact fields, units, signs, masks and joins. This is a local scientific review handback, not a paper or publication payload.

## Accepted authorities retained unchanged

SIM04 is accepted locally; its publication is not asserted. SIM03's source checkpoint is `e1f5115402a05965834493c1254b03118a531c92`. The original SIM04 ZIP and all 95 of its manifested members plus the transport seal were checked against the actual original files, making 97 protected SIM04 files. The 12 specifically required source copies below are unchanged and accessible in this bundle. Their roles and exact supplied NPZ/CSV schemas are in [INPUT_MAP.json](evidence/INPUT_MAP.json).

| Bundled path | Bytes | SHA-256 |
|---|---|---|
| `inputs/MANIFEST.json` | 14521 | `1f33b8b7cdd37475f50357df22c32682405985253386bb7ab3e4a061abb2dce3` |
| `inputs/SIM04_REPORT.md` | 18458 | `b95abdb7aecfbe38b7e340035497db6bc5801719aec257ce30a65344bcdaaf2f` |
| `inputs/MATHEMATICAL_RESULTS.md` | 8250 | `a0e655157fa848c3aa882a9f0105deac8514b38d4380b7f0f288eb7a89d56765` |
| `inputs/OUTPUT_FIELD_GUIDE.md` | 9981 | `bcee2a03988bad465561a257bd13879cf9cfd9cf60f20cb0294a394dc271d143` |
| `inputs/analysis/PRE_OUTPUT_BOUNDS.npz` | 4788324 | `5df03134e083e9879458eb8a0d560c3c1e9bd91f6a57b6d8c367e0a3ed749e6f` |
| `inputs/analysis/PRE_OUTPUT_BOUNDS_SEAL.json` | 610 | `7172a90d4ac7374e6bb48fb225dfbd0504266bf775e8615f8ed9ccfce6428b86` |
| `inputs/analysis/center_pair_bounds.npz` | 6009501 | `953b87a544cd963239d3a95e1d6fe96484e4b4438dbe51d9e8197d1a0107b820` |
| `inputs/analysis/cycle_phase_speeds.csv` | 69795 | `4dfbd6f7f8c20cab393370962a35dbb1ced8f277cdceb8e510a3eb554abb7d1f` |
| `inputs/analysis/phase_dispersion_bounds.csv` | 650889 | `4cf05a7f5f2f081c7520136a62b8ff5af910577b6a998256e45ab9f408c4718a` |
| `inputs/analysis/pair_phase_bounds.csv` | 2600784 | `00fb4c0a154f3afacb74cebe07414d8b1a4b22f8e840a582482d900d2a7d4c5e` |
| `inputs/analysis/selected_record_map.csv` | 297411 | `c04b68db071bd287fcb4443ac29741a2732baa69a3e06abd0eca7e222cbe7095` |
| `inputs/evidence/OUTPUT_SCHEMAS.json` | 28319 | `daafea246a5a0b9317f4018d780206584f008706539c5a3f20dfc1ac6f976a16` |

The original SIM04 MANIFEST.json is a historical inventory of a wider submission. It is intentionally not the inventory of this selected-input bundle; unchanged historical documents can link to files outside the selected 12. Use this new access map and the new root MANIFEST.json for the delivered scope. No upstream center_decomposition.npz, raw motion states, full old workspace or original SIM04 submission ZIP is duplicated into the review bundle.

The complete accepted GPT review is retained both as [the unchanged original reviewer ZIP](received/reference/SIM04_GPT_SCIENTIFIC_REVIEW_v0.1.zip) and as all ten unpacked members under `review/`. Its [review manifest](review/REVIEW_MANIFEST.json) checks the nine other members. The [additional dominance theorem](review/ADDITIONAL_PROFILE_DOMINANCE_THEOREM.md) is separately attributed to that later GPT review. The reviewer script is provenance material and was never imported or executed. Its original execution prerequisites belong to the earlier review and are not new SIM05 dependencies.

All received handoff documents are unchanged under `received/`; HANDOFF_MANIFEST.json covers its other eleven members. The original outer handoff remains at the supplied Downloads path and is hash-recorded in RECEIVE.json. No historical search or remote query was needed.

## Gates, sealed bounds and numerical outputs

The proof, [input gate](evidence/INPUT_GATE.json), [fixture record](evidence/ALGEBRA_FIXTURES.json), [outcome-isolation canary](evidence/OUTCOME_ISOLATION.json) and [implementation gate](evidence/IMPLEMENTATION_GATE.json) precede the primary pass. The implementation gate freezes the analytic/primary/fixture/supervisor/summary scripts, proof and specifications. The pure [radial.py](analyst/radial.py) accepts only p,q,P; it has no D/F, file, engine or outcome dependency. The new [fixtures.py](analyst/fixtures.py) contains the synthetic-only reference D. No historical scientific entry point is imported.

The [analytic seal](analysis/PRE_OUTPUT_INTERVALS_SEAL.json) covers all center/pair/variance intervals in PRE_OUTPUT_INTERVALS.npz before the saved-outcome join. [DATA_ACCESS_LOG.json](evidence/DATA_ACCESS_LOG.json) records the field allowlist and later accesses. Pair and center rows are explicit joins, retained in [join_map.csv](analysis/join_map.csv). All outcomes used are copied accepted saved differences or scalar reference values, never newly computed exact damping responses.

The 2,000-row pair table and 400-row dispersion table contain all raw/effective upper/lower intervals, all five upper families, all phases, masks and the independent decrease/increase/actual classifications. The center archive retains all nodes, numerator/denominator envelopes, original/raw/effective endpoints, activity flags and saved signed differences. Complete summary/gap/phase tables and RESULTS.json preserve native-unit quantities, ratios, linear quantiles with locators, categories, signs and condition phase lists. NUMERICAL_RESIDUALS.npz and NUMERICAL_QA.json preserve all 96 signed check arrays and extrema. OUTPUT_SCHEMAS.json enumerates all exact array names/dtypes/shapes and CSV columns; its field-guide path is root-relative.

All selected numeric inputs needed to independently inspect the fixed construction are included. The one-shot supervisor intentionally refuses to overwrite a prior stage start. Preservation guards require the original Windows checkout and are not advertised as a portable execution package. Inspection does not authorize rerunning any scientific stage.

## Presentation and transport

Six new PNGs are under `plots/`, with all 200 phases and native units. [VISUAL_QA.json](evidence/VISUAL_QA.json) records individual inspection. Existing figures remain untouched. The execution receipt, command ledger, STARTED/COMPLETE/progress and stdout/stderr records document one attempt per stage and the file-only preparation exception. Preservation is bounded to the supplied source set and known protected working-tree files; local paths are private-review provenance.

The new root MANIFEST.json covers every archive member except itself. The external SIM05_TRANSPORT_SEAL.json records exact ZIP bytes/hash, the manifest identity, CRC/path/name/member verification, post-packaging preservation and aggregate file size including ZIP/cache/seal. It is outside the archive whose identity it asserts. The complete prior reviewer ZIP is the sole deliberately included historical ZIP. Fonts, cache/tmp files and unrelated materials are excluded from the archive while still counted against the local size cap.

`analyst/verify_bundle.py` is a new standard-library-only, read-only transport verifier. From CMD with torment active, `python -B analyst\verify_bundle.py` checks the default SIM05_GPT_REVIEW.zip, or accepts an explicit ZIP path. It executes no scientific code and writes no file. Compare its SHA-256 with the separate transport seal to authenticate the intended transport identity.
