# H6B conformance and local admission

Run the full Windows certification from the conda torment interpreter:

```bat
python -I -B historical_kernel/tools/certify_distribution.py --source . --workspace C:\path\outside-checkout\h6b-certification
```

The workspace must be new and outside the checkout. `--precommit` marks uncommitted
candidate evidence with a null source revision and an exact content manifest.
CI never uses that option. It certifies the checked-out committed HEAD and retains
the exact wheel and external evidence. The source checkout is verified unchanged.

Acquisition reuses the unchanged hashed Core dependency lock and pinned current
comparison wheel. The exact accepted H6A/analysis wheels are acquired from the
H6A artifact with independent ZIP and wheel pins. Core regressions run in a separate
environment containing the current kernel. Historical science runs in an isolated
environment with no current, old or production package installed. No acquisition
occurs inside Historical computation.

Certification checks wheel contents and every RECORD digest against the copied
source; source and installed tests; static import allowlists; runtime import denial;
the exact narrow generic transitive Core closure; and an installed-removal negative
control. Removing the Historical package must cause the scientific tests to fail
with ModuleNotFoundError. It is restored immediately. Tests are never satisfied
by the checkout in the installed lane.

Frozen H2 fixtures cover 39 of 91 one-step cases and 640 of 1,280 trajectory steps.
The remainder have parameters outside H4 and remain comparison-only. Independent
processes export Historical and current tokens; a third process compares inert
outputs, including signed zero, q/t, staged and EMA readouts and memory. An unexpected
difference writes the first witness and stops certification before admission.

Expected divergence tests cover canonical zero, constructor zero, K versus H,
strict response refusal and naive-chart underflow. N28 instruments both cubic J
and advancement entry points. N30 instruments abs/square/sum and substitutes the
basis in a test to prove cu is obtained by the matrix operation. H6B closes
N06,N17,N28,N30,N31,N33,N36,N37 only after its actual checks pass. P2 retains
N18,N21,N34. B2 remains blocked.

`tools/evidence_formats.py` defines closed inert source, conformance and measurement
formats. `tools/conformance_map.json` maps every formula to frozen authority,
implementation and tests. Generated manifests are external to the wheel. The
dependency graph is acyclic:

1. Source content and wheel -> conformance manifest.
2. Conformance plus installed members/dependencies -> provider build.
3. Build plus measured table and negative-test evidence -> measurement manifest.
4. Measurement -> finite resource policy.
5. Build and resource policy -> catalogue -> local admission byte pin.

No generated file embeds its own digest. No wheel contains the catalogue, build,
measurement or admission pin. Test-only envelopes use conspicuous TEST_ONLY
identities and are not real admission. A real local bundle is generated only after
all preceding gates pass. Its `runtime_prefix` is part of the retained evidence:
installed metadata is local, so copying only a CI catalogue to another installation
does not admit that installation. Recertify locally and pin its exact bundle.

After admission the pipeline exercises all five operations, including a maximum-N
EMA run, and retains canonical complete artifacts. Local conformance review is
not a human signature, protected execution snapshot or production attestation.
