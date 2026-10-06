"""Typeset the approved science from public master derivatives; no historical writer runs."""
from pathlib import Path
import re,json,os
ROOT=Path(__file__).resolve().parents[1]
INV=json.loads((ROOT/'provenance/source_inventory.json').read_text())
LINKS={Path(e['source_locator']).name:e['path'] for e in INV}
def esc(s):
    table={'&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}','≥':r'\(\ge\)','≤':r'\(\le\)','→':r'\(\to\)','±':r'\(\pm\)','Ω':r'\(\Omega\)','η':r'\(\eta\)','ν':r'\(\nu\)','λ':r'\(\lambda\)','²':r'\(^{2}\)','³':r'\(^{3}\)'}
    table.update({'–':'--','—':'---','“':r'\textquotedblleft{}','”':r'\textquotedblright{}','‘':"'","’":"'","·":r'\textperiodcentered{}','§':r'\S{}'})
    return ''.join(table.get(c,c) for c in s).replace(r'\_',r'\_\allowbreak{}').replace('/',r'/\allowbreak{}')
def inline(s,lane):
    saved=[]
    def stash(t):
        saved.append(t);return f'ZZZTOKEN{len(saved)-1}ZZZ'
    def link(m):
        label,url=m.groups()
        if re.match(r'^[A-Za-z]:/',url) or url.startswith('project-source/'):
            name=Path(url).name
            if name not in LINKS:return stash(esc(label)+' (historical source locator)')
            url=Path(os.path.relpath(ROOT/LINKS[name],ROOT/lane)).as_posix()
        return stash(r'\href{\detokenize{'+url+'}}{'+esc(label)+'}')
    s=re.sub(r'\\\(.*?\\\)',lambda m:stash(m.group()),s)
    s=re.sub(r'\[([^\]\n]+)\]\(([^)\n]+)\)',link,s)
    s=re.sub(r'\x60([^\x60]+)\x60',lambda m:stash(r'\texttt{'+esc(m.group(1))+'}'),s)
    s=re.sub(r'\*\*(.+?)\*\*',lambda m:stash(r'\textbf{'+inline(m.group(1),lane)+'}'),s)
    s=esc(s)
    for i,v in reversed(list(enumerate(saved))):s=s.replace(f'ZZZTOKEN{i}ZZZ',v)
    return re.sub(r'\(((?:MA|DA|M|D)\d+)\)',lambda m:r'\eqref{eq:'+m.group(1)+'}',s)
def cells(line):
    saved=[]
    def hide(m):saved.append(m.group());return f'CELLTOKEN{len(saved)-1}Z'
    line=re.sub(r'\\\(.*?\\\)',hide,line)
    result=line.strip().strip('|').split('|')
    for i,c in enumerate(result):
        for j,v in enumerate(saved):c=c.replace(f'CELLTOKEN{j}Z',v)
        result[i]=c.strip()
    return result
def convert(md,lane):
    lines=md.splitlines();out=[];i=0;append=False
    while i<len(lines):
        line=lines[i];s=line.strip()
        if not s:out.append('');i+=1;continue
        if s.startswith('\\['):
            block=[line];i+=1
            while i<len(lines) and '\\]' not in block[-1]:block.append(lines[i]);i+=1
            text='\n'.join(block)
            out.append(re.sub(r'\\tag\{([^}]+)\}',lambda m:m.group()+r'\label{eq:'+m.group(1)+'}',text));continue
        if s.startswith('@@TEX@@'):out.append(s[7:]);i+=1;continue
        if s.startswith('## '):
            name=re.sub(r'^\d+\.\s*','',s[3:])
            if name.startswith('Appendix '):
                if not append:out.append(r'\clearpage\appendix');append=True
                name=re.sub(r'^Appendix [A-Z]\.\s*','',name)
            out.append(r'\section{'+inline(name,lane)+'}');i+=1;continue
        if s.startswith('### '):out.append(r'\subsection{'+inline(s[4:],lane)+'}');i+=1;continue
        if s.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=cells(lines[i])
                if not all(re.fullmatch(r'[:\- ]+',c) for c in row):rows.append(row)
                i+=1
            n=len(rows[0]);weights={2:[.32,.68],3:[.25,.37,.38],4:[.25,.24,.27,.24],5:[.10,.21,.23,.23,.23]}.get(n,[1/n]*n)
            spec='@{}'+''.join(r'>{\raggedright\arraybackslash}p{'+f'{w:.4f}'+r'\dimexpr\textwidth-'+str(12*(n-1))+r'pt\relax}' for w in weights)+'@{}'
            out.append(r'\begingroup\small\setlength{\LTpre}{5pt}\setlength{\LTpost}{7pt}'+'\n'+r'\begin{longtable}{'+spec+'}\n'+r'\toprule')
            head=' & '.join(r'\textbf{'+inline(c,lane)+'}' for c in rows[0])+r'\\ \midrule'
            out.extend([head,r'\endfirsthead',head,r'\endhead',r'\bottomrule\endfoot'])
            for row in rows[1:]:out.append(' & '.join(inline(c,lane) for c in row)+r'\\[4pt]')
            out.append(r'\end{longtable}\endgroup');continue
        if s.startswith('!['):
            out.append(r'\begin{figure}[htbp]\centering\includegraphics[width=\textwidth]{figures/TL4_MEASUREMENT_VIEWS.png}\caption{Retained TL4 static views in width-one coordinates: actual shell projections and a separate regular reference hexagon. Surface edges, measurement chords and reference geometry are distinguished by the original labels. Source: TL4, copied byte-for-byte; geometric diagram, not a dynamical simulation. Source hash in the supplement inventory.}\label{fig:tl4}\end{figure}');i+=1;continue
        if s.startswith('- ') or re.match(r'^\d+\.\s',s):
            numbered=bool(re.match(r'^\d+\.\s',s));env='enumerate' if numbered else 'itemize';out.append(r'\begin{'+env+'}')
            while i<len(lines):
                v=lines[i].strip()
                if not v:
                    if i+1<len(lines) and (lines[i+1].strip().startswith('- ') or re.match(r'^\d+\.\s',lines[i+1].strip())):i+=1;continue
                    break
                if numbered and re.match(r'^\d+\.\s',v):out.append(r'\item '+inline(re.sub(r'^\d+\.\s*','',v),lane));i+=1
                elif not numbered and v.startswith('- '):out.append(r'\item '+inline(v[2:],lane));i+=1
                else:break
            out.append(r'\end{'+env+'}');continue
        out.append(inline(line,lane));i+=1
    return '\n'.join(out)

PRE=r"""\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath,amssymb,amsthm,mathtools}
\usepackage[margin=25mm,headheight=16pt]{geometry}
\usepackage{graphicx,booktabs,longtable,array,tabularx}
\usepackage[dvipsnames]{xcolor}
\usepackage{microtype,enumitem,fancyhdr,needspace}
\usepackage[unicode=true,pdfencoding=unicode,colorlinks=true,linkcolor=MidnightBlue,citecolor=MidnightBlue,urlcolor=MidnightBlue]{hyperref}
\usepackage{bookmark}
\setlength{\parskip}{4pt}\setlength{\parindent}{0pt}
\setlength{\emergencystretch}{3em}\setlist{itemsep=2pt,topsep=4pt}
\allowdisplaybreaks[2]
\pagestyle{fancy}\fancyhf{}\fancyhead[L]{\small SHORTTITLE}
\fancyhead[R]{\small Research publication v0.1}\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\newtheorem{theorem}{Theorem}[section]
\hypersetup{pdftitle={TITLE},pdfauthor={Hilmir Fr\'imann Halld\'orsson},pdfsubject={Research publication v0.1}}
\begin{document}
\begin{center}
{\small\color{MidnightBlue} TRI-OCTAGON MATHEMATICAL RESEARCH}\\[7mm]
{\LARGE\bfseries TITLE\par}\vspace{5mm}
{\large Hilmir Frímann Halldórsson}\\[3mm]
Research publication v0.1\\6 October 2026
\end{center}
\begin{abstract}
ABSTRACT
\end{abstract}
\noindent\textbf{Keywords:} KEYWORDS\par
\vspace{3mm}
PRINCIPAL
\clearpage
\begingroup\small\setcounter{tocdepth}{1}\tableofcontents\endgroup
\clearpage
"""
MAB=r"""We give an exact account of the measurement geometry and adopted lens-to-state interface of the Tri-Octagon model. The width-one folded module is enclosed by the minimum centered vertical cylinder of radius \(1/\sqrt3\) and half-height \(1/2\). Its highest measurement ring is distinct from the nonplanar upper rim. Explicit projections separate normal, seam and tangent directions, and distinguish a measurement polygon from a regular reference hexagon. Historical changes of units are separated from fixed-centre changes of construction. For fixed nonzero extraction data, the lens initializer retains only the ratio \(d/r\); its fibres are positive scaling rays. Ratio recovery from amplitude is sharply Lipschitz, while angle recovery at tangency is Hölder. Deterministic vector error and finite-transfer attenuation explain conditioning without restoring absent absolute scale. Conditional enclosing hosts are retained in appendices. The cylinder is a static measurement definition and the oriented lens remains a kinematic interface; neither is assigned a material or rotational law."""
DAB=r"""We explain a nonzero common-phase drift on a locally continued chiral branch of the native Tri-Octagon map. For \((\epsilon,g,\lambda)=h(1,1/6,1/30)\), \(k=(1-\eta,1,1+\eta)\) and \(0\le h\le1/4\), a seven-real-variable bordered system isolates the branch from \(z_j^*=2^{-1/2}e^{2\pi ij/3}\). The extended rate satisfies \(\nu_+=2c_+(h)\eta^3+O(\eta^5)\), with \(c_+(h)=\sqrt3(33h^2-240h+688)/(6(1-3h)^3)>0\). The full state jet, symmetry divisibility and reference determinant give the coefficient proof. Retained interval continuation certifies a finite ladder at four step values, separately from the local analytic theorem. Common-phase-invariant coherences remain stationary, and the nonzero generator rate excludes a specified invariant-potential pure-gradient representation. The reference is a saddle; attraction and physical phase calibration are not established. The result concerns native complex-state dynamics and supplies no spatial rotation law."""
MPR=r"""\textbf{Principal results and hypotheses.}
Lengths use the current octagon width as one. With the fixed centre and vertical axis, \(R_{\min}=1/\sqrt3\), \(H_{\min}=1/2\) (Section 3).
For known fixed \(v\ne0\), \(\Omega_0=Gv\) determines \(q=d/r\), but not \(r\); each fibre is \(\{(r,qr):r>0\}\) (Section 6).
The inverse obeys \(|Q(t_1)-Q(t_2)|\le\pi|t_1-t_2|\), whereas \(\theta(t)\sim(3\pi/4)^{1/3}t^{2/3}\) at tangency (Section 7). If \(v=0\), the whole lens domain collapses.

\textbf{Notation.} \(S\): folded surface; \(o\): centre; \(R,H\): cylinder radius and half-height; \(r,d\): lens radius and separation; \(q=d/r\); \(t=G\): amplitude gain; \(v\): fixed extracted vector. Appendix C gives the full crosswalk. Master labels M1--M38 and MA1--MA9 are retained."""
DPR=r"""\textbf{Principal result and hypotheses.}
All state and prestage components are nonzero on the regular domain.
The reference phase slice retains six real state coordinates and \(\nu\).
The border determinant is \(-(3h-1)^2/1600\); the local branch, cubic coefficient and generator limit follow in Sections 5--8.
Finite certificates cover \(h\in\{0,1/10,1/100,1/1000\}\), \(\eta\in\{\pm1/1000,\pm1/2000,\pm1/4000\}\), with the separately stated control (Section 10).

\textbf{Notation.} \(z\in\mathbb C^3\): state; \(h\): mathematical step scale; \(\eta\): coefficient perturbation; \(\nu\): extended rate; \(\omega=h\nu\): per-step phase; \(\mathcal A\): oriented Vandermonde, with \(\mathcal A(-1,0,1)=2\). At \(h=0\), the extended generator equations select \(\nu\); \(F_0=\mathrm{id}\) does not. Master labels D1--D47 and DA1--DA6 are retained."""
SRG=r"""
\section{Fixed SRG matrices and branch convention}
This transcription specifies the adopted preparation in M22--M23 from the pinned native source. Put \(\zeta_3=e^{2\pi i/3}\), \(f_j=(1,\zeta_3^{-j},\zeta_3^{-2j})^T/\sqrt3\), \(\Pi_0=f_0f_0^\dagger\). In the standard channel basis,
\[
\begin{aligned}
R_s&=q_s I_3+(r_s-q_s)\Pi_0,& C_s&=c_s I_3+(1-c_s)\Pi_0,\\
Z_s&=\operatorname{diag}(1,\zeta_3^{-1},\zeta_3),& A_s&=R_sZ_sC_s .
\end{aligned}
\]
Here \(q_s=e^{-0.423}\), \(r_s=e^{0.577}\), \(c_s=1-0.618=0.382\). With \(\alpha_s=2\pi(0.244)\), \(\beta_s=\pi(0.244)\),
\[
B_s=\begin{pmatrix}e^{-i\alpha_s}&0\\0&e^{i\alpha_s}\end{pmatrix}
\begin{pmatrix}\cos\beta_s&-i\sin\beta_s\\-i\sin\beta_s&\cos\beta_s\end{pmatrix},
\qquad U_s=B_s\otimes A_s .
\]
The tensor order is helicity-major \(\mathbb C^2\otimes\mathbb C^3\).
Set \(\tau_s=\cos\alpha_s\cos\beta_s\), \(b_\pm=\tau_s\pm i\sqrt{1-\tau_s^2}\).
For the named positive\_imag or negative\_imag branch \(b\), define
\[
\Pi_b=\frac{B_s-\overline b I_2}{b-\overline b},\qquad
\chi=\frac{\Pi_b e_p}{\sqrt{(\Pi_b)_{pp}}}.
\]
The pivot \(p\) maximizes the real diagonal of \(\Pi_b\), taking the first index on an exact tie; its component is positive real. Since \(B_s\) is unitary, this is an orthogonal spectral projector and \(\chi^\dagger B_s=b\chi^\dagger\). Input is \(G(\xi\otimes f_0)\); extraction is \(\chi^\dagger\otimes I_3\).
This negative-exponent Fourier basis is the native SRG convention. The companion drift paper's positive-exponent chiral reference is a different object.
Source: pinned \texttt{srg.py}, \texttt{fourier\_basis}, \texttt{fixed\_november\_srg}, \texttt{helicity\_mode}; copied in the native software supplement with the original license scope.
"""
REF=r"""
\begin{thebibliography}{99}
\bibitem{TL} H. F. Halldórsson, TL0--TL4 measurement and lens-interface research checkpoints (2026). Public reports, verifier-source derivatives and retained scientific results in the measurement supplement; original and public hashes in the source inventory.
\bibitem{D0D1} H. F. Halldórsson, D0: Chiral Reference and Reconciliation; D1: Native Chiral Phase Drift, and supplied scientific closeout (2026). Reports and evidence in the drift supplement.
\bibitem{native} Tri-Octagon scientific project, \texttt{kernel\_physics} definitions, pinned revision \texttt{82cab10cbe550f58c43163fb8b05fabdad1b05ae} (2026). Native subset, original software license and scope notice.
\bibitem{NRG} H. F. Halldórsson, \emph{Native Response Geometry and Spectral Circulation in the Tri-Octagon Map}, research publication v0.1 (2026). Prior response classification; manuscript sources in the drift supplement.
\bibitem{PaperA} H. F. Halldórsson, \emph{Cycle-Covering Dynamics of a Three-State Nonlinear Kernel}, Paper A project manuscript v0.5.1 (2026). Inherited recurrence; retained source in the drift supplement.
\bibitem{PaperG} Tri-Octagon research programme, Paper G project record (2026). Prior chirality framework; source locator and status in the supplement.
EXTERNAL
\end{thebibliography}
"""
EXT=r"""
\bibitem{AK} I. S. Aranson and L. Kramer, The world of the complex Ginzburg--Landau equation, \emph{Reviews of Modern Physics} 74 (2002), 99--143. \href{https://doi.org/10.1103/RevModPhys.74.99}{doi:10.1103/RevModPhys.74.99}. \href{https://arxiv.org/abs/cond-mat/0106115}{Author preprint}, Section II.A, equations (7)--(9).
\bibitem{PAL} F. C. Poderoso, J. J. Arenzon and Y. Levin, New ordered phases in a class of generalized XY models, \emph{Physical Review Letters} 106 (2011), 067202. \href{https://doi.org/10.1103/PhysRevLett.106.067202}{doi:10.1103/PhysRevLett.106.067202}. \href{https://arxiv.org/abs/1008.0868}{Author preprint}, equation (1).
\bibitem{Krupa} M. Krupa, Bifurcations of Relative Equilibria, \emph{SIAM Journal on Mathematical Analysis} 21(6) (1990), 1453--1486. \href{https://doi.org/10.1137/0521081}{doi:10.1137/0521081}.
\bibitem{Rump} S. M. Rump, Verification methods: rigorous results using floating-point arithmetic, \emph{Acta Numerica} 19 (2010), 287--449. \href{https://doi.org/10.1017/S096249291000005X}{doi:10.1017/S096249291000005X}. \href{https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf}{Author manuscript}, Sections 1.1--1.4 and 13.1, Theorem 13.3.
"""
def prepare(lane):
    name='MEASUREMENT_GEOMETRY_SYNTHESIS.md' if lane=='measurement' else 'CHIRAL_DRIFT_SYNTHESIS.md'
    original=(ROOT/lane/'supplement/historical'/name).read_text(encoding='utf-8')
    title=original.splitlines()[0][2:];md=original[original.index('## 1.'):]
    if lane=='drift':
        b=md.index('## Appendix B.');e=md.index('## Appendix C.')
        (ROOT/'provenance/drift_correction_record.md').write_text(md[b:e],encoding='utf-8')
        md=md[:b]+'## Appendix B. Scientific corrections and source record\n\nThe determinant placement, reflection action, gradient qualifications and zero-domain restrictions are retained in the arguments above. The original correction table is retained in the provenance record. The public master derivative preserves its scientific content; the raw original remains privately archived. Current receipt of reviewer companions is recorded below.\n\n'+md[e:]
        md=md[:md.index('For future reproduction,')]
        old=re.search(r'The fresh-eyes review compared .*?No new literature audit is used here\.\]',md,re.S).group()
        md=md.replace(old,r'@@TEX@@The real-coefficient variational form in Aranson and Kramer \cite{AK}, Section II.A, provides context for the quartic amplitude/coupling increment. Poderoso, Arenzon and Levin \cite{PAL}, equation (1), gives the familiar harmonic bond-energy form. These structural comparisons identify displayed terms only: neither the continuous Ginzburg--Landau evolution nor the two-dimensional equilibrium phase diagram identifies this split triad map. Ordered explicit increments are not exact gradient-flow time maps; separate coordinate gradients do not establish a common Lyapunov function.')
        md=md.replace('The state is allowed to change by a common phase',r'@@TEX@@Relative equilibria are group-orbit dynamics; Krupa \cite{Krupa} treats this setting for equivariant flows. Here the finite-map equation is defined directly by (D1), and no flow bifurcation theorem is applied to this continuation.'+'\n\nThe state is allowed to change by a common phase',1)
        md=md.replace('D1 uses 110-digit Newton approximations',r'@@TEX@@The distinction between approximation and mathematical verification is standard \cite{Rump}. That reference supplies context for enclosure methods, not an audit of this implementation.'+'\n\nD1 uses 110-digit Newton approximations',1)
        clarification=r"""The normalized \(w\)-coordinate border in (D35) is the original seven-variable border in (D24), expressed in (D31), with residual rows transformed by the inverse state-coordinate map. If \(K\) maps the six real normalized perturbations to the original real state perturbations, the transformed border is \(\operatorname{diag}(K^{-1},1)\mathcal B_h\operatorname{diag}(K,1)\). In D0's already rotating local coordinates \(K=A I_6\); in ambient coordinates it also includes the fixed channel rotations. The rate column becomes \((0,0,0,-1,-1,-1)^T\), and the gauge row becomes \((0,0,0,1/3,1/3,1/3)\). The determinants agree. The invertible residual row rotation in (D34) is the identity at the reference. This is the coordinate form used by D1's derive_jets calculation, not a new isolation theorem.

"""
        md=md.replace('The invertible border (D25)',clarification+'The invertible border (D25)')
        md=md.replace('Original real residual components over the fixed-root boxes are bounded below','Absolute original real residual components over the fixed-root boxes are at most')
        md=md.replace('and identity residuals below','and absolute identity residual components are at most')
        md=md.replace("The supplied GPT closeout's independent-check statements are review attributions, not newly reproduced certificates.","Reviewer companions are now included with verified archival hashes. Their stored outcomes remain retained review evidence, not newly reproduced certificates or an audit of D1's interval implementation.")
        md=md.replace('The next activity authorized here is review of this explanatory text, not D2, new dynamics or publication.','This publication presents the established result; it adds no continuation beyond D1.')
        md=md.replace('No review printout or missing companion check is added','No review printout or reviewer-companion check is added')
        md=md.replace('This consolidation performed only editorial/source checks.','The reviewed master consolidation performed editorial/source checks only; the publication package retains and repeats the bounded portable smoke path documented in the joint build record.')
        fig=r'@@TEX@@\begin{figure}[htbp]\centering\includegraphics[width=.82\textwidth]{figures/coefficient.pdf}\caption{Evaluation of the proved \(c_+(h)\) formula (D3) on \(0\le h\le1/4\). Dots identify the four retained certificate step values; they evaluate the analytic coefficient, not finite-\(\eta\) rates or newly certified fixtures. The axis \(h\) is a mathematical step scale. Figure code and formula samples are supplied.}\label{fig:coefficient}\end{figure}'
        md=md.replace('## 9. Necessary',fig+'\n\n## 9. Necessary')
    else:
        md=md.replace('*Existing TL4 figure, visually inspected for this consolidation and linked without modification.* ','')
        md=md.replace("Absolute local links and the original writers' path assumptions require deliberate packaging before public reproduction; see START_HERE.","Public derivatives replace private locators and omit unrelated operational snapshots. Portable commands, original and public hashes, and their tested scope are documented in the joint README and export map.")
        fig=r'@@TEX@@\begin{figure}[htbp]\centering\includegraphics[width=.88\textwidth]{figures/scaffold.pdf}\caption{Exact coordinate construction in width-one units centered at \(o\): three filled panels (blue) and added static cylinder rings/guides (gold), with \(R=1/\sqrt3\), \(H=1/2\). Cylinder guides are measurement geometry, not shell edges. Equations (M1)--(M11); formula-based rendering, no dynamics.}\label{fig:scaffold}\end{figure}'
        md=md.replace('## 4. Projections',fig+'\n\n## 4. Projections',1)
    body=convert(md,lane)
    if lane=='measurement':
        body=body.replace(r'\textbf{Exact theorem: fibres for fixed data.}',r'\begin{theorem}[Fixed-data fibres]\label{thm:fibres}')
        body=body.replace('An output outside the segment has empty fibre.',r'\end{theorem}'+'\nAn output outside the segment has empty fibre.')
        body+=SRG
    body+=r"""
\section*{Acknowledgments and AI-assistance disclosure}
The author acknowledges assistance from ChatGPT/GPT in scientific review and work-order preparation, and from Codex in explanatory organization, transcription, packaging, typesetting and bounded checks. These contributions do not constitute external peer review or independent certification. Assertions are supported by written arguments and specifically identified evidence.
\section*{Code and evidence availability}
The source project is \url{https://github.com/pzychozen/trioctagon-physics}. Scientific definitions use the unchanged baseline commit \texttt{82cab10cbe550f58c43163fb8b05fabdad1b05ae}.
The planned publication-package location is \path{papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/} in that repository. These final files are prepared; repository publication is pending. The shared package contains two separate papers, their sources, figures and supporting evidence.

The complete extracted package provides the local supplement links used here. Its source inventory and public-export map distinguish unchanged copies from labeled public derivatives, retain both raw-original and public-file hashes, and specify exact operational omissions and locator substitutions. Scientific data are preserved; private raw records remain separately archived.
The joint README documents bounded build and smoke commands using the pinned native subset and unchanged verifier function bodies. Historical writers must not be executed in-place; the active tools use designated output records. Full historical suites and reviewer companion scripts were not regenerated. Retained evidence, prior review receipts and final packaging checks remain separate.
"""
    if lane=='drift':body+=r"""
The five reviewer companion files are included with their received hashes; the original ZIP identity is retained in provenance. They were unavailable during the earlier local closeout; that historical statement is preserved. The scripts and stored outputs are reviewer companions, not an audit of D1's interval verifier. No companion-script replay is claimed here.
"""
    body+=r"""
The software subset retains its original Apache-2.0 license and scope notice. That license is not assigned to manuscripts, research scripts, results or figures. This packaging grants no new redistribution rights and claims no external peer review, journal acceptance or DOI.
"""
    pre=PRE.replace('SHORTTITLE','Measurement geometry' if lane=='measurement' else 'Cubic common-phase drift').replace('TITLE',title).replace('ABSTRACT',MAB if lane=='measurement' else DAB).replace('KEYWORDS','folded geometry; measurement scaffold; lens identifiability; inverse conditioning; SRG preparation' if lane=='measurement' else 'relative equilibrium; equivariant map; chiral branch; implicit series; validated numerics').replace('PRINCIPAL',MPR if lane=='measurement' else DPR)
    if lane=='drift':
        body=body.replace(r'\section*{Code and evidence availability}',r'\clearpage'+'\n'+r'\section*{Code and evidence availability}')
        body+='\n'+r'\clearpage'+'\n'
    text=pre+body+REF.replace('EXTERNAL',EXT if lane=='drift' else '')+'\n\\end{document}\n'
    text=text.replace('border in \\eqref{eq:D24}, expressed','border in \\eqref{eq:D25}, expressed')
    text=text.replace(r'\section{Phase gauge, full border, and the \(h=0\) equations}',r'\section[Phase gauge, full border, and the h=0 equations]{Phase gauge, full border, and the \(h=0\) equations}')
    text=text.replace('(1/2,s/2),(s/2,1/2),(-s/2,1/2),(-1/2,s/2).',r'(1/2,s/2),(s/2,1/2),(-s/2,1/2),(-1/2,s/2).\end{gathered}')
    text=text.replace('(-1/2,-s/2),(-s/2,-1/2),(s/2,-1/2),(1/2,-s/2),',r'\begin{gathered}(-1/2,-s/2),(-s/2,-1/2),(s/2,-1/2),(1/2,-s/2),\\')
    (ROOT/lane/'manuscript.tex').write_text(text,encoding='utf-8')
    tags=re.findall(r'\\tag\{([^}]+)\}',original)
    assert len(tags)==(47 if lane=='measurement' else 53)
    assert set(tags)==set(re.findall(r'\\tag\{([^}]+)\}',text))
    return {t:{'master':t,'manuscript_tag':t,'latex_label':'eq:'+t} for t in tags}
if __name__=='__main__':
    cross={lane:prepare(lane) for lane in ['measurement','drift']}
    (ROOT/'provenance/equation_crosswalk.json').write_text(json.dumps(cross,indent=2)+'\n',encoding='utf-8')
    print('Both sources generated; 47 measurement and 53 drift labels retained.')
