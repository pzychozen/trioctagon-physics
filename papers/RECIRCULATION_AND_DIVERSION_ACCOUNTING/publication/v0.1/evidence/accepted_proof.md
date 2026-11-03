# Native toroidal recirculation and possible diversion — proof review

Task: `NATIVE_TOROIDAL_RECIRCULATION_AND_DIVERSION_01`  
Research author: Hilmir Frímann Halldórsson / pzychozen  
Review: GPT / author; mathematical and source challenge: Codex  
Investigation date: 2 November 2026, Atlantic/Reykjavik  
Status: completed bounded analytical review; no model change or publication.

## Executive answer

**The separately adopted C1 carrier supports exact internal recirculation. It does not establish transport from, or energetic return to, the native center.** During a source-off interval its two characteristic profiles travel in opposite directions around the periodic circle. After one circuit time, each profile returns to the same carrier coordinates, and total carrier storage is unchanged. Passing a cut can remove storage from a subarc while putting it on the complementary arc. It does not remove that storage from the circle.

**Unmodified source-off C1 has zero fractional depletion of its positive total storage.** C6 reads delayed carrier history without imposing a debit. Negative work through an existing drive can reduce C1 storage during driving, but the model does not identify a recipient or pair that work with a native balance. Thus neither periodic travel nor a nonzero exterior record establishes non-returning energetic loss.

**No 15–20% diversion share can be inferred.** The author's range, including the possibility of more, remains an unverified intuition. For C1 total-storage depletion after source-off the exact answer is zero, when the denominator is positive. For a route-specific diverted or non-returning share, the numerator, reference throughput, accounting boundary, time window and receiving state are missing. Those are different questions. The zero-depletion theorem does not decide physical loss or rule out a future expanded system.

The smallest missing connection is a typed exchange account: identify what receives launch/return/diversion, define the corresponding transfers and storage, attach the route to the intended geometry, and pair any claimed native supply or return with a reciprocal native balance and a time/unit bridge. The existing two-drive readout is already defined conditionally; it is not that reciprocal exchange law.

Source IDs below resolve to exact file paths, line ranges, editions and SHA-256 values in `CLAIM_SOURCE_LEDGER.md` and `SOURCE_IDENTITIES.json`. Claim IDs R01–R23 cross-reference the ledger. Accepted results are inherited, not re-proved or recalculated here.

| Question | Status | Scope of answer |
|---|---|---|
| Is native intensity bookkeeping exact? | Yes | Ideal unchanged map, with mismatch and full finite-step square retained. |
| Does the accepted potential descend? | Yes, on its fixed domain | Exact coefficient tuple and coherent domain below; no recipient is identified. |
| Can C1 carry storage past a section and around its circle? | Conditional yes | Separately adopted C1; directional travel and source-off recurrence below. |
| Is there necessarily one circulating direction? | No | Counterpropagation is allowed; signed flux can cancel. |
| Does source-off periodic travel deplete total C1 storage? | No | Conservation excludes positive depletion; the ratio requires positive storage. |
| Can existing drives remove C1 storage? | Conditional yes | Negative signed source work; destination is unspecified. |
| Does C6 deliver measured energy to a receiver? | No such account is defined | It supplies an observation map, without loading. |
| Is the circle the central tight toroid or a path through O? | No | The registered offset circle meets one finite host-notch pair and excludes O. |
| Does energy transfer from and return to the native center? | Underdetermined | No reciprocal exchange/return balance or route assignment. |
| Is a 15–20% diverted fraction established? | No inference available | No accepted theorem selects that interval or defines the intended fraction. |

## A. Exact circulation and conservation within C1

### A.1 Definitions, notation and regularity

The paired-driving source uses `r`, `g`, `L`, `epsilon`; this review writes $r_c,g_c,L_c,\epsilon_c$ to distinguish them from native coefficients and geometry. No equation changes. With $s\in\mathbb R/L_c\mathbb Z$, $c>0$, and the source's periodic, normalized, disjoint tent profiles $b_\pm\in H^1_{\rm per}$,

$$
g_c(s,t)=b_+(s)f_+(t)+b_-(s)f_-(t),\qquad
p_t+c(r_c)_s=g_c,\qquad (r_c)_t+cp_s=0. \tag{A1}
$$

The tent half-width satisfies $0<\epsilon_c<\eta$; it is a width along the carrier, not a tube radius. The real initial pair $(p_0,r_{c,0})$ is independently specified. The two $f_\pm$ are distributed source strengths, not values prescribed for $p$ at endpoints. There are no endpoints on this circle. [R03; C1_CARRIER 1–48]

For periodic $H^1$ preparation and continuous drives on finite intervals, the inherited theorem gives a unique solution in $C_tH^1_s\cap C_t^1L^2_s$. It also gives a $C_tL^2_s$ mild solution for $L^2$ preparation and $L^1_tL^2_s$ forcing. Its signed-work theorem explicitly extends the integrated global balance, and its derivative almost everywhere, to the finite-profile time-$L^2$ inputs, including finite sample/hold histories. These regularity statements are reused here; no trajectory is solved. [R03–R04]

Define

$$
e=\tfrac12(p^2+r_c^2),\quad j=cpr_c,\quad
E(t)=\int_0^{L_c}e\,ds,\quad y_\pm(t)=\int_0^{L_c}b_\pm p\,ds.
$$

The inherited local distributional and global accounts are

$$
e_t+j_s=pg_c,\qquad E'(t)=f_+y_++f_-y_-,\qquad
E(b)-E(a)=\int_a^b(f_+y_++f_-y_-)\,dt. \tag{A2}
$$

The differential global identity has the strong-data meaning above and the almost-everywhere meaning for the stated mild extension. All point-cut statements below use spatial $H^1$ regularity, hence continuous spatial representatives and justified traces. We do not extend arbitrary point traces to every $L^2$ state. Source-off conservation and profile recurrence also hold as $L^2$ identities. [R04; C1_CARRIER 50–75; PUB_GEOMETRY 78–103]

### A.2 Theorem: what returns, and what a full circuit counts

**Theorem (new deductions from inherited characteristics).** Suppose the entire interval in question is source-off, $g_c=0$. Put

$$
w_\sigma=\frac{p+\sigma r_c}{\sqrt2},\quad
\rho_\sigma=\frac{w_\sigma^2}{2},\quad
E_\sigma=\int_0^{L_c}\rho_\sigma\,ds,\quad \sigma\in\{+1,-1\}.
$$

Then:

1. Each $E_\sigma$, and therefore $E=E_++E_-$, is constant. The $+$ profile travels toward increasing $s$, and the $-$ profile toward decreasing $s$, both at speed $c$.
2. $T_{\rm loop}=L_c/c$ is a period of the source-off state: if the interval $[t,t+T_{\rm loop}]$ is source-off, the state at its endpoints agrees. It need not be the smallest period.
3. At any fixed cut $s_*$, at the stated trace regularity, define the nonnegative directional throughputs

   $$
   Q_\sigma(s_*;a,b)=\int_a^b c\rho_\sigma(s_*,u)\,du.
   $$

   For one full source-off circuit,

   $$
   Q_\sigma(s_*;t,t+T_{\rm loop})=E_\sigma(t),\qquad
   \int_t^{t+T_{\rm loop}}j(s_*,u)\,du=E_+(t)-E_-(t),
   $$

   $$
   \int_t^{t+T_{\rm loop}}j_{\rm gross}(s_*,u)\,du=E(t),\qquad
   j_{\rm gross}:=c(\rho_++\rho_-)=ce. \tag{A3}
   $$

**Written proof.** Adding/subtracting (A1) gives

$$
(\partial_t+\sigma c\partial_s)w_\sigma=g_c/\sqrt2.
$$

Multiplication by $w_\sigma$ gives the directional distributional balance

$$
\partial_t\rho_\sigma+\sigma c\partial_s\rho_\sigma
=w_\sigma g_c/\sqrt2. \tag{A4}
$$

On a source-off interval starting at $a$, the inherited characteristic formula specializes to

$$
w_\sigma(s,t)=w_\sigma(s-\sigma c(t-a),a). \tag{A5}
$$

Periodic translation preserves the $L^2$ norm, proving conservation of $E_\sigma$, including for $L^2$ preparation. A translation by $-\sigma L_c$ is the identity, proving recurrence. Direct inversion of the orthogonal transform gives

$$
e=\rho_++\rho_-,\qquad j=c(\rho_+-\rho_-),\qquad |j|\le j_{\rm gross}.
$$

For the cut identity, substitute (A5) into $Q_\sigma$ and change variables $x=s_*-\sigma c(u-t)$. In time $L_c/c$, this traverses the circle exactly once; reversing integration limits when necessary cancels the sign. The result is $\int_0^{L_c}\rho_\sigma(x,t)\,dx=E_\sigma(t)$. Taking the difference and sum proves (A3). This uses the source's representation, not a newly generated wave solution. □ [R05–R07; C1_CARRIER 27–45, 73–75]

The signed directional fluxes are $+c\rho_+$ and $-c\rho_-$; their nonnegative magnitudes are $c\rho_\pm$. Gross throughflow is their sum, **not** $|j|$. Equal directional storage can give zero full-circuit net cut amount with positive gross throughput. The theorem therefore provides neither a universal clockwise preference nor a requirement that any chosen state have nonzero flux.

Over $m$ full source-off circuits, gross throughput at the cut is $mE$, while stored energy is still $E$. Repeated cut passage counts circulating storage again; it is not $mE$ of new energy emitted by the total system. “All of it returns” is defensible only for a declared mathematical profile or same-direction section-turnover definition with a positive denominator. It does not identify tagged particles, energy cohorts in a superposed driven field, or an efficiency of return to the native center. [R07]

**Corollary (depletion obstruction).** If $E(t)>0$ and $[t,t+T_{\rm loop}]$ is source-off,

$$
d_E:=\frac{E(t)-E(t+T_{\rm loop})}{E(t)}=0. \tag{A6}
$$

An assumed depletion law $E(t+T_{\rm loop})=(1-d)E(t)$ with $d>0$ contradicts (A2). At $E=0$ the ratio is undefined; conservation still holds. The same obstruction applies to any source-off time interval, without waiting for a whole circuit. There is no intrinsic damping, leakage branch or loaded receiver in the inspected C1/C6 equations. [R08; C1_CARRIER 65–70; C6_EXTERIOR 1–10; C1_LIMITS 14]

This is conditional homogeneous circulation of mathematical profiles. It does not contradict the source's statement that autonomous physical circulation has not been established: the source does not establish a native-powered physical cycle, its initialization, a material route or a reciprocal core mechanism.

### A.3 Driven intervals: preparation and signed work

Write $W_{\rm src}[a,b]=\int_a^b\sum_\pm f_\pm y_\pm\,dt$. It is signed, and equals $E(b)-E(a)$. Positive net work increases total storage; negative net work reduces it; zero net work can conceal positive and negative contributions during the interval. Cut transport is a different account. [R04, R09]

Equal drives **and equal preparation** give the same state and storage by uniqueness. Drives alone do not determine storage history. This remains true even if the initial total storage is specified. For a generic continuous drive with $g_0=g_c(\cdot,a)\ne0$, consider the two allowed preparations

$$
p_0^{(\pm)}=\pm A g_0,\quad r_{c,0}^{(\pm)}=0,\quad A>0,
$$

where $A$ has time dimension. Both have $E(a)=A^2\|g_0\|_2^2/2$, but (A2) gives

$$
E'_{(+)}(a)=+A\|g_0\|_2^2,\qquad E'_{(-)}(a)=-A\|g_0\|_2^2. \tag{A7}
$$

Thus the same prescribed drives and same initial total storage can give different energy histories. This is a written comparison of admissible initial data and the inherited identity, with no evaluated trajectory. It strengthens the source's negative-work preparation example. It is an existence statement when $g_0\ne0$, not a claim about every forcing: for source-off histories and equal initial storage, total storage histories agree. [R09; C1_CARRIER 77–84]

Negative source work identifies an existing mathematical interface through which C1 storage decreases. It does not assign that decrease to an exterior receiver, dissipation or the native core. C1 includes no native debit for positive work and no native credit for negative work. Neither source strengths squared nor projected inputs squared replace $f_\pm y_\pm$. Storage is quadratic: superposed responses have cross terms, so a unique “newly launched energy” cannot be separated from a pre-existing field merely by adding amplitude solutions. [R09, R12]

### A.4 The two cuts and the complementary arc

Let $I=[s_+,s_-]$ be the short arc and $K=[s_-,s_++L_c]$ its periodic complement. Reuse the accepted host-notch signs

$$
P_{\rm out,+}=-j(s_+,t),\qquad P_{\rm out,-}=+j(s_-,t),\qquad
B=P_{\rm out,+}+P_{\rm out,-}=j(s_-,t)-j(s_+,t).
$$

Define $\dot W_I=\int_I pg_c\,ds$, $\dot W_K=\int_K pg_c\,ds$. The accepted short-arc balance and the complementary balance are

$$
E_I'=\dot W_I-B,\qquad E_K'=\dot W_K+B,\qquad
E'=\dot W_I+\dot W_K=\sum_\pm f_\pm y_\pm. \tag{A8}
$$

**Written complementary-arc proof.** Integrating $e_t+j_s=pg_c$ over $K$ gives $E_K'=\dot W_K+j(s_-)-j(s_++L_c)$. Periodicity identifies the last value with $j(s_+)$, giving the second equation. Adding cancels the internal boundary flux. The trace assumptions are those in A.1; derivatives hold almost everywhere. In integrated form, for $J=I,K$,

$$
E_I(b)-E_I(a)=W_I[a,b]-\int_a^b B\,dt,
$$

$$
E_K(b)-E_K(a)=W_K[a,b]+\int_a^b B\,dt. \tag{A9}
$$

When sources are off, any net decrease in $E_I$ equals an increase in $E_K$. During driving, each local account also includes its own work, and a decrease in total storage occurs exactly when the net total source work is negative. A positive $B$ alone does not prove total loss. The tents straddle the cuts, so $W_I$ is generally not the full source work. [R10–R11; PUB_GEOMETRY 78–103]

Positive $j(s_+)$ is incoming at the upper cut; positive $j(s_-)$ is outgoing at the lower. Negative local $j$ reverses the corresponding sign. Upper and lower are geometric labels, not permanent exhaust assignments. Both cuts remain internal sections of one periodic domain; neither is an absorbing endpoint or a boundary of a defined central control volume.

## B. Diversion: types, denominators and exact limits

### B.1 Existing quantities versus proposed fractions

Use the source's abstract dimensions $\mathrm U,\mathrm L,\mathrm T$. No SI calibration is supplied. An amount of C1 storage has dimension $\mathrm U^2\mathrm L$; a cut power has dimension $\mathrm U^2\mathrm L/\mathrm T$. [R12; C1_FOUNDATIONS 69–90]

| Quantity | Mathematical type and current meaning | Return/diversion limitation |
|---|---|---|
| $E(t)$, $E_\pm(t)$ | Nonnegative stocks, $\mathrm U^2\mathrm L$; characteristic stocks follow from the orthogonal transform | Not automatically energy launched from the core. $d_E$ is defined for $E>0$ and is zero source-off. |
| $\int_a^b j(s_*,t)dt$ | Signed net cut amount, $\mathrm U^2\mathrm L$ | Can be zero or negative through cancellation; not a default positive fraction denominator. |
| $Q_\pm(s_*;a,b)$ | Nonnegative directional cut amounts, $\mathrm U^2\mathrm L$ | Need a specified cut, direction, window and positive denominator. Available as mathematical throughput, not a native launch/return assignment. |
| $\int_a^b j_{\rm gross}(s_*,t)dt$ | Nonnegative gross amount counting both directions | Recounts storage on later circuits. Not a count of distinct exported energy. |
| $W_{\rm src}[a,b]$ | Signed source work, same storage dimension | May remove rather than supply storage. Not automatically launch throughput or an exterior delivery. |
| $\int_0^{L_c}j(s,t)ds$ | Spatially integrated flux, $\mathrm U^2\mathrm L^2/\mathrm T$ | Neither a cut power nor a transported amount; a different dimension. |
| Native $I,V,D_{ij},A_{ij}$, decoded vector | Native scalars/quadratics/potential or based vector; no canonical C1 energy calibration | A decrease, arrow length or area is not a measured launch or diversion amount. |
| C6 $Y_X=(U,B^TV_{\rm ext})$ | Delayed linear record with amplitude dimension $\mathrm U$ | No receiver storage or receiving-power balance; squared record is not declared emitted power. |
| $Q_{\rm launch},Q_{\rm return},Q_{\rm div}$ for the intended central route | Proposed nonnegative transfer amounts after interfaces are assigned | The intended numerator and denominator are not defined by the existing sources. |

Two minimal future definitions would answer different questions: **a per-pass diverted share** $Q_{\rm div}/Q_{\rm launch}$, or **a finite-window return deficit** $1-Q_{\rm return}/Q_{\rm launch}$. Neither is adopted here. Their equality needs additional bookkeeping conditions. Eventual non-return is a third, limiting question and cannot be substituted for either finite-window definition. [R12–R14]

### B.2 Hypothetical control-region ledger — necessary, not adopted

Suppose, solely for bookkeeping, a future route region and interval $[a,b]$ are specified. Assign nonnegative, oriented transfer amounts $Q_{\rm launch},Q_{\rm return},Q_{\rm div},Q_{\rm other,in},Q_{\rm other,out}$, signed non-boundary work $W_{\rm route}$, and route inventory change $\Delta S_{\rm route}$. Compatible accounting requires

$$
Q_{\rm launch}+Q_{\rm other,in}+W_{\rm route}
=Q_{\rm return}+Q_{\rm div}+Q_{\rm other,out}+\Delta S_{\rm route}. \tag{B1}
$$

No such control region or transfer law is selected by this equation. All terms must use the same energy unit and time window, and each interaction must be counted once: a distributed source contribution already booked as $W_{\rm route}$ cannot also be counted as boundary launch work without changing the accounting partition. The individual transfer labels require orientations and a rule for separating incoming/outgoing events, especially when paths are revisited.

With no “other” transfers and $Q_{\rm launch}>0$, define, hypothetically, $f_{\rm div}=Q_{\rm div}/Q_{\rm launch}$. Rearranging (B1) gives

$$
\frac{Q_{\rm return}}{Q_{\rm launch}}
=1-f_{\rm div}+\frac{W_{\rm route}-\Delta S_{\rm route}}{Q_{\rm launch}}. \tag{B2}
$$

Therefore $Q_{\rm return}=(1-f_{\rm div})Q_{\rm launch}$ requires the extra balance $W_{\rm route}=\Delta S_{\rm route}$, for example both zero, as well as no other transfers and compatible event/window counting. In that restricted account, nonnegative amounts give $0\le f_{\rm div}\le1$. With other work or inventory release, a raw ratio need not even have that upper bound and would not be a simple share of newly launched energy. [R13]

**Written non-identifiability example at the level of accounts.** For $Q>0$ and $0<d<1$, a measured finite-window return $(1-d)Q$ with launch $Q$ and zero other work is compatible both with (i) diversion $dQ$, zero inventory change, and (ii) zero diversion, inventory increase $dQ$. Both satisfy (B1). These are alternative ledger assignments, not constructed dynamics or synthetic observations. Return deficit alone therefore cannot identify diversion; storage or delayed arrival can give the same deficit. [R14]

To test a diverted share, a future model needs an actual destination state or receiving-power law (an internal store is one possible destination), not just a subtraction symbol. To attribute the supply to the native center it also needs a commensurate native energy candidate, an index-to-carrier-time bridge, and reciprocal debit/credit or backreaction. Neither $I$ nor $V$ is selected here as that native energy. A baseline/preparation and an attribution convention are needed to distinguish new launch from stored waves and quadratic interference.

If “elsewhere” is an internal store, the compatible hypothetical special case is

$$
\Delta S_{\rm route}=Q_{\rm launch}-Q_{\rm return}-Q_{\rm div}+W_{\rm route},
$$

$$
\Delta S_{\rm core}=-Q_{\rm launch}+Q_{\rm return}+W_{\rm core},\qquad
\Delta S_{\rm dest}=Q_{\rm div}+W_{\rm dest}. \tag{B3}
$$

Adding cancels all three internal transfers. The union changes only by the summed work. This explains why diversion from a return path need not mean loss from the total system. If the destination is outside the chosen total boundary, its transfer belongs in that total's outgoing account instead. A dissipative interpretation would require its own energy/heat account if total conservation is claimed. Equations (B1)–(B3) are necessary accounting templates, not new laws for F, C1 or C6. [R13–R14]

### B.3 Per-pass versus eventual non-return; the numerical intuition

If a future law assumed a constant per-pass removed share $f$, no additional work or inventory ambiguity, and no re-entry of removed energy, then

$$
Q_{m+1}=(1-f)Q_m,\qquad Q_m=(1-f)^mQ_0,
$$

$$
Q_{\rm removed,cumulative}(m)=Q_0[1-(1-f)^m]. \tag{B4}
$$

This follows by repeated substitution and a telescoping sum. For $0<f<1$, the remaining amount tends to zero as $m\to\infty$. Thus an assumed per-pass percentage cannot silently become a one-time or eventual efficiency. This conditional algebra neither installs a loss coefficient nor evaluates the author's percentages. Re-entry, changing fractions, forcing and finite observation windows would change the account. [R15]

The accepted theorems do **not** restrict a central-route $f_{\rm div}$ to $[0.15,0.20]$, establish any value above that range, or establish an actual nonzero leak. In unmodified source-off C1, the total-storage depletion ratio is exactly zero. For the intended diverted-route ratio, it is **unidentifiable from the inspected definitions**, rather than a measured quantity with an uncertain estimate. No coefficient, gain, width, speed or native parameter has been set to 0.15 or 0.20. [R08, R14–R16]

A future expanded or intermittently diverted system is not refuted by (A6). The range could be entertained only as a future hypothesis or parameter, or ultimately as a measured ratio after specifying and measuring both numerator and denominator. The present sources supply no experiment or return-ratio dataset testing it. The author's “possibly more” is retained as intuition, not turned into a bound.

### B.4 C6 does not debit C1

The adopted C6 record has the schematic form $Y_X=g_o\mathcal K_X[p,r_c]$: a linear retarded integral at an off-circle point, with prescribed geometry, delay speed and gain. Its exact source explicitly assumes absence of loading. Neither $X$, $Y_X$ nor $g_o$ enters C1's state equations or work balance. [R17; C6_EXTERIOR 1–10, 20–35]

**Written independence argument.** Fix a carrier preparation and forcing, hence its unique history. Rescaling the allowed exterior gain rescales any nonzero record but leaves C1 and $E$ unchanged. Adding or changing observations likewise supplies no new term in (A2). A nonzero exterior record therefore cannot, from these equations, require an energetic debit. Conservation still holds on a source-off carrier interval even if a delayed record is nonzero there. No new history or receiver is evaluated to make this argument. [R17]

An energetic interpretation needs a source-to-receiver power functional and receiver storage/load equation, paired with a debit or boundary reaction in the supplying system. The source also flags the absent ambient energy/self-force construction. A radiating-looking display, $|U|^2+\|V_{\rm ext}\|^2$, or $r_c\hat t$ is not thereby measured radiated power or Poynting flux. [C1_LIMITS 14]

## C. Attaching the account to the intended central picture

### C.1 Distinct geometric objects

| Object | What the accepted sources establish | What is not supplied |
|---|---|---|
| C1 centerline $\Gamma$ | A periodic 1D coordinate embedded on an adopted vertical offset circle | A tube cross section, surrounding 3D vector field, material conduit or core return path |
| Intended tight toroid and paired up/down cones | Author's intended central outward/curved/inward circulation picture | A source-defined route, field, central control volume or coupling to C1 |
| $N_k^\pm$ | Finite host-notch measurement triangles with oriented normals; third side is a measurement closure | Identity with central broken boundaries or a material cap |
| $G_k^\pm$ | Six central broken two-segment boundaries | Filled aperture, closing chord, flux normal or six-port allocation law |
| Original close sphere | A geometric reference about O with radius $\sqrt{13/12-\sqrt2/2}$ | A wall, receiver, extended-line sphere or intended tight toroid |

In the accepted registration,

$$
\Gamma(s)=O+K_cu+R_c(\cos\chi\,u+\sin\chi\,e_z),\qquad \chi=s/R_c.
$$

The primary geometry proof gives $K_c-R_c>0$, so $(\Gamma(s)-O)\cdot u\ge K_c-R_c>0$. In particular O is not on this circle. Its axis is perpendicular to the shell's central axis; no identification with a cone or toroid axis follows. It meets only its own finite upper/lower patch pair. The accepted dictionary is $\Delta_j^\sigma-O=N_{(j+1)\bmod3}^\sigma$; C1 chooses $j=0$, hence $N_1^\pm$. [R18; PAIRED_GEOMETRY 75–108; PUB_GEOMETRY 31–76]

The central definitions instead give

$$
G_k^+=U_k\!\;--\;T_{2k+1}\!\;--\;U_{k+1},\qquad
G_k^-=L_k\!\;--\;B_{2k+1}\!\;--\;L_{k+1}.
$$

These list joined segments, not flow directions. The accepted fixed-gap obstruction rules out placing each entire broken arc in a host patch by a centered rotation; it does not rule out every future transfer construction. No missing chord, normal, filled surface or channel is added here. A closed curve in 3D alone cannot define the intended 3D circulation around it. [R19; PUB_GEOMETRY 20–29, 54–56; FIXED_GAP 63–99; FIXED_GAP_REVIEW 1–20]

### C.2 Available native observations and their limits

The unchanged native map evolves three complex channels. With $s_i=|\Omega_i|^2$, $D_{ij}=|\Omega_i-\Omega_j|^2$, $b_i=\epsilon(k_i-s_i)\Omega_i+g\sum_{j\ne i}(\Omega_j-\Omega_i)$, the accepted ideal finite-step account is

$$
\Delta I=2\epsilon\sum_i s_i(k_i-s_i)-2g\sum_{i<j}D_{ij}+\|b\|^2. \tag{C1}
$$

Its selected antisymmetric exchange $J^I_{i\to j}=g(s_i-s_j)$ is channel bookkeeping, not a spatial current. Divergence does not uniquely select a graph current; the mismatch and full square cannot be dropped. Real coefficients are allowed in the algebraic identity; sign conclusions need their stated signs. [R01; PUB_NATIVE 6–67; NATIVE; DIAGNOSTICS]

The inherited potential

$$
V=\epsilon\sum_i(s_i^2/4-k_is_i/2)+(g/2)\sum_{i<j}D_{ij}
$$

satisfies $V(F\Omega)-V(\Omega)\le-(16869/20000)\|b\|^2$ at precisely $\epsilon=1/10, g=1/60, \lambda=1/300, k=(999/1000,1,1001/1000)$, for $9/10\le|\Omega_i|\le11/10$ and ordinary phase width at most $\pi/12$, arbitrary common orientation. That invariant domain has nonzero prestages; descent is strict off the inherited aligned fixed circle. No new potential proof or historical symbolic check is run. This does not identify $V$ with C1 energy or assign a destination to its decrease. [R02; PUB_NATIVE 69–110]

For phase-sensitive observations the actual decoder gives $v_i=\Re\Omega_i\,t_i+\Im\Omega_i\,e_z$, based at fixed $c_i$. Its length is $\sqrt{s_i}$, not travel distance. Accepted frame identities give $n_i=-g_{i-1}$ and $c_i+\mathbb Rn_i=O+\mathbb Rg_{i-1}$. Common phase rotates each vector about its own stationary support line with the source's directed sign; it is not a common rigid-body pose. Full F also changes amplitudes and relative phases. Matched tangent-plane transport compares vectors and is not flow along seams. These are candidates for observations of orientation, not already selected flux directions or trajectories. [R20; PUB_READOUTS 10–28; FACE]

On the accepted coherent domain, $y=(s_1,s_2,s_3,A_{12},A_{13})$ determines full coherence, and the inherited closed map and unit multiplier reconstruct

$$
\Omega_n=u_0\left(\prod_{j=0}^{n-1}\kappa(G^jy_0)\right)z(G^ny_0).
$$

If only $y$ is retained, initial common phase $u_0$ is required for the actual phase-sensitive vectors. A recorded full complex state already includes that information. Frozen-setting staged Z discards common phase, so a genuinely common-phase-dependent outlet quantity cannot be inferred from that staged history alone. Recovering phase still does not supply an outlet transfer law. EMA has a distinct prior-memory/innovation path; no memory or observer is advanced here. Historical Z01–Z03 snapshots are context, not evidence of circulating energetic fields. [R21; PUB_READOUTS 30–57]

The conditional driving interface is not wholly missing: choose the source's named native family $v_{\rm in}=M$ or $C=\Re\Omega\times\Im\Omega$, register by $A_{\rm reg}=\lambda_gR_z(\delta_g)$, and set

$$
f_\pm=\kappa_{\rm in}n_\pm^T A_{\rm reg}v_{\rm in},\qquad \kappa_{\rm in}>0. \tag{C2}
$$

Its clock/configuration and sample/hold interpretation are adopted inputs. The two projections lose the component along $v=e_z\times u$; a positive gain converts data units to source strength, not energy efficiency. Raw channel chirality $C$ must not be conflated with its separately defined ambient attachment $T_fC$. None of this selects six central outflows from three native channels or two C1 contacts. [R22; C1_FOUNDATIONS 43–90; C1_NATIVE 1–10; PUB_READOUTS 28, 45–57]

### C.3 Text dependency map and interface table

```text
unchanged native F / recorded complex state
    -> named native readout                         [defined, settings/family explicit]
    -> registration + gain + sample/hold drives    [conditional adoption]
    -> C1 state (p,r_c), storage E and flux j      [conditional; preparation required]
       |-> same carrier coordinates after L_c/c  [deduced when source-off throughout]
       |-> C6 delayed exterior record            [conditional observation; no debit]
       -> two finite host-notch cuts N_1^+,N_1^- [established conditional signs]
       -> central broken boundaries G_k^±        [transfer registration absent]
       -> intended cone/toroid route             [geometry/field assignment absent]
       -> destination / diversion / core return  [transfer and receiving account absent]
       -> reciprocal native debit or credit      [exchange/backreaction absent]
```

The return arrow internal to C1 is not a feedback arrow into F. This dependency map does not prescribe that every future route must traverse G; it records precisely the requested central-opening interpretation that has not been supplied.

| Interface | Status | Smallest outstanding assignment |
|---|---|---|
| F/state to native readout | Defined once family/settings are named | Preserve retained phase if the chosen observation needs it. |
| Readout to $f_\pm$ | Conditional, existing | Retain registration, gain, clock/hold and preparation; these do not calibrate native energy. |
| $f_\pm$ to C1 $E,j$ | Conditional, existing | Well-posed data and signed source-work account already supplied. |
| C1 $j$ to host-notch cuts | Conditional, existing | $H^1$ traces and the established two signs; no new surface integral. |
| Host cuts to $G_k^\pm$ / intended route | Absent | A transfer registration and route definition, without identifying distinct objects. |
| Route to diversion/return | Absent | Destination and receiving state/power, oriented transfer rule, window and positive denominator. |
| Native supply and returned credit | Absent | Compatible native storage/time units and reciprocal balance or load/backreaction; unchanged F contains none. |
| C6 observation to receiver energy | Absent | Source/receiver energy balance and loading; observation alone is insufficient. |

[R18–R23]

## Final scientific interpretation

### PROVED by existing native algebra / accepted paper

The ideal F has the exact finite-step intensity account (C1), including edge mismatch and the full square. The accepted potential descends on the stated fixed coherent domain. The phase reconstruction, decoder and stationary support identities supply actual phase-sensitive observations. None of those inherited results identifies a spatial energy current, physical energy unit or destination of a decrease. The finite-patch dictionary and two conditional cut signs are accepted geometric results. [R01–R02, R10, R18–R22]

### PROVED within the separately adopted C1 carrier

C1 has the inherited existence/uniqueness and regularity statements, characteristic representation and signed work account. Source-off total storage is conserved, including at the stated weaker global level. The source profiles are distributed on a periodic domain; there is no absorbing end. C6 is a separate delayed history observation without loading. These are conditional model facts, not a proof that the native state supplies a physical circulating field. [R03–R04, R08, R17]

### DEDUCED here from those exact definitions

The written proofs establish directional storage conservation, full-circuit profile recurrence, signed versus gross section-throughput identities, repeated counting over circuits, and the zero-depletion obstruction. They also establish complementary-arc cancellation, the equal-initial-storage preparation comparison, finite-window diversion non-identifiability, conditional compounding, and the absence of a C6-induced debit. The hypothetical ledgers expose necessary terms without adding dynamics. [R05–R09, R11, R13–R15, R17]

### NOT DEFINED / NOT INFERABLE from inspected sources

The central native-to-route energy transfer, energetic return into F, receiving/diverting state, reciprocal debit/credit, physical time/unit bridge, and transfer from the two registered patches to the intended central geometry are missing. A route-specific diversion fraction and its 15–20% value cannot be inferred. There is no defined filled six-aperture flux account, 3D toroidal field or receiving load to evaluate. Negative source work is possible but does not name its destination. [R08–R09, R12–R14, R16–R19, R23]

### AUTHOR'S INTUITION

The center as a meeting/start region, the upward/downward cones, outward movement curving around an intended tight toroid and returning inward, and possible 15–20% or greater diversion remain the author's motivating picture. Flower/petal and heart-field comparisons are analogies. No empirical value, efficiency, field-line geometry or fitted parameter is claimed. [R16]

### Focused checkpoint after review

No additional input is needed to complete this investigation. The single useful decision for any later modeling discussion is: **Does “elsewhere” mean another store/route inside the chosen total system, or a destination outside that total-system boundary?** Internal diversion cancels in an enlarged total balance as in (B3); an external destination requires an outgoing total-system transfer and a receiving account. This decision changes the next mathematical problem, but neither answer supplies the presently missing transfer law. It is a review checkpoint, not a request to start a successor investigation.

The investigation stops here for GPT/author review. No parameters, native updates, carrier solves, geometry, observer states, repositories or publications have been changed.
