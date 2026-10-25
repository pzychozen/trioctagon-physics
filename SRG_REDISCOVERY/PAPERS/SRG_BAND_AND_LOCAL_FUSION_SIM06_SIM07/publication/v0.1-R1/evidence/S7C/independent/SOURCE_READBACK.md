# SIM07 original-source readback

## Original source lines 60–103

```text
60: class GlyphFieldUniverse:
61:     def __init__(self, N, R_range=(0, 0.3), spatial_range=(-5, 5), seed=None,
62:                  horizon=None, multi_freq=False, breathing=False):
63:         if seed is not None:
64:             np.random.seed(seed)
65:         self.N = N
66:         self.positions = np.random.uniform(spatial_range[0], spatial_range[1], (N, 3))
67:         self.resonance = np.random.uniform(R_range[0], R_range[1], N)
68:         self.velocities = np.zeros((N, 3))
69:         self.pass_count = 0
70: 
71:         # NEW: Causal horizon (max interaction distance)
72:         self.horizon = horizon  # None = infinite, float = max range
73: 
74:         # NEW: Multi-frequency (each glyph has a natural frequency)
75:         self.multi_freq = multi_freq
76:         if multi_freq:
77:             # Assign natural frequencies from a discrete set
78:             self.natural_freq = np.random.choice(
79:                 [0.244, 0.244*PHI, 0.244*PHI**2, 0.244/PHI],
80:                 size=N
81:             )
82:         else:
83:             self.natural_freq = np.ones(N) * 0.244
84: 
85:         # NEW: Breathing RPCO
86:         self.breathing = breathing
87:         self.base_L = 9.0
88: 
89:         # Standard params
90:         self.alpha = 0.05
91:         self.beta = 0.15
92:         self.lam_H = 0.05
93:         self.k_neighbors = 5
94:         self.gamma_srg = 0.08699
95: 
96:         self.metrics_history = []
97: 
98:     def _get_rpco_L(self, t):
99:         if self.breathing:
100:             # L oscillates like a vesica piscis breath
101:             breath = 1.0 + 0.3 * np.sin(0.244 * 2 * np.pi * t) * np.exp(-0.01 * t)
102:             return self.base_L * breath
103:         return self.base_L
```

## Original source lines 105–153

```text
105:     def _adjacency_with_horizon(self):
106:         dists = squareform(pdist(self.positions))
107:         adj = np.zeros((self.N, self.N))
108:         for i in range(self.N):
109:             # Apply horizon mask
110:             if self.horizon is not None:
111:                 candidates = np.where(dists[i] < self.horizon)[0]
112:                 candidates = candidates[candidates != i]
113:             else:
114:                 candidates = np.arange(self.N)
115:                 candidates = candidates[candidates != i]
116: 
117:             if len(candidates) == 0:
118:                 continue
119: 
120:             # k-nearest within horizon
121:             within = np.argsort(dists[i, candidates])[:self.k_neighbors]
122:             neighbors = candidates[within]
123:             adj[i, neighbors] = 1
124: 
125:         return adj, dists
126: 
127:     def _resonance_coupling_with_freq(self, adj, dists):
128:         R_new = self.resonance.copy()
129:         for i in range(self.N):
130:             nbrs = np.where(adj[i] > 0)[0]
131:             if len(nbrs) == 0:
132:                 continue
133:             w = 1.0 / (dists[i, nbrs] + 1e-8)
134:             w /= w.sum()
135: 
136:             # Frequency-dependent coupling: only couple strongly if frequencies match
137:             if self.multi_freq:
138:                 freq_match = np.exp(-5.0 * (self.natural_freq[nbrs] - self.natural_freq[i])**2)
139:                 w *= freq_match
140:                 w_sum = w.sum()
141:                 if w_sum > 1e-10:
142:                     w /= w_sum
143:                 else:
144:                     continue
145: 
146:             R_nbr = np.sum(w * self.resonance[nbrs])
147:             R_new[i] += self.beta * (R_nbr - self.resonance[i])
148: 
149:             # Frequency-specific oscillation
150:             if self.multi_freq:
151:                 R_new[i] *= (1.0 + 0.01 * np.sin(self.natural_freq[i] * 2*np.pi * self.pass_count))
152: 
153:         return R_new
```

## Original source lines 155–266

```text
155:     def evolve_pass(self):
156:         self.pass_count += 1
157:         t = float(self.pass_count)
158:         old_pos = self.positions.copy()
159: 
160:         adj, dists = self._adjacency_with_horizon()
161: 
162:         # Spatial
163:         lap = np.zeros_like(self.positions)
164:         for i in range(self.N):
165:             nbrs = np.where(adj[i] > 0)[0]
166:             if len(nbrs) > 0:
167:                 lap[i] = np.mean(self.positions[nbrs] - self.positions[i], axis=0)
168:         self.positions += self.alpha * lap + self.beta * np.tanh(lap)
169: 
170:         # Resonance
171:         self.resonance = self._resonance_coupling_with_freq(adj, dists)
172: 
173:         # Memory
174:         h_t = H(t)
175:         mem = 1.0 + self.lam_H * h_t / H_MAX
176:         self.resonance *= mem
177: 
178:         # Fusion (only within horizon)
179:         if self.horizon is not None:
180:             # Local fusion: each glyph pulled toward its LOCAL cluster center
181:             for i in range(self.N):
182:                 nbrs = np.where(adj[i] > 0)[0]
183:                 if len(nbrs) > 0:
184:                     local_center = np.average(
185:                         self.positions[nbrs], axis=0,
186:                         weights=np.abs(self.resonance[nbrs]) + 1e-8
187:                     )
188:                     self.positions[i] += 0.03 * self.resonance[i] * (local_center - self.positions[i])
189:         else:
190:             center = np.average(self.positions, axis=0,
191:                               weights=np.abs(self.resonance) + 1e-8)
192:             self.positions += 0.03 * self.resonance[:, np.newaxis] * (center - self.positions)
193: 
194:         # RPCO with optional breathing
195:         L = self._get_rpco_L(t)
196:         self.resonance = rpco(self.resonance, L=L)
197: 
198:         # Decaying noise
199:         noise_scale = 0.01 / (1 + 0.01 * t)
200:         self.positions += np.random.normal(0, noise_scale, self.positions.shape)
201: 
202:         self.velocities = self.positions - old_pos
203:         self._record(adj, dists)
204: 
205:     def _record(self, adj, dists):
206:         t = self.pass_count
207:         R = self.resonance
208: 
209:         # Cluster detection: how many distinct resonance groups?
210:         R_sorted = np.sort(np.abs(R))[::-1]
211:         # Count clusters by finding gaps > 5% of max
212:         gaps = np.diff(R_sorted)
213:         significant_gaps = np.where(np.abs(gaps) > 0.05 * R_sorted[0])[0]
214:         n_clusters = len(significant_gaps) + 1
215: 
216:         # Spatial cluster detection
217:         from scipy.cluster.hierarchy import fcluster, linkage
218:         if len(self.positions) >= 2:
219:             Z = linkage(self.positions, method='average')
220:             spatial_clusters = fcluster(Z, t=2.0, criterion='distance')
221:             n_spatial_clusters = len(set(spatial_clusters))
222:         else:
223:             n_spatial_clusters = 1
224: 
225:         # Resonance diversity (entropy-like)
226:         R_abs = np.abs(R)
227:         if R_abs.sum() > 0:
228:             p = R_abs / R_abs.sum()
229:             entropy = -np.sum(p * np.log(p + 1e-12))
230:         else:
231:             entropy = 0
232: 
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
260: 
261:     def evolve(self, n_passes):
262:         for _ in range(n_passes):
263:             self.evolve_pass()
264: 
265:     def get_metrics_df(self):
266:         return pd.DataFrame(self.metrics_history)
```

## Original source lines 278–355

```text
278:     # First: build a condensate (100 passes, no horizon)
279:     field = GlyphFieldUniverse(50, R_range=(0, 0.3), spatial_range=(-5, 5), seed=2038)
280:     field.evolve(100)
281: 
282:     R_equilibrium = field.resonance.copy()
283:     pos_equilibrium = field.positions.copy()
284:     print(f"\n  Condensate formed: R_eq = {R_equilibrium[0]:.6f} (uniform)")
285: 
286:     # Now: perturb a single glyph and watch the response
287:     perturbation_strengths = [0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0]
288:     results = []
289: 
290:     for delta in perturbation_strengths:
291:         # Reset to equilibrium
292:         field.resonance = R_equilibrium.copy()
293:         field.positions = pos_equilibrium.copy()
294:         field.velocities = np.zeros_like(field.velocities)
295:         field.metrics_history = []
296:         field.pass_count = 100
297: 
298:         # Perturb glyph 0
299:         field.resonance[0] += delta
300: 
301:         # Watch response for 50 passes
302:         response = []
303:         for p in range(50):
304:             field.evolve_pass()
305:             # Track the perturbed glyph and its neighbors
306:             R_perturbed = field.resonance[0]
307:             R_mean_others = np.mean(field.resonance[1:])
308:             deviation = R_perturbed - R_mean_others
309:             response.append({
310:                 'pass_after_kick': p + 1,
311:                 'R_perturbed': float(R_perturbed),
312:                 'R_mean_others': float(R_mean_others),
313:                 'deviation': float(deviation)
314:             })
315: 
316:         resp_df = pd.DataFrame(response)
317: 
318:         # Analyze response type
319:         deviations = resp_df['deviation'].values
320:         final_dev = abs(deviations[-1])
321:         max_dev = max(abs(deviations))
322: 
323:         # Check for oscillation
324:         peaks, _ = find_peaks(np.abs(deviations), height=0.001)
325:         n_oscillations = len(peaks)
326: 
327:         # Decay time (when deviation drops below 10% of initial)
328:         initial_dev = abs(deviations[0])
329:         decay_idx = np.where(np.abs(deviations) < 0.1 * initial_dev)[0]
330:         decay_time = decay_idx[0] + 1 if len(decay_idx) > 0 else None
331: 
332:         # Classification
333:         if final_dev < 0.001 * max_dev:
334:             response_type = "ABSORBED"  # perturbation fully absorbed
335:         elif n_oscillations > 3:
336:             response_type = "OSCILLATING"  # quasi-particle excitation
337:         elif final_dev > 0.5 * initial_dev:
338:             response_type = "PERSISTENT"  # new state
339:         else:
340:             response_type = "DECAYING"
341: 
342:         result = {
343:             'delta': delta,
344:             'delta_over_Req': delta / R_equilibrium[0],
345:             'initial_deviation': float(initial_dev),
346:             'final_deviation': float(final_dev),
347:             'n_oscillations': n_oscillations,
348:             'decay_time': decay_time,
349:             'response_type': response_type
350:         }
351:         results.append(result)
352: 
353:         print(f"  δ={delta:.3f} ({delta/R_equilibrium[0]:.1%} of R_eq): "
354:               f"{response_type}, decay_τ={decay_time}, "
355:               f"oscillations={n_oscillations}, final_dev={final_dev:.6f}")
```

## Original source lines 388–474

```text
388:     # Place 4 clusters at corners of a tetrahedron
389:     cluster_centers = np.array([
390:         [5, 5, 5],
391:         [5, -5, -5],
392:         [-5, 5, -5],
393:         [-5, -5, 5]
394:     ], dtype=float)
395: 
396:     for horizon in [3.0, 5.0, 8.0, 12.0, 20.0, None]:
397:         horizon_label = f"{horizon:.1f}" if horizon else "∞"
398:         print(f"\n  Horizon = {horizon_label}")
399: 
400:         for trial in range(3):
401:             np.random.seed(42 + trial)
402: 
403:             N_per = 20
404:             N_total = N_per * 4
405:             all_pos = []
406:             for c in cluster_centers:
407:                 all_pos.append(np.random.normal(c, 1.0, (N_per, 3)))
408:             all_pos = np.vstack(all_pos)
409: 
410:             field = GlyphFieldUniverse(N_total, horizon=horizon, seed=None)
411:             field.positions = all_pos
412:             field.resonance = np.random.uniform(0, 0.3, N_total)
413:             field.evolve(100)
414: 
415:             df = field.get_metrics_df()
416: 
417:             # How many spatial clusters survive?
418:             final_n_spatial = df.iloc[-1]['n_spatial_clusters']
419:             final_n_resonance = df.iloc[-1]['n_resonance_clusters']
420:             final_entropy = df.iloc[-1]['entropy']
421: 
422:             # Check if clusters remained separate
423:             final_pos = field.positions
424:             cluster_coms = []
425:             for k in range(4):
426:                 idx = range(k*N_per, (k+1)*N_per)
427:                 com = np.mean(final_pos[idx], axis=0)
428:                 cluster_coms.append(com)
429:             cluster_coms = np.array(cluster_coms)
430: 
431:             # Inter-cluster distances
432:             inter_dists = pdist(cluster_coms)
433:             mean_inter = np.mean(inter_dists)
434:             min_inter = np.min(inter_dists)
435: 
436:             # Intra-cluster spread
437:             intra_spreads = []
438:             for k in range(4):
439:                 idx = range(k*N_per, (k+1)*N_per)
440:                 spread = np.std(final_pos[idx])
441:                 intra_spreads.append(spread)
442:             mean_intra = np.mean(intra_spreads)
443: 
444:             # Separation ratio: inter/intra > 3 means well-separated
445:             sep_ratio = mean_inter / (mean_intra + 1e-8)
446: 
447:             # Resonance uniformity within clusters
448:             R_uniformity = []
449:             for k in range(4):
450:                 idx = list(range(k*N_per, (k+1)*N_per))
451:                 R_k = field.resonance[idx]
452:                 R_uniformity.append(np.std(R_k) / (np.mean(np.abs(R_k)) + 1e-8))
453:             mean_uniformity = np.mean(R_uniformity)
454: 
455:             # Are the clusters' resonances DIFFERENT from each other?
456:             cluster_means = []
457:             for k in range(4):
458:                 idx = list(range(k*N_per, (k+1)*N_per))
459:                 cluster_means.append(np.mean(np.abs(field.resonance[idx])))
460:             inter_R_diversity = np.std(cluster_means) / (np.mean(cluster_means) + 1e-8)
461: 
462:             result = {
463:                 'horizon': horizon if horizon else 999,
464:                 'trial': trial,
465:                 'n_spatial_clusters': int(final_n_spatial),
466:                 'n_resonance_clusters': int(final_n_resonance),
467:                 'entropy': float(final_entropy),
468:                 'separation_ratio': float(sep_ratio),
469:                 'mean_inter_dist': float(mean_inter),
470:                 'min_inter_dist': float(min_inter),
471:                 'mean_intra_spread': float(mean_intra),
472:                 'intra_uniformity': float(mean_uniformity),
473:                 'inter_R_diversity': float(inter_R_diversity)
474:             }
```

## Original source lines 514–575

```text
514:     for multi_freq in [False, True]:
515:         label = "multi-freq" if multi_freq else "single-freq"
516:         print(f"\n  --- {label} ---")
517: 
518:         for trial in range(3):
519:             field = GlyphFieldUniverse(
520:                 60, R_range=(0, 0.3), spatial_range=(-5, 5),
521:                 seed=42+trial, multi_freq=multi_freq
522:             )
523:             field.evolve(150)
524: 
525:             df = field.get_metrics_df()
526: 
527:             # Analyze frequency band survival
528:             if multi_freq:
529:                 unique_freqs = np.unique(field.natural_freq)
530:                 band_data = {}
531:                 for f in unique_freqs:
532:                     mask = field.natural_freq == f
533:                     R_band = np.abs(field.resonance[mask])
534:                     band_data[f] = {
535:                         'mean_R': float(np.mean(R_band)),
536:                         'std_R': float(np.std(R_band)),
537:                         'count': int(np.sum(mask)),
538:                         'max_R': float(np.max(R_band))
539:                     }
540: 
541:                 # Does one band dominate?
542:                 band_means = [bd['mean_R'] for bd in band_data.values()]
543:                 dominant_ratio = max(band_means) / (min(band_means) + 1e-10)
544: 
545:                 print(f"    Trial {trial}: {len(unique_freqs)} bands, "
546:                       f"dominant ratio={dominant_ratio:.2f}")
547:                 for f, bd in sorted(band_data.items()):
548:                     print(f"      ω={f:.4f}: <R>={bd['mean_R']:.6f}, "
549:                           f"n={bd['count']}, max={bd['max_R']:.6f}")
550: 
551:                 results.append({
552:                     'type': label,
553:                     'trial': trial,
554:                     'n_bands': len(unique_freqs),
555:                     'dominant_ratio': dominant_ratio,
556:                     'n_resonance_clusters': int(df.iloc[-1]['n_resonance_clusters']),
557:                     'entropy': float(df.iloc[-1]['entropy']),
558:                     'R_max': float(df.iloc[-1]['R_max'])
559:                 })
560:             else:
561:                 results.append({
562:                     'type': label,
563:                     'trial': trial,
564:                     'n_bands': 1,
565:                     'dominant_ratio': 1.0,
566:                     'n_resonance_clusters': int(df.iloc[-1]['n_resonance_clusters']),
567:                     'entropy': float(df.iloc[-1]['entropy']),
568:                     'R_max': float(df.iloc[-1]['R_max'])
569:                 })
570:                 print(f"    Trial {trial}: single band, "
571:                       f"R_max={df.iloc[-1]['R_max']:.6f}, "
572:                       f"entropy={df.iloc[-1]['entropy']:.3f}")
573: 
574:     results_df = pd.DataFrame(results)
575:     results_df.to_csv(f"{OUTPUT_DIR}/multi_frequency.csv", index=False)
```

## Original source lines 594–654

```text
594:     for breathing in [False, True]:
595:         label = "breathing" if breathing else "static"
596:         print(f"\n  --- {label} RPCO ---")
597: 
598:         field = GlyphFieldUniverse(
599:             50, R_range=(0, 0.3), spatial_range=(-5, 5),
600:             seed=2038, breathing=breathing
601:         )
602:         field.evolve(200)
603: 
604:         df = field.get_metrics_df()
605: 
606:         # Does breathing prevent full condensation?
607:         R_final_10 = df['R_max'].iloc[-10:].values
608:         R_drift = np.std(R_final_10) / (np.mean(R_final_10) + 1e-12)
609: 
610:         R_div = df['R_std'].iloc[-1] / (df['R_mean'].iloc[-1] + 1e-12)
611: 
612:         # Check for persistent oscillation in R_max
613:         R_series = df['R_max'].values
614:         if len(R_series) > 50:
615:             # Detrend
616:             from numpy.polynomial import polynomial as P
617:             t_arr = np.arange(len(R_series))
618:             coeffs = P.polyfit(t_arr, R_series, 2)
619:             trend = P.polyval(t_arr, coeffs)
620:             residual = R_series - trend
621: 
622:             # FFT of residual
623:             fft_vals = np.fft.rfft(residual[50:])  # skip transient
624:             freqs = np.fft.rfftfreq(len(residual[50:]))
625:             power = np.abs(fft_vals)**2
626: 
627:             # Dominant frequency
628:             dom_idx = np.argmax(power[1:]) + 1  # skip DC
629:             dom_freq = freqs[dom_idx]
630:             dom_power = power[dom_idx]
631:             total_power = np.sum(power[1:])
632:             dom_fraction = dom_power / (total_power + 1e-12)
633: 
634:             print(f"    R_drift: {R_drift:.6f}")
635:             print(f"    R diversity (std/mean): {R_div:.6f}")
636:             print(f"    Dominant oscillation freq: {dom_freq:.4f} (fraction: {dom_fraction:.3f})")
637:             print(f"    Final entropy: {df.iloc[-1]['entropy']:.4f}")
638:             print(f"    Final R_max: {df.iloc[-1]['R_max']:.6f}")
639:             print(f"    Final R_std: {df.iloc[-1]['R_std']:.6f}")
640: 
641:             results.append({
642:                 'type': label,
643:                 'R_drift': float(R_drift),
644:                 'R_diversity': float(R_div),
645:                 'dom_freq': float(dom_freq),
646:                 'dom_fraction': float(dom_fraction),
647:                 'entropy': float(df.iloc[-1]['entropy']),
648:                 'R_max': float(df.iloc[-1]['R_max']),
649:                 'R_std': float(df.iloc[-1]['R_std']),
650:                 'n_resonance_clusters': int(df.iloc[-1]['n_resonance_clusters'])
651:             })
652: 
653:     results_df = pd.DataFrame(results)
654:     results_df.to_csv(f"{OUTPUT_DIR}/breathing_condensate.csv", index=False)
```

## Original source lines 675–757

```text
675:     np.random.seed(1618)
676: 
677:     N = 120
678:     # Place 6 clusters in 3D space, well-separated
679:     centers = np.array([
680:         [8, 0, 0], [-8, 0, 0],
681:         [0, 8, 0], [0, -8, 0],
682:         [0, 0, 8], [0, 0, -8]
683:     ], dtype=float)
684: 
685:     N_per = N // 6
686:     all_pos = []
687:     for c in centers:
688:         all_pos.append(np.random.normal(c, 1.5, (N_per, 3)))
689:     all_pos = np.vstack(all_pos)
690: 
691:     field = GlyphFieldUniverse(
692:         len(all_pos),
693:         horizon=6.0,        # Each cluster only sees itself
694:         multi_freq=True,     # Multiple resonance bands
695:         breathing=True,      # Living compression
696:         seed=None
697:     )
698:     field.positions = all_pos
699:     field.resonance = np.random.uniform(0, 0.3, len(all_pos))
700: 
701:     # Evolve for a long time
702:     field.evolve(200)
703:     df = field.get_metrics_df()
704: 
705:     print(f"\n  --- Final State (200 passes) ---")
706:     print(f"  Spatial clusters: {df.iloc[-1]['n_spatial_clusters']}")
707:     print(f"  Resonance clusters: {df.iloc[-1]['n_resonance_clusters']}")
708:     print(f"  Entropy: {df.iloc[-1]['entropy']:.4f}")
709:     print(f"  R_max: {df.iloc[-1]['R_max']:.6f}")
710:     print(f"  R_std: {df.iloc[-1]['R_std']:.6f}")
711: 
712:     # Analyze each physical cluster
713:     print(f"\n  --- Per-Cluster Analysis ---")
714:     for k in range(6):
715:         idx = list(range(k*N_per, (k+1)*N_per))
716:         R_k = field.resonance[idx]
717:         pos_k = field.positions[idx]
718:         freq_k = field.natural_freq[idx]
719: 
720:         com = np.mean(pos_k, axis=0)
721:         spread = np.std(pos_k)
722:         R_mean = np.mean(np.abs(R_k))
723:         R_std = np.std(R_k)
724: 
725:         # How many frequency bands in this cluster?
726:         unique_f = np.unique(freq_k)
727:         freq_report = ", ".join([f"{f:.3f}({np.sum(freq_k==f)})" for f in unique_f])
728: 
729:         print(f"    Cluster {k}: COM=({com[0]:.1f},{com[1]:.1f},{com[2]:.1f}), "
730:               f"spread={spread:.3f}, <R>={R_mean:.6f}, σR={R_std:.6f}")
731:         print(f"      Frequency bands: {freq_report}")
732: 
733:     # Are the clusters INDEPENDENT?
734:     cluster_R_means = []
735:     for k in range(6):
736:         idx = list(range(k*N_per, (k+1)*N_per))
737:         cluster_R_means.append(np.mean(np.abs(field.resonance[idx])))
738: 
739:     inter_diversity = np.std(cluster_R_means) / (np.mean(cluster_R_means) + 1e-10)
740:     print(f"\n  Inter-cluster R diversity: {inter_diversity:.4f}")
741:     print(f"  (> 0.01 means clusters are independently evolving)")
742: 
743:     # Check if any clusters have merged
744:     cluster_coms = []
745:     for k in range(6):
746:         idx = list(range(k*N_per, (k+1)*N_per))
747:         cluster_coms.append(np.mean(field.positions[idx], axis=0))
748:     cluster_coms = np.array(cluster_coms)
749: 
750:     inter_dists = squareform(pdist(cluster_coms))
751:     print(f"\n  Inter-cluster distances:")
752:     for i in range(6):
753:         for j in range(i+1, 6):
754:             status = "SEPARATE" if inter_dists[i,j] > 3 else "MERGED"
755:             print(f"    C{i}-C{j}: {inter_dists[i,j]:.2f} [{status}]")
756: 
757:     df.to_csv(f"{OUTPUT_DIR}/full_universe.csv", index=False)
```
