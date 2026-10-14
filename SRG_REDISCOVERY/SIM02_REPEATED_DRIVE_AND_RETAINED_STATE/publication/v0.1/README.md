# Repeated Driving and Retained State in Early SRG Motion

**A Bounded Paired Continuation of Historical Engine C · SIM02 paper v0.1 · 14 October 2026**

What returns when a driving waveform repeats but the state keeps evolving? This paper follows eight labeled centers in the unchanged historical SRG engine C. Two arms inherit the same accepted 200-update prefix and complete RNG checkpoint, then each add 800 updates. CONTINUOUS increases the supplied frame; REPEATED cycles through frames 0–199 while carrying positions, velocities, binary signs and RNG state forward.

Read the **[paper PDF](SRG_SIM02_REPEATED_DRIVING_AND_RETAINED_STATE_v0.1.pdf)** or its **[editable LaTeX source](SRG_SIM02_REPEATED_DRIVING_AND_RETAINED_STATE_v0.1.tex)**. The six figures are included unchanged under plots/.

REPEATED renews substantial speed pulses: its four new block-average speeds remain about 0.10, while CONTINUOUS's block means decrease from 0.008812 to 0.002106. The repeated drive does not reproduce the tested same-phase labeled state. Positions and velocities diverge between arms at S_201, before the first new toggle at update 202 / S_203. Nevertheless, both arms consume identical draw values at identical update/center assignments and retain identical bit histories. These conclusions and their distinct provenance are traced in the [claim-source map](CLAIM_SOURCE_MAP.csv).

![Accepted mean-speed comparison](plots/01_mean_speed.png)

The shaded first block is inherited once and shared by both views; the later four blocks are new. Speed is measured after the update. Repeated input amplitude can renew forcing without establishing learned memory, a memory advantage, statistical superiority or an asymptotic attractor. The paper explains the unchanged sequential operator and the reviewer's pre-damping increment identity within those limits.

The completed [accepted report](SIM02_REPORT.md) and the separate [GPT scientific review](review/SIM02_GPT_SCIENTIFIC_REVIEW.md) are preserved byte-for-byte. GPT's [additional readout](review/ADDITIONAL_READOUTS.json) supplies the first-toggle observation; it was a saved-data observation, not another experiment. The [review results](review/INDEPENDENT_REVIEW_RESULTS.json) distinguish saved-transition and RNG verification from the original 1,604-call execution.

This is a curated research edition. The [access and evidence map](ACCESS_AND_EVIDENCE_MAP.md) identifies its numerical records, source hierarchy, omitted local operational files and original checker-layout requirements. [PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) covers this edition except itself. The [disposition](PUBLICATION_DISPOSITION.md) records authorship, internal acceptance, rights and the separate manuscript/publication gate. Preparation added no simulation or scientific checker run.
