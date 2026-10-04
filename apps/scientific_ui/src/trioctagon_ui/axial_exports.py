"""Export immutable accepted observations without scientific recomputation."""
import csv
import os
from pathlib import Path
import tempfile
from trioctagon_ui.axial_artifacts import AxialAnalysisView, plain
from trioctagon_ui.exports import stage_export, export_image


def provenance(view):
    if not isinstance(view, AxialAnalysisView): raise ValueError('Accepted axial cache required')
    a = view.artifact
    return {k: plain(a[k]) for k in ('artifact_type', 'schema_version', 'observation_api_version', 'observer_revision',
        'analysis_kind', 'evidence_class', 'parent', 'selection', 'implementation', 'content_sha256', 'reference_comparison', 'qualification')} | {
        'saved_import': view.saved_import, 'execution_authentication': 'UNAUTHENTICATED SAVED OBSERVATION' if view.saved_import else 'NO_EXTERNAL_ATTESTATION'}


def export_json(view, destination):
    provenance(view); destination = Path(destination).resolve()
    if destination.suffix.lower() != '.json': raise ValueError('Choose .axial.json')
    if destination.exists(): raise FileExistsError('Axial exports never overwrite existing files')
    with tempfile.TemporaryDirectory(prefix='.trioctagon-axial-', dir=destination.parent) as stage:
        p = Path(stage) / destination.name
        with p.open('wb') as f:
            f.write(view.canonical_json.encode('utf-8')); f.flush(); os.fsync(f.fileno())
        os.link(p, destination)
    if destination.read_bytes() != view.canonical_json.encode('utf-8'):
        raise ValueError('Published axial JSON differs from retained bytes')
    return str(destination)


def export_csv(view, destination):
    context = provenance(view)
    def writer(path):
        with path.open('w', encoding='utf-8', newline='') as f:
            out = csv.writer(f); out.writerow(('field', 'display_value', 'exact_stored_token'))
            out.writerows(view.rows(17))
    return stage_export(destination, 'derived_csv', writer, {'axial_observation': context})


def export_plot(view, figure, destination):
    context = provenance(view)
    return export_image(figure, destination, {'view_type': 'axial_cached_signed_history', 'parents': [context['parent']] if context['parent'] else [],
        'analysis_lineage': context, 'axial_observation': context,
        'connections': 'Visual connections between selected stored samples; no interpolated evolution'})
