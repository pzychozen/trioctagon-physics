# Source readback for Volume III R1 closure

Original programs were read as text only. No function was imported or executed.

## T: Tower II band versus global observer

Candidate member: `evidence/S6/source_package/original/srg_golden_tower_II.py`. SHA-256 `147a32be3b6d6aad17ada6ab7be2fbc3994c3363f74d6a2b351fb8eecda80304`.

```text
218:     def _record(self):
219:         t = self.pass_count
220:         R = self.resonance
221: 
222:         band_stats = {}
223:         for b in range(self.n_bands):
224:             mask = self.band_id == b
225:             if np.sum(mask) == 0:
226:                 continue
227:             R_b = np.abs(R[mask])
228:             mean_R = float(np.mean(R_b))
229:             band_stats[b] = {
230:                 'freq': float(self.tower_freqs[b]),
231:                 'tower_idx': self.tower_indices[b],
232:                 'mean_R': mean_R,
233:                 'max_R': float(np.max(R_b)),
234:                 'std_R': float(np.std(R_b)),
235:                 'count': int(np.sum(mask)),
236:                 'coherence': float(1.0 - np.std(R_b)/(np.mean(R_b)+1e-10)),
237:                 'mean_grf': float(np.mean(1.0/(1.0+np.linalg.norm(self.velocities[mask], axis=1))))
238:             }
239: 
240:             # Track lock time: first pass where band coherence > 0.7
241:             if b not in self.lock_times and band_stats[b]['coherence'] > 0.7 and mean_R > 0.01:
242:                 self.lock_times[b] = t
243: 
244:         self.band_history.append({'pass': t, 'bands': band_stats})
245:         self.metrics_history.append({
246:             'pass': t,
247:             'R_max': float(np.max(np.abs(R))),
248:             'R_mean': float(np.mean(np.abs(R))),
249:             'n_surviving_bands': len([b for b in band_stats.values() if b['mean_R'] > 0.01]),
250:         })
```

## U: Universe whole-field observer

Candidate member: `evidence/S7C/source_package/original/srg_condensate_breaking.py`. SHA-256 `a645a3bb564a2cae5e2b3ac3744f3f34f559a67132f255b3b0a97d277e68beb5`.

```text
243:         top_idx = np.argmax(np.abs(R))
244:         grf = 1.0 / (1.0 + np.linalg.norm(self.velocities, axis=1))
245: 
246:         self.metrics_history.append({
247:             'pass': t,
248:             'R_max': float(np.max(np.abs(R))),
249:             'R_min': float(np.min(np.abs(R))),
250:             'R_mean': float(np.mean(np.abs(R))),
251:             'R_std': float(np.std(R)),
252:             'n_resonance_clusters': n_clusters,
253:             'n_spatial_clusters': n_spatial_clusters,
254:             'entropy': float(entropy),
255:             'mean_grf': float(np.mean(grf)),
256:             'top_seed_id': int(top_idx),
257:             'L_effective': float(self._get_rpco_L(t)),
258:             **{f'band_{k}': v for k, v in band_R.items()}
259:         })
```

## Dated Universe construction review

Candidate member: `evidence/S7C/SIM07_GPT_SCIENTIFIC_REVIEW.md`. SHA-256 `3b48648a900598df5854431d184ec7d20d8d682e327900131d87c1e6cc0cdec4`.

```text
1: # SIM07 — Universe/condensate construction and original-aggregate review
2: 
3: **Date:** 25 October 2026  
4: **Author and research director:** Hilmir Frímann Halldórsson  
5: **Scientific reviewer:** GPT  
6: **Submitted research engineering:** Codex  
7: **Disposition:** **ACCEPTED_WITHIN_HISTORICAL_SOURCE_AND_ORIGINAL_AGGREGATE_SCOPE**  
8: **Required scientific revisions:** **None**  
9: **Status:** Research acceptance only. No new replay, merger study, paper, ledger edit, publication or Git action is authorized or executed by this receipt.
```

## Delivered generic C34 row

Candidate member: `CLAIM_EVIDENCE_MATRIX.md`. SHA-256 `c2eb953d7516da46cc84b8923aa8e02894de48b35ea20d653238b1f21e38ea43`.

```text
46: | C34 §10.1, Eqs31–32 | Entropy, amplitude-gap groups, linkage groups and mean reciprocal GRF; ORIGINAL / DERIVED | U:205–259; T:218–250; [S7C source readback](evidence/S7C/independent/SOURCE_READBACK.md) | Observer definitions do not add force/energy dynamics. |
```
