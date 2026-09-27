"""Derived presentation exports with staged provenance sidecars; no kernel calls."""
import csv
import hashlib
import json
import os
from pathlib import Path
import tempfile
from trioctagon_ui.comparison import leaves, plain

FIELD_GROUPS = ("omega", "raw_readouts", "observer_states", "observer_results", "diagnostics")
QUALIFICATION = "Derived presentation artifact. Authoritative scientific source is the referenced public record. Detached analysis retains its separate application lineage."


def select_samples(record, selection):
    if record.kind != "KERNEL_RUN_RECORD": raise ValueError("Sample CSV requires a RunRecord")
    mode = selection.get("mode")
    if mode == "all" and set(selection) == {"mode"}: ordinals = list(range(len(record.samples)))
    elif mode == "range" and set(selection) == {"mode", "start", "stop"}:
        start, stop = selection["start"], selection["stop"]
        if type(start) is not int or type(stop) is not int or stop < start: raise ValueError("Explicit inclusive ordinal range required")
        if not 0 <= start <= stop < len(record.samples): raise ValueError("Sample range outside stored history")
        ordinals = list(range(start, stop + 1))
    elif mode == "ordinals" and set(selection) == {"mode", "ordinals"} and isinstance(selection["ordinals"], list): ordinals = selection["ordinals"][:]
    else: raise ValueError("Select all samples, an inclusive range, or explicit ordinals")
    if not ordinals or any(type(i) is not int or not 0 <= i < len(record.samples) for i in ordinals): raise ValueError("Explicit sample ordinals must exist in stored history")
    return ordinals


def parent_identity(record):
    return {"digest": record.digest, "source_commit": record.data["implementation"]["commit"], "record_type": record.kind}


def stage_export(destination, artifact_type, writer, metadata):
    destination = Path(destination).resolve(); sidecar = destination.with_suffix(destination.suffix + ".provenance.json")
    extension = {"derived_csv": ".csv", "derived_png": ".png", "derived_svg": ".svg"}[artifact_type]
    if destination.suffix.lower() != extension: raise ValueError("Choose the matching derived-export extension")
    if destination.exists() or sidecar.exists(): raise FileExistsError("Exports never overwrite existing files; choose a new destination")
    if destination.parent.name == "records" and (destination.parent.parent / "sweep-manifest.json").exists():
        raise ValueError("Choose an export location separate from authoritative dataset records/")
    published = []
    try:
        with tempfile.TemporaryDirectory(prefix=".trioctagon-export-", dir=destination.parent) as staging:
            staging = Path(staging); artifact = staging / destination.name; companion = staging / sidecar.name
            writer(artifact)
            raw = artifact.read_bytes()
            result = {**plain(metadata), "artifact_type": artifact_type, "export_schema_version": 1, "app_version": "0.1.0",
                "filename": destination.name, "sha256": hashlib.sha256(raw).hexdigest(), "qualification": QUALIFICATION}
            if artifact_type == "derived_svg":
                result["rasterized_layers_detected"] = b"<image" in raw
                result["svg_qualification"] = "Presentation only; not exact symbolic geometry"
            companion.write_text(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
            # Hard-link publication is atomic and refuses a concurrently created
            # destination. Staging cleanup unlinks its copies; existing data is safe.
            for staged, target in ((artifact, destination), (companion, sidecar)):
                os.link(staged, target); published.append(target)
        return {"artifact": str(destination), "sidecar": str(sidecar), "metadata": result}
    except Exception:
        for path in reversed(published): path.unlink(missing_ok=True)
        raise


def export_csv(record, destination, groups, selection, *, precision=17, kernel_identity=None):
    ordinals = select_samples(record, selection)
    if not isinstance(groups, (tuple, list)) or not groups or len(set(groups)) != len(groups) or set(groups) - set(FIELD_GROUPS):
        raise ValueError("Choose explicit stored field groups")
    if type(precision) is not int or not 1 <= precision <= 17: raise ValueError("Display precision must be 1..17")
    values = [{path: value for group in groups for path, value in leaves(record.samples[i][group], group)} for i in ordinals]
    paths = sorted({path for row in values for path in row})
    f64 = {path for row in values for path, value in row.items() if isinstance(value, dict) and set(value) == {"f64"}}
    columns = ["sample_ordinal", "update_index"]
    semantics = {}
    for path in paths:
        if path in f64:
            columns.extend((path + ".decimal", path + ".f64_hex")); semantics[path] = "human decimal and exact stored binary64 hex"
        else: columns.append(path); semantics[path] = "stored scalar text; missing means not recorded"
    def writer(path):
        with path.open("w", encoding="utf-8", newline="") as out:
            csv_writer = csv.writer(out); csv_writer.writerow(columns)
            for ordinal, row in zip(ordinals, values):
                fields = [ordinal, record.samples[ordinal]["update_index"]]
                for field in paths:
                    value = row.get(field)
                    if field in f64:
                        fields.extend((format(float.fromhex(value["f64"]), f".{precision}g"), value["f64"]) if value is not None else ("not recorded", ""))
                    else: fields.append("not recorded" if value is None else str(value))
                csv_writer.writerow(fields)
    return stage_export(destination, "derived_csv", writer, {"parent_record_digest": record.digest,
        "parent_source_commit": record.data["implementation"]["commit"], "record_type": record.kind,
        "selection": selection, "sample_ordinals": ordinals, "update_indices": [record.samples[i]["update_index"] for i in ordinals],
        "selected_fields": list(groups), "scalar_paths": paths, "columns": columns, "column_semantics": semantics,
        "display_formatting": {"significant_digits": precision, "f64_authority": "exact stored hex companion", "complex": "separate .re and .im paths", "missing": "not recorded"},
        "kernel_artifact_identity": kernel_identity})


def camera_metadata(figure):
    result = []
    for ax in figure.axes:
        row = {"title": ax.get_title(), "xlim": list(ax.get_xlim()), "ylim": list(ax.get_ylim())}
        if hasattr(ax, "get_zlim"): row.update(elevation=ax.elev, azimuth=ax.azim, zlim=list(ax.get_zlim()))
        result.append(row)
    return result


def export_image(figure, destination, context):
    if not context.get("view_type") or "parents" not in context: raise ValueError("Explicit cached-view provenance required")
    if not context["parents"] and not context.get("analysis_lineage"): raise ValueError("Export requires record parents or detached analysis lineage")
    suffix = Path(destination).suffix.lower()
    if suffix not in (".png", ".svg"): raise ValueError("Choose PNG or SVG")
    metadata = {**plain(context), "camera": camera_metadata(figure)}
    return stage_export(destination, "derived_" + suffix[1:], lambda p: figure.savefig(p, format=suffix[1:]), metadata)
