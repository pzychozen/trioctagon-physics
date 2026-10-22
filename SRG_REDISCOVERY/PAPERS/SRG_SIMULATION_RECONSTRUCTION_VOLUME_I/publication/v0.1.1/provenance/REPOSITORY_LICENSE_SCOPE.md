# Apache-2.0 software distribution scope

The standard unmodified Apache License 2.0 in LICENSE applies to the approved
software distribution of trioctagon-physics. It is not a blanket license for
this repository or for scientific material stored alongside the software.

## Covered software

- The distributed top-level kernel_physics runtime/software .py modules,
  including internal modules; licensing does not change public API support.
- pyproject.toml and _build_backend.py: package metadata and build tooling.
- tools/verify_distribution.py: distribution verification tooling.
- kernel_physics/tests/test_distribution_provenance.py: software distribution
  regression tests, not a grant covering other tests or their evidence.
- kernel_physics/requirements.txt: software dependency declarations.
- kernel_physics/README.md insofar as distributed software/install/use
  documentation.
- Software distribution metadata and generated distribution provenance metadata.

The wheel and minimal sdist contain only this software-distribution scope and
the accompanying license and scope notice. The Apache-2.0 SPDX expression in
distribution metadata describes those archives, not every repository artifact.

## Not automatically covered

No Apache-2.0 license is inferred for papers/, research/, research datasets,
figures, publication manuscripts, Twisted Hex Crystal research, parity
fixtures/evidence datasets, golden_388, Paper-F support datasets, historical
scientific/publication artifacts, or other scientific/publication material.
These exclusions apply regardless of where material is stored, including
fixtures beneath kernel_physics/tests/.

Excluded material retains its existing licensing/publication status. A
specific file or directory may be governed by a separate explicit license
notice if one exists or is authorized later. This notice does not alter those
materials or their status and does not modify the Apache license text.
