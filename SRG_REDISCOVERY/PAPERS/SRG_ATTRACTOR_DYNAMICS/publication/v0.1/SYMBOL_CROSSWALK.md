# Symbol crosswalk

This is editorial renaming only. The complete update, clipping constant/offset, remapping and clock are unchanged.

| Source usage | Paper usage | Meaning / distinction |
| --- | --- | --- |
| Historical `s`, `state`; CA01–04 `s` | `s_n`, `u_n` | Carried state and pre-remap Euler state. No stored velocity. |
| `roll(s,1)` / `C s` | `C s=(z,x,y)` | Fixed cyclic operator; not the limiting circle. |
| Fixed circle `C` / `𝒞` | `\mathcal C` | Fixed set of the unforced limiting map. |
| Historical `theta=atan2(rho,z)` | `\vartheta` | Incoming polar angle. |
| CA01–03 torus angle `theta` | `\theta` | Intrinsic meridional coordinate, `atan2(z,rho-1)`. |
| `phi`, lifted phases | `\varphi`, `\Phi_{\alpha,k}` | Azimuth and limiting lift; the endpoint includes the future clock. |
| TGMO / `P` | `P` | Active historical remapping. Not a passive measurement overlay. |
| RPCO clipping | `\widehat q` rule | Retained min factor with `4/5` and `1/100000`. Historical Figure 3 has a different printed clipping rule. |
| REFU `H` | `H(t)` | Prescribed four-term drive, not a memory state. No invented expansion of the acronym. |
| CA02 `D`, `W` | `D(s_0)`, `W(s)` | First coupling derivative of the endpoint and its angular-response summand. |
| CA02 constant `b` | `b=z_*^2/rho_*` | Leading circle-response coefficient. |
| CA02 diagonal scalar `c` in `c(1,1,1)` | `d` | Avoids collision with certificate coordinate `c`. |
| CA03 `M_alpha`, `A_alpha`, `T_alpha` | Same | Both components of the complete block, not an angular-only model. |
| CA03 block factor `K_N` | Same | Finite drive sum times 1/10. Distinct from the Lipschitz constant `K_0` in Appendix A. |
| CA04 `(c,v)` | Same | `c=cos(theta)`, `v=tan(phi/2)`, upper-surface chart. |
| CA04 temporary `r,z,C,S` | `r,z,C_v,S_v` | Radius, height, cosine and sine of azimuth; `C_v` is not cyclic roll. |
| CA04 temporary `R,W,Z` | `R_t,W_t,Z_t` | Radial/tangential/vertical torque components; `W_t` is not CA02 `W(s)`. |
| CA04 temporary `a,b,d,h,L,w` | `a_r,b_t,d_z,h_r,L_u,w_t` | Stable chart evaluation graph. Avoids conflicts with response coefficient and state norm. |
| CA04 rational centre, regions `X,B` | `\widehat x`, `X,B` | Exact centre and intrinsic rectangles; no physical enclosure. |
| CA04 root phase | `\varphi_*` in §6 | Certified returning-block root, distinct from the arbitrary circle label and from leading CA03 roots. |
| CA01 geometric origin/offset `O` | `O` | Passive placement `(0,sqrt(3)/6,0)`, unit scale; no dynamical force. |

All native-state and reference-frame quantities retain the accepted meanings. Exact certificate endpoints remain in their original JSON representations; paper decimals are summaries only.
