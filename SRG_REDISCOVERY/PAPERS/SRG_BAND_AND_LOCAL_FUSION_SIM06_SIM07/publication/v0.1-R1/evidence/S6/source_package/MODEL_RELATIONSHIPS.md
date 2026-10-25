# Relationships and the remaining reconstruction boundary

Tower II has now been described independently, using its own source and one existing record. The comparisons below identify actual code differences. They do not attribute a behavioral difference to one change without a suitable controlled comparison, and they do not establish invention order.

For SIM04 and SIM05, the accepted Volume II account is retained as [context/Volume_II_manuscript.tex](context/Volume_II_manuscript.tex), especially its construction sections, comparison table at lines 440–459 and source map at 473–500. Relevant unchanged source portions were read from [srg_seed_explorer.py](context/srg_seed_explorer.py) and [srg_infinity.py](context/srg_infinity.py). That published volume and its accepted science were not modified or reopened.

## Mechanisms shared and changed

| Mechanism | SIM04 Seed Explorer | SIM05 Infinity | Tower II selected setting |
|---|---|---|---|
| Changing arrays | X, one real R; diagnostic V | X, real R and second real D; diagnostic V | X, one real R; diagnostic V; permanently assigned bands/frequencies |
| Local geometry | Directed five-neighbor graph rebuilt from incoming X | Same basic selection | Same selected selection, plus optional horizon branch outside this selected setting |
| Local movement | .05 lap + .15 tanh(lap) | Same | Same |
| Exchange weights | Inverse distance, normalized | Same, separate mixing strengths .15 for R and .075 for D | Inverse distance multiplied by exp(−width log-frequency-ratio²), normalized; raw-sum guard |
| Additional coupling | No band-targeted additions | Symmetric R↔D cross terms, scheduled coefficient with literal .08699 | Four supplied phi-ratio targets and supplied sum/difference match additions; no D field |
| Assigned frequency sine | Common .244 sine applied to R after fusion, amplitude −.001 | Same post-fusion R sine plus separate cross-field angular convention | Per-point assigned omega sine before additive mixing and H, amplitude +.01 |
| H | Common R modulation; sampled normalization recomputed on [0,10p] | Fixed H_max, H(p) for R and H(p+pi/2) for D | Fixed H_max, H(p) for R |
| Fusion | One global center, weights abs(pre-fusion R)+1e−8, signed .03 R displacement | Same global-center construction; D affects R upstream | One center per fixed band, signed .02 Q displacement; graph/horizon does not restrict it |
| Resonance bound | Signed RPCO, L=9 | Signed RPCO on R and D, L=9 | Same signed map on R; optional incoming-R-dependent L, enabled here |
| Noise | Positional standard deviation .01 | .01/(1+.01p) | Same decreasing scale; initialization's band shuffle changes RNG consumption |
| Velocity and space | V records displacement; no wrapping | Same | Same; no velocity friction/inertial recurrence |

Exact source support: SIM04 60–89,91–124,139–178; Infinity 70–137,162–205; Tower II 62–216. These implement shared operations with consequential differences in staging and scope. Similar names or constants do not make the entire programs equivalent. Infinity's five final replay groups and Tower II's three local components before its 600th update come from different configurations and durations; that is not a controlled experiment identifying the cause of the difference.

## Remaining March variants: bounded source map

The following entries use the earlier R0 recovery's explicit source map, [R0 report lines 220–227](context/SRG_R0_REPORT.md), rather than opening separate investigations. Complete-original locators and hashes are retained in [R0's source inventory](context/R0/external_and_selected_sources.json).

| Variant and exact source range recorded by R0 | Demonstrable construction distinction | What this study covers / leaves open |
|---|---|---|
| `srg_golden_tower.py`, `GoldenTowerField`, 50–190 | Random independent band assignments instead of balanced shuffled allocation; fixed L; one phi-ratio addition +.001 exp(−10[log(w_i/w_j)−log(phi)]²)R_j for differing frequencies; no horizon/breathing. Stored freq_amplitude=1 is unused. | Tower II's walkthrough covers the common sequence and distinguishes this narrower rule. It does not reproduce Tower I or transfer its outcomes. |
| `srg_condensate_breaking.py`, `GlyphFieldUniverse`, 60–203 | Optional assigned frequencies, raw squared-frequency-difference kernel rather than log ratio; no explicit mixing additions. Optional L=9[1+.3 sin(2pi .244 p)exp(−.01p)] is a prescribed schedule. Horizon-enabled fusion uses local centers and current in-place positions; no-horizon branch uses one global center. | The local, order-sensitive fusion differs from Tower II's once-computed band centers. Its exact spatial isolation and movement cannot be read off this Tower II path. |
| `srg_breathing_collision.py`, `BreathingField`, 63–174 | Balanced bands, algebraically recalculated L, no additional mixing terms; band fusion and noise remain. R_trace is allocated but not appended; L_trace and mean-R trace read the incoming state. | Basic single-field update largely represented by this construction map, with the removed mixing explicitly noted. Not proof that its saved outputs match Tower II. |
| Same file, `merge_fields`, 181–198 | Constructs a field (consuming RNG), then concatenates supplied states; adopts max(input clocks), averages stored L and may restore default coupling width. The next update overwrites averaged L from merged R. | This is a genuine composition/initialization and clock issue, not a new independent breathing phase. No merged field was constructed here. |

These distinctions should be preserved even if later comparisons show similar pictures. In particular, common words such as “horizon,” “memory” and “breathing” refer to different operations across files.

## Construction-history map

| Implementation | Shared or changed construction | Dated statements / intended idea actually available | Attributable saved evidence used here | Chronology or causal claim still unresolved |
|---|---|---|---|---|
| Seed Explorer | Geometry-dependent local exchange, one-center fusion, signed bound | Original header names Claude collaborating with pzychozen, 2026-03-14; accepted Volume II reports this as source attribution | Accepted study of original 21 boundaries in deep_trajectory.csv and metrics, summarized in Volume II; no new SIM04 analysis | Header date is not a run certificate or proof that this file was invented before the others |
| Infinity | Adds second real channel/cross terms; modifies schedules and noise | Same header attribution/date; source comments call D a phase-orthogonal mirror field (77–79), while actual state is real | Historical aggregate CSV plus accepted 200-pass full replay; Volume II's evidence distinctions retained | Physical dark-field interpretation and unique development succession are not established |
| Tower I | Assigned frequency bands and targeted mixing | R0 places the source in the March 14 group and inventories The_Golden_Tower.md; no additional intent claim is inferred here | R0 inventories tower_height.csv and source/narrative. These are navigation references, not freshly validated outcomes in this package | Name “I” or shared functions do not establish the date/order of invention relative to Infinity or Universe |
| Tower II | Enhanced additions, optional algebraic bound and horizon, same-band fusion | Original header 2026-03-14 (S:7–17) explicitly asks about lock predictions, breathing, new bands and tunneling. Original note lines 28–38 describes a response to an earlier decaying-bound attempt | Seven-row original breathing CSV; selected matched-configuration R1 record; retained R1/R2/R3 analysis with status qualifiers | The note's “previous attempt” is a dated narrative claim, not a proven code lineage. Self-sustaining oscillation and zeta-controlled coupling are not established by this program |
| Universe/condensate | Local in-place fusion option and externally scheduled bound | R0 March grouping and code-option map are available; distinct intended experiment names survive in its inventory | R0 inventories causal_horizons.csv, condensate_perturbation.csv, full_universe.csv and a companion narrative. None is promoted to a new verified SIM06 outcome | Whether its horizon/local-fusion branch caused a particular historical observation needs source-output-specific work, if commissioned |
| BreathingField/collision | Simplified band engine plus composition utility | R0 inventories The_Breathing_Collision.md and the March source; a “phase” filename does not establish an independently carried L phase | R0 inventories breathing_phase_collision.csv, phase_locked_merger.csv, heartbeat_fingerprints.csv and related tables. No fresh attribution or control analysis here | Which setup, constructor RNG effects, clock selection and parameter inheritance explain an alleged collision/phase effect remains outside this study |

The retained inventory records source bytes and former archive locators; it does not certify when the historical author executed each file. R0's report dates, later R1/R2/R3 execution dates and SIM06 review order likewise do not establish the original invention chronology. A comment describing intent is preserved as a comment even when the equations fail to implement its interpretation.

## Recommendation after this checkpoint

**Do not open every remaining March file automatically.** Tower I and the single-field BreathingField recurrence are adequately distinguished for the present construction account; they need not be reconstructed again merely because their filenames remain on a list. They are not thereby declared behaviorally equivalent or historically exhausted.

There are two materially different unresolved constructions: Universe/condensate's local in-place fusion, and BreathingField's merger with clock/RNG/configuration inheritance. They justify a future focused source-and-existing-evidence decision if GPT and Hilmir want to resolve those historical claims. The present evidence does not authorize a new run or prove either claimed mechanism's outcome. No next engine, control, theorem work order, manuscript or Volume III has been started.
