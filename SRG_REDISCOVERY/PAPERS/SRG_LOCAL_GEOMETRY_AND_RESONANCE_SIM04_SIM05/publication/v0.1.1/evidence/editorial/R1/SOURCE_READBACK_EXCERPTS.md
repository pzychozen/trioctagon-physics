# Exact source readback for E01–E03

These are text excerpts from byte-identical original source copies in the candidate. No source was imported or executed.

## SIM04/srg_seed_explorer.py

Bytes: 29820; SHA-256 `0c8ec661624bd100212b29d75dd184cacf2adbf5d173584e3817460d9fd6ea10`.

### Lines 268–274

```text
 268      def compute_coherence(self):
 269          """Measure global resonance coherence"""
 270          R = self.resonance
 271          if np.std(R) < 1e-12:
 272              return 1.0
 273          # Coherence = 1 - normalized variance
 274          return float(1.0 - np.std(R) / (np.mean(np.abs(R)) + 1e-8))
```

### Lines 617–650

```text
 617          # Cluster analysis
 618          dists = squareform(pdist(pos))
 619          _, dists_full = field._compute_adjacency()
 620          corridors = field._detect_echo_corridors(dists_full)
 621  
 622          # Resonance distribution stats
 623          R_mean = np.mean(np.abs(R))
 624          R_max = np.max(np.abs(R))
 625          R_std = np.std(R)
 626  
 627          # Spatial concentration (gyration radius)
 628          center = np.mean(pos, axis=0)
 629          Rg = np.sqrt(np.mean(np.sum((pos - center)**2, axis=1)))
 630  
 631          # Energy metrics
 632          kinetic = np.mean(np.sum(field.velocities**2, axis=1))
 633  
 634          # Top seed tracking
 635          top_idx = np.argmax(np.abs(R))
 636  
 637          metrics = {
 638              'pass': p + 1,
 639              'R_mean': float(R_mean),
 640              'R_max': float(R_max),
 641              'R_std': float(R_std),
 642              'Rg': float(Rg),
 643              'kinetic_energy': float(kinetic),
 644              'n_corridors': len(corridors),
 645              'coherence': field.compute_coherence(),
 646              'top_seed_id': int(top_idx),
 647              'top_seed_R': float(R[top_idx]),
 648              'top_seed_x': float(pos[top_idx, 0]),
 649              'top_seed_y': float(pos[top_idx, 1]),
 650              'top_seed_z': float(pos[top_idx, 2])
```

## SIM05/srg_infinity.py

Bytes: 33529; SHA-256 `742e40f1b4326f3ea5c8c88bd59aec7ee5a2bb942755a0fbc1861ce7c5eddf9d`.

### Lines 190–205

```text
 190          # 5. Vesica frequency modulation
 191          self.resonance *= (1.0 - 0.001 * np.sin(t * self.omega_vesica * 2 * np.pi))
 192  
 193          # 6. RPCO compression on both fields
 194          self.resonance = rpco(self.resonance, L=self.rpco_L)
 195          self.dark_resonance = rpco(self.dark_resonance, L=self.rpco_L)
 196  
 197          # 7. Small tunneling noise (decreases with time for asymptotic study)
 198          noise_scale = 0.01 / (1 + 0.01 * t)  # decaying noise
 199          self.positions += np.random.normal(0, noise_scale, self.positions.shape)
 200  
 201          # Update velocities
 202          self.velocities = self.positions - old_pos
 203  
 204          # Record metrics
 205          self._record_metrics(adj, dists)
```

### Lines 225–226

```text
 225          # Coherence
 226          coh = 1.0 - np.std(R) / (np.mean(np.abs(R)) + 1e-8) if np.mean(np.abs(R)) > 1e-12 else 0
```

### Lines 245–249

```text
 245          metrics = {
 246              'pass': t,
 247              'R_max': float(np.max(np.abs(R))),
 248              'R_mean': float(np.mean(np.abs(R))),
 249              'R_std': float(np.std(R)),
```

### Lines 361–371

```text
 361      pos = field.positions
 362      R = np.abs(field.resonance)
 363  
 364      # Get the top glyphs by resonance
 365      top_n = min(12, field.N)
 366      top_idx = np.argsort(-R)[:top_n]
 367      top_pos = pos[top_idx]
 368      top_R = R[top_idx]
 369  
 370      center = np.mean(top_pos, axis=0)
 371      relative = top_pos - center
```

### Lines 439–445

```text
 439      # Inertia tensor analysis — what are the principal axes?
 440      weighted_pos = relative * top_R[:, np.newaxis]
 441      if len(weighted_pos) >= 3:
 442          inertia = np.zeros((3, 3))
 443          for p in weighted_pos:
 444              r2 = np.dot(p, p)
 445              inertia += r2 * np.eye(3) - np.outer(p, p)
```
