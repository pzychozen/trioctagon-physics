# SIM04 — independently checked mathematical results

Status: analytical verification before fixtures and empirical evaluation. Authoritative proposal: received/SIM04_MATHEMATICAL_SPEC_v0.1.md. The source and accepted SIM03 findings are retained unchanged. All statements below concern real-valued arithmetic; later float64 checks are not interval certificates.

## 1. Hypotheses and provenance

Inherited from the source/SIM03: eight labeled centers; v incoming, a the realized signed impulse, w=v+a, and successor y=D(w), with componentwise D(x)=x/[1+log(1+|x|)]. Incoming, pre-damping and successor collective speeds are the means of eight Euclidean norms, not RMS speeds. The historical code's sign is +1 for bit 0 and -1 for bit 1. At a common phase H is shared; alpha=0.1H, h=|alpha|, g=(1-2bit)d/(||d||+0.01), a=alpha Gg, G=1/(1+u). Thus ||g||<1 for every finite d, including g=0 at d=0.

The accepted arrays already encode sequential mixed-position geometry. This task reads those intermediates and never reconstructs positions/centroids, reevaluates H, evolves a state or executes historical code. Stored w and a remain the numeric inputs; equivalent real formulas serve only consistency checks.

The earlier finite-step note supplies the vector/nonexpansion approach and coarse source condition. The monotone derivative refinement, profile refinement, full-pair aggregation and slack ladder are GPT proposals for SIM04, independently derived here rather than attributed as new SIM03 observations.

## 2. Damping derivative and its maximum on an interval

For s>=0 put b=1+log(1+s). Differentiating x/b(|x|) on either side of zero gives
D'(x)=k(|x|), k(s)=[b-s/(1+s)]/b².
At zero the difference quotient tends to 1, so D'(0)=1 and the derivative is continuous. The numerator is positive because b>=1 and s/(1+s)<1. Also k<=1/b<=1; strict inequality holds when s>0. Componentwise mean-value estimates imply Euclidean nonexpansion for two fixed input vectors.

Independent differentiation gives
k'(s)=[2s-(s+2)b]/[(1+s)²b³].
Let J(s)=(s+2)b-2s. Then J(0)=2 and J'(s)=log(1+s)+1/(1+s)>0. Thus k'<0 for s>=0 (the derivative at zero is the right derivative). This verifies the proposed monotonicity without a numeric derivative grid.

For a signed closed interval joining x_a and y_a, the nearest magnitude to zero is ell_a=0 when min(x_a,y_a)<=0<=max(x_a,y_a), otherwise min(|x_a|,|y_a|). Monotonicity makes k(ell_a) its exact maximal derivative. Therefore
|D(x_a)-D(y_a)|<=k(ell_a)|x_a-y_a|.
The three squared component bounds sum to K_i². Averaging yields S<=K<=Q. Zero-crossing intervals require kappa=1; no uniform strict contraction is implied.

## 3. Baseline and the source-separated chain

Write Delta v=v_c-v_d, Delta a=a_c-a_d and Delta w=w_c-w_d. Successor scalar differences obey
S=|mean_i(||y_ci||-||y_di||)|
 <=mean_i| ||y_ci||-||y_di|| |
 <=mean_i||y_ci-y_di||
 <=mean_i||Delta w_i||=Q.
Triangle inequality gives Q<=V+J_a=T, where V=mean||Delta v|| and J_a=mean||Delta a||.

Expand G_c g_c-G_d g_d as (G_c-G_d)g_c+G_d(g_c-g_d), or as (G_c-G_d)g_d+G_c(g_c-g_d). Multiplication by common |alpha| and triangle inequalities give both Gamma_(c|d) and Gamma_(d|c), hence T<=Gamma=min of the two.

For nonnegative incoming speeds, |G_c-G_d|=|u_c-u_d|/[(1+u_c)(1+u_d)]<=|u_c-u_d|<=V. Choose the expansion whose Rg coefficient is min(G_c,G_d), and bound its qbar by 1. That particular Gamma candidate is <=(1+h)V+h min(G_c,G_d)Rg=Omega. The minimum Gamma is therefore also <=Omega. This establishes S<=Q<=T<=Gamma<=Omega, including H=0 and either sign of H.

Expanding ||Delta v+Delta a||² gives ||Delta v||²+||Delta a||²+2 Delta v·Delta a. This is cross-history difference alignment, distinct from SIM03's single-history 2v·a. Direct stored Delta w determines Q; no cancellation-prone reconstructed square root is needed.

## 4. Scalar component profiles

D is odd and uses the same scalar function on all three coordinates. For any coordinate sign changes and permutation, ||D(w)|| is invariant. Let p(w)=sort(|w|) in ascending order. Then ||D(w)||=||D(p(w))||. Center labels are never sorted, and arbitrary rotations are not symmetries.

The nonnegative intervals joining corresponding profile components have maximal derivatives lambda_a=k(min(p_c,a,p_d,a)). The mean-value estimate and reverse norm triangle inequality give S<=P, where P_i=||lambda*(p_c-p_d)|| and P=mean P_i.

For nonnegative vectors, minimizing squared matching distance is equivalent to maximizing the matching dot product. If a<=b and c<=d, the ordered match exceeds the reversed dot product by (b-a)(d-c)>=0. Removing inversions proves that jointly sorted matching is minimal. Hence
||p(x)-p(y)||<=|| |x|-|y| ||<=||x-y||.
Together with lambda<=1 this gives P<=Q centerwise and after averaging. K and P are both retained without asserting an ordering between them. BEST_PRE=min(K,P) is taken at pair level before variance aggregation, with ties assigned to K.

Equal input norms do not suffice for equal damped norms: at r>0, an axis vector has damped norm r/[1+log(1+r)], whereas the equal-component vector has r/[1+log(1+r/sqrt(3))], which is larger. This disproves any attempted scalar contraction inference based only on equality of input norms, while preserving vector nonexpansion.

## 5. Complete-pair variance and sufficient conditions

For m scalars x_c, sum_(c>d)(x_c-x_d)²=m sum_c x_c²-(sum_c x_c)²=m² Var(x), with population ddof=0. Thus the unordered denominator is m², not m(m-1)/2. For m=5 use ten pairs; for m=4 use the six corresponding pairs, reusing their evaluated arrays.

For each nonnegative pair bound B>=|x_c-x_d|, squaring and summing proves Var(x)<=W_B=sum B²/m²; SD<=sqrt(W_B). Taking BEST_PRE before this sum is valid independently of outcomes because both K and P bound every pair.

For epsilon>=0: B<=epsilon implies the corresponding absolute output difference<=epsilon; W_B<=epsilon² implies output SD<=epsilon. If W_B<=Var(pre-damping speeds), it suffices for damping-stage scalar dispersion nonincrease. If W_B<=Var(incoming speeds), it suffices for incoming-to-output nonincrease conditional on the realized impulses, geometry and bits. Failure of either sufficient comparison establishes no expansion. Conditions are separately evaluated; strict margins above 1e-14, below -1e-14, and within tolerance receive the fixed PASS, NOT_ESTABLISHED, UNRESOLVED labels.

## 6. Post-output slack ladder

From saved successors only, form Zsigned, Zprofile, Tnorm and S as in the fixed specification. Reverse triangle inequality yields Tnorm<=Zsigned, and the component bound yields Zsigned<=K. Since D is increasing on nonnegative arguments, it preserves their sorted order, so p(D(w))=D(p(w)). The symmetry/profile argument therefore gives Tnorm<=Zprofile<=P. Also S<=Tnorm.

When K<=P choose Zstar=Zsigned; otherwise choose Zprofile. Then S<=Tnorm<=Zstar<=BEST_PRE<=Q. Subtracting adjacent terms telescopes exactly:
Q-S=(Q-BEST_PRE)+(BEST_PRE-Zstar)+(Zstar-Tnorm)+(Tnorm-S).
The four nonnegative real-valued gaps respectively identify fixed refinement, remaining derivative-bound slack, norm projection, and signed center cancellation. They are losses of information in inequalities, not causal shares of the dynamics. Floating residuals remain signed and are never clipped.

## 7. Implementation boundary and conclusion of proof gate

Analytic routines have explicit v,a,w,d,H,G,bit inputs only. They do not access saved successors, endpoint D(w), losses, retention, post norms or measured variances. The complete pre-output bound arrays must be written and hashed before successor arrays/reference outcome columns are loaded. D itself is evaluated only on the 14 fixed synthetic fixture groups; production uses analytic k and saved w.

The proposed equations and hierarchies are verified under their stated hypotheses. No changed formula, new family, tuned coefficient or weakened theorem is needed. Source-dependent families require shared H and source-factor/G hypotheses; arbitrary-vector fixture groups use only the vector families. No long-time or mean-speed-only predictive theorem follows. Empirical validity/tightness and sufficient-condition frequencies remain to be measured in the one authorized pass.
