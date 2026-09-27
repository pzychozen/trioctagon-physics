"""Four-workspace scientific client. This module performs no kernel operations."""
from collections.abc import Mapping
from copy import deepcopy
from decimal import Decimal
from importlib import metadata
import json
from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFileDialog, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMessageBox, QPlainTextEdit,
    QPushButton, QScrollArea, QSlider, QSpinBox, QSplitter, QTabWidget, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
from trioctagon_ui import requests
from trioctagon_ui.geometry_view import GeometryView
from trioctagon_ui.jobs import JobManager
from trioctagon_ui.plots import StoredPlots
from trioctagon_ui.record_views import RecordView, atomic_text, f64, kernel_lock


def button(text, name, callback):
    item = QPushButton(text)
    item.setAccessibleName(name)
    item.clicked.connect(callback)
    return item


def readonly_text(name):
    item = QPlainTextEdit(); item.setReadOnly(True); item.setAccessibleName(name)
    return item


def fill_tree(tree, value):
    tree.clear()
    def add(parent, name, data):
        if isinstance(data, Mapping) and set(data) == {"f64"}:
            item = QTreeWidgetItem([str(name), repr(f64(data)), data["f64"]])
        elif isinstance(data, (Mapping, tuple, list)):
            item = QTreeWidgetItem([str(name), f"{len(data)} entries", ""])
            values = data.items() if isinstance(data, Mapping) else enumerate(data)
            for key, sub in values:
                add(item, key, sub)
        else:
            item = QTreeWidgetItem([str(name), str(data), str(data)])
        (parent.addTopLevelItem if isinstance(parent, QTreeWidget) else parent.addChild)(item)
    for name, data in value.items():
        add(tree, name, data)
    tree.expandToDepth(0)
    tree.resizeColumnToContents(0)


def tree(name):
    item = QTreeWidget(); item.setHeaderLabels(["Field", "Display / exact node", "Stored spelling"])
    item.setAccessibleName(name)
    return item


class NumericControl(QWidget):
    changed = Signal(str)

    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.name = name
        self.low, self.high, self.step = map(Decimal, requests.SOFT_RANGES[name])
        box = QVBoxLayout(self); box.setContentsMargins(0, 0, 0, 0)
        self.edit = QLineEdit(); self.edit.setAccessibleName(name + " authoritative numeric entry")
        self.edit.setPlaceholderText("Enter an explicit value")
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, int((self.high - self.low) / self.step))
        self.slider.setAccessibleName(name + " display-range slider; numeric entry is authoritative")
        self.note = QLabel(); self.note.setWordWrap(True)
        self.note.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        box.addWidget(self.edit); box.addWidget(self.slider); box.addWidget(self.note)
        self.edit.textChanged.connect(self._text_changed)
        self.slider.valueChanged.connect(self._dragged)
        self._text_changed("")

    def _text_changed(self, text):
        label = f"DISPLAY_RANGE_ONLY [{self.low}, {self.high}], step {self.step}"
        try:
            (requests.integer if self.name == "updates" else requests.number)(text, self.name)
            exact = Decimal(text.strip())
            if self.low <= exact <= self.high:
                self.slider.blockSignals(True)
                self.slider.setValue(int((exact - self.low) / self.step))
                self.slider.blockSignals(False)
            else:
                label += " — outside soft range; typed value retained"
        except ValueError:
            label += " — unset or invalid"
        self.note.setText(label)
        self.changed.emit(text)

    def _dragged(self, tick):
        self.edit.setText(format(self.low + tick * self.step, "f"))

    def text(self):
        return self.edit.text()

    def setText(self, text):
        self.edit.setText(text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trioctagon Scientific UI — explicit inputs, stored results")
        self.resize(1450, 980)
        self.draft = requests.blank_draft()
        self._setting = False
        self.checkpoint = None
        self.current = None
        self.current_run = None
        self.current_geometry = None
        self.records = []
        self.saved = {}
        self.loaded = set()
        self.resumed = set()
        self.runtime_source = "Unknown until a public result is produced"
        self.lock = kernel_lock()
        self.help = requests.help_data()
        self.jobs = JobManager(self)
        central = QWidget(); self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        self.identity = QLabel(); self.identity.setWordWrap(True)
        self.identity.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.identity.setAccessibleName("Selected record identity and save state")
        layout.addWidget(self.identity)
        self.tabs = QTabWidget(); self.tabs.setAccessibleName("Scientific workspaces")
        layout.addWidget(self.tabs)
        self._dynamics(); self._observers(); self._geometry(); self._records()
        bottom = QHBoxLayout(); layout.addLayout(bottom)
        self.job_label = QLabel("Job: idle; no scientific computation has been submitted")
        self.job_label.setAccessibleName("Worker state, elapsed time and requested sample count")
        bottom.addWidget(self.job_label, 1)
        self.cancel_button = button("Cancel active job", "Cancel scientific worker", self.jobs.cancel)
        self.cancel_button.setEnabled(False); bottom.addWidget(self.cancel_button)
        self.jobs.state_changed.connect(self._job_state)
        self.jobs.elapsed_changed.connect(lambda elapsed: self.job_label.setText(f"Job: {self.jobs.state}; {elapsed:.1f} s; requested samples: {self.requested_samples}"))
        self.jobs.completed.connect(self._completed)
        self.jobs.failed.connect(self._failed)
        self.jobs.cancelled.connect(lambda: self.statusBar().showMessage("Cancelled; previous completed records preserved"))
        self.requested_samples = "not applicable"
        self._render_draft(); self._identity(); self._validity()

    def _help(self, name):
        item = next(v for v in self.help["items"] if v["id"] == name)
        return f"{item['text']}\n[{item['class']}; {item['source']}]"

    def _dynamics(self):
        page = QWidget(); row = QHBoxLayout(page)
        splitter = QSplitter(); row.addWidget(splitter)
        scroll = QScrollArea(); scroll.setWidgetResizable(True); scroll.setMinimumWidth(400)
        controls = QWidget(); form = QVBoxLayout(controls); scroll.setWidget(controls)
        splitter.addWidget(scroll)
        form.addWidget(QLabel("Topology: triad (fixed in K4b; ring editing is K4c)"))
        self.origin_label = QLabel(); self.origin_label.setWordWrap(True); form.addWidget(self.origin_label)
        seed = button("Apply HISTORICAL PRESET: gate_torus_seed_v1", "Apply historical seed", self._seed)
        seed.setToolTip(self._help("historical")); form.addWidget(seed); self.seed_button = seed
        form.addWidget(QLabel("Recorded provenance known. Original design rationale unresolved where O02 applies."))
        presets = QHBoxLayout(); form.addLayout(presets)
        self.reference_zero = button("L01 fill: phase 0", "Apply L01 reference parameters with phase strength zero", lambda: self._reference("0"))
        self.reference_phase = button("L01 fill: phase .001", "Apply L01 reference parameters with phase strength 0.001", lambda: self._reference("0.001"))
        presets.addWidget(self.reference_zero); presets.addWidget(self.reference_phase)
        self.counts_button = button("UI example counts: index 0, updates 100", "Explicitly fill example counts; not historical science", self._counts)
        form.addWidget(self.counts_button)
        self.numeric = {}
        primary = QFormLayout(); form.addLayout(primary)
        for name in ("eps", "g", "phase_strength", "updates"):
            control = NumericControl(name); self.numeric[name] = control
            primary.addRow(name, control); control.changed.connect(lambda _, n=name: self._edited(n))
            control.setToolTip(self._help("inputs"))
        self.advanced_toggle = QCheckBox("Show advanced input and provenance")
        self.advanced_toggle.setAccessibleName("Show full Omega, k triple, index and provenance")
        form.addWidget(self.advanced_toggle)
        self.advanced = QWidget(); adv = QFormLayout(self.advanced); form.addWidget(self.advanced)
        self.advanced.setVisible(False); self.advanced_toggle.toggled.connect(self.advanced.setVisible)
        self.omega_edits = []
        for i in range(3):
            pair = []
            for part in ("re", "im"):
                edit = QLineEdit(); edit.setAccessibleName(f"Omega{i} {part} authoritative input")
                edit.setToolTip(self._help("state")); adv.addRow(f"Omega{i}.{part}", edit)
                edit.textChanged.connect(lambda _: self._edited("omega")); pair.append(edit)
            self.omega_edits.append(pair)
        self.index_edit = QLineEdit(); self.index_edit.setAccessibleName("Initial update_index")
        self.index_edit.textChanged.connect(lambda _: self._edited("update_index")); adv.addRow("update_index", self.index_edit)
        for i in range(3):
            control = NumericControl(f"k{i}"); self.numeric[f"k{i}"] = control
            adv.addRow(f"k{i}", control); control.changed.connect(lambda _: self._edited("k"))
        self.equal_edit = QLineEdit(); self.equal_edit.setAccessibleName("Explicit value to copy into all three k components")
        adv.addRow("Equal-k value", self.equal_edit)
        adv.addRow(button("Copy equal-k value into k0/k1/k2", "Set explicit equal k triple", self._equal))
        self.provenance = {}
        for name in ("source_id", "source_revision", "locator", "notes"):
            edit = QLineEdit(); edit.setAccessibleName("User provenance " + name)
            adv.addRow("Provenance " + name, edit); self.provenance[name] = edit
            edit.textChanged.connect(lambda _: self._edited("provenance"))
        self.checkpoint_label = QLabel("New explicit run draft"); self.checkpoint_label.setWordWrap(True)
        form.addWidget(self.checkpoint_label)
        self.checkpoint_reset = QCheckBox("Checkpoint: explicitly reinitialize selected named observers")
        self.checkpoint_reset.setAccessibleName("Approve named observer reinitialization for checkpoint draft")
        self.checkpoint_reset.setVisible(False); self.checkpoint_reset.toggled.connect(self._validity)
        form.addWidget(self.checkpoint_reset)
        self.validation = QLabel(); self.validation.setWordWrap(True); form.addWidget(self.validation)
        actions = QHBoxLayout(); form.addLayout(actions)
        self.zero_button = button("Zero updates", "Run zero explicit updates", lambda: self._run(0))
        self.one_button = button("One update", "Run one explicit update", lambda: self._run(1))
        self.run_button = button("Run N updates", "Run complete explicit draft", lambda: self._run(None))
        for action in (self.zero_button, self.one_button, self.run_button):
            actions.addWidget(action)
        form.addWidget(button("New blank draft", "Clear draft while preserving completed records", self._blank))
        self.preview = readonly_text("Explicit draft and resolved request preview")
        self.preview.setMaximumHeight(190); form.addWidget(self.preview)
        form.addStretch()
        result = QWidget(); views = QVBoxLayout(result); splitter.addWidget(result)
        self.plots = StoredPlots(); views.addWidget(self.plots, 2)
        sample_row = QHBoxLayout(); views.addLayout(sample_row)
        sample_row.addWidget(QLabel("Stored sample ordinal"))
        self.sample = QSpinBox(); self.sample.setAccessibleName("Stored sample ordinal; changes view only")
        self.sample.setRange(0, 0); self.sample.valueChanged.connect(self._sample_changed)
        sample_row.addWidget(self.sample)
        self.sample_label = QLabel("No record"); sample_row.addWidget(self.sample_label)
        self.sample_table = QTableWidget(0, 3)
        self.sample_table.setHorizontalHeaderLabels(["Field", "Displayed value", "Exact stored spelling"])
        self.sample_table.setAccessibleName("Selected sample table; equivalent to all sample plots")
        self.sample_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        views.addWidget(self.sample_table, 1)
        splitter.setSizes([460, 920])
        self.tabs.addTab(page, "A — Dynamics")

    def _observers(self):
        page = QWidget(); layout = QVBoxLayout(page)
        banner = QLabel("PASSIVE OBSERVATION / DIAGNOSTIC — nothing here feeds back into Omega")
        banner.setWordWrap(True); layout.addWidget(banner)
        self.observer_combo = QComboBox(); self.observer_combo.setAccessibleName("Explicit named observer selection")
        self.observer_combo.addItems(["None", *requests.OBSERVER_NAMES, "Both"])
        self.observer_combo.setToolTip(self._help("observers"))
        layout.addWidget(self.observer_combo)
        layout.addWidget(QLabel("HISTORICAL PRESETS: named observers use their public clock/configuration/memory values; custom observers are K4c."))
        layout.addWidget(QLabel("Recorded provenance known. Original design rationale unresolved where O02 applies."))
        self.observer_combo.currentIndexChanged.connect(lambda _: self._edited("observers"))
        self.output_checks = {}
        for name in ("z_chiral", *requests.DIAGNOSTICS):
            check = QCheckBox(name); check.setAccessibleName("Request " + name)
            check.setToolTip(self._help("observers")); layout.addWidget(check)
            self.output_checks[name] = check
            check.toggled.connect(lambda _: self._edited("outputs"))
        layout.addWidget(QLabel("readout_accounting and historical_alignment require an explicitly selected observer. No outputs are selected initially."))
        self.passive_tree = tree("Read-only returned observer and diagnostic fields at selected sample")
        layout.addWidget(self.passive_tree, 1)
        self.tabs.addTab(page, "B — Observers & Diagnostics")

    def _geometry(self):
        page = QWidget(); layout = QVBoxLayout(page)
        row = QHBoxLayout(); layout.addLayout(row)
        self.geometry_combo = QComboBox(); self.geometry_combo.setAccessibleName("Independent geometry definition")
        self.geometry_combo.addItems(["Choose geometry", "C01 — sections []", "D03 — regular(s)"])
        row.addWidget(self.geometry_combo)
        self.s_edit = QLineEdit(); self.s_edit.setPlaceholderText("Exact positive s: integer or integer/integer")
        self.s_edit.setAccessibleName("D03 regular exact positive s")
        row.addWidget(self.s_edit)
        self.geometry_button = button("Request geometry", "Compute independent public GeometryRecord", self._request_geometry)
        row.addWidget(self.geometry_button)
        self.geometry_combo.currentIndexChanged.connect(self._validity)
        self.s_edit.textChanged.connect(self._validity)
        self.geometry_view = GeometryView(); layout.addWidget(self.geometry_view, 2)
        self.geometry_tree = tree("Exact geometry objects, parameters, incidence, roles and symmetry")
        layout.addWidget(self.geometry_tree, 1)
        self.tabs.addTab(page, "C — Geometry")

    def _records(self):
        page = QWidget(); layout = QVBoxLayout(page)
        self.kernel_identity = QLabel(); self.kernel_identity.setWordWrap(True)
        self.kernel_identity.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.kernel_identity.setAccessibleName("Expected kernel artifact versus installed and current source identity")
        layout.addWidget(self.kernel_identity)
        self.history = QComboBox(); self.history.setAccessibleName("Completed and loaded immutable record history")
        self.history.currentIndexChanged.connect(self._history_selected); layout.addWidget(self.history)
        row = QHBoxLayout(); layout.addLayout(row)
        self.load_button = button("Load record JSON", "Load public record through worker validation", self._load_record)
        self.save_button = button("Save current record JSON", "Save exact canonical public record JSON", self._save_record)
        row.addWidget(self.load_button); row.addWidget(self.save_button)
        row.addWidget(button("Save draft configuration", "Save application draft separately", self._save_draft))
        row.addWidget(button("Load draft configuration", "Load application draft without science", self._load_draft))
        continuation = QHBoxLayout(); layout.addLayout(continuation)
        self.resume_updates = QLineEdit(); self.resume_updates.setPlaceholderText("Explicit additional updates")
        self.resume_updates.setAccessibleName("Resume update count; no parameter overrides")
        self.resume_updates.textChanged.connect(self._validity); continuation.addWidget(self.resume_updates)
        self.resume_button = button("Resume current RunRecord", "Resume with unchanged recorded parameters and observers", self._resume)
        continuation.addWidget(self.resume_button)
        self.checkpoint_button = button("Prepare new checkpoint draft", "Copy selected sample to a new run draft", self._prepare_checkpoint)
        continuation.addWidget(self.checkpoint_button)
        layout.addWidget(QLabel("Resume preserves configuration. A checkpoint creates a NEW RUN with explicit parameter choices and observer reinitialization."))
        self.trust = QLabel("No record loaded"); self.trust.setWordWrap(True); layout.addWidget(self.trust)
        self.record_tree = tree("Structured record provenance, source, hashes, paper references and producer environment")
        layout.addWidget(self.record_tree, 2)
        raw_toggle = QCheckBox("Show canonical raw JSON (read-only)")
        raw_toggle.setAccessibleName("Show canonical raw JSON")
        layout.addWidget(raw_toggle)
        self.raw_json = readonly_text("Canonical public record JSON; read-only")
        self.raw_json.setVisible(False); raw_toggle.toggled.connect(self.raw_json.setVisible)
        layout.addWidget(self.raw_json, 1)
        self.error_details = readonly_text("Original exception, operation, request ID, traceback and child stderr")
        self.error_details.setMaximumHeight(170); layout.addWidget(self.error_details)
        layout.addWidget(button("Copy error details", "Copy original technical error details", lambda: QApplication.clipboard().setText(self.error_details.toPlainText())))
        layout.addWidget(QLabel(self._help("license")))
        self.tabs.addTab(page, "D — Records & Reproducibility")

    def _gather(self):
        draft = deepcopy(self.draft)
        for name in ("eps", "g", "phase_strength", "updates"):
            draft[name] = self.numeric[name].text()
        draft["k"] = [self.numeric[f"k{i}"].text() for i in range(3)]
        draft["omega"] = [[edit.text() for edit in pair] for pair in self.omega_edits]
        draft["update_index"] = self.index_edit.text()
        draft["provenance"] = {k: edit.text() for k, edit in self.provenance.items()}
        draft["provenance"]["source_revision"] = draft["provenance"]["source_revision"] or None
        selection = self.observer_combo.currentIndex()
        draft["observers"] = [] if selection == 0 else list(requests.OBSERVER_NAMES) if selection == 3 else [requests.OBSERVER_NAMES[selection - 1]]
        draft["readouts"] = ["z_chiral"] if self.output_checks["z_chiral"].isChecked() else []
        draft["diagnostics"] = [n for n in requests.DIAGNOSTICS if self.output_checks[n].isChecked()]
        return draft

    def _render_draft(self):
        self._setting = True
        try:
            for name in ("eps", "g", "phase_strength", "updates"):
                self.numeric[name].setText(self.draft[name])
            for i in range(3):
                self.numeric[f"k{i}"].setText(self.draft["k"][i])
                for j in range(2):
                    self.omega_edits[i][j].setText(self.draft["omega"][i][j])
            self.index_edit.setText(self.draft["update_index"])
            for k, edit in self.provenance.items():
                edit.setText(self.draft["provenance"][k] or "")
            observers = self.draft["observers"]
            index = 0 if not observers else 3 if len(observers) == 2 else requests.OBSERVER_NAMES.index(observers[0]) + 1
            self.observer_combo.setCurrentIndex(index)
            for name, check in self.output_checks.items():
                check.setChecked(name in self.draft["readouts"] + self.draft["diagnostics"])
        finally:
            self._setting = False
        self._validity()

    def _edited(self, field):
        if self._setting or not hasattr(self, "output_checks"):
            return
        self.draft = requests.mark_edited(self._gather(), field)
        if field in ("omega", "update_index") and self.checkpoint:
            self.checkpoint = None
            self.checkpoint_label.setText("Checkpoint state edited: new explicit draft; no continuation claim")
            self.checkpoint_reset.setVisible(False)
        self._validity()

    def _validity(self, *_):
        if self._setting or not hasattr(self, "resume_updates"):
            return
        draft = self._gather()
        for name in ("readout_accounting", "historical_alignment"):
            check = self.output_checks[name]
            check.setEnabled(bool(draft["observers"]) or check.isChecked())
        try:
            resolved = requests.resolve_draft(draft)
            valid = True
            message = "Complete explicit draft. Kernel validation remains authoritative."
        except (ValueError, TypeError) as exc:
            resolved = None; valid = False; message = str(exc)
        if self.checkpoint and not self.checkpoint_reset.isChecked():
            valid = False; message = "Explicitly acknowledge named observer reinitialization for this new checkpoint run."
        self.validation.setText(message)
        for item in (self.run_button, self.zero_button, self.one_button):
            item.setEnabled(valid and not self.jobs.busy)
        self.run_button.setText("Run checkpoint draft" if self.checkpoint else "Run N updates")
        origin = draft["origin"]
        self.origin_label.setText(f"Seed: {'HISTORICAL PRESET '+origin['seed'] if origin['seed'] else 'USER VALUE'}; parameters: {'REFERENCE FILL L01' if origin['parameters'] else 'USER VALUE'}")
        self.preview.setPlainText(json.dumps({"draft": draft, "resolved_binary64_hex": resolved}, indent=2, ensure_ascii=False))
        geometry_valid = self.geometry_combo.currentIndex() == 1
        if self.geometry_combo.currentIndex() == 2:
            try:
                requests.rational(self.s_edit.text()); geometry_valid = True
            except ValueError:
                geometry_valid = False
        self.s_edit.setEnabled(self.geometry_combo.currentIndex() == 2)
        self.geometry_button.setEnabled(geometry_valid and not self.jobs.busy)
        is_run = self.current is not None and self.current.kind == "KERNEL_RUN_RECORD"
        try:
            requests.integer(self.resume_updates.text(), "resume updates"); resume_valid = True
        except ValueError:
            resume_valid = False
        self.resume_button.setEnabled(is_run and resume_valid and not self.jobs.busy)
        self.checkpoint_button.setEnabled(is_run and int(self.current.data["state_size"]) == 3 and not self.jobs.busy)
        self.save_button.setEnabled(self.current is not None)
        self.load_button.setEnabled(not self.jobs.busy)
        self.cancel_button.setEnabled(self.jobs.busy)

    def _seed(self):
        self.draft = requests.apply_seed(self._gather()); self.checkpoint = None
        self.checkpoint_reset.setVisible(False); self.checkpoint_label.setText("New run from explicit historical seed fill")
        self._render_draft()

    def _reference(self, phase):
        self.draft = requests.apply_reference(self._gather(), phase); self._render_draft()

    def _counts(self):
        self.draft = self._gather()
        if not self.checkpoint:
            self.draft["update_index"] = "0"
        self.draft["updates"] = "100"; self._render_draft()

    def _equal(self):
        try:
            self.draft = requests.equal_k(self._gather(), self.equal_edit.text()); self._render_draft()
        except ValueError as exc:
            self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": "draft equal-k"})

    def _blank(self):
        self.draft = requests.blank_draft(); self.checkpoint = None
        self.checkpoint_reset.setVisible(False); self.checkpoint_reset.setChecked(False)
        self.checkpoint_label.setText("New explicit run draft"); self._render_draft()

    def _submit(self, envelope, count="not applicable"):
        if isinstance(count, int) and count > 10000:
            if QMessageBox.question(self, "Large application job", f"This requests {count:,} total samples. Record size depends on selected outputs. This is a UI warning, not a scientific limit. Continue?") != QMessageBox.StandardButton.Yes:
                return
        self.requested_samples = count
        self.error_details.clear()
        self.preview.setPlainText(json.dumps(envelope, indent=2, ensure_ascii=False))
        try:
            self.jobs.start(envelope)
            self._validity()
        except Exception as exc:
            self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": envelope["operation"], "request_id": envelope["request_id"]})

    def _run(self, updates):
        try:
            envelope = requests.run_request(self._gather(), updates)
            if self.checkpoint:
                if not self.checkpoint_reset.isChecked():
                    raise ValueError("Checkpoint observer reset must be explicitly acknowledged")
                envelope["operation"] = "new_checkpoint_run"
                envelope["payload"].update(self.checkpoint)
                envelope["payload"]["observer_reset"] = "reinitialize_named"
            self._submit(envelope, int(envelope["payload"]["resolved"]["updates"]) + 1)
        except Exception as exc:
            self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": "run draft"})

    def _request_geometry(self):
        definition = "C01" if self.geometry_combo.currentIndex() == 1 else "D03"
        self._submit(requests.request("geometry", {"definition_id": definition, "s": None if definition == "C01" else self.s_edit.text()}))

    def _resume(self):
        try:
            n = requests.integer(self.resume_updates.text(), "resume updates")
            self._submit(requests.request("resume", {"record_json": self.current.canonical_json, "updates": self.resume_updates.text()}), len(self.current.samples) + n)
        except Exception as exc:
            self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": "resume"})

    def _prepare_checkpoint(self):
        parent = self.current
        index = self.sample.value()
        sample = parent.samples[index]
        self.draft = self._gather()
        self.draft["omega"] = [[repr(f64(pair[p])) for p in ("re", "im")] for pair in sample["omega"]]
        self.draft["update_index"] = sample["update_index"]
        self.draft["origin"]["seed"] = None
        self.draft["origin"]["changes"].append(f"Checkpoint from {parent.digest} sample {index}; new run")
        self.checkpoint = {"record_json": parent.canonical_json, "sample_index": str(index)}
        self.checkpoint_label.setText(f"NEW CHECKPOINT RUN: parent {parent.digest}; sample {index}. Parameters and outputs use the visible draft.")
        self.checkpoint_reset.setChecked(False); self.checkpoint_reset.setVisible(True)
        self._render_draft(); self.tabs.setCurrentIndex(0)

    def _job_state(self, state):
        self.job_label.setText(f"Job: {state}; requested samples: {self.requested_samples}")
        self.cancel_button.setEnabled(self.jobs.busy)
        self._validity()

    def _completed(self, response):
        result = response["result"]
        view = RecordView(result["canonical_json"])
        if result["produced_current"]:
            self.runtime_source = result["source_commit"]
        else:
            self.loaded.add(view.digest)
        if response["operation"] == "resume":
            self.resumed.add(view.digest)
        self.records.append(view)
        self.history.blockSignals(True)
        self.history.addItem(f"{view.kind} · {view.digest[:12]}")
        self.history.setCurrentIndex(len(self.records) - 1)
        self.history.blockSignals(False)
        self._select_record(view)
        self.statusBar().showMessage("Complete immutable record accepted; draft remains separate")

    def _history_selected(self, index):
        if 0 <= index < len(self.records):
            self._select_record(self.records[index])

    def _select_record(self, view):
        self.current = view
        self.raw_json.setPlainText(view.canonical_json)
        fill_tree(self.record_tree, {k: v for k, v in view.data.items() if k not in ("samples", "objects")})
        self.trust.setText("Structure/digest valid. Producer claims inspected. Current resume compatibility not checked. No scientific replay or authentication claimed.")
        if view.digest in self.resumed:
            self.trust.setText("Structure/digest valid. Public resume accepted the parent source/module identity and produced this continuation. No independent scientific replay or producer authentication claimed.")
        self._identity()
        try:
            if view.kind == "KERNEL_RUN_RECORD":
                self.current_run = view
                self.sample.blockSignals(True); self.sample.setRange(0, len(view.samples) - 1); self.sample.setValue(0); self.sample.blockSignals(False)
                self.plots.set_record(view); self._sample_changed(0)
            else:
                self.current_geometry = view
                fill_tree(self.geometry_tree, {k: v for k, v in view.data.items() if k not in ("execution_metadata", "paper_references", "implementation")})
                self.geometry_view.set_record(view)
        except Exception as exc:
            self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": "presentation", "qualification": "Record remains accepted; exact inspector and save remain available"})
        self._validity()

    def _sample_changed(self, index):
        view = self.current_run
        if view is None or not 0 <= index < len(view.samples):
            return
        rows = view.sample_rows(index)
        self.sample_table.setRowCount(len(rows))
        for i, values in enumerate(rows):
            for j, value in enumerate(values):
                self.sample_table.setItem(i, j, QTableWidgetItem(value))
        self.sample_table.resizeColumnsToContents()
        sample = view.samples[index]
        self.sample_label.setText(f"update_index={sample['update_index']}; raw chirality: {view.missing_series('chirality0')}" + ("; plots show first three channels" if int(view.data['state_size']) > 3 else ""))
        fill_tree(self.passive_tree, {k: sample[k] for k in ("observer_states", "observer_results", "diagnostics", "raw_readouts")})
        self.plots.select_sample(index)

    def _identity(self):
        try:
            installed = metadata.version("trioctagon-physics")
        except metadata.PackageNotFoundError:
            installed = "missing"
        self.kernel_identity.setText(f"Expected locked kernel: {self.lock['artifact_filename']}\nSHA-256: {self.lock['artifact_sha256']}\nExpected source: {self.lock['source_commit']}\nInstalled distribution version: {installed}\nCurrent source identity: {self.runtime_source}\nApplication: trioctagon-scientific-ui 0.1.0; separate software identity")
        if self.current is None:
            self.identity.setText("Draft configuration · no completed record · geometry and dynamics remain independent")
        else:
            view = self.current
            state = "Saved" if view.digest in self.saved else "Loaded validated record — not saved by this session" if view.digest in self.loaded else "Completed record — UNSAVED"
            self.identity.setText(f"{view.kind} · source {view.data['implementation']['commit'][:12]} · digest {view.digest[:16]} · {state}\nDraft edits prepare a new run; recorded inputs stay unchanged.")

    def _failed(self, error):
        self.error_details.setPlainText(json.dumps(error, indent=2, ensure_ascii=False))
        self.statusBar().showMessage(f"{error.get('exception_class', 'Error')}: {error.get('message', '')}; previous records preserved")
        if error.get("operation") == "resume":
            self.trust.setText("Resume rejected. Original reason is shown below. Choose an explicit new checkpoint run if appropriate.")
        self._validity()

    def _load_record(self):
        path, _ = QFileDialog.getOpenFileName(self, "Load public record JSON", "", "JSON (*.json)")
        if not path:
            return
        try:
            if Path(path).stat().st_size > 50_000_000 and QMessageBox.question(self, "Large record", "This file exceeds the 50 MB application warning threshold. Load it explicitly?") != QMessageBox.StandardButton.Yes:
                return
            self._submit(requests.request("load_record", {"record_json": Path(path).read_text(encoding="utf-8")}))
        except Exception as exc:
            self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": "load record file"})

    def _save_record(self):
        if self.current is None:
            return
        path, _ = QFileDialog.getSaveFileName(self, "Save exact canonical record JSON", "record.json", "JSON (*.json)")
        if path:
            try:
                self.current.save(path); self.saved[self.current.digest] = path; self._identity()
            except Exception as exc:
                self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": "save record"})

    def _save_draft(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save application draft (not a kernel record)", "draft.json", "JSON (*.json)")
        if path:
            try:
                atomic_text(path, requests.draft_json(self._gather()))
                self.statusBar().showMessage("Application draft saved separately from scientific records")
            except Exception as exc:
                self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": "save draft"})

    def _load_draft(self):
        path, _ = QFileDialog.getOpenFileName(self, "Load application draft", "", "JSON (*.json)")
        if path:
            try:
                self.draft = requests.load_draft(Path(path).read_text(encoding="utf-8"))
                self.checkpoint = None; self.checkpoint_reset.setVisible(False)
                self.checkpoint_label.setText("Loaded application draft; submit as a new explicit run")
                self._render_draft()
            except Exception as exc:
                self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": "load draft"})

    def closeEvent(self, event):
        if self.jobs.busy:
            self.jobs.cancel()
            event.ignore()
            self.jobs.cancelled.connect(self.close)
            return
        event.accept()
