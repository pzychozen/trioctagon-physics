# Known limitations of the unchanged BOUNDARY-12 prototype

## V01: custom-radius lower-bound roundoff

The original HTML is retained byte-for-byte. The subsequent internal GPT review, section 5, records this pure-evaluator input:

```javascript
boundary12Geometry(data, {mode: 'R', value: data.geometry.rho, w: 1, unit: 'width'})
```

It reports `ell_over_w = -2.220446049250313e-16` without an exact-event tag. Floating conversion at the stored lower-bound radius produces a small negative extension; the mathematical domain is ell >= 0. The explicit Original preset is correct. This does not revise any accepted exact event, length, graph or hull. It is a known engineering issue to address before live integration under separate authorization. No patch, tolerance snapping or new browser test was performed for this manuscript.

Reproduction reference: [complete BOUNDARY-12 review](../reviews/boundary12/BOUNDARY12_GPT_SCIENTIFIC_REVIEW.md), section 5, and its unchanged reviewer test sources. These are records, not instructions to run a new test in Stage A.

Codex's original browser QA and screenshots are inherited evidence. GPT's independent browser navigation was blocked before page code loaded. The current manuscript preparation adds no browser-control certification. Export-download destination workflow and separately automated mouse drag were not certified by the original Codex QA. On invalid input the last valid drawing can remain with an error and disabled export.

Download the HTML and open the downloaded file in a WebGL-capable browser. It embeds Plotly, math and data. A GitHub file-page link is access to the file, not a claim of hosted interactive rendering. No network or live application connection is required by the file itself.

## Plotly licence accompanying the prototype

Keep [PLOTLY_LICENSE.txt](PLOTLY_LICENSE.txt) with the downloaded HTML when copying or redistributing the prototype. This is the full upstream MIT licence for its embedded Plotly 3.1.0 code and the same library retained at `../accepted/boundary11/assets/plotly-3.1.0.min.js`. The HTML, vendor bundle and their existing notices remain unchanged. This notice does not grant rights over the scientific content.
