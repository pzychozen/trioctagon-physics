# Bounded exact search for distinguished members

This is an exact comparison of the explicitly defined functions in
`METRIC_FUNCTIONS.md`, not a parameter sweep or a claim about every possible
geometric functional. Positive magnitudes lie in (0,U], U=(sqrt(2)-1)/2.
Every positive result gives two mirror members t=+u and t=-u. No hand and
no value is preferred or chosen by Hilmir.

## Exhausted finite comparison classes

`SPECIAL_MEMBER_RESULTS.json` contains all 28 pair comparisons of the eight
edge functions and all six pair comparisons of the four face-area functions,
including zero and endpoint tests and exact root isolation. Roots of
polynomials over the exact radical coefficient field are isolated before
testing admission. Squared-length and squared-area comparisons are
equivalent to the original positive-metric comparisons here.

Only E1=E7 has an interior edge-class equality. Its defining polynomial is

\[
Q(u)=(-\sqrt6/2-1+\sqrt3)u^2
+(-9/4+3\sqrt2/2)u
+17/12-\sqrt2-\sqrt6/24+\sqrt3/12.
\]

It has exactly one positive admitted root,
u_e=0.19779748604884162... . With Q=A u^2+B u+C,
the exact radical expression is (-B-sqrt(B^2-4AC))/(2A). The JSON also
records its rational isolator and algebraic root identity. The remaining
27 edge-pair comparisons have no interior root. At zero only E0=E5,
E3=E6 and E4=E7 occur between distinct edge functions. No new pair equality
occurs at U.

No distinct face-area functions agree at any positive admitted magnitude.
At zero P0=P1 and P2=P3, while the band and cap areas still differ. No new
area equality occurs at U. Six triangles in each existing orbit are equal
for all u; that permanent equality does not select a member.

The whole mesh cannot be equi-edge: E1 squared minus E0 squared stays
strictly positive. It cannot be equi-area at any admitted magnitude,
including zero. These absence claims are limited to this exact mesh.

## Selected fold-angle equality

For the unoriented plane angles along edges (0,8) and (0,7), equal cos
squared reduces exactly, with nonzero normal-length denominators, to

\[
48u^3-28u^2+40u-1=0.
\]

Its derivative 144u^2-56u+40 is positive for all real u, so its unique real
root is the unique admitted equality:

\[
u_d=0.02543304657063014\ldots,\quad
\frac{68552749}{2695420260}<u_d<
\frac{45311102}{1781583731}.
\]

The upper/lower fan-rib plane angles, along (0,12) and (6,15), agree only
at zero. The full algebraic numerator and root exclusion are in the JSON.
No assertion about all possible signed dihedral equalities is made.

## Unique total-area minimum

For S(u)=6 sum_j sqrt(P_j(u)), strict convexity is certified on [0,1/4],
which contains [0,U]. For every nonconstant P_j the numerator

\[
N_j=2P_jP_j''-(P_j')^2
\]

is strictly positive there. The JSON records **all positive Bernstein
coefficients** on that interval, as well as positivity certificates for
P_j. Since (sqrt(P_j))''=N_j/(4P_j^(3/2)), their sum has S''>0; P2 is
constant. Also S'(0)<0 and S'(1/5)>0, with 1/5<U. Therefore exactly one
stationary point occurs, and it is the unique magnitude minimum.

The exact implicit definition S'(u_a)=0 and rational isolator are

\[
\frac{148072145237}{5497558138880}<u_a<
\frac{59228858095}{2199023255552},\qquad
u_a=0.02693416631468608\ldots.
\]

The endpoint derivative signs are bounded with outward rational intervals
using 100-bit square-root bounds; no decimal tolerance certifies the signs.
The area there is approximately 0.6580785503383781 physical area units.
This is an area optimum of the imposed triangulation, **not energy or a
physical optimization law**. It does not prescribe an author's design.
S(|t|) has the two mirror minima; its one-sided slope at zero is nonzero,
so zero is not an ordinary differentiable stationary point of that even
signed metric function. Surface continuity is addressed separately.

## Other checked conditions and limits of absence claims

| Condition | Result on the admitted interval |
|---|---|
| Side quad planar | No; determinant is a nonzero constant times (u-1/2), and U<1/2 |
| Additional Euclidean symmetry | At zero only: vertex D3h, each face complex D3; nonzero sets stay C3 |
| Three-way covariance degeneracy | No; vertical eigenvalue stays strictly larger |
| Lower apex-triangle area stationary for u>0 | No; derivative is 3 sqrt(3) u/2 > 0 |
| Ring/apex radius ratio | a/r for every u, imposed rather than selecting |
| Footprint angle equals octagonal half-angle pi/8 | u=r tan(pi/8)=r(sqrt(2)-1), inside the interval |

The pi/8 comparison is tied to the existing octagonal angle rather than
an arbitrary number hunt, but that additional equation is not demanded by
the contact fit. It gives 0.11957315586905014..., distinct from all three
interior intrinsic conditions above. The originally illustrated s/4 is
neither newly adopted nor privileged.

For completeness of the symmetry exclusion: the distinct covariance axis
forces any isometry to preserve the vertical axis. Unequal upper/lower
apex radii forbid a height exchange at u>0. The upper equilateral triangle
admits only D3 planar operations, and the lower triangle's angle satisfies
0<delta<pi/3. Their reflection axes cannot coincide, leaving exactly C3.
No extra value was missed inside this domain by numerical angle sampling.

```text
DISTINGUISHED_t_FOUND = YES
NO_INTRINSIC_t_SELECTION_FOUND = NO, WITHIN THE DECLARED CONDITIONS
HOST_OR_AUTHOR_SELECTED_t = NONE
UNIQUE_NATURAL_OR_PHYSICAL_SELECTION = NOT_ESTABLISHED
GEOMETRICAL_FORM_SEARCH = CLOSED_AFTER_THIS_ORDER
```

The bounded search establishes conditional geometric special members. It
does not establish a universal notion of “natural,” nor exclude further
equalities of unexamined functions. The complete family remains preserved.
