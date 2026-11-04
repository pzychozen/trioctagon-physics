# Document-only rebuild

Use a separate writable copy of this edition with an existing Tectonic executable and populated cache. From the edition root:

```text
python manuscript/build.py --tectonic PATH_TO_EXISTING_TECTONIC
```

On the author's Windows environment, use Command Prompt and `call conda activate torment` first. The portable standard-library helper has no project imports or scientific execution. It uses `--only-cached --untrusted`, no TeX shell escape, automatic package fetching or installation. It writes intermediates under build/ and emits [RECIPROCAL_CHIRAL_EXCHANGE_v0.1.pdf](RECIPROCAL_CHIRAL_EXCHANGE_v0.1.pdf). The fixed source epoch is the actual edition date, 3 November 2026 UTC. Byte reproduction also depends on matching cached TeX/fonts/compiler; font files are not redistributed, while PDF fonts are embedded.

With existing Poppler, create a render directory and run:

```text
pdftoppm -r 125 -png RECIPROCAL_CHIRAL_EXCHANGE_v0.1.pdf renders/page
```

Inspect every page after any rebuild. This final 15-page artifact passed [document checks](verification/DOCUMENT_CHECKS.json), [fidelity review](verification/FIDELITY_REVIEW.md) and [visual inspection](verification/VISUAL_INSPECTION.json). The [build receipt](verification/BUILD_RECEIPT.json) and final normalized compiler log record the document build; raw paths/logs and renders are retained externally. Historical scientific helpers in evidence are not build dependencies and were not rerun.
