# Paper A — Reference Ledger v0.1
Annotated bibliography for the literature-context pass on `PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.3.md`. Located by targeted web search (Sep 2026). DOIs verified against publisher/aggregator records; where a page range is quoted from memory it is marked "(verify at typesetting)". No manuscript edit; the mathematics is frozen.

## A. Coupled-cell networks, synchrony subspaces, balanced/equitable partitions
- **[SGP03]** I. Stewart, M. Golubitsky, M. Pivato, "Symmetry groupoids and patterns of synchrony in coupled cell networks," *SIAM J. Appl. Dyn. Syst.* **2**(4):609–646, 2003. DOI 10.1137/S1111111103419896. — Introduces **balanced equivalence relations / polydiagonal (synchrony) subspaces**; a polydiagonal is flow-invariant for *all* admissible vector fields iff the coloring is balanced. This is the exact home of Paper A's $V_3$.
- **[GST05]** M. Golubitsky, I. Stewart, A. Török, "Patterns of synchrony in coupled cell networks with multiple arrows," *SIAM J. Appl. Dyn. Syst.* **4**(1):78–100, 2005. DOI 10.1137/040612634. — Multi-arrow/quotient machinery; the quotient network on synchrony classes.
- **[GS06]** M. Golubitsky, I. Stewart, "Nonlinear dynamics of networks: the groupoid formalism," *Bull. Amer. Math. Soc.* **43**(3):305–364, 2006. DOI 10.1090/S0273-0979-06-01108-6. — Survey of the groupoid formalism; balanced colorings, quotient dynamics, synchrony subspaces.
- **[Field04]** M. Field, "Combinatorial dynamics," *Dynamical Systems* **19**(3):217–243, 2004. DOI 10.1080/14689360410001729379. — Coupled-cell / network **dynamics for maps (discrete time)**, relevant to Paper A being a map rather than a flow.
- **[Stewart07]** I. Stewart, "The lattice of balanced equivalence relations of a coupled cell network," *Math. Proc. Camb. Phil. Soc.* **143**(1):165–183, 2007. DOI 10.1017/S0305004107000273 (verify at typesetting). — Balanced-relation lattice; context for "which synchrony subspaces exist."
- **[GFBC24]** review: "Groupoids, fibrations, and balanced colorings of networks," *Int. J. Bifurcation and Chaos*, 2024. DOI 10.1142/S0218127424300143. — Recent synthesis explicitly tying **groupoids, graph fibrations, and balanced colorings** together (the three descriptions Paper A's crosswalk needs).

## B. Graph fibrations / coverings in network dynamics
- **[BV02]** P. Boldi, S. Vigna, "Fibrations of graphs," *Discrete Math.* **243**(1–3):21–66, 2002. DOI 10.1016/S0012-365X(00)00455-6. — Original combinatorial theory of **graph fibrations** (coverings are a special surjective/local-iso case).
- **[DL15]** L. DeVille, E. Lerman, "Modular dynamical systems on networks," *J. Eur. Math. Soc.* **17**(11):2977–3013, 2015. DOI 10.4171/JEMS/577. — A graph fibration induces a **semiconjugacy / conjugacy** between network dynamical systems: "the original network and its quotients are related by graph fibrations and hence their dynamics are conjugate." This is the general home of Paper A's Proposition 2 identity $F_M\circ P=P\circ F_3$.
- **[NRS16]** E. Nijholt, B. Rink, J. Sanders, "Graph fibrations and symmetries of network dynamics," *J. Differential Equations* **261**(9):4861–4896, 2016 (arXiv:1410.6021). DOI 10.1016/j.jde.2016.07.013 (verify at typesetting). — Self-fibrations as symmetries; builds on the fibration→conjugacy result.

## C. Equitable partitions / quotient Laplacian (algebraic graph theory)
- **[GR01]** C. Godsil, G. Royle, *Algebraic Graph Theory*, Springer GTM 207, 2001. DOI 10.1007/978-1-4613-0163-9. — **Equitable partitions**, the **quotient/divisor matrix**, and the fact that quotient-matrix eigenvalues are a sub-multiset of the graph's. The textbook home of Paper A's $\Delta_M P=P\Delta_d$ / $Q^\ast\Delta_M Q=\Delta_d$.
- **[OYSB13]** N. O'Clery, Y. Yuan, G.-B. Stan, M. Barahona, "Observability and coarse graining of consensus dynamics through the external equitable partition," *Phys. Rev. E* **88**:042805, 2013. DOI 10.1103/PhysRevE.88.042805. — **External equitable partitions** and Laplacian quotient; consensus/Laplacian reduction.
- **[Schaub16]** M. T. Schaub, N. O'Clery, Y. N. Billeh, J.-C. Delvenne, R. Lambiotte, M. Barahona, "Graph partitions and cluster synchronization in networks of oscillators," *Chaos* **26**(9):094821, 2016. DOI 10.1063/1.4961065 (arXiv:1608.04283). — Ties **(external) equitable partitions** to **cluster-synchronization invariance and stability**.

## D. Master stability & cluster synchronization (transverse stability, IRR blocks)
- **[PC98]** L. M. Pecora, T. L. Carroll, "Master stability functions for synchronized coupled systems," *Phys. Rev. Lett.* **80**:2109–2112, 1998. DOI 10.1103/PhysRevLett.80.2109. — The master-stability paradigm: block-diagonalize the variational equation transverse to the synchronous state.
- **[Pecora14]** L. M. Pecora, F. Sorrentino, A. M. Hagerstrom, T. E. Murphy, R. Roy, "Cluster synchronization and isolated desynchronization in complex networks with symmetries," *Nat. Commun.* **5**:4079, 2014. DOI 10.1038/ncomms5079 (arXiv:1309.6605). — **Symmetry/IRR block-diagonalization** of the variational dynamics into synchronization-cluster blocks — the general method that Paper A's deck-character decomposition $U_0\oplus U_2\oplus U_{13}$ specializes.
- **[Sorrentino16]** F. Sorrentino, L. M. Pecora, A. M. Hagerstrom, T. E. Murphy, R. Roy, "Complete characterization of the stability of cluster synchronization in complex dynamical networks," *Sci. Adv.* **2**(4):e1501737, 2016. DOI 10.1126/sciadv.1501737. — Transverse stability of cluster-synchronous states via irreducible-representation blocks; equitable/orbital partitions.

## E. Transverse instability / blowout / bubbling (loss-of-stability terminology)
- **[ABS96]** P. Ashwin, J. Buescu, I. Stewart, "From attractor to chaotic saddle: a tale of transverse instability," *Nonlinearity* **9**(3):703–737, 1996. DOI 10.1088/0951-7715/9/3/006. — **Transverse Lyapunov/Floquet loss of stability** of an invariant subspace.
- **[ABS94]** P. Ashwin, J. Buescu, I. Stewart, "Bubbling and riddling of chaotic attractors," *Phys. Lett. A* **193**:126–139, 1994. DOI 10.1016/0375-9601(94)90947-4 (verify at typesetting). — Bubbling/riddling at transverse-stability loss.
- **[OS94]** E. Ott, J. C. Sommerer, "Blowout bifurcations: the occurrence of riddled basins and on-off intermittency," *Phys. Lett. A* **188**:39–47, 1994. DOI 10.1016/0375-9601(94)90114-7 (verify at typesetting). — **Blowout bifurcation** terminology.

## F. Higher-harmonic phase coupling / cluster states
- **[HMM93]** D. Hansel, G. Mato, C. Meunier, "Clustering and slow switching in globally coupled phase oscillators," *Phys. Rev. E* **48**:3470–3477, 1993. DOI 10.1103/PhysRevE.48.3470. — Second-harmonic phase coupling → **multi-cluster states**; canonical reference that higher-harmonic $\sin(m\Delta\phi)$ coupling supports $m$-cluster synchrony (Paper A's $\sin 3(\phi_i-\phi_j)$ with three residue classes).
- **[AS92]** P. Ashwin, J. W. Swift, "The dynamics of $n$ weakly coupled identical oscillators," *J. Nonlinear Sci.* **2**:69–108, 1992. DOI 10.1007/BF02429852 (verify at typesetting). — Symmetric phase-oscillator cluster dynamics; higher-harmonic terms.

## G. Covering-graph / lift spectra
- Standard lift/voltage-graph spectral theory (the spectrum of a regular cover decomposes over the deck-group irreducible representations; for an abelian deck group these are characters, giving the lifted eigenvectors and inherited eigenvalues). Textbook: [GR01] (equitable partition / quotient) and lift-spectra literature (e.g. Dalfó–Fiol et al., "Spectra of lifted digraphs," *J. Algebraic Combin.*, 2019, DOI 10.1007/s10801-018-0862-y). Paper A's $e_0,e_4,e_8$ with inherited eigenvalues $\{0,-3,-3\}$ are a textbook instance.

## H. Coupled map lattices (discrete-time dynamical neighbour)
- **[Kaneko90]** K. Kaneko, "Clustering, coding, switching, hierarchical ordering, and control in a network of chaotic elements," *Physica D* **41**(2):137–172, 1990. DOI 10.1016/0167-2789(90)90119-A. — **Cluster states in coupled map lattices** (discrete-time); the closest dynamical genre to Paper A's map, though with real logistic maps rather than a complex Mexican-hat + harmonic-3 phase step.

## I. Adaptive / state-dependent coupling preserving synchrony
- Covered within [Schaub16]/[Sorrentino16] and the balanced-partition invariance principle: a coupling that respects the balanced partition preserves the synchrony subspace. Paper A's Corollary 3 ($k$-only feedback) is a specialization of this principle; no single stronger stand-alone theorem is needed to subsume it, and none more specific than the balanced-invariance statement was located.

---
**Note on completeness.** This is a *focused* pass across the families named in the work order, not an exhaustive survey. No priority or novelty determination is made from absence. Exact volume/page details flagged "(verify at typesetting)" should be confirmed against the publisher record before a referenced manuscript v0.4.
