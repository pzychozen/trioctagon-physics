# Paper D: symbols and theorem reference

Revision v0.1.1, 2026-09-23. Author: Hilmir Frímann Halldórsson. GPT accepted v0.1 with minor revisions; this revision awaits GPT review. D-01/D-02 clarify existing sets and their boundary without changing coordinates or kernel options. D-03 preserves tentative, adopted-relay provenance.

| Symbol | Definition / distinction |
|---|---|
| s > 0 | Selected regular-octagon edge length |
| V_s, boundary O_s, O_s | Ordered eight-vertex list, closed polygonal outline, filled convex hull; equation (2a) |
| a, w, R_oct | `(1+sqrt(2))*s/2`, `2a`, `s/(2*sin(pi/8))` |
| u_i, t_i | C3 radial unit vector; positive quarter-turn tangent |
| p | Selected-edge midpoint radius; `p > s/(2sqrt(3))` |
| A_i, B_i | `p*u_i - (s/2)*t_i`, `p*u_i + (s/2)*t_i` |
| E_i, G_i | A_i to B_i; B_i to A_(i+1) |
| g_gap | Positive connector length `sqrt(3)*p-s/2`; not recurrence coupling |
| p_* | Regular placement `sqrt(3)*s/2` |
| R_H, q_H | Hexagon circumradius; connector support-line distance |
| V_i, W | Support-triangle vertices; side `s+2*g_gap` |
| H, n_i^G | Closed residual hexagon `T intersect all {x: n_i^G dot x <= q_H}`; connector normals R60 u_i, equations (16a)–(16b) |
| L | Planar octagon centre radius `p+a`; not vertical face-centre radius |
| p_0 | Paper-C vertical centre radius `a/sqrt(3)` |
| lambda | Fixed vertical face-centre shrink `(1+sqrt(2))/3` |
| delta_face | Minimum finite-face separation `sqrt(3)*p-a` for `p>=p_0` |
| g_coupling | Three-channel Laplacian coefficient, distinct from g_gap |
| Omega, Z_chiral | Complex canonical triad and bilinear raw chirality |

| Result | Hypotheses and conclusion | Proof in manuscript |
|---|---|---|
| Lemma 1 | Tangent alignment (3)–(4); directed connector = g_gap R60 t_i | §6, equations (6)–(8) |
| Theorem 2 | s,g_gap positive; convex equiangular alternating hexagon; regular iff g_gap=s | §7; global convexity supplied by Proposition 4 |
| Proposition 3 | Same domain; cyclicity, general area, regular specialization | §8; area uses Proposition 4 |
| Proposition 4 | Support half-planes; equilateral W=s+2g_gap; three closed equilateral corner cells; residual defined by closed cuts | §9; (16a) removes exterior apex/legs while retaining connectors; barycentric proof unchanged |
| Proposition 5 | Unmarked D3 generically, D6 at equality; role-marked D3 | §10; D_n means order 2n; directed role-preserving rotations are C3 |
| Proposition 6 | Full planar regular-octagon completion exists at L=p+a | §11; no uniqueness claim |
| Proposition 7 | Vertical family at p_0; exact rigid map to Paper C; g_gap=s/sqrt(2) | §12; identity of finite faces, not merely planes |
| Proposition 8 | p>=a/sqrt(3); finite faces F_i(O_s), with the filled convex domain; exact distance and loss of seams | §14; supporting planes continue to intersect |

The two tuning operations are derived in §13, equations (23)–(24). Width-one shrink in §14 gives side and connector 1/3, top height `(1+sqrt(2))/6`, support side 1, hexagon area `sqrt(3)/6`. The published Paper-C geometry stays unchanged. No numerical plot is a proof and no predicate count is a theorem count.
