# Evidence summary

SRG Amplitude Equality: Conditional Persistence and Minimal Splitting in Tower II — v0.1.

Accepted analyses and pending manuscript review are distinct. These counts describe saved historical results; none was rerun:

- OC05_TOWER_STATE_PERSISTENCE_01: 9 executed groups, 9 passing in the accepted final JSON.
- OC07_TOWER_TWO_BAND_SPLIT_01: 8 executed groups, 8 passing in the accepted final JSON.

Analytic proofs carry the conclusions. Saved arbitrary-precision decimals corroborate them; they are not interval certificates or source floating-point certification. New work is limited to transcription, static source/formula correspondence, identity, references, compilation, rendering and artifact review.

| Saved field | Accepted check group | Rounded manuscript value | Location |
|---|---|---|---|
| OC05: output_difference | same_clock_counterexample_scalars | 0.002058402961068474 | §1; (4.4) |
| OC07: values.eta_star | single_clock_scalar_corroboration | 0.001323940975761039 | §5 table |
| OC07: values.common_enhanced_increment | single_clock_scalar_corroboration | 0.000272714173360112 | §5 table |
| OC07: values.output_low | single_clock_scalar_corroboration | 0.207931904558321191 | §5 table |
| OC07: values.output_high | single_clock_scalar_corroboration | 0.208317773395512482 | §5 table |
| OC07: values.compressed_gap | single_clock_scalar_corroboration | 0.000385868837191291 | §5 table |

Rounding: 18 decimal places, Decimal ROUND_HALF_EVEN, applied only to saved strings. Full strings and locators are in private NUMERICAL_TRANSCRIPTION_QA.json. No sine, exp, tanh, inverse solve, source step or accepted checker was evaluated.

## OC05 preserved correction history

The initial comparison used 0.002058402961068466. The corrected accepted saved value begins 0.0020584029610684738530430701485, hence the manuscript rounds it to 0.002058402961068474. The initial record has 6 groups: 5 passing and 1 failed. The accepted final record has 9 passing groups and explicitly retains CORRECTION_REQUIRED_AT_DISPLAYED_PRECISION for that earlier quote. This is correction provenance, not an unresolved final theorem failure. Both audit files and every accepted final deliverable remain unchanged. Their identities are recorded privately; raw audit files are excluded from public payload and review transport.

## Limits

Conditional equality does not prove indefinite activity or scalar constancy. The geometric and frequency mechanisms have distinct minimality hypotheses. Neither is a rollout, later OC04 pass, full-state capture or general memory-recovery result.
