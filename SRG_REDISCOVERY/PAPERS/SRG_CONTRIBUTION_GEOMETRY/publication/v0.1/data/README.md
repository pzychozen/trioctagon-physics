# Exact PH04 tables — reader guide

This proposed supplement belongs to **SRG Contribution Geometry v0.1** (13 October 2026). SRG_PH04_EXACT_TABLES_v0.1.zip contains exactly seven accepted PH04 JSON files, at its root, with original bytes. No scientific output was recomputed or normalized for this edition.

## Schema and authority

| Member | Top-level structure and purpose |
|---|---|
| constant_certificates.json | Methods and common accuracy target; scan precisions; exact bounds; digit_floor_certificates; accelerated-zeta term/tail records and saved finite helper comparisons. |
| profiles.json | schedule, primary, control, and profiles list. Each profile retains id, product, precision, representation, radix, factor labels/digit arrays/truncations, coefficients, exact weights and finite product. |
| pairs.json | display_metadata and complete rows. Row IDs carry product/precision/representation/depth; fields include lag, coefficients,a,b,R,X,H2,x,y2, symbolic/display values, subtotal/support, zero status and prefix status. |
| triples_and_blocks.json | tables list, each identified by profile, with positive triples and positive_blocks. Triples retain depths, exact scale squared, logarithm argument/sign and rational matrix entries. |
| ranked_summaries.json | 57 named product/precision/representation/lag/certification groups with full positive rankings, exact-tie competition ranks and declared threshold/zero counts. |
| anchor_carries_and_terms.json | elementary_carries(all51 q values), full_d4_carry_trace_reused, and selected_labelled_breakdowns with nonzero and zero digit-product terms. |
| findings.json | Exact anchor, next pair, d2 anchor, minimal prefix, nearest legal state, auxiliary balance, certified Q64 rank population, full-carry accounting, global-peak evidence and zero-tail witnesses. |

Integer values and exact rational strings such as "762/3125" or "0" govern algebra and comparison. Root/log display strings are retained approximations, produced in PH04 at 100 working decimal places and 24 significant digits. H2 and y2 are squared exact quantities; they must not be read as H and y. Symbolic strings describe roots/logarithms, not executable source.

JSON null means undefined, never an ordinary infinity. For a double-zero pair normalization and rho are undefined. A single-zero endpoint has normalized geometry but no finite logarithmic coordinate. Positive-block identities stop at zeros.

The factors are explicitly labelled pi,e,phi,gamma for Q and the first three for P. Gamma is defined from the exact master product then independently truncated. Coefficient dictionary keys are arithmetic depths, not time steps. Multi-index convolution is specified by manuscript(8); the factor arrays and selected anchor term breakdowns retain factor provenance without a huge duplicate tuple dump.

## Scope and populations

Q precisions are 2,4,6,8,12,20,32,64; Q raw pairs have lags1,2,3 and Q carried pairs lag1. P64 is a separate adjacent-only raw control. Raw rows retain zero coefficients and allocated finite tails. Integer parts are preserved.

The status certified_full_raw_pair applies when the pair lies inside the sufficient certified raw prefix. The status finite_raw_tail is an exact pair for the finite product, with no automatic full-profile guarantee. The status finite_carried_output_no_raw_prefix_guarantee identifies canonical output of the finite product; the raw-prefix theorem does not apply to it.

Rankings use exact rational |x| on positive pairs, retaining exact ties. Fixed thresholds are1/1000,1/100,1/20. Support is (a+b)/Q_d or (a+b)/P_d for the stated product; it is not normalized by an assumed exact zeta value. Populations, precision copies and overlapping pairs are not independent samples. The anchor's rank1/62 concerns certified positive adjacent Q64 pairs, not all infinite depths.

## Retained original report locators

Frozen strings such as "REPORT.md section6" refer to the accepted private **PH04 report**, not a missing renamed public file. Its identity is in the source index. This map supplies public manuscript locations without changing those JSON bytes.

| Original PH04 report locator | This manuscript v0.1 |
|---|---|
| §1, pair geometry and exact values | §§1–1.1 pp1–2, equations(1)–(6), Table1 |
| §2, elementary carry | §4 p5, equations(14)–(17), Proposition4.1, Figure1 p6 |
| §2, reciprocal action | §4.1 p7, equations(18)–(19) |
| §2, full canonical carry | §4.2 p8, Table2, equations(20)–(21); zero domains§4.3 |
| §3, product and convolution | §2 p3, equations(7)–(10) |
| §3, exact prefix | §3 p4, Theorem3.1, equations(11)–(13) |
| §4, neighboring-pair transition and blocks | §§5–5.1 pp9–10, equations(22)–(29) |
| §5, finite scan and rankings | §§7–7.2 pp12–16, Tables3–5 and Figures2–4 |
| §6, constant certification | AppendixA p17, equations(37)–(40) |
| §6, accelerated zeta helper | AppendixB p18, equations(41)–(45) |
| §7, global raw maximum and canonical bound | §6 p11, Theorems6.1–6.2, equations(30)–(33) |
| §7, opposite eta signs | §5.1 p10, equations(26),(28)–(29) |
| §8, conditional interpretation and open question | §8 p16, equations(35)–(36); AppendixC p19 |

Saved origin strings identifying PH02 or its carry trace still refer to those earlier accepted records, as listed in SOURCE_INDEX.md. They are provenance, not runtime dependencies. PH02's source JSON exact_product was a nested object; PH04's first reader invocation accidentally passed that object to Fraction. The corrected reader selected its exact scalar field. PH04's final profile schema above is separately described by its actual fields. This recorded format error is not a mathematical counterexample; failed/final scripts and execution evidence remain private and were not rerun.

No licence is assigned or expanded by this packaging. The archive is the single proposed public copy of these seven accepted data files. The private nested-member manifest verifies exact membership, CRC, byte sizes and SHA-256 against acceptance identities.
