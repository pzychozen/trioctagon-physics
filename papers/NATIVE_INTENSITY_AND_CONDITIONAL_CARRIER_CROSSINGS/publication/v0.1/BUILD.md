# Portable document rebuild

Use a separate writable copy of this edition with an existing Tectonic installation and populated cache. From the edition root:

```text
python manuscript/build.py --tectonic PATH_TO_EXISTING_TECTONIC
```

The helper uses `--only-cached --untrusted`, writes temporary files under `build/`, and emits `NATIVE_INTENSITY_CARRIER_CROSSINGS_v0.1.pdf`. It imports only the standard library. It performs no network TeX fetching, shell escape, installation or scientific execution. The fixed build epoch is 2 November 2026 UTC. Fonts are obtained from the existing environment and embedded; no font files are distributed. Tectonic 0.17.0 was used for this edition. Exact byte reproduction also depends on the same cached resource/font/tool versions.

For visual review with existing Poppler, create a `renders` directory, then run:

```text
pdftoppm -r 115 -png NATIVE_INTENSITY_CARRIER_CROSSINGS_v0.1.pdf renders/page
```

Inspect every output page. Metadata, embedded fonts, labels, citation resolution and navigation were checked with existing pypdf/Poppler tools during publication. Build logs in `verification/` have preparation-machine paths normalized; the external closeout retains the raw build record. Scientific evidence helpers are not build dependencies and must not be run merely to typeset the note.
