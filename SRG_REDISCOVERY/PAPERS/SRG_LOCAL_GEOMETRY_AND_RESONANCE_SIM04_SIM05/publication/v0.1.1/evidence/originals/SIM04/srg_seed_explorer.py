#!/usr/bin/env python3
"""
=============================================================================
 PROTO-SRG SEED EXPLORER

 Full simulation of glyph fields using REFU + RPCO + TGMO operators
 to classify seed families, find minimal emergence conditions,
 and explore multi-seed interactions.

 Author: Claude (collaborating with pzychozen)
 Date: 2026-03-14
=============================================================================
"""

import numpy as np
import pandas as pd
from scipy.spatial import ConvexHull, Delaunay
from scipy.spatial.distance import pdist, squareform
from collections import defaultdict
import json
import os
import warnings
warnings.filterwarnings('ignore')

OUTPUT_DIR = "/sessions/vigilant-bold-allen/mnt/SRG_claude/Claude_SRG_Analysis"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================================
# CORE OPERATORS (from your refu.py and tgmo.py, adapted for glyph particles)
# ============================================================================

def H(t):
    """REFU memory curve"""
    t = np.asarray(t, dtype=float)
    return (2.0*np.exp(-0.5*t)*np.cos(t) + 1.0*np.exp(-0.3*t)*np.sin(t)
            + 1.5*np.exp(-0.7*t) + 1.0*np.exp(-0.4*t))

def rpco(x, L=9.0, eps=1e-9, mode="signed"):
    """RPCO: sign-preserving compression"""
    x = np.asarray(x, dtype=float)
    mag = np.abs(x) + eps
    z = np.clip(np.log(mag), -L, L)
    return np.sign(x) * np.exp(z)

def compute_Hmax(t_end, n=20000):
    t = np.linspace(0, t_end, n)
    return float(np.max(np.abs(H(t)))) + 1e-12

# ============================================================================
# GLYPH FIELD EVOLUTION ENGINE
# ============================================================================

class GlyphField:
    """
    A field of N glyphs in 3D space, each with position (x,y,z) and
    resonance amplitude R. Evolves under REFU-like dynamics adapted
    for particle-based (rather than grid-based) geometry.
    """

    def __init__(self, N, R_init_range=(0.0, 0.1), spatial_range=(-5, 5), seed=None):
        if seed is not None:
            np.random.seed(seed)
        self.N = N
        self.positions = np.random.uniform(spatial_range[0], spatial_range[1], (N, 3))
        self.resonance = np.random.uniform(R_init_range[0], R_init_range[1], N)
        self.velocities = np.zeros((N, 3))
        self.history = []
        self.pass_count = 0

        # Parameters
        self.alpha = 0.05       # diffusion strength
        self.beta = 0.15        # feedback gain
        self.lambda_vp = 0.618  # vesica compression (golden ratio)
        self.gamma_srg = 0.0870 # resonance modulation
        self.theta_lock = 0.244 # lock frequency
        self.rpco_L = 9.0
        self.lam_H = 0.05
        self.k_neighbors = 5    # neighbor count for Laplacian
        self.echo_threshold = 0.85  # threshold for echo corridor detection

        self._record_state()

    def _record_state(self):
        self.history.append({
            'pass': self.pass_count,
            'positions': self.positions.copy(),
            'resonance': self.resonance.copy(),
            'velocities': self.velocities.copy()
        })

    def _compute_adjacency(self):
        """Build k-nearest-neighbor adjacency"""
        dists = squareform(pdist(self.positions))
        adj = np.zeros((self.N, self.N))
        for i in range(self.N):
            neighbors = np.argsort(dists[i])[1:self.k_neighbors+1]
            adj[i, neighbors] = 1
        return adj, dists

    def _compute_laplacian(self, adj):
        """Discrete graph Laplacian for position field"""
        lap = np.zeros_like(self.positions)
        for i in range(self.N):
            neighbors = np.where(adj[i] > 0)[0]
            if len(neighbors) == 0:
                continue
            diff_sum = np.sum(self.positions[neighbors] - self.positions[i], axis=0)
            lap[i] = diff_sum / len(neighbors)
        return lap

    def _compute_resonance_coupling(self, adj, dists):
        """Resonance exchange between neighbors"""
        R_new = self.resonance.copy()
        for i in range(self.N):
            neighbors = np.where(adj[i] > 0)[0]
            if len(neighbors) == 0:
                continue
            # Weighted resonance exchange: closer neighbors contribute more
            weights = 1.0 / (dists[i, neighbors] + 1e-8)
            weights /= weights.sum()
            R_neighbor = np.sum(weights * self.resonance[neighbors])
            # Feedback: pull toward weighted neighbor average
            R_new[i] += self.beta * (R_neighbor - self.resonance[i])
        return R_new

    def _detect_echo_corridors(self, dists):
        """Find pairs of glyphs forming resonance echo corridors"""
        corridors = []
        for i in range(self.N):
            for j in range(i+1, self.N):
                # Echo corridor condition: similar resonance AND spatial proximity
                R_similarity = 1 - abs(self.resonance[i] - self.resonance[j]) / (max(self.resonance) + 1e-8)
                spatial_proximity = np.exp(-dists[i,j] / 3.0)
                echo_strength = R_similarity * spatial_proximity
                if echo_strength > self.echo_threshold:
                    corridors.append((i, j, echo_strength))
        return corridors

    def evolve_pass(self):
        """One full recursive pass"""
        self.pass_count += 1
        t = float(self.pass_count)

        # Build adjacency
        adj, dists = self._compute_adjacency()

        # 1. Spatial evolution via graph Laplacian (TGMO analog)
        lap = self._compute_laplacian(adj)
        self.positions += self.alpha * lap + self.beta * np.tanh(lap)

        # 2. Resonance coupling (REFU feedback)
        self.resonance = self._compute_resonance_coupling(adj, dists)

        # 3. Memory modulation
        H_max = compute_Hmax(t * 0.05 * 200)
        h_t = H(t)
        memory_factor = 1.0 + self.lam_H * h_t / H_max
        self.resonance *= memory_factor

        # 4. Fusion field: pull toward cluster centers
        center = np.average(self.positions, axis=0, weights=np.abs(self.resonance)+1e-8)
        fusion_force = (center - self.positions) * 0.03 * self.resonance[:, np.newaxis]
        self.positions += fusion_force

        # 5. Vesica compression on resonance
        self.resonance *= (1.0 - 0.001 * np.sin(t * self.theta_lock * 2*np.pi))

        # 6. RPCO compression
        self.resonance = rpco(self.resonance, L=self.rpco_L)

        # 7. Small tunneling noise
        self.positions += np.random.normal(0, 0.01, self.positions.shape)

        # Update velocities (for tracking)
        if len(self.history) > 0:
            self.velocities = self.positions - self.history[-1]['positions']

        self._record_state()

    def evolve(self, n_passes=10):
        """Run n recursive passes"""
        for _ in range(n_passes):
            self.evolve_pass()

    def find_proto_seeds(self):
        """Identify proto-SRG seeds: highest-resonance attractors"""
        # Final resonance
        R_final = self.resonance.copy()
        # Sort by resonance amplitude
        sorted_idx = np.argsort(-np.abs(R_final))

        seeds = []
        for rank, idx in enumerate(sorted_idx[:5]):
            seeds.append({
                'rank': rank + 1,
                'glyph_id': int(idx),
                'position': self.positions[idx].tolist(),
                'resonance': float(R_final[idx]),
                'velocity_mag': float(np.linalg.norm(self.velocities[idx]))
            })
        return seeds

    def classify_geometry(self):
        """Classify the emergent lattice geometry"""
        # Use top-resonance glyphs
        R_final = np.abs(self.resonance)
        threshold = np.percentile(R_final, 75)
        active_idx = np.where(R_final >= threshold)[0]

        if len(active_idx) < 4:
            return {"type": "sub-critical", "n_active": len(active_idx)}

        active_pos = self.positions[active_idx]

        # Analyze angular relationships
        center = np.mean(active_pos, axis=0)
        relative = active_pos - center
        dists_from_center = np.linalg.norm(relative, axis=1)

        # Compute pairwise angles from center
        angles = []
        for i in range(len(relative)):
            for j in range(i+1, len(relative)):
                cos_angle = np.dot(relative[i], relative[j]) / (
                    np.linalg.norm(relative[i]) * np.linalg.norm(relative[j]) + 1e-10)
                angles.append(np.arccos(np.clip(cos_angle, -1, 1)) * 180 / np.pi)

        angles = np.array(angles)

        # Classification based on angle distribution
        if len(active_idx) <= 5:
            # Check tetrahedral: angles ≈ 109.47°
            tet_angle = 109.47
            tet_err = np.mean(np.abs(angles - tet_angle))
            return {
                "type": "tetrahedral" if tet_err < 30 else "amorphous",
                "n_active": len(active_idx),
                "mean_angle": float(np.mean(angles)),
                "angle_std": float(np.std(angles)),
                "tet_error": float(tet_err),
                "mean_dist": float(np.mean(dists_from_center)),
                "dist_ratio": float(np.std(dists_from_center) / (np.mean(dists_from_center)+1e-8))
            }
        elif len(active_idx) <= 7:
            # Check octahedral: angles ≈ 90° and 180°
            oct_angles = [90, 180]
            oct_err = min(np.mean([min(abs(a-90), abs(a-180)) for a in angles]), 90)
            return {
                "type": "octahedral" if oct_err < 25 else "transitional",
                "n_active": len(active_idx),
                "mean_angle": float(np.mean(angles)),
                "angle_std": float(np.std(angles)),
                "oct_error": float(oct_err),
                "mean_dist": float(np.mean(dists_from_center)),
                "dist_ratio": float(np.std(dists_from_center) / (np.mean(dists_from_center)+1e-8))
            }
        else:
            # Check icosahedral or higher
            return {
                "type": "higher_polyhedra",
                "n_active": len(active_idx),
                "mean_angle": float(np.mean(angles)),
                "angle_std": float(np.std(angles)),
                "mean_dist": float(np.mean(dists_from_center)),
                "dist_ratio": float(np.std(dists_from_center) / (np.mean(dists_from_center)+1e-8))
            }

    def compute_coherence(self):
        """Measure global resonance coherence"""
        R = self.resonance
        if np.std(R) < 1e-12:
            return 1.0
        # Coherence = 1 - normalized variance
        return float(1.0 - np.std(R) / (np.mean(np.abs(R)) + 1e-8))

    def get_trajectory_df(self):
        """Export full trajectory as DataFrame"""
        rows = []
        for state in self.history:
            p = state['pass']
            for i in range(self.N):
                rows.append({
                    'Pass': p,
                    'Glyph_ID': i,
                    'X': state['positions'][i, 0],
                    'Y': state['positions'][i, 1],
                    'Z': state['positions'][i, 2],
                    'Resonance': state['resonance'][i],
                    'VX': state['velocities'][i, 0],
                    'VY': state['velocities'][i, 1],
                    'VZ': state['velocities'][i, 2]
                })
        return pd.DataFrame(rows)


# ============================================================================
# EXPERIMENT 1: SEED FAMILY CLASSIFICATION
# ============================================================================

def experiment_seed_families():
    print("=" * 70)
    print("EXPERIMENT 1: PROTO-SRG SEED FAMILY CLASSIFICATION")
    print("=" * 70)

    # Vary initial conditions systematically
    results = []

    configs = [
        # (N, R_range, spatial_range, n_passes, label)
        (10, (0.0, 0.05), (-2, 2), 15, "small_low_R"),
        (10, (0.0, 0.5), (-2, 2), 15, "small_high_R"),
        (20, (0.0, 0.05), (-3, 3), 15, "medium_low_R"),
        (20, (0.0, 0.5), (-3, 3), 15, "medium_high_R"),
        (50, (0.0, 0.1), (-5, 5), 15, "large_standard"),
        (50, (0.0, 0.5), (-5, 5), 15, "large_high_R"),
        (100, (0.0, 0.1), (-5, 5), 12, "very_large"),
        (50, (0.0, 0.1), (-1, 1), 15, "large_compact"),
        (50, (0.0, 0.1), (-10, 10), 15, "large_diffuse"),
        (30, (0.3, 0.5), (-3, 3), 15, "medium_preheated"),
    ]

    for trial in range(3):  # 3 random seeds per config
        for N, R_range, s_range, n_passes, label in configs:
            seed = trial * 1000 + hash(label) % 1000
            field = GlyphField(N, R_init_range=R_range, spatial_range=s_range, seed=seed)
            field.evolve(n_passes)

            seeds = field.find_proto_seeds()
            geometry = field.classify_geometry()
            coherence = field.compute_coherence()

            # Detect echo corridors at final state
            _, dists = field._compute_adjacency()
            corridors = field._detect_echo_corridors(dists)

            result = {
                'config': label,
                'trial': trial,
                'N': N,
                'R_init_max': R_range[1],
                'spatial_extent': s_range[1] - s_range[0],
                'n_passes': n_passes,
                'n_proto_seeds': len([s for s in seeds if s['resonance'] > 0.1]),
                'top_seed_R': seeds[0]['resonance'],
                'top_seed_pos': seeds[0]['position'],
                'geometry_type': geometry['type'],
                'n_active_glyphs': geometry['n_active'],
                'mean_angle': geometry.get('mean_angle', None),
                'coherence': coherence,
                'n_echo_corridors': len(corridors),
                'seed_velocity': seeds[0]['velocity_mag']
            }
            results.append(result)

            print(f"  {label} (trial {trial}): geometry={geometry['type']}, "
                  f"coherence={coherence:.4f}, seeds={result['n_proto_seeds']}, "
                  f"corridors={len(corridors)}")

    df = pd.DataFrame(results)
    df.to_csv(f"{OUTPUT_DIR}/seed_family_classification.csv", index=False)

    # Summary statistics
    print(f"\n{'Config':<25} {'Geometry Mode':<18} {'Avg Coherence':<15} {'Avg Seeds'}")
    print("-" * 75)
    for label in df['config'].unique():
        sub = df[df['config'] == label]
        geom_mode = sub['geometry_type'].mode().iloc[0] if len(sub) > 0 else "N/A"
        avg_coh = sub['coherence'].mean()
        avg_seeds = sub['n_proto_seeds'].mean()
        print(f"  {label:<23} {geom_mode:<18} {avg_coh:<15.4f} {avg_seeds:.1f}")

    return df


# ============================================================================
# EXPERIMENT 2: MINIMAL SEED CONDITIONS (Phase Boundary)
# ============================================================================

def experiment_minimal_conditions():
    print("\n" + "=" * 70)
    print("EXPERIMENT 2: MINIMAL SEED CONDITIONS — PHASE BOUNDARY")
    print("=" * 70)

    # Binary search for minimum N that produces a proto-SRG
    results = []

    # Sweep N from 3 to 50
    for N in range(3, 51):
        emergences = 0
        total_trials = 5
        coherences = []

        for trial in range(total_trials):
            field = GlyphField(N, R_init_range=(0, 0.1), spatial_range=(-5, 5),
                             seed=42 + trial + N*100)
            field.evolve(15)

            seeds = field.find_proto_seeds()
            coherence = field.compute_coherence()
            coherences.append(coherence)

            # Proto-SRG emerges if: coherence > 0.5 AND top seed resonance > 0.15
            if coherence > 0.5 and seeds[0]['resonance'] > 0.15:
                emergences += 1

        emergence_rate = emergences / total_trials
        avg_coherence = np.mean(coherences)

        results.append({
            'N': N,
            'emergence_rate': emergence_rate,
            'avg_coherence': avg_coherence
        })

        if N % 10 == 0 or emergence_rate > 0:
            print(f"  N={N:3d}: emergence_rate={emergence_rate:.2f}, avg_coherence={avg_coherence:.4f}")

    df = pd.DataFrame(results)
    df.to_csv(f"{OUTPUT_DIR}/minimal_seed_conditions.csv", index=False)

    # Find phase boundary
    threshold_rates = [0.2, 0.5, 0.8, 1.0]
    for tr in threshold_rates:
        candidates = df[df['emergence_rate'] >= tr]
        if len(candidates) > 0:
            N_min = candidates['N'].min()
            print(f"\n  Phase boundary (emergence ≥ {tr:.0%}): N_min = {N_min}")

    # Now sweep R_init for fixed N=20
    print(f"\n  --- R_init sweep at N=20 ---")
    r_results = []
    for R_max in np.arange(0.01, 1.01, 0.02):
        emergences = 0
        for trial in range(5):
            field = GlyphField(20, R_init_range=(0, R_max), spatial_range=(-5, 5),
                             seed=42 + trial)
            field.evolve(15)
            seeds = field.find_proto_seeds()
            coherence = field.compute_coherence()
            if coherence > 0.5 and seeds[0]['resonance'] > 0.15:
                emergences += 1

        r_results.append({'R_max': R_max, 'emergence_rate': emergences/5})

    r_df = pd.DataFrame(r_results)
    r_df.to_csv(f"{OUTPUT_DIR}/R_init_phase_sweep.csv", index=False)

    # Find R threshold
    for tr in [0.5, 0.8]:
        candidates = r_df[r_df['emergence_rate'] >= tr]
        if len(candidates) > 0:
            print(f"  R threshold (emergence ≥ {tr:.0%}): R_max_min = {candidates['R_max'].min():.3f}")

    return df, r_df


# ============================================================================
# EXPERIMENT 3: MULTI-SEED INTERACTIONS
# ============================================================================

def experiment_multi_seed():
    print("\n" + "=" * 70)
    print("EXPERIMENT 3: MULTI-SEED INTERACTIONS")
    print("=" * 70)

    results = []

    # Scenario A: Two clusters far apart → do they form independent seeds?
    print("\n  --- Scenario A: Two separated clusters ---")
    for sep in [4, 8, 12, 16, 20]:
        for trial in range(3):
            np.random.seed(42 + trial + sep*10)
            N_per_cluster = 25
            # Cluster 1 centered at (-sep/2, 0, 0)
            pos1 = np.random.normal([-sep/2, 0, 0], 1.0, (N_per_cluster, 3))
            # Cluster 2 centered at (+sep/2, 0, 0)
            pos2 = np.random.normal([sep/2, 0, 0], 1.0, (N_per_cluster, 3))

            field = GlyphField(N_per_cluster*2, seed=None)
            field.positions = np.vstack([pos1, pos2])
            field.resonance = np.random.uniform(0, 0.1, N_per_cluster*2)
            field._record_state()

            field.evolve(15)

            seeds = field.find_proto_seeds()

            # Check if seeds are from different clusters
            seed_positions = np.array([s['position'] for s in seeds[:3]])
            # Distance between top 2 seeds
            if len(seed_positions) >= 2:
                seed_dist = np.linalg.norm(seed_positions[0] - seed_positions[1])
            else:
                seed_dist = 0

            # Classification: independent if seeds far apart, merged if close
            interaction_type = "independent" if seed_dist > sep/3 else "merged"

            results.append({
                'scenario': 'two_clusters',
                'separation': sep,
                'trial': trial,
                'interaction_type': interaction_type,
                'seed_distance': float(seed_dist),
                'top_R': seeds[0]['resonance'],
                'coherence': field.compute_coherence()
            })

        avg_dist = np.mean([r['seed_distance'] for r in results if r['separation']==sep])
        interactions = [r['interaction_type'] for r in results if r['separation']==sep]
        print(f"    sep={sep:3d}: avg_seed_dist={avg_dist:.2f}, "
              f"outcomes={dict((x, interactions.count(x)) for x in set(interactions))}")

    # Scenario B: Ring of clusters → hierarchical lattice?
    print("\n  --- Scenario B: Ring arrangement ---")
    for n_clusters in [3, 4, 5, 6]:
        for trial in range(3):
            np.random.seed(42 + trial + n_clusters*100)
            N_per = 15
            radius = 8
            all_pos = []
            for k in range(n_clusters):
                angle = 2*np.pi*k/n_clusters
                center = [radius*np.cos(angle), radius*np.sin(angle), 0]
                cluster_pos = np.random.normal(center, 0.8, (N_per, 3))
                all_pos.append(cluster_pos)

            all_pos = np.vstack(all_pos)
            N_total = len(all_pos)

            field = GlyphField(N_total, seed=None)
            field.positions = all_pos
            field.resonance = np.random.uniform(0, 0.1, N_total)
            field._record_state()

            field.evolve(15)

            seeds = field.find_proto_seeds()
            geometry = field.classify_geometry()

            results.append({
                'scenario': 'ring',
                'n_clusters': n_clusters,
                'trial': trial,
                'interaction_type': 'ring',
                'geometry_type': geometry['type'],
                'n_active': geometry['n_active'],
                'top_R': seeds[0]['resonance'],
                'coherence': field.compute_coherence()
            })

        geoms = [r['geometry_type'] for r in results
                 if r.get('n_clusters')==n_clusters and r['scenario']=='ring']
        print(f"    n_clusters={n_clusters}: geometries={geoms}")

    # Scenario C: Competing seeds — two preheated glyphs
    print("\n  --- Scenario C: Competing pre-seeded attractors ---")
    for R_ratio in [1.0, 1.5, 2.0, 3.0, 5.0]:
        for trial in range(3):
            np.random.seed(42 + trial)
            N = 50
            field = GlyphField(N, R_init_range=(0, 0.05), spatial_range=(-5, 5), seed=42+trial)

            # Pre-heat two glyphs
            field.resonance[0] = 0.5  # Seed A
            field.resonance[25] = 0.5 * R_ratio  # Seed B (stronger by ratio)
            field.positions[0] = np.array([-3, 0, 0])
            field.positions[25] = np.array([3, 0, 0])

            field.evolve(20)

            seeds = field.find_proto_seeds()

            # Did seed A or B win?
            winner = "A" if seeds[0]['glyph_id'] == 0 else ("B" if seeds[0]['glyph_id'] == 25 else "new")

            results.append({
                'scenario': 'competing',
                'R_ratio': R_ratio,
                'trial': trial,
                'winner': winner,
                'top_R': seeds[0]['resonance'],
                'top_glyph': seeds[0]['glyph_id'],
                'coherence': field.compute_coherence()
            })

        winners = [r['winner'] for r in results if r.get('R_ratio')==R_ratio and r['scenario']=='competing']
        print(f"    R_ratio={R_ratio:.1f}: winners={winners}")

    df = pd.DataFrame(results)
    df.to_csv(f"{OUTPUT_DIR}/multi_seed_interactions.csv", index=False)
    return df


# ============================================================================
# EXPERIMENT 4: DEEP TRAJECTORY ANALYSIS — ProtoSRG_1 Recreation
# ============================================================================

def experiment_deep_trajectory():
    print("\n" + "=" * 70)
    print("EXPERIMENT 4: DEEP TRAJECTORY ANALYSIS")
    print("=" * 70)

    # Recreate the conditions from the original research
    field = GlyphField(50, R_init_range=(0, 0.1), spatial_range=(-5, 5), seed=2038)

    # Record detailed metrics at each pass
    pass_metrics = []

    for p in range(20):
        field.evolve_pass()

        # Compute metrics
        R = field.resonance
        pos = field.positions

        # Cluster analysis
        dists = squareform(pdist(pos))
        _, dists_full = field._compute_adjacency()
        corridors = field._detect_echo_corridors(dists_full)

        # Resonance distribution stats
        R_mean = np.mean(np.abs(R))
        R_max = np.max(np.abs(R))
        R_std = np.std(R)

        # Spatial concentration (gyration radius)
        center = np.mean(pos, axis=0)
        Rg = np.sqrt(np.mean(np.sum((pos - center)**2, axis=1)))

        # Energy metrics
        kinetic = np.mean(np.sum(field.velocities**2, axis=1))

        # Top seed tracking
        top_idx = np.argmax(np.abs(R))

        metrics = {
            'pass': p + 1,
            'R_mean': float(R_mean),
            'R_max': float(R_max),
            'R_std': float(R_std),
            'Rg': float(Rg),
            'kinetic_energy': float(kinetic),
            'n_corridors': len(corridors),
            'coherence': field.compute_coherence(),
            'top_seed_id': int(top_idx),
            'top_seed_R': float(R[top_idx]),
            'top_seed_x': float(pos[top_idx, 0]),
            'top_seed_y': float(pos[top_idx, 1]),
            'top_seed_z': float(pos[top_idx, 2])
        }
        pass_metrics.append(metrics)

        print(f"  Pass {p+1:2d}: R_max={R_max:.4f}, Rg={Rg:.3f}, "
              f"corridors={len(corridors)}, coherence={metrics['coherence']:.4f}, "
              f"top_seed={top_idx}")

    # Final analysis
    seeds = field.find_proto_seeds()
    geometry = field.classify_geometry()

    print(f"\n  Final geometry: {geometry['type']}")
    print(f"  Proto-SRG seeds:")
    for s in seeds[:3]:
        print(f"    Glyph_{s['glyph_id']}: R={s['resonance']:.6f}, "
              f"pos=({s['position'][0]:.3f}, {s['position'][1]:.3f}, {s['position'][2]:.3f})")

    # Save trajectory
    traj_df = field.get_trajectory_df()
    traj_df.to_csv(f"{OUTPUT_DIR}/deep_trajectory.csv", index=False)

    metrics_df = pd.DataFrame(pass_metrics)
    metrics_df.to_csv(f"{OUTPUT_DIR}/pass_metrics.csv", index=False)

    return metrics_df, seeds, geometry


# ============================================================================
# EXPERIMENT 5: PARAMETER SENSITIVITY — WHAT CONTROLS GEOMETRY?
# ============================================================================

def experiment_parameter_sensitivity():
    print("\n" + "=" * 70)
    print("EXPERIMENT 5: PARAMETER SENSITIVITY ANALYSIS")
    print("=" * 70)

    results = []

    # Sweep key parameters
    param_sweeps = {
        'alpha': np.arange(0.01, 0.20, 0.02),
        'beta': np.arange(0.05, 0.50, 0.05),
        'lambda_vp': np.arange(0.1, 1.5, 0.1),
        'rpco_L': np.arange(3, 15, 1),
        'k_neighbors': np.arange(2, 10, 1),
    }

    for param_name, values in param_sweeps.items():
        print(f"\n  Sweeping {param_name}:")
        for val in values:
            coherences = []
            geometries = []
            for trial in range(3):
                field = GlyphField(30, R_init_range=(0, 0.1), spatial_range=(-4, 4),
                                 seed=42+trial)
                setattr(field, param_name, val)
                field.evolve(12)

                coherences.append(field.compute_coherence())
                geometries.append(field.classify_geometry()['type'])

            avg_coh = np.mean(coherences)
            geom_mode = max(set(geometries), key=geometries.count)

            results.append({
                'parameter': param_name,
                'value': float(val),
                'avg_coherence': avg_coh,
                'geometry_mode': geom_mode
            })

            print(f"    {param_name}={val:.3f}: coherence={avg_coh:.4f}, geometry={geom_mode}")

    df = pd.DataFrame(results)
    df.to_csv(f"{OUTPUT_DIR}/parameter_sensitivity.csv", index=False)
    return df


# ============================================================================
# MAIN — RUN ALL EXPERIMENTS
# ============================================================================

if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║           PROTO-SRG SEED EXPLORER — FULL ANALYSIS SUITE           ║")
    print("╚══════════════════════════════════════════════════════════════════════╝\n")

    # Run all experiments
    seed_df = experiment_seed_families()
    min_df, r_df = experiment_minimal_conditions()
    multi_df = experiment_multi_seed()
    metrics_df, seeds, geometry = experiment_deep_trajectory()
    param_df = experiment_parameter_sensitivity()

    print("\n" + "=" * 70)
    print("ALL EXPERIMENTS COMPLETE")
    print("=" * 70)
    print(f"\nOutput files saved to: {OUTPUT_DIR}/")
    print("  - seed_family_classification.csv")
    print("  - minimal_seed_conditions.csv")
    print("  - R_init_phase_sweep.csv")
    print("  - multi_seed_interactions.csv")
    print("  - deep_trajectory.csv")
    print("  - pass_metrics.csv")
    print("  - parameter_sensitivity.csv")
