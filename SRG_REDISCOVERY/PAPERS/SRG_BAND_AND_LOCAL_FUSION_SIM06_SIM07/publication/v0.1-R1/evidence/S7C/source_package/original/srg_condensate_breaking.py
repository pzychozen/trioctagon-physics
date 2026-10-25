#!/usr/bin/env python3
"""
=============================================================================
 SRG-∞ PART II: BREAKING THE CONDENSATE

 The SRG-∞ condensate is a uniform resonance droplet where all glyphs
 share the same state. This is beautiful but featureless.

 Real universes have structure. So: how do you break the condensate?

 Three experiments:
 1. PERTURBATION RESPONSE — Kick one glyph. Does it snap back, oscillate,
    or trigger a cascade? This reveals the quasi-particle spectrum.
 2. CAUSAL HORIZONS — Limit interaction range. Can independent seeds form?
 3. MULTI-FREQUENCY FIELDS — Give glyphs different natural frequencies.
    Can multiple resonance bands coexist at infinity?

 Plus a bonus:
 4. THE VESICA PISCIS BREATH — What if the compression bound L oscillates
    like a breathing membrane? This is the "living" SRG.

 Author: Claude (collaborating with pzychozen)
 Date: 2026-03-14
=============================================================================
"""

import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, squareform
from scipy.signal import find_peaks
import json
import os
import warnings
warnings.filterwarnings('ignore')

OUTPUT_DIR = "/sessions/vigilant-bold-allen/mnt/SRG_claude/Claude_SRG_Analysis"

# ============================================================================
# OPERATORS
# ============================================================================

def H(t):
    t = np.asarray(t, dtype=float)
    return (2.0*np.exp(-0.5*t)*np.cos(t) + 1.0*np.exp(-0.3*t)*np.sin(t)
            + 1.5*np.exp(-0.7*t) + 1.0*np.exp(-0.4*t))

def rpco(x, L=9.0, eps=1e-9):
    x = np.asarray(x, dtype=float)
    mag = np.abs(x) + eps
    z = np.clip(np.log(mag), -L, L)
    return np.sign(x) * np.exp(z)

H_MAX = float(np.max(np.abs(H(np.linspace(0, 100, 50000))))) + 1e-12
PHI = (1 + np.sqrt(5)) / 2

# ============================================================================
# ENHANCED ENGINE WITH HORIZONS + MULTI-FREQUENCY + BREATHING
# ============================================================================

class GlyphFieldUniverse:
    def __init__(self, N, R_range=(0, 0.3), spatial_range=(-5, 5), seed=None,
                 horizon=None, multi_freq=False, breathing=False):
        if seed is not None:
            np.random.seed(seed)
        self.N = N
        self.positions = np.random.uniform(spatial_range[0], spatial_range[1], (N, 3))
        self.resonance = np.random.uniform(R_range[0], R_range[1], N)
        self.velocities = np.zeros((N, 3))
        self.pass_count = 0

        # NEW: Causal horizon (max interaction distance)
        self.horizon = horizon  # None = infinite, float = max range

        # NEW: Multi-frequency (each glyph has a natural frequency)
        self.multi_freq = multi_freq
        if multi_freq:
            # Assign natural frequencies from a discrete set
            self.natural_freq = np.random.choice(
                [0.244, 0.244*PHI, 0.244*PHI**2, 0.244/PHI],
                size=N
            )
        else:
            self.natural_freq = np.ones(N) * 0.244

        # NEW: Breathing RPCO
        self.breathing = breathing
        self.base_L = 9.0

        # Standard params
        self.alpha = 0.05
        self.beta = 0.15
        self.lam_H = 0.05
        self.k_neighbors = 5
        self.gamma_srg = 0.08699

        self.metrics_history = []

    def _get_rpco_L(self, t):
        if self.breathing:
            # L oscillates like a vesica piscis breath
            breath = 1.0 + 0.3 * np.sin(0.244 * 2 * np.pi * t) * np.exp(-0.01 * t)
            return self.base_L * breath
        return self.base_L

    def _adjacency_with_horizon(self):
        dists = squareform(pdist(self.positions))
        adj = np.zeros((self.N, self.N))
        for i in range(self.N):
            # Apply horizon mask
            if self.horizon is not None:
                candidates = np.where(dists[i] < self.horizon)[0]
                candidates = candidates[candidates != i]
            else:
                candidates = np.arange(self.N)
                candidates = candidates[candidates != i]

            if len(candidates) == 0:
                continue

            # k-nearest within horizon
            within = np.argsort(dists[i, candidates])[:self.k_neighbors]
            neighbors = candidates[within]
            adj[i, neighbors] = 1

        return adj, dists

    def _resonance_coupling_with_freq(self, adj, dists):
        R_new = self.resonance.copy()
        for i in range(self.N):
            nbrs = np.where(adj[i] > 0)[0]
            if len(nbrs) == 0:
                continue
            w = 1.0 / (dists[i, nbrs] + 1e-8)
            w /= w.sum()

            # Frequency-dependent coupling: only couple strongly if frequencies match
            if self.multi_freq:
                freq_match = np.exp(-5.0 * (self.natural_freq[nbrs] - self.natural_freq[i])**2)
                w *= freq_match
                w_sum = w.sum()
                if w_sum > 1e-10:
                    w /= w_sum
                else:
                    continue

            R_nbr = np.sum(w * self.resonance[nbrs])
            R_new[i] += self.beta * (R_nbr - self.resonance[i])

            # Frequency-specific oscillation
            if self.multi_freq:
                R_new[i] *= (1.0 + 0.01 * np.sin(self.natural_freq[i] * 2*np.pi * self.pass_count))

        return R_new

    def evolve_pass(self):
        self.pass_count += 1
        t = float(self.pass_count)
        old_pos = self.positions.copy()

        adj, dists = self._adjacency_with_horizon()

        # Spatial
        lap = np.zeros_like(self.positions)
        for i in range(self.N):
            nbrs = np.where(adj[i] > 0)[0]
            if len(nbrs) > 0:
                lap[i] = np.mean(self.positions[nbrs] - self.positions[i], axis=0)
        self.positions += self.alpha * lap + self.beta * np.tanh(lap)

        # Resonance
        self.resonance = self._resonance_coupling_with_freq(adj, dists)

        # Memory
        h_t = H(t)
        mem = 1.0 + self.lam_H * h_t / H_MAX
        self.resonance *= mem

        # Fusion (only within horizon)
        if self.horizon is not None:
            # Local fusion: each glyph pulled toward its LOCAL cluster center
            for i in range(self.N):
                nbrs = np.where(adj[i] > 0)[0]
                if len(nbrs) > 0:
                    local_center = np.average(
                        self.positions[nbrs], axis=0,
                        weights=np.abs(self.resonance[nbrs]) + 1e-8
                    )
                    self.positions[i] += 0.03 * self.resonance[i] * (local_center - self.positions[i])
        else:
            center = np.average(self.positions, axis=0,
                              weights=np.abs(self.resonance) + 1e-8)
            self.positions += 0.03 * self.resonance[:, np.newaxis] * (center - self.positions)

        # RPCO with optional breathing
        L = self._get_rpco_L(t)
        self.resonance = rpco(self.resonance, L=L)

        # Decaying noise
        noise_scale = 0.01 / (1 + 0.01 * t)
        self.positions += np.random.normal(0, noise_scale, self.positions.shape)

        self.velocities = self.positions - old_pos
        self._record(adj, dists)

    def _record(self, adj, dists):
        t = self.pass_count
        R = self.resonance

        # Cluster detection: how many distinct resonance groups?
        R_sorted = np.sort(np.abs(R))[::-1]
        # Count clusters by finding gaps > 5% of max
        gaps = np.diff(R_sorted)
        significant_gaps = np.where(np.abs(gaps) > 0.05 * R_sorted[0])[0]
        n_clusters = len(significant_gaps) + 1

        # Spatial cluster detection
        from scipy.cluster.hierarchy import fcluster, linkage
        if len(self.positions) >= 2:
            Z = linkage(self.positions, method='average')
            spatial_clusters = fcluster(Z, t=2.0, criterion='distance')
            n_spatial_clusters = len(set(spatial_clusters))
        else:
            n_spatial_clusters = 1

        # Resonance diversity (entropy-like)
        R_abs = np.abs(R)
        if R_abs.sum() > 0:
            p = R_abs / R_abs.sum()
            entropy = -np.sum(p * np.log(p + 1e-12))
        else:
            entropy = 0

        # Frequency band analysis
        if self.multi_freq:
            unique_freqs = np.unique(self.natural_freq)
            band_R = {}
            for f in unique_freqs:
                mask = self.natural_freq == f
                band_R[f"{f:.4f}"] = float(np.mean(np.abs(R[mask])))
        else:
            band_R = {}

        top_idx = np.argmax(np.abs(R))
        grf = 1.0 / (1.0 + np.linalg.norm(self.velocities, axis=1))

        self.metrics_history.append({
            'pass': t,
            'R_max': float(np.max(np.abs(R))),
            'R_min': float(np.min(np.abs(R))),
            'R_mean': float(np.mean(np.abs(R))),
            'R_std': float(np.std(R)),
            'n_resonance_clusters': n_clusters,
            'n_spatial_clusters': n_spatial_clusters,
            'entropy': float(entropy),
            'mean_grf': float(np.mean(grf)),
            'top_seed_id': int(top_idx),
            'L_effective': float(self._get_rpco_L(t)),
            **{f'band_{k}': v for k, v in band_R.items()}
        })

    def evolve(self, n_passes):
        for _ in range(n_passes):
            self.evolve_pass()

    def get_metrics_df(self):
        return pd.DataFrame(self.metrics_history)


# ============================================================================
# EXPERIMENT 1: PERTURBATION OF THE CONDENSATE
# ============================================================================

def experiment_perturbation():
    print("=" * 70)
    print("EXPERIMENT 1: CONDENSATE PERTURBATION RESPONSE")
    print("=" * 70)

    # First: build a condensate (100 passes, no horizon)
    field = GlyphFieldUniverse(50, R_range=(0, 0.3), spatial_range=(-5, 5), seed=2038)
    field.evolve(100)

    R_equilibrium = field.resonance.copy()
    pos_equilibrium = field.positions.copy()
    print(f"\n  Condensate formed: R_eq = {R_equilibrium[0]:.6f} (uniform)")

    # Now: perturb a single glyph and watch the response
    perturbation_strengths = [0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0]
    results = []

    for delta in perturbation_strengths:
        # Reset to equilibrium
        field.resonance = R_equilibrium.copy()
        field.positions = pos_equilibrium.copy()
        field.velocities = np.zeros_like(field.velocities)
        field.metrics_history = []
        field.pass_count = 100

        # Perturb glyph 0
        field.resonance[0] += delta

        # Watch response for 50 passes
        response = []
        for p in range(50):
            field.evolve_pass()
            # Track the perturbed glyph and its neighbors
            R_perturbed = field.resonance[0]
            R_mean_others = np.mean(field.resonance[1:])
            deviation = R_perturbed - R_mean_others
            response.append({
                'pass_after_kick': p + 1,
                'R_perturbed': float(R_perturbed),
                'R_mean_others': float(R_mean_others),
                'deviation': float(deviation)
            })

        resp_df = pd.DataFrame(response)

        # Analyze response type
        deviations = resp_df['deviation'].values
        final_dev = abs(deviations[-1])
        max_dev = max(abs(deviations))

        # Check for oscillation
        peaks, _ = find_peaks(np.abs(deviations), height=0.001)
        n_oscillations = len(peaks)

        # Decay time (when deviation drops below 10% of initial)
        initial_dev = abs(deviations[0])
        decay_idx = np.where(np.abs(deviations) < 0.1 * initial_dev)[0]
        decay_time = decay_idx[0] + 1 if len(decay_idx) > 0 else None

        # Classification
        if final_dev < 0.001 * max_dev:
            response_type = "ABSORBED"  # perturbation fully absorbed
        elif n_oscillations > 3:
            response_type = "OSCILLATING"  # quasi-particle excitation
        elif final_dev > 0.5 * initial_dev:
            response_type = "PERSISTENT"  # new state
        else:
            response_type = "DECAYING"

        result = {
            'delta': delta,
            'delta_over_Req': delta / R_equilibrium[0],
            'initial_deviation': float(initial_dev),
            'final_deviation': float(final_dev),
            'n_oscillations': n_oscillations,
            'decay_time': decay_time,
            'response_type': response_type
        }
        results.append(result)

        print(f"  δ={delta:.3f} ({delta/R_equilibrium[0]:.1%} of R_eq): "
              f"{response_type}, decay_τ={decay_time}, "
              f"oscillations={n_oscillations}, final_dev={final_dev:.6f}")

    results_df = pd.DataFrame(results)
    results_df.to_csv(f"{OUTPUT_DIR}/condensate_perturbation.csv", index=False)

    # Find the critical perturbation threshold
    persistent = results_df[results_df['response_type'].isin(['PERSISTENT', 'OSCILLATING'])]
    absorbed = results_df[results_df['response_type'].isin(['ABSORBED', 'DECAYING'])]

    if len(persistent) > 0 and len(absorbed) > 0:
        critical_delta = persistent['delta'].min()
        print(f"\n  Critical perturbation threshold: δ_c ≈ {critical_delta:.3f} "
              f"({critical_delta/R_equilibrium[0]:.1%} of R_eq)")
    else:
        print(f"\n  All perturbations: {results_df['response_type'].value_counts().to_dict()}")

    return results_df


# ============================================================================
# EXPERIMENT 2: CAUSAL HORIZONS — MULTI-SEED UNIVERSE
# ============================================================================

def experiment_causal_horizons():
    print("\n" + "=" * 70)
    print("EXPERIMENT 2: CAUSAL HORIZONS — MULTI-SEED UNIVERSE")
    print("=" * 70)

    # Hypothesis: with a finite horizon, separated clusters should form
    # independent SRG-∞ seeds that DON'T merge.

    results = []

    # Place 4 clusters at corners of a tetrahedron
    cluster_centers = np.array([
        [5, 5, 5],
        [5, -5, -5],
        [-5, 5, -5],
        [-5, -5, 5]
    ], dtype=float)

    for horizon in [3.0, 5.0, 8.0, 12.0, 20.0, None]:
        horizon_label = f"{horizon:.1f}" if horizon else "∞"
        print(f"\n  Horizon = {horizon_label}")

        for trial in range(3):
            np.random.seed(42 + trial)

            N_per = 20
            N_total = N_per * 4
            all_pos = []
            for c in cluster_centers:
                all_pos.append(np.random.normal(c, 1.0, (N_per, 3)))
            all_pos = np.vstack(all_pos)

            field = GlyphFieldUniverse(N_total, horizon=horizon, seed=None)
            field.positions = all_pos
            field.resonance = np.random.uniform(0, 0.3, N_total)
            field.evolve(100)

            df = field.get_metrics_df()

            # How many spatial clusters survive?
            final_n_spatial = df.iloc[-1]['n_spatial_clusters']
            final_n_resonance = df.iloc[-1]['n_resonance_clusters']
            final_entropy = df.iloc[-1]['entropy']

            # Check if clusters remained separate
            final_pos = field.positions
            cluster_coms = []
            for k in range(4):
                idx = range(k*N_per, (k+1)*N_per)
                com = np.mean(final_pos[idx], axis=0)
                cluster_coms.append(com)
            cluster_coms = np.array(cluster_coms)

            # Inter-cluster distances
            inter_dists = pdist(cluster_coms)
            mean_inter = np.mean(inter_dists)
            min_inter = np.min(inter_dists)

            # Intra-cluster spread
            intra_spreads = []
            for k in range(4):
                idx = range(k*N_per, (k+1)*N_per)
                spread = np.std(final_pos[idx])
                intra_spreads.append(spread)
            mean_intra = np.mean(intra_spreads)

            # Separation ratio: inter/intra > 3 means well-separated
            sep_ratio = mean_inter / (mean_intra + 1e-8)

            # Resonance uniformity within clusters
            R_uniformity = []
            for k in range(4):
                idx = list(range(k*N_per, (k+1)*N_per))
                R_k = field.resonance[idx]
                R_uniformity.append(np.std(R_k) / (np.mean(np.abs(R_k)) + 1e-8))
            mean_uniformity = np.mean(R_uniformity)

            # Are the clusters' resonances DIFFERENT from each other?
            cluster_means = []
            for k in range(4):
                idx = list(range(k*N_per, (k+1)*N_per))
                cluster_means.append(np.mean(np.abs(field.resonance[idx])))
            inter_R_diversity = np.std(cluster_means) / (np.mean(cluster_means) + 1e-8)

            result = {
                'horizon': horizon if horizon else 999,
                'trial': trial,
                'n_spatial_clusters': int(final_n_spatial),
                'n_resonance_clusters': int(final_n_resonance),
                'entropy': float(final_entropy),
                'separation_ratio': float(sep_ratio),
                'mean_inter_dist': float(mean_inter),
                'min_inter_dist': float(min_inter),
                'mean_intra_spread': float(mean_intra),
                'intra_uniformity': float(mean_uniformity),
                'inter_R_diversity': float(inter_R_diversity)
            }
            results.append(result)

            if trial == 0:
                print(f"    spatial_clusters={int(final_n_spatial)}, "
                      f"sep_ratio={sep_ratio:.2f}, "
                      f"inter_R_diversity={inter_R_diversity:.4f}, "
                      f"entropy={final_entropy:.3f}")

    results_df = pd.DataFrame(results)
    results_df.to_csv(f"{OUTPUT_DIR}/causal_horizons.csv", index=False)

    # Summary
    print(f"\n  --- Summary by Horizon ---")
    print(f"  {'Horizon':<10} {'Spatial Clusters':<20} {'Sep Ratio':<14} {'R Diversity'}")
    print(f"  {'-'*58}")
    for h in results_df['horizon'].unique():
        sub = results_df[results_df['horizon'] == h]
        h_label = f"{h:.1f}" if h < 100 else "∞"
        print(f"  {h_label:<10} {sub['n_spatial_clusters'].mean():<20.1f} "
              f"{sub['separation_ratio'].mean():<14.2f} "
              f"{sub['inter_R_diversity'].mean():.4f}")

    return results_df


# ============================================================================
# EXPERIMENT 3: MULTI-FREQUENCY FIELDS
# ============================================================================

def experiment_multi_frequency():
    print("\n" + "=" * 70)
    print("EXPERIMENT 3: MULTI-FREQUENCY GLYPH FIELDS")
    print("=" * 70)

    # Can different frequency bands coexist at infinity?
    # Or does one frequency dominate and suppress the others?

    results = []

    for multi_freq in [False, True]:
        label = "multi-freq" if multi_freq else "single-freq"
        print(f"\n  --- {label} ---")

        for trial in range(3):
            field = GlyphFieldUniverse(
                60, R_range=(0, 0.3), spatial_range=(-5, 5),
                seed=42+trial, multi_freq=multi_freq
            )
            field.evolve(150)

            df = field.get_metrics_df()

            # Analyze frequency band survival
            if multi_freq:
                unique_freqs = np.unique(field.natural_freq)
                band_data = {}
                for f in unique_freqs:
                    mask = field.natural_freq == f
                    R_band = np.abs(field.resonance[mask])
                    band_data[f] = {
                        'mean_R': float(np.mean(R_band)),
                        'std_R': float(np.std(R_band)),
                        'count': int(np.sum(mask)),
                        'max_R': float(np.max(R_band))
                    }

                # Does one band dominate?
                band_means = [bd['mean_R'] for bd in band_data.values()]
                dominant_ratio = max(band_means) / (min(band_means) + 1e-10)

                print(f"    Trial {trial}: {len(unique_freqs)} bands, "
                      f"dominant ratio={dominant_ratio:.2f}")
                for f, bd in sorted(band_data.items()):
                    print(f"      ω={f:.4f}: <R>={bd['mean_R']:.6f}, "
                          f"n={bd['count']}, max={bd['max_R']:.6f}")

                results.append({
                    'type': label,
                    'trial': trial,
                    'n_bands': len(unique_freqs),
                    'dominant_ratio': dominant_ratio,
                    'n_resonance_clusters': int(df.iloc[-1]['n_resonance_clusters']),
                    'entropy': float(df.iloc[-1]['entropy']),
                    'R_max': float(df.iloc[-1]['R_max'])
                })
            else:
                results.append({
                    'type': label,
                    'trial': trial,
                    'n_bands': 1,
                    'dominant_ratio': 1.0,
                    'n_resonance_clusters': int(df.iloc[-1]['n_resonance_clusters']),
                    'entropy': float(df.iloc[-1]['entropy']),
                    'R_max': float(df.iloc[-1]['R_max'])
                })
                print(f"    Trial {trial}: single band, "
                      f"R_max={df.iloc[-1]['R_max']:.6f}, "
                      f"entropy={df.iloc[-1]['entropy']:.3f}")

    results_df = pd.DataFrame(results)
    results_df.to_csv(f"{OUTPUT_DIR}/multi_frequency.csv", index=False)
    return results_df


# ============================================================================
# EXPERIMENT 4: THE BREATHING CONDENSATE
# ============================================================================

def experiment_breathing():
    print("\n" + "=" * 70)
    print("EXPERIMENT 4: THE BREATHING CONDENSATE (OSCILLATING RPCO)")
    print("=" * 70)

    # What if the compression bound L breathes — oscillates at the vesica
    # frequency? This makes the "walls" of the system expand and contract,
    # like a living membrane.

    results = []

    for breathing in [False, True]:
        label = "breathing" if breathing else "static"
        print(f"\n  --- {label} RPCO ---")

        field = GlyphFieldUniverse(
            50, R_range=(0, 0.3), spatial_range=(-5, 5),
            seed=2038, breathing=breathing
        )
        field.evolve(200)

        df = field.get_metrics_df()

        # Does breathing prevent full condensation?
        R_final_10 = df['R_max'].iloc[-10:].values
        R_drift = np.std(R_final_10) / (np.mean(R_final_10) + 1e-12)

        R_div = df['R_std'].iloc[-1] / (df['R_mean'].iloc[-1] + 1e-12)

        # Check for persistent oscillation in R_max
        R_series = df['R_max'].values
        if len(R_series) > 50:
            # Detrend
            from numpy.polynomial import polynomial as P
            t_arr = np.arange(len(R_series))
            coeffs = P.polyfit(t_arr, R_series, 2)
            trend = P.polyval(t_arr, coeffs)
            residual = R_series - trend

            # FFT of residual
            fft_vals = np.fft.rfft(residual[50:])  # skip transient
            freqs = np.fft.rfftfreq(len(residual[50:]))
            power = np.abs(fft_vals)**2

            # Dominant frequency
            dom_idx = np.argmax(power[1:]) + 1  # skip DC
            dom_freq = freqs[dom_idx]
            dom_power = power[dom_idx]
            total_power = np.sum(power[1:])
            dom_fraction = dom_power / (total_power + 1e-12)

            print(f"    R_drift: {R_drift:.6f}")
            print(f"    R diversity (std/mean): {R_div:.6f}")
            print(f"    Dominant oscillation freq: {dom_freq:.4f} (fraction: {dom_fraction:.3f})")
            print(f"    Final entropy: {df.iloc[-1]['entropy']:.4f}")
            print(f"    Final R_max: {df.iloc[-1]['R_max']:.6f}")
            print(f"    Final R_std: {df.iloc[-1]['R_std']:.6f}")

            results.append({
                'type': label,
                'R_drift': float(R_drift),
                'R_diversity': float(R_div),
                'dom_freq': float(dom_freq),
                'dom_fraction': float(dom_fraction),
                'entropy': float(df.iloc[-1]['entropy']),
                'R_max': float(df.iloc[-1]['R_max']),
                'R_std': float(df.iloc[-1]['R_std']),
                'n_resonance_clusters': int(df.iloc[-1]['n_resonance_clusters'])
            })

    results_df = pd.DataFrame(results)
    results_df.to_csv(f"{OUTPUT_DIR}/breathing_condensate.csv", index=False)

    return results_df


# ============================================================================
# EXPERIMENT 5: THE FULL MULTI-SEED UNIVERSE
# ============================================================================

def experiment_full_universe():
    print("\n" + "=" * 70)
    print("EXPERIMENT 5: THE FULL SRG-∞ UNIVERSE")
    print("(Horizons + Multi-Frequency + Breathing)")
    print("=" * 70)

    # The ultimate test: combine ALL three mechanisms.
    # This should produce a universe with:
    # - Multiple independent SRG-∞ seeds (from horizons)
    # - Internal frequency structure (from multi-freq)
    # - Dynamic "living" evolution (from breathing)

    np.random.seed(1618)

    N = 120
    # Place 6 clusters in 3D space, well-separated
    centers = np.array([
        [8, 0, 0], [-8, 0, 0],
        [0, 8, 0], [0, -8, 0],
        [0, 0, 8], [0, 0, -8]
    ], dtype=float)

    N_per = N // 6
    all_pos = []
    for c in centers:
        all_pos.append(np.random.normal(c, 1.5, (N_per, 3)))
    all_pos = np.vstack(all_pos)

    field = GlyphFieldUniverse(
        len(all_pos),
        horizon=6.0,        # Each cluster only sees itself
        multi_freq=True,     # Multiple resonance bands
        breathing=True,      # Living compression
        seed=None
    )
    field.positions = all_pos
    field.resonance = np.random.uniform(0, 0.3, len(all_pos))

    # Evolve for a long time
    field.evolve(200)
    df = field.get_metrics_df()

    print(f"\n  --- Final State (200 passes) ---")
    print(f"  Spatial clusters: {df.iloc[-1]['n_spatial_clusters']}")
    print(f"  Resonance clusters: {df.iloc[-1]['n_resonance_clusters']}")
    print(f"  Entropy: {df.iloc[-1]['entropy']:.4f}")
    print(f"  R_max: {df.iloc[-1]['R_max']:.6f}")
    print(f"  R_std: {df.iloc[-1]['R_std']:.6f}")

    # Analyze each physical cluster
    print(f"\n  --- Per-Cluster Analysis ---")
    for k in range(6):
        idx = list(range(k*N_per, (k+1)*N_per))
        R_k = field.resonance[idx]
        pos_k = field.positions[idx]
        freq_k = field.natural_freq[idx]

        com = np.mean(pos_k, axis=0)
        spread = np.std(pos_k)
        R_mean = np.mean(np.abs(R_k))
        R_std = np.std(R_k)

        # How many frequency bands in this cluster?
        unique_f = np.unique(freq_k)
        freq_report = ", ".join([f"{f:.3f}({np.sum(freq_k==f)})" for f in unique_f])

        print(f"    Cluster {k}: COM=({com[0]:.1f},{com[1]:.1f},{com[2]:.1f}), "
              f"spread={spread:.3f}, <R>={R_mean:.6f}, σR={R_std:.6f}")
        print(f"      Frequency bands: {freq_report}")

    # Are the clusters INDEPENDENT?
    cluster_R_means = []
    for k in range(6):
        idx = list(range(k*N_per, (k+1)*N_per))
        cluster_R_means.append(np.mean(np.abs(field.resonance[idx])))

    inter_diversity = np.std(cluster_R_means) / (np.mean(cluster_R_means) + 1e-10)
    print(f"\n  Inter-cluster R diversity: {inter_diversity:.4f}")
    print(f"  (> 0.01 means clusters are independently evolving)")

    # Check if any clusters have merged
    cluster_coms = []
    for k in range(6):
        idx = list(range(k*N_per, (k+1)*N_per))
        cluster_coms.append(np.mean(field.positions[idx], axis=0))
    cluster_coms = np.array(cluster_coms)

    inter_dists = squareform(pdist(cluster_coms))
    print(f"\n  Inter-cluster distances:")
    for i in range(6):
        for j in range(i+1, 6):
            status = "SEPARATE" if inter_dists[i,j] > 3 else "MERGED"
            print(f"    C{i}-C{j}: {inter_dists[i,j]:.2f} [{status}]")

    df.to_csv(f"{OUTPUT_DIR}/full_universe.csv", index=False)
    return field, df


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║        SRG-∞ PART II: BREAKING THE CONDENSATE                      ║")
    print("╚══════════════════════════════════════════════════════════════════════╝\n")

    perturb_df = experiment_perturbation()
    horizon_df = experiment_causal_horizons()
    freq_df = experiment_multi_frequency()
    breath_df = experiment_breathing()
    universe_field, universe_df = experiment_full_universe()

    print("\n" + "=" * 70)
    print("ALL EXPERIMENTS COMPLETE")
    print("=" * 70)
