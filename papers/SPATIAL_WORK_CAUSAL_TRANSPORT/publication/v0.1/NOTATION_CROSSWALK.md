# Final editorial notation crosswalk

This records the notation in the delivered v0.1 PDF. The supplied recommendations remain unchanged in `inputs/NOTATION_CROSSWALK.md`. All changes below are editorial; the accepted equations and hypotheses are retained.

| Original/source role | Final notation | Distinction |
|---|---|---|
| Native complex state and real components | Ω, x=(a_N,b_N) | Boundary signals a,b remain separate. |
| Native quadratic observable and derivative | f, J_f | Not spatial duplication J or spatial mixing C. |
| Original finite source-profile operator | calligraphic B | Not the T source pointwise Gram matrix B(X). |
| T pointwise Gram matrix B(X) | bold G(X), scalar block m_0 | Not the labeled arc union G. |
| Carrier components p,r | Q=(p,r_c) | No collision with geometry radius or old receiver. |
| C1 carrier speed | c_car | Independent observation speed c_e; neither is a physical calibration. |
| Observation coefficient g/(4π) | a_o=g_o/(4π) | Separate from native synchronization g=1/60. |
| Carrier domain | S_L=R/LZ | S alone denotes the whole-construction reflection matrix in Section 2. |
| C6 scalar/vector outputs | U_o,V_o | U,V,Y denote Hilbert spaces. |
| Horizontal geometry transform A_tau | A^perp_tau_g, with quarter-turn J_perp | Separate from the 4-by-2 scalar/tangent inclusion A_s and duplication J. |
| Static geometry parameter | tau_g | Not physical time t or channel age xi. |
| Enclosing ball factor | R_ball | Width-one full three-dimensional radius; actual enclosing radius w R_ball. |
| Cylindrical radius | rho_perp | Omits height; not R_ball. |
| Carrier circle radius | R_Gamma | Width-one circle radius; physical circle radius w R_Gamma. |
| Original source width | epsilon_c | Arclength half-width; not native epsilon=1/10 or witness varepsilon. |
| Old metric alpha,beta | alpha_N,beta_R | New receiving metric is beta_G, with different declared dimensions. |
| Old/new receiving state | z / zeta | Old z counted once in H_RX; new zeta in H_G. |
| Original native map F | F_native | Added carrier force is calligraphic F. |
| Temporal observation/adjoint | K_G, K_G* | Complete supplied history and finite test window; different from spatial C*. |
| Zero-prehistory direct component | K_G,0 | Not the entire loaded receiving drive. |
| Spatial same-time maps | J,J*,C,C* | Adjoint meanings are relative to the declared real L2 metrics. |
| Boundary waves | a,b,c,d | Near forward outflow / near return / far arrival / far return outflow. |
| Carrier and G measures | ds, d ell_X; lengths L,M | Arclength, not physical aperture area or normal flux. |
| Transport interval coordinate | xi in (0,theta_X(s)) | Time/age; not embedded spatial length. Fiber identity uses theta, never arc length ell. |
| Delay bounds and history ceiling | theta_-,theta_+,Theta | Actual extrema versus sufficient nonoptimized ceiling. |
| Original geometry height coordinate | explicit Cartesian triples, e_z | No geometry height field named zeta is introduced. |
| Native synchronization coefficient lambda | lambda_N | Distinct from temporal dual test lambda. |

Appendix A prints a compact reader-facing crosswalk and the declared dimensional account. Figures use the same carrier, wave, stock and time notation as their surrounding text.
