# Source readback supporting E01–E02

All excerpts below were read as text. No source was imported or executed. PDF pages are physical, not printed labels.

## `closing_sections.tex` — lines 1–18

```text
1: \section{Observers, bounds and reviewed mathematics}\label{sec:observers}
2: \subsection{What the labels measure}
3: Universe sorts \(|R|\) descending, counts adjacent gaps whose magnitude exceeds \(0.05\max|R|\), and adds one. One amplitude group means no such large adjacent gap; it does not require equal extrema. Spatial groups come from average linkage of completed \(X\), cut at distance 2.0. Neither observer drives the next update.
4: 
5: With \(\pi_i=|R_i|/\sum_j|R_j|\), entropy is
6: \begin{equation}
7: \mathcal S=-\sum_i\pi_i\log(\pi_i+10^{-12}),
8: \end{equation}
9: or zero if the amplitude sum is zero. This is a dimensionless distribution statistic. Maximum, minimum and mean use \(|R|\), but \texttt{R\_std} uses signed \(R\). \texttt{top\_seed\_id} is the first argmax of \(|R|\), not a leader trajectory. Four-decimal frequency keys label fixed assignments, not measured instantaneous frequency.
10: 
11: Both sources' GRF observer is
12: \begin{equation}\label{eq:grf}
13: \overline{\mathrm{GRF}}=\frac1N\sum_i\frac1{1+\norm{V_i}},
14: \end{equation}
15: not \(1/(1+\mean_i\norm{V_i})\). This relation to displacement defines no force law. Lock, cluster, separate, merged and condensate must be read through actual thresholds. The full-universe printout calls population centers separate when distance exceeds 3; its diversity threshold is not a proof of independence.
16: 
17: \subsection{A large pooled spread can describe a tiny cloud}\label{sec:pooled}
18: The horizon and full-universe drivers use \texttt{np.std(pos\_k)} with no axis. For \(n\) points with vector mean \(\mu=(\mu_x,\mu_y,\mu_z)\), this pools \(3n\) entries around scalar mean \(m=(\mu_x+\mu_y+\mu_z)/3\). The reviewed identity is
```

## `evidence/S6/source_package/original/srg_golden_tower_II.py` — lines 218–250

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

## `evidence/S7C/source_package/original/srg_condensate_breaking.py` — lines 233–259

```text
233:         # Frequency band analysis
234:         if self.multi_freq:
235:             unique_freqs = np.unique(self.natural_freq)
236:             band_R = {}
237:             for f in unique_freqs:
238:                 mask = self.natural_freq == f
239:                 band_R[f"{f:.4f}"] = float(np.mean(np.abs(R[mask])))
240:         else:
241:             band_R = {}
242: 
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

## `references.bib` — lines 5–7

```text
5: @misc{s6review,author={{GPT}},title={{SIM06} scientific review and acceptance: Tower II},year={2026},note={24 October. Internal review and independent/FINDINGS.json, combined\_dependency\_graph.csv, VERIFICATION.json. S6: SIM06\_GPT\_SCIENTIFIC\_REVIEW.md.}}
6: @misc{s7creview,author={{GPT}},title={{SIM07} scientific review and acceptance: Universe construction},year={2026},note={24 October. Internal review and independent/FINDINGS.json, SOURCE\_READBACK.md. S7C: SIM07\_GPT\_SCIENTIFIC\_REVIEW.md.}}
7: @misc{s7rreview,author={{GPT}},title={{SIM07} replay scientific review and acceptance},year={2026},note={25 October. Internal review, independent/FINDINGS.json, GRAPH\_COUNTS.csv, ORDERED\_READ\_COUNTS.csv and three audit receipts. S7R: SIM07\_REPLAY\_GPT\_SCIENTIFIC\_REVIEW.md.}}
```

## `evidence/S7C/SIM07_GPT_SCIENTIFIC_REVIEW.md` — lines 1–10

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
10: 
```

## `evidence/S7C/GPT_ACCEPTANCE_RECEIPT.json` — lines 1–8

```text
1: {
2:   "date": "2026-10-25",
3:   "study": "SIM07_UNIVERSE_CONSTRUCTION_01",
4:   "disposition": "ACCEPTED_WITHIN_HISTORICAL_SOURCE_AND_ORIGINAL_AGGREGATE_SCOPE",
5:   "scientific_revisions_required": [],
6:   "source_file": "srg_condensate_breaking.py",
7:   "source_sha256": "a645a3bb564a2cae5e2b3ac3744f3f34f559a67132f255b3b0a97d277e68beb5",
8:   "submitted_zip": {
```
