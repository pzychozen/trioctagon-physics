# Paper C — Symbols and Identities v0.2

Companion to `PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.2.md`. Symbols, exact identities, and sign/orientation conventions. Revised from v0.1 for referee findings F01 (area chain), F09 (chamfer-edge inclination), F10 ("size measures"), F11 (two free edges). Normalization: octagon flat-to-flat width $=$ principal equilateral side $=w=1$ (nonphysical unit).

## Frame and conventions

| Symbol | Meaning |
|---|---|
| $(x,y,z)$ | ambient coordinates; **prism (fold) axis is $z$** |
| $(u,z)$ | octagon local frame; $u$ across the panel, $z$ along the hinge |
| horizontal / axial section | constant-$z$ slice, lies in the $xy$-plane |
| $R_z(\theta)$ | rotation about the $z$-direction (the hinge direction) |
| outward normal | face normal oriented away from the prism axis through $(0,\tfrac{\sqrt3}{6})$ |

## Core constants — four octagon size measures

**Only the apothem and circumradius are radii** (F10). The four size measures:

| Symbol | Exact | Numerical | Meaning |
|---|---:|---:|---|
| $s$ | $\sqrt2-1$ | $0.4142135624$ | octagon edge; hinge length; central-band height |
| $w$ | $1$ | $1$ | flat-to-flat width $=(1+\sqrt2)s$; equilateral side |
| $a$ | $\tfrac12$ | $0.5$ | apothem (a radius: center→edge) |
| $R$ | $\tfrac{s}{2}\sqrt{4+2\sqrt2}$ | $0.5411961001$ | circumradius (a radius: center→vertex) |
| $d$ | $1-\tfrac{\sqrt2}{2}=\tfrac{s}{\sqrt2}=a-\tfrac{s}{2}$ | $0.2928932188$ | chamfer cutback |
| $\beta$ | $60^\circ$ | $60$ | fold magnitude (from reversed stacked start; domain $[0,\pi]$) |

Edge $s$ and width $w$ are lengths, **not** radii — do not call the set "four radii."

## Octagon identities

- $w=(1+\sqrt2)s=1$, hence $s=\sqrt2-1$; apothem $a=\tfrac{s}{2}(1+\sqrt2)=\tfrac12$ (the support-line distance from the centre to each edge).
- circumradius radical chain: $R=\sqrt{a^2+(\tfrac{s}{2})^2}=\tfrac{s}{2}\sqrt{4+2\sqrt2}=\dfrac{(2-\sqrt2)\sqrt{2+\sqrt2}}{2}=\dfrac{1}{\sqrt{2+\sqrt2}}$.
- interior angle $135^\circ$; eight equal edges $s$; four $45^\circ$ chamfers of cutback $d=s/\sqrt2$; $2d^2=s^2$.
- **octagon area (F01, corrected chain):**
$$
A_O=4as=2(1+\sqrt2)s^2=8(\sqrt2-1)a^2=2(\sqrt2-1)w^2=2\sqrt2-2\quad(w=1).
$$
  The v0.1 intermediate "$2(1+\sqrt2)a^2$" was wrong: it equals $(1+\sqrt2)/2\approx1.207\ne A_O$, differing from the true area by $(5-3\sqrt2)/2$. The correct coefficient $2(1+\sqrt2)$ multiplies $s^2$, not $a^2$. Shell panel area $=3A_O=6(\sqrt2-1)$.

## Construction identities

- middle panel fixed: $P_2^\beta(u,z)=(u,0,z)$.
- reversed outer start: $P_1^0=P_3^0=(-u,0,z)$.
- **general-$\beta$ maps (F02):**
$$
P_1^\beta(u,z)=\bigl(-\tfrac12+(\tfrac12-u)\cos\beta,\ (\tfrac12-u)\sin\beta,\ z\bigr),\quad
P_3^\beta(u,z)=\bigl(\tfrac12-(\tfrac12+u)\cos\beta,\ (\tfrac12+u)\sin\beta,\ z\bigr).
$$
- hinges fixed for all $\beta$: $P_1^\beta(\tfrac12,z)=(-\tfrac12,0,z)=H_1$, $P_3^\beta(-\tfrac12,z)=(\tfrac12,0,z)=H_2$.
- free outer edges: $F_1^\beta(z)=(-\tfrac12+\cos\beta,\sin\beta,z)$, $F_3^\beta(z)=(\tfrac12-\cos\beta,\sin\beta,z)$; $F_3^\beta-F_1^\beta=(1-2\cos\beta,0,0)$; $y,z$ agree identically.
- **closure (F02):** on $0\le\beta\le\pi$ the unique closure is $\beta=\tfrac\pi3$; for unrestricted real $\beta$, $\beta=2k\pi\pm\tfrac\pi3$.
- **F11:** there are **two** free outer edges; at closure they coincide into a **third** seam $F=\{(0,\tfrac{\sqrt3}{2},z):|z|\le s/2\}$ alongside the two hinges $H_1,H_2$.

## Topology identities

| Quantity | Value |
|---|---|
| faces $F$ | $3$ |
| vertices $V$ | $18=24-3\cdot2$ |
| edges $E$ | $21=24-3\cdot1$ |
| Euler characteristic $\chi$ | $V-E+F=0$ |
| connected components | $1$ |
| seam (interior) edges | $3$: $(3,4)=H_1$, $(10,11)=H_2$, $(0,7)=$ apex |
| boundary edges | $18=9+9$ |
| boundary loops | $2$ (each a degree-two $9$-cycle) |
| surface hypotheses | connected, compact, orientable, manifold-with-boundary, $b=2$ |
| genus / type | $g=0$ from $\chi=2-2g-b$; **annulus = sphere minus 2 open discs** (F03), not a torus |

## Central-band / angle identities

- filled triangle $T$: corners $C_1=(-\tfrac12,0)$, $C_2=(\tfrac12,0)$, $C_3=(0,\tfrac{\sqrt3}{2})$; side $1$, altitude $\tfrac{\sqrt3}{2}$, area $\tfrac{\sqrt3}{4}$, inradius $\tfrac{\sqrt3}{6}$, circumradius $\tfrac{\sqrt3}{3}$.
- **section vs region (F04):** for $|z_0|\le\tfrac{s}{2}$, $S\cap\{z=z_0\}=\partial T\times\{z_0\}$ (triangle **perimeter**, planar area $0$); area/inradius/circumradius belong to the **filled** $T$, not the section curve.
- outward normals $n_2=(0,-1,0)$, $n_1=(-\tfrac{\sqrt3}{2},\tfrac12,0)$, $n_3=(\tfrac{\sqrt3}{2},\tfrac12,0)$; $n_i\cdot n_j=-\tfrac12$.
- three distinct angles: fold magnitude $\beta=60^\circ$ (from reversed start; $=180^\circ-120^\circ$ from unfolded / co-directional strip); interior dihedral $=60^\circ$; outward-normal separation $=120^\circ$ (supplement of dihedral).
- **F09 (chamfer-edge inclination):** each chamfer boundary edge satisfies $|\Delta z|=\sqrt{\Delta x^2+\Delta y^2}=d$, so its inclination to the horizontal is $45^\circ$. The **panel planes are vertical** (plane inclination $90^\circ$; face normals have zero $z$-component). The notch plane has inclination $\arctan(2/\sqrt3)$. Never "$45^\circ$ wall."

## Notch identities

- exact incident edge vectors at apex tip $A=V_7$, neighbours $B=V_6$, $C=V_{16}$: $e_1=B-A=d(-\tfrac12,-\tfrac{\sqrt3}{2},1)$, $e_2=C-A=d(\tfrac12,-\tfrac{\sqrt3}{2},1)$ (F05).
- $|e_1|^2=|e_2|^2=2d^2=s^2$; $e_1-e_2=(-d,0,0)$; $e_1\cdot e_2=\tfrac32 d^2=\tfrac34 s^2$.
- tip angle $\alpha_{\mathrm{notch}}=\arccos(\tfrac34)\approx41.4096221093^\circ$; base cosine $\dfrac{(-e_1)\cdot(e_2-e_1)}{s\,d}=\dfrac{\sqrt2}{4}$, base angle $\arccos(\tfrac{\sqrt2}{4})=\tfrac{\pi-\arccos(3/4)}{2}\approx69.2951889454^\circ$.
- projection: $e_1^\perp,e_2^\perp$ with $|e_1^\perp|=|e_2^\perp|=|e_1^\perp-e_2^\perp|=d$ (equilateral, $60^\circ$).
- $e_1\times e_2=d^2(0,1,\tfrac{\sqrt3}{2})$; notch-plane inclination $\arctan(2/\sqrt3)\approx49.1066053509^\circ$.
- areas: spatial $\tfrac{\sqrt7}{8}s^2$, projected $\tfrac{\sqrt3}{8}s^2$.
- rim (each end): nonplanar $9$-edge closed curve, perimeter $9s$; projection $\partial T$ split $d,s,d$ ($2d+s=1$).
- enclosed regions: central hexagon (six $120^\circ$, alternating $s,d$), area $\tfrac{\sqrt3}{4}(1-3d^2)=\tfrac{\sqrt3(3+4\sqrt2)}{8}s^2=-\tfrac{7\sqrt3}{8}+\tfrac{3\sqrt6}{4}$; identity $A_{\mathrm{hex}}+3A_{\mathrm{notch,proj}}=\tfrac{\sqrt3}{4}$. Virtual measurement regions, not mesh/cap faces.

## Symmetry

- group $\operatorname{Sym}(S)=D_3\times C_s\cong D_{3h}$, order $12$: elements $\{E,2C_3,3\sigma_v,\sigma_h,2S_3,3C_2'\}$.
- generators: $C_3$ (120° about vertical axis through $O_c=(0,\tfrac{\sqrt3}{6},0)$); $\sigma_v$ (mirror $x=0$); $\sigma_h$ (mirror $z=0$); $S_3=\sigma_h C_3$.
- lower bound: twelve exhibited maps permuting whole faces (convex hulls of vertex cycles). Upper bound (F06): the three crease segments $K_i=\{(C_i,z):|z|\le\tfrac s2\}$ force block form $(r,z)\mapsto(Br,\varepsilon z)$, $B$ one of $6$ triangle symmetries, $\varepsilon\in\{\pm1\}$, so $|\operatorname{Sym}(S)|\le12$; bounds meet.
- relations: $C_3^3=\mathrm{id}$, $C_3\ne\mathrm{id}$, $\sigma_v^2=\sigma_h^2=\mathrm{id}$, $\sigma_vC_3\sigma_v=C_3^{-1}$, $\sigma_hC_3=C_3\sigma_h$.
- **not** $D_{24}/\mathbb Z_{24}$: those label different (concentric, planar) constructions, not this welded shell.
