"""Render numerical evidence by method, preserving unrounded originals in JSON."""
from pathlib import Path
import json
L=Path(__file__).resolve().parents[1]
D={k:v['verification'] for k,v in json.loads((L/'verification/retained_evidence.json').read_text(encoding='utf8')).items()}
def num(v):
    if float(v)==0:return '0'
    a,b=f'{float(v):.5e}'.split('e')
    return r'\('+a+r'\times10^{'+str(int(b))+r'}\)'
def table(headers,rows,widths=None):
    cols=widths or ('l'+'r'*(len(headers)-1))
    return '\n'.join([r'\begin{center}\begin{tabular}{@{}'+cols+r'@{}}',r'\toprule',' & '.join(headers)+r'\\\midrule',*[' & '.join(map(str,row))+r'\\' for row in rows],r'\bottomrule\end{tabular}\end{center}'])
out=[r'''The complete measurements, including every stored high-precision digit and
all exact rational fixtures, are retained in \texttt{retained\_evidence.json}.
The following tables round values for print only. Maxima below compare like
quantities within a stated checkpoint, never across error types. The 429
retained exact/source predicates are enumerated separately; none is replaced
by these residuals. Paper-local checks are an additional bounded algebra and
reference audit, with their own machine-readable result.

\subsection*{Native complex128 finite differences}
For GR0 the error is the maximum entrywise error of the complete real
Jacobian. For GR1 it is separated into phase and radial blocks; for GR2 only
phase response was tested. These are different quantities.''']
rows=[]
for q in D['GR0']['numerical_groups'][1:]:
    for row in q['native_central_difference']:
        rows.append([q['name'].split()[0],num(row['difference_step']),num(row['max_abs_error'])])
out.append(table(['GR0 ring','Step','Complete Jacobian error'],rows))
rows=[]
for q in D['GR1']['native_complex128_checks']:
    for row in q['finite_differences']:rows.append([q['N'],num(row['h']),num(row['phase_max_error']),num(row['radial_max_error'])])
out.append(table(['GR1 N','Step','Phase error','Radial error'],rows))
out.append(table(['GR2 N','Step','Phase error'],[[q['N'],num(q['phase_increment']),num(q['finite_difference_max_error'])] for q in D['GR2']['native_response_checks']]))
out.append(r'''GR0 uses \(\eps=1/20,g=1/5,\lambda=1/1000\), with
\((k,\chi)=(1,0)\) on C3 and \((4,\pi/7)\) on C12. GR1/GR2 use the
weak positive branch at \(k=1,\kappa=(-1,0,1),\eta=.01\) and the same
parameters. Native fixed residuals are zero in GR0, and at most
\(1.11023\times10^{-16}\) in the two GR1 tests.
GR0's native frame/transport comparison and potential comparison each give
\(1.11023\times10^{-16}\), as two separate quantities.

\subsection*{100-digit transcription finite differences}
These checks use the mathematical transcription with mpmath, not a
100-digit execution of the complex128 native kernel.''')
rows=[]
for q in D['GR0']['numerical_groups'][1:]:
    for row in q['mpmath_100_digit_central_difference']:rows.append(['GR0 '+q['name'].split()[0],num(row['difference_step']),num(row['max_abs_error'])])
for row in D['GR1']['high_precision_phase_differences']:rows.append(['GR1 phase',num(row['h']),num(row['maximum_error'])])
out.append(table(['Method/domain','Step','Maximum error'],rows))
out.append(r'\subsection*{Weak-branch residuals and asymptotic coefficients}')
out.append(table([r'\(\eta\)',r'\(\|r-r_0-\eta u\|_\infty/\eta^2\)',r'\(\mathcal C_{\rm cyc}/\eta^3\)'],[[q['eta'],num(q['first_order_error_over_eta_squared']),num(q['cycle_over_eta_cubed'])] for q in D['GR1']['weak_branch_samples']]))
for key,label in [('fixed_residual','GR1 fixed-equation residual'),('cycle_factorization_error','GR1 cycle-factorization error'),('pre_sync_balance_residual','GR1 pre-stage balance residual')]:
    out.append(label+' has maximum '+num(max(float(q[key]) for q in D['GR1']['weak_branch_samples']))+'.')
out.append(r'The proved leading cycle coefficient is '+num(D['GR1']['weak_branch_samples'][0]['cycle_leading_coefficient'])+'.')
rows=[]
for q in D['GR2']['GR1_weak_family']:
    block=q['blocks'][2]
    rows.append([q['eta'],num(q['triad_transverse_discriminant_over_eta_squared']),num(block['maximum_imaginary_part']),num(block['maximum_imaginary_part_over_eta_cubed'])])
out.append(table([r'\(\eta\)',r'\(\mathcal D_3/\eta^2\)',r'\(\max|\im\rho|,\ z=i\)',r'\(\max|\im\rho|/\eta^3\)'],rows))
out.append('GR2 fixed-equation residual has maximum '+num(max(float(q['fixed_equation_residual']) for q in D['GR2']['GR1_weak_family']))+'.')
out.append('GR2 characteristic residual has maximum '+num(max(float(b['maximum_characteristic_residual']) for q in D['GR2']['GR1_weak_family'] for b in q['blocks']))+'.')
metric=D['GR2']['constructed_triad_SPD_metric']
out.append('The constructed triad SPD matrix has minimum eigenvalue '+num(metric['minimum_eigenvalue'])+', balance residual '+num(metric['balance_residual'])+', and a simultaneous nonzero cycle obstruction '+num(metric['triad_cycle_obstruction'])+'. Its complete entries and all block eigenvalues are retained separately. These 100-digit quantities resolve the small imaginary parts; the native finite-difference residuals alone would not certify them.')
out.append(r'\subsection*{Observable, quotient and preparation evidence}')
out.append(table(['CM0 observable derivative','Step','Maximum over 12 observables'],[[q['background'].replace('_',' '),num(q['increment']),num(q['all_12_observable_derivatives_max_error'])] for q in D['CM0']['numerical_checks'][:2]]))
out.append('The separate CM0 partial-zero chirality formula error is '+num(D['CM0']['numerical_checks'][2]['maximum_error'])+'. The native decoder identity passed as a Boolean check, with no numerical residual invented.')
out.append(table(['SA0 identity','Residual','Tolerance'],[[q['name'].replace('Hermitian Gram','Complex coherence'),num(q['residual']),num(q['tolerance'])] for q in D['SA0']['numerical_checks']],r'p{.52\linewidth}rr'))
out.append('The SA0 zero-stratum real-Gram output gap is '+num(D['SA0']['zero_stratum_numerical_gap'])+'. It is a nonclosure signal, not an approximation error.')
out.append(r'''\paragraph{Separation of evidence classes.}
Exact rational signs at the six-ring unfolding, integer symmetry dimensions,
and source-dependency predicates belong to the retained exact inventory.
Finite differences, nonlinear equation residuals, eigenvalue residuals,
constructed-metric residuals and quotient comparisons are numerical evidence.
The written proofs in the main text do not depend on interpreting one type
of measurement as another.''')
(L/'manuscript/evidence_tables.tex').write_text('\n\n'.join(out)+'\n',encoding='utf8')
selected={k:{name:value for name,value in v.items() if name in ['numerical_groups','weak_branch_samples','high_precision_phase_differences','native_complex128_checks','GR1_weak_family','constructed_triad_SPD_metric','native_response_checks','numerical_checks','zero_stratum_numerical_gap']} for k,v in D.items()}
md=['# Retained numerical evidence\n','These are unchanged predecessor measurements, not new runs. Native complex128, 100-digit transcription finite differences, equation residuals, spectral quantities and quotient comparisons remain distinct. All stored digits are retained below; printed tables are rounded. See retained_evidence.json for exact fixtures and predicate records.\n']
for k,v in selected.items():md.extend(['## '+k+'\n','```json\n'+json.dumps(v,indent=2)+'\n```\n'])
(L/'verification/NUMERICAL_EVIDENCE.md').write_text('\n'.join(md),encoding='utf8')
print('Rendered separate numerical tables and complete measurement record.')
