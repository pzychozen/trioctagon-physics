"""Four-workspace scientific client. This module performs no kernel operations."""
from collections.abc import Mapping
from copy import deepcopy
from decimal import Decimal
from importlib import metadata
import json
from pathlib import Path

from trioctagon_ui.qt_runtime import prepare_qt
prepare_qt()
from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFileDialog, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMessageBox, QPlainTextEdit,
    QPushButton, QScrollArea, QSlider, QSpinBox, QDoubleSpinBox, QListWidget, QListWidgetItem, QSplitter, QTabWidget, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
from trioctagon_ui import requests
from trioctagon_ui.artifact_panel import ArtifactsPanel
from trioctagon_ui.axial_views import AxialPanel
from trioctagon_ui.axial_artifacts import AxialAnalysisView
from trioctagon_ui.geometry_view import GeometryView
from trioctagon_ui.jobs import JobManager
from trioctagon_ui.plots import StoredPlots, HistoryPlot, ComparisonPlot
from trioctagon_ui import sweeps, exports
from trioctagon_ui.comparison import ComparisonView, plain
from trioctagon_ui.record_views import RecordView, AnalysisView, atomic_text, f64, kernel_lock


def button(text, name, callback):
    item = QPushButton(text)
    item.setAccessibleName(name)
    item.clicked.connect(callback)
    return item


def readonly_text(name):
    item = QPlainTextEdit(); item.setReadOnly(True); item.setAccessibleName(name)
    return item


def fill_tree(tree, value, precision=None):
    tree.clear()
    def add(parent, name, data):
        if isinstance(data, Mapping) and set(data) == {"f64"}:
            item = QTreeWidgetItem([str(name), repr(f64(data)) if precision is None else format(f64(data), f".{precision}g"), data["f64"]])
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
        self.analysis_cache = []
        self.analysis_current = None
        self._artifact_selected = False
        self._artifact_core_pending = False
        self.saved = {}
        self.loaded = set()
        self.resumed = set()
        self.runtime_source = "Unknown until a public result is produced"
        self.lock = kernel_lock()
        self.help = requests.help_data()
        self.jobs = JobManager(self)
        self.sweep_controller = sweeps.SweepController(self.jobs, self)
        self.sweep_plan = None; self.comparison = None
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
        self.cancel_button = button("Cancel active job", "Cancel scientific worker or active dataset", self._cancel_job)
        self.cancel_button.setEnabled(False); bottom.addWidget(self.cancel_button)
        self.jobs.state_changed.connect(self._job_state)
        self.jobs.elapsed_changed.connect(lambda elapsed: self.job_label.setText(f"Job: {self.jobs.state}; {elapsed:.1f} s; requested samples: {self.requested_samples}"))
        self.jobs.completed.connect(self._completed)
        self.jobs.failed.connect(self._failed)
        self.jobs.cancelled.connect(self._cancelled)
        self.sweep_controller.changed.connect(self._dataset_changed)
        self.sweep_controller.record_ready.connect(self._dataset_record)
        self.sweep_controller.persistence_failed.connect(self._failed)
        self.requested_samples = "not applicable"
        self.tabs.currentChanged.connect(self._artifact_context_changed)
        self.repro_tabs.currentChanged.connect(self._artifact_context_changed)
        self._render_draft(); self._identity(); self._validity()

    def _artifact_context_active(self):
        return self._artifact_selected or (hasattr(self, "artifacts") and self.tabs.currentIndex() == 3 and self.repro_tabs.currentWidget() is self.artifacts)

    def _artifact_selection_changed(self):
        self._artifact_selected = True
        self._artifact_context_changed()

    def _artifact_context_changed(self, *unused):
        self._validity(); self._identity()

    def _load_artifact_core(self, candidate):
        # Explicit closed routing to the unchanged v2 Core loader.
        if self.jobs.busy or self.sweep_controller.active:
            self.artifacts.status.setText("Core loader busy; current selection preserved")
            return
        self._artifact_core_pending = True
        self._submit(requests.request("load_record", {"record_json": candidate.raw.decode("utf-8")}))

    def _help(self, name):
        item = next(v for v in self.help["items"] if v["id"] == name)
        return f"{item['text']}\n[{item['class']}; {item['source']}]"

    def _dynamics(self):
        page = QWidget(); row = QHBoxLayout(page)
        splitter = QSplitter(); row.addWidget(splitter)
        scroll = QScrollArea(); scroll.setWidgetResizable(True); scroll.setMinimumWidth(400)
        controls = QWidget(); form = QVBoxLayout(controls); scroll.setWidget(controls)
        splitter.addWidget(scroll)
        self.topology_banner = QLabel("Topology: triad; state size 3")
        form.addWidget(self.topology_banner)
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
        self.topology_combo = QComboBox(); self.topology_combo.addItems(["triad", "ring"])
        self.topology_combo.setAccessibleName("Explicit topology: triad or ring")
        adv.addRow("Topology", self.topology_combo)
        self.q_spin = QSpinBox(); self.q_spin.setRange(1, 1000)
        self.q_spin.setAccessibleName("UI triad row count q; state size is 3q; new rows remain blank")
        self.q_spin.setToolTip(self._help("ring"))
        adv.addRow("q / row structure", self.q_spin)
        self.topology_combo.currentTextChanged.connect(lambda _: self._edited("topology"))
        self.q_spin.valueChanged.connect(self._resize_rows)
        self.omega_box = QWidget(); self.omega_form = QFormLayout(self.omega_box); adv.addRow(self.omega_box)
        self.omega_edits = []; self._omega_widgets(3)
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
        self.checkpoint_reset = QCheckBox("Checkpoint: explicitly initialize selected observer descriptors")
        self.checkpoint_reset.setAccessibleName("Acknowledge explicit observer clocks and memory for checkpoint draft")
        self.checkpoint_reset.setVisible(False); self.checkpoint_reset.toggled.connect(self._validity)
        form.addWidget(self.checkpoint_reset)
        self.validation = QLabel(); self.validation.setWordWrap(True); form.addWidget(self.validation)
        actions = QHBoxLayout(); form.addLayout(actions)
        self.zero_button = button("Zero updates", "Run zero explicit updates", lambda: self._run(0))
        self.one_button = button("One update", "Run one explicit update", lambda: self._run(1))
        self.run_button = button("Run N updates", "Run complete explicit draft", lambda: self._run(None))
        for action in (self.zero_button, self.one_button, self.run_button):
            actions.addWidget(action)
        self.step_preview_button = button("Step preview — detached, not a record", "Explicit public step scratchpad preview", self._step_preview)
        form.addWidget(self.step_preview_button)
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
        playback = QHBoxLayout(); views.addLayout(playback)
        self.play_timer = QTimer(self); self.play_timer.timeout.connect(self._play_tick)
        self.play_button = button("Play", "Play stored samples only", self._play)
        self.pause_button = button("Pause", "Pause stored-sample playback", self.play_timer.stop)
        self.back_button = button("Step back", "Previous stored sample", lambda: self.sample.setValue(max(0, self.sample.value() - 1)))
        self.forward_button = button("Step forward", "Next stored sample", lambda: self.sample.setValue(min(self.sample.maximum(), self.sample.value() + 1)))
        for item in (self.play_button, self.pause_button, self.back_button, self.forward_button): playback.addWidget(item)
        self.playback_rate = QDoubleSpinBox(); self.playback_rate.setRange(.1, 60); self.playback_rate.setValue(5)
        self.playback_rate.setAccessibleName("Playback frames per wall-clock second; unrelated to Clock.dt, updates or physical time")
        self.playback_rate.valueChanged.connect(lambda _: self.play_timer.setInterval(round(1000 / self.playback_rate.value())))
        playback.addWidget(self.playback_rate)
        self.reduced_motion = QCheckBox("Reduced motion"); self.reduced_motion.setAccessibleName("Reduced motion; use manual stored-sample steps")
        self.reduced_motion.setAccessibleDescription("Stops and prevents automatic playback. Rate edits cannot start animation; records remain unchanged.")
        self.reduced_motion.toggled.connect(lambda checked: (self.play_timer.stop(), self.play_button.setEnabled(not checked)))
        views.addWidget(self.reduced_motion)
        views.addWidget(QLabel("Playback: stored sample ordinals; frames / wall-clock second, unrelated to Clock.dt or physical time."))
        self.precision = QSpinBox(); self.precision.setRange(1, 17); self.precision.setValue(8)
        self.precision.setAccessibleName("Displayed significant digits only; stored hex and plot values unchanged")
        precision_row = QHBoxLayout(); views.addLayout(precision_row)
        precision_row.addWidget(QLabel("Display significant digits")); precision_row.addWidget(self.precision)
        self.precision.valueChanged.connect(self._precision_changed)
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
        self.observer_tabs = QTabWidget(); layout.addWidget(self.observer_tabs)
        run_page = QWidget(); run_layout = QVBoxLayout(run_page)
        actions = QHBoxLayout(); run_layout.addLayout(actions)
        self.add_staged = button("Add staged observer", "Add blank custom staged observer", lambda: self._add_observer(requests.blank_observer("staged")))
        self.add_ema = button("Add EMA observer", "Add blank custom EMA observer", lambda: self._add_observer(requests.blank_observer("ema")))
        actions.addWidget(self.add_staged); actions.addWidget(self.add_ema)
        for name in requests.OBSERVER_NAMES:
            actions.addWidget(button("Add HISTORICAL " + name, "Add historical observer " + name, lambda _, n=name: self._add_observer({"mode": "preset", "name": n})))
        pair = QSplitter(); run_layout.addWidget(pair, 2)
        self.observer_list = QListWidget(); self.observer_list.setAccessibleName("Independent observer descriptors; select to inspect or edit")
        pair.addWidget(self.observer_list)
        scroll = QScrollArea(); scroll.setWidgetResizable(True); self.observer_editor = QWidget()
        self.observer_form = QFormLayout(self.observer_editor); scroll.setWidget(self.observer_editor); pair.addWidget(scroll)
        self.observer_fields = {}; self._observer_rendering = False
        self.observer_list.currentRowChanged.connect(self._observer_selected)
        row = QHBoxLayout(); run_layout.addLayout(row)
        self.convert_observer = button("Convert preset to CUSTOM / USER-SUPPLIED", "Explicitly convert historical observer before editing", self._convert_observer)
        self.remove_observer = button("Remove selected observer", "Remove selected observer descriptor", self._remove_observer)
        row.addWidget(self.convert_observer); row.addWidget(self.remove_observer)
        self.clear_passive = button("Clear incompatible passive selections", "Explicitly clear observers, readouts and diagnostics for ring", self._clear_passive)
        run_layout.addWidget(self.clear_passive)
        run_layout.addWidget(QLabel("Recorded provenance known. Original design rationale unresolved where O02 applies. Clock dt is not a dynamics timestep."))
        self.output_checks = {}
        output_row = QHBoxLayout(); run_layout.addLayout(output_row)
        for name in ("z_chiral", *requests.DIAGNOSTICS):
            check = QCheckBox(name); check.setAccessibleName("Request " + name)
            check.setToolTip(self._help("observers")); output_row.addWidget(check)
            self.output_checks[name] = check
            check.toggled.connect(lambda _: self._edited("outputs"))
        run_layout.addWidget(QLabel("Accounting/alignment require observers. Ring requires no passive selections; switching topology never clears them automatically."))
        self.passive_tree = tree("Read-only returned observer and diagnostic fields at selected sample")
        run_layout.addWidget(self.passive_tree, 1)
        self.observer_tabs.addTab(run_page, "Run observers and recorded outputs")
        scratch = QWidget(); form = QVBoxLayout(scratch)
        self.analysis_kind = QComboBox(); self.analysis_kind.addItems(["Choose detached analysis", *[v for v in requests.ANALYSIS_TYPES if v not in requests.HISTORY_TYPES]])
        self.analysis_kind.setAccessibleName("Standalone public analysis function")
        form.addWidget(self.analysis_kind)
        self.analysis_source = QComboBox(); self.analysis_source.addItems(["Explicit scratchpad values", "Explicitly selected stored triad sample"])
        self.analysis_source.setAccessibleName("Explicit scratchpad source choice")
        form.addWidget(self.analysis_source)
        self.analysis_source_label = QLabel("Explicit scratchpad; no implicit selected sample"); self.analysis_source_label.setWordWrap(True)
        form.addWidget(self.analysis_source_label)
        self.analysis_inputs = QPlainTextEdit(); self.analysis_inputs.setAccessibleName("Explicit analysis inputs JSON; numbers entered as strings")
        form.addWidget(self.analysis_inputs)
        form.addWidget(QLabel("All blank strings require explicit entry. JSON is application input, never Python code. Observe calls return recomputed readouts; constructor-zero belongs to recorded run initialization."))
        fill = QHBoxLayout(); form.addLayout(fill)
        fill.addWidget(button("Copy visible dynamics inputs", "Copy visible draft state and parameters into scratchpad", self._copy_analysis_dynamics))
        fill.addWidget(button("Copy selected observer fields", "Copy visible observer clock config memory into scratchpad", self._copy_analysis_observer))
        self.analysis_button = button("Run detached analysis", "Submit explicit standalone public API analysis", self._request_analysis)
        form.addWidget(self.analysis_button)
        self.analysis_kind.currentIndexChanged.connect(self._analysis_template)
        self.analysis_source.currentIndexChanged.connect(self._analysis_context)
        self.observer_tabs.addTab(scratch, "Passive scratchpad")
        history = QWidget(); hist = QVBoxLayout(history)
        fields = QFormLayout(); hist.addLayout(fields)
        self.history_kind = QComboBox(); self.history_kind.addItems(["Choose history display", *requests.HISTORY_TYPES])
        self.history_kind.setAccessibleName("Explicit history coordinate helper")
        fields.addRow("History operation", self.history_kind)
        self.history_observer = QComboBox(); self.history_observer.setAccessibleName("Explicit stored observer history selection")
        fields.addRow("Recorded observer", self.history_observer)
        self.history_key = QComboBox(); self.history_key.addItems(["Choose vector key", "Z_macro", "Z_chiral", "Z_total"])
        fields.addRow("Direct stored vector", self.history_key)
        self.kappa_source = QComboBox(); self.kappa_source.addItems(["Choose recorded kappa source", *requests.KAPPA_SOURCES])
        fields.addRow("DISPLAY_DERIVATION_ONLY sqrt source", self.kappa_source)
        self.history_fields = {}
        for name in ("N", "R", "r_max"):
            edit = QLineEdit(); edit.setAccessibleName("Explicit history " + name); self.history_fields[name] = edit
            fields.addRow(name, edit)
        self.history_context = QLabel("Select a RunRecord, then an observer and explicit coordinate inputs.")
        self.history_context.setWordWrap(True); hist.addWidget(self.history_context)
        hist.addWidget(QLabel("Stored z = observer scalar; phi_index = stored q. Kappa uses the labelled recorded nonnegative diagnostic only. Torus normalization uses the entire supplied history once; playback never renormalizes."))
        self.history_button = button("Request complete stored history display", "Explicit whole-history public coordinate request", self._request_history)
        hist.addWidget(self.history_button)
        self.history_plot = HistoryPlot(); hist.addWidget(self.history_plot, 2)
        self.observer_tabs.addTab(history, "History coordinates")
        self.axial_panel = AxialPanel(self._analysis_source_record)
        self.axial_panel.requested.connect(self._submit)
        self.axial_panel.loaded.connect(self._accept_axial_saved)
        self.observer_tabs.addTab(self.axial_panel, 'Axial Observables')
        self.analysis_table = QTableWidget(0, 3); self.analysis_table.setHorizontalHeaderLabels(["Detached result / input / lineage", "Display value", "Exact stored spelling"])
        self.analysis_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.analysis_table.setAccessibleName("Detached analysis table including every returned history coordinate and normalization field")
        layout.addWidget(self.analysis_table, 1)
        self.observer_tabs.currentChanged.connect(lambda _: self.analysis_table.setVisible(self.observer_tabs.currentWidget() is not self.axial_panel))
        self.tabs.addTab(page, "B — Observers & Diagnostics")

    def _geometry(self):
        page = QWidget(); layout = QVBoxLayout(page)
        row = QHBoxLayout(); layout.addLayout(row)
        self.geometry_combo = QComboBox(); self.geometry_combo.setAccessibleName("Independent geometry definition")
        self.geometry_combo.addItems(["Choose geometry", "C01 — explicit sections", "D03 — explicit construction"])
        row.addWidget(self.geometry_combo)
        self.construction_combo = QComboBox(); self.construction_combo.addItems(["Choose construction", *requests.D03_FIELDS])
        self.construction_combo.setAccessibleName("D03 public construction selector"); row.addWidget(self.construction_combo)
        self.geometry_fields = {}
        params = QFormLayout(); layout.addLayout(params)
        for name in ("s", "g_gap", "p"):
            edit = QLineEdit(); edit.setAccessibleName("D03 exact " + name)
            edit.setToolTip(self._help("exact"))
            edit.setPlaceholderText("Exact expression; no floats"); params.addRow(name + (" — geometric reference length, distinct from dynamics g" if name == "g_gap" else ""), edit)
            self.geometry_fields[name] = edit; edit.textChanged.connect(self._validity)
        self.s_edit = self.geometry_fields["s"]
        self.section_heights = QListWidget(); self.section_heights.setMaximumHeight(85)
        self.section_heights.setAccessibleName("Ordered exact C01 section heights; duplicates preserved; double-click to edit")
        layout.addWidget(self.section_heights)
        self.section_heights.itemChanged.connect(self._validity)
        sections = QHBoxLayout(); layout.addLayout(sections)
        self.section_input = QLineEdit(); self.section_input.setAccessibleName("New exact C01 section-height text")
        self.section_input.setToolTip(self._help("exact") + "\n" + self._help("sections"))
        sections.addWidget(self.section_input)
        self.add_section = button("Add section height", "Append explicit C01 height, preserving repeats", self._add_section)
        self.remove_section = button("Remove selected height", "Remove explicitly selected C01 section height", self._remove_section)
        sections.addWidget(self.add_section); sections.addWidget(self.remove_section)
        self.fixed_geometry = QLabel("C01 w, s, beta are fixed accepted parameters, shown in the exact record. Arbitrary fold angle and inferred symmetry actions remain unavailable.")
        self.fixed_geometry.setWordWrap(True); layout.addWidget(self.fixed_geometry)
        self.geometry_validation = QLabel(); self.geometry_validation.setWordWrap(True); layout.addWidget(self.geometry_validation)
        self.geometry_button = button("Request geometry", "Compute independent public GeometryRecord", self._request_geometry)
        row.addWidget(self.geometry_button)
        self.geometry_combo.currentIndexChanged.connect(self._validity)
        self.construction_combo.currentIndexChanged.connect(self._validity)
        self.geometry_view = GeometryView(); layout.addWidget(self.geometry_view, 2)
        self.geometry_tree = tree("Exact geometry objects, parameters, incidence, roles and symmetry")
        layout.addWidget(self.geometry_tree, 1)
        self.tabs.addTab(page, "C — Geometry")

    def _records(self):
        container = QWidget(); outer = QVBoxLayout(container)
        self.repro_tabs = QTabWidget(); self.repro_tabs.setAccessibleName("Records, comparison, datasets and derived exports")
        outer.addWidget(self.repro_tabs)
        page = QWidget(); layout = QVBoxLayout(page)
        self.kernel_identity = QLabel(); self.kernel_identity.setWordWrap(True)
        self.kernel_identity.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.kernel_identity.setAccessibleName("Expected kernel artifact versus installed and current source identity")
        layout.addWidget(self.kernel_identity)
        self.history = QComboBox(); self.history.setAccessibleName("Completed and loaded immutable record history")
        self.history.currentIndexChanged.connect(self._history_selected); layout.addWidget(self.history)
        self.history.activated.connect(self._history_selected)
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
        layout.addWidget(QLabel("Detached analysis cache — application data, separate from public record history"))
        self.analysis_history = QComboBox(); self.analysis_history.setAccessibleName("Detached analysis cache history")
        self.analysis_history.currentIndexChanged.connect(self._select_analysis)
        layout.addWidget(self.analysis_history)
        self.analysis_tree = tree("Detached analysis lineage and qualification; parent identity is separate from current implementation")
        layout.addWidget(self.analysis_tree, 1)
        self.repro_tabs.addTab(page, "Records")
        self._comparison_panel(); self._dataset_panel(); self._export_panel()
        self.artifacts = ArtifactsPanel("\n\n".join(self._help(name) for name in (
            "artifacts", "derived_artifact", "attempt_receipt", "legacy_analysis", "producer_claim",
            "app04_copy", "analysis_execution", "exact_tokens")))
        self.artifacts.setToolTip(self._help("artifacts"))
        self.artifacts.selection_changed.connect(self._artifact_selection_changed)
        self.artifacts.core_requested.connect(self._load_artifact_core)
        self.repro_tabs.addTab(self.artifacts, "Artifacts")
        self.tabs.addTab(container, "D — Records & Reproducibility")

    def _gather(self):
        draft = deepcopy(self.draft)
        for name in ("eps", "g", "phase_strength", "updates"):
            draft[name] = self.numeric[name].text()
        draft["k"] = [self.numeric[f"k{i}"].text() for i in range(3)]
        draft["omega"] = [[edit.text() for edit in pair] for pair in self.omega_edits]
        draft["update_index"] = self.index_edit.text()
        draft["provenance"] = {k: edit.text() for k, edit in self.provenance.items()}
        draft["provenance"]["source_revision"] = draft["provenance"]["source_revision"] or None
        draft["topology"] = self.topology_combo.currentText()
        draft["readouts"] = ["z_chiral"] if self.output_checks["z_chiral"].isChecked() else []
        draft["diagnostics"] = [n for n in requests.DIAGNOSTICS if self.output_checks[n].isChecked()]
        return draft

    def _render_draft(self):
        self._setting = True
        try:
            for name in ("eps", "g", "phase_strength", "updates"):
                self.numeric[name].setText(self.draft[name])
            for i in range(3): self.numeric[f"k{i}"].setText(self.draft["k"][i])
            if len(self.omega_edits) != len(self.draft["omega"]): self._omega_widgets(len(self.draft["omega"]))
            self.topology_combo.setCurrentText(self.draft["topology"])
            self.q_spin.blockSignals(True); self.q_spin.setValue(len(self.draft["omega"]) // 3); self.q_spin.blockSignals(False)
            for i in range(len(self.draft["omega"])):
                for j in range(2):
                    self.omega_edits[i][j].setText(self.draft["omega"][i][j])
            self.index_edit.setText(self.draft["update_index"])
            for k, edit in self.provenance.items():
                edit.setText(self.draft["provenance"][k] or "")
            self._refresh_observers()
            for name, check in self.output_checks.items():
                check.setChecked(name in self.draft["readouts"] + self.draft["diagnostics"])
        finally:
            self._setting = False
        self._validity()

    def _edited(self, field):
        if self._setting or not hasattr(self, "output_checks"):
            return
        self.draft = requests.mark_edited(self._gather(), field)
        if field in ("omega", "update_index", "topology") and self.checkpoint:
            self.checkpoint = None
            self.checkpoint_label.setText("Checkpoint state edited: new explicit draft; no continuation claim")
            self.checkpoint_reset.setVisible(False)
        self._validity()

    def _validity(self, *_):
        if self._setting or not hasattr(self, "resume_updates"):
            return
        draft = self._gather()
        ring = draft["topology"] == "ring"
        self.topology_banner.setText(f"Topology: {draft['topology']}; q={len(draft['omega']) // 3}; state_size={len(draft['omega'])}. q controls rows, not a kernel parameter.")
        self.seed_button.setEnabled(len(draft["omega"]) == 3)
        for name in self.output_checks:
            check = self.output_checks[name]
            check.setEnabled(not ring and (name not in ("readout_accounting", "historical_alignment") or bool(draft["observers"]) or check.isChecked()))
        try:
            resolved = requests.resolve_draft(draft)
            valid = True
            message = "Complete explicit draft. Kernel validation remains authoritative."
        except (ValueError, TypeError) as exc:
            resolved = None; valid = False; message = str(exc)
        if self.checkpoint and not self.checkpoint_reset.isChecked():
            valid = False; message = "Explicitly acknowledge selected observer initialization for this new checkpoint run."
        self.validation.setText(message)
        for item in (self.run_button, self.zero_button, self.one_button):
            item.setEnabled(valid and not (self.jobs.busy or self.sweep_controller.active))
        self.run_button.setText("Run checkpoint draft" if self.checkpoint else "Run N updates")
        origin = draft["origin"]
        self.origin_label.setText(f"Seed: {'HISTORICAL PRESET '+origin['seed'] if origin['seed'] else 'USER VALUE'}; parameters: {'REFERENCE FILL L01' if origin['parameters'] else 'USER VALUE'}")
        self.preview.setPlainText(json.dumps({"draft": draft, "resolved_binary64_hex": resolved}, indent=2, ensure_ascii=False))
        is_d03 = self.geometry_combo.currentIndex() == 2
        self.construction_combo.setEnabled(is_d03)
        active = requests.D03_FIELDS.get(self.construction_combo.currentText(), ()) if is_d03 else ()
        for name, edit in self.geometry_fields.items(): edit.setEnabled(name in active)
        for widget in (self.section_heights, self.section_input, self.add_section, self.remove_section): widget.setEnabled(self.geometry_combo.currentIndex() == 1)
        try:
            self._geometry_envelope(); geometry_valid = True; self.geometry_validation.setText("Explicit exact request ready; public geometry validation remains authoritative.")
        except ValueError as exc:
            geometry_valid = False; self.geometry_validation.setText(str(exc))
        self.geometry_button.setEnabled(geometry_valid and not (self.jobs.busy or self.sweep_controller.active))
        is_run = not self._artifact_context_active() and self.current is not None and self.current.kind == "KERNEL_RUN_RECORD"
        try:
            requests.integer(self.resume_updates.text(), "resume updates"); resume_valid = True
        except ValueError:
            resume_valid = False
        self.resume_button.setEnabled(is_run and resume_valid and not (self.jobs.busy or self.sweep_controller.active))
        self.checkpoint_button.setEnabled(is_run and not (self.jobs.busy or self.sweep_controller.active))
        self.save_button.setEnabled(self.current is not None and not self._artifact_context_active())
        self.load_button.setEnabled(not (self.jobs.busy or self.sweep_controller.active))
        self.cancel_button.setEnabled(self.jobs.busy or self.sweep_controller.active)
        self.step_preview_button.setEnabled(not (self.jobs.busy or self.sweep_controller.active))
        self.analysis_button.setEnabled(self.analysis_kind.currentIndex() > 0 and not (self.jobs.busy or self.sweep_controller.active))
        self.axial_panel.set_busy(self.jobs.busy or self.sweep_controller.active)
        self.history_button.setEnabled(is_run and not (self.jobs.busy or self.sweep_controller.active))

        for item in (self.sweep_build, self.sweep_load, self.sweep_start, self.sweep_continue, self.dataset_choose):
            item.setEnabled(not (self.jobs.busy or self.sweep_controller.active))
        self.sweep_cancel.setEnabled(self.sweep_controller.active)

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
        if self.sweep_controller.active:
            self._local_error(ValueError("A dataset owns the scientific worker; finish or cancel it first"), "worker ownership")
            return
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
                envelope["payload"]["observer_reset"] = "reinitialize_selected"
            self._submit(envelope, int(envelope["payload"]["resolved"]["updates"]) + 1)
        except Exception as exc:
            self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": "run draft"})

    def _request_geometry(self):
        try: self._submit(self._geometry_envelope())
        except ValueError as exc: self._local_error(exc, "geometry input")

    def _resume(self):
        if self._artifact_context_active(): return
        try:
            n = requests.integer(self.resume_updates.text(), "resume updates")
            self._submit(requests.request("resume", {"record_json": self.current.canonical_json, "updates": self.resume_updates.text()}), len(self.current.samples) + n)
        except Exception as exc:
            self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": "resume"})

    def _prepare_checkpoint(self):
        if self._artifact_context_active(): return
        parent = self.current
        index = self.sample.value()
        sample = parent.samples[index]
        if len(sample["omega"]) > 3000:
            self._local_error(ValueError("Checkpoint exceeds the draft editor resource guard of 1000 triads; the stored record remains inspectable"), "checkpoint draft")
            return
        self.draft = self._gather()
        self.draft["topology"] = parent.data["topology"]
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

    def _completed(self, response, dataset=False):
        if not dataset and self.sweep_controller.handles(response.get("request_id")): return
        result = response["result"]
        if result["result_kind"] == "analysis":
            view = AxialAnalysisView(result) if result['analysis_type'] in requests.AXIAL_TYPES else AnalysisView(result)
            self.analysis_cache.append(view)
            self.artifacts.add_session('AXIAL FLOATING OBSERVATION' if isinstance(view, AxialAnalysisView) else "LEGACY DETACHED ANALYSIS", view)
            self.analysis_history.addItem(f"{result['analysis_type']} · parent {(result['parent_digest'] or 'none')[:12]}")
            self.analysis_history.setCurrentIndex(len(self.analysis_cache) - 1)
            self._select_analysis(len(self.analysis_cache) - 1)
            self.statusBar().showMessage("Detached analysis cached; public record history unchanged")
            self._validity(); return
        view = RecordView(result["canonical_json"])
        if self._artifact_core_pending:
            self._artifact_core_pending = False
            self._artifact_selected = False
            self.repro_tabs.setCurrentIndex(0)
        if result["produced_current"]:
            self.runtime_source = result["source_commit"]
        else:
            self.loaded.add(view.digest)
        if response["operation"] == "resume":
            self.resumed.add(view.digest)
        self.records.append(view)
        self.artifacts.add_session("CORE RUN RECORD" if view.kind == "KERNEL_RUN_RECORD" else "CORE GEOMETRY RECORD", view)
        self._comparison_choices()
        self.history.blockSignals(True)
        self.history.addItem(f"{view.kind} · {view.digest[:12]}")
        self.history.setCurrentIndex(len(self.records) - 1)
        self.history.blockSignals(False)
        self._select_record(view)
        self.statusBar().showMessage("Complete immutable record accepted; draft remains separate")

    def _history_selected(self, index):
        if 0 <= index < len(self.records):
            self._artifact_selected = False
            self._select_record(self.records[index])

    def _select_record(self, view):
        self.play_timer.stop()
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
                self.history_observer.clear(); self.history_observer.addItem("Choose recorded observer")
                self.history_observer.addItems(list(view.samples[0]["observer_results"]))
                self.history_context.setText(f"Selected record {view.digest}; {len(view.samples)} stored samples. Explicit history request uses the entire history.")
            else:
                self.current_geometry = view
                fill_tree(self.geometry_tree, {k: v for k, v in view.data.items() if k not in ("execution_metadata", "paper_references", "implementation")})
                self.geometry_view.set_record(view)
                if view.data["geometry_definition_id"] == "C01": self.fixed_geometry.setText("C01 fixed exact parameters (read-only): " + str(view.data["resolved_parameters"]))
        except Exception as exc:
            self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": "presentation", "qualification": "Record remains accepted; exact inspector and save remain available"})
        self._validity()
        self._analysis_context()

    def _sample_changed(self, index):
        view = self.current_run
        if view is None or not 0 <= index < len(view.samples):
            return
        rows = view.sample_rows(index, self.precision.value())
        self.sample_table.setRowCount(len(rows))
        for i, values in enumerate(rows):
            for j, value in enumerate(values):
                self.sample_table.setItem(i, j, QTableWidgetItem(value))
        self.sample_table.resizeColumnsToContents()
        sample = view.samples[index]
        self.sample_label.setText(f"sample ordinal={index}; actual update_index={sample['update_index']}; raw chirality: {view.missing_series('chirality0')}")
        fill_tree(self.passive_tree, {k: sample[k] for k in ("observer_states", "observer_results", "diagnostics", "raw_readouts")}, self.precision.value())
        self.plots.select_sample(index)
        self.axial_panel.select_sample(view.digest, index)
        if self.analysis_current and self.analysis_current.result["parent_digest"] == view.digest: self.history_plot.select_sample(index)
        self._analysis_context()

    def _identity(self):
        try:
            installed = metadata.version("trioctagon-physics")
        except metadata.PackageNotFoundError:
            installed = "missing"
        self.kernel_identity.setText(f"Preferred locked kernel archive: {self.lock['artifact_filename']}\nPreferred archive SHA-256: {self.lock['artifact_sha256']}\nCertified reconstruction also accepted under lock-v2 equivalence; this is not an installed-archive identity query.\nExpected source: {self.lock['source_commit']}\nInstalled distribution version: {installed}\nCurrent source identity: {self.runtime_source}\nApplication: trioctagon-scientific-ui 0.2.0; separate software identity")
        if self._artifact_context_active():
            self.identity.setText("Artifact inspection — " + self.artifacts.heading.text() + "\nUI: trioctagon-scientific-ui 0.2.0 · Analysis loader: independent installed pin 0.1.1 · Core kernel: separate Records identity")
            return
        if self.current is None:
            self.identity.setText("Draft configuration · no completed record · geometry and dynamics remain independent")
        else:
            view = self.current
            state = "Saved" if view.digest in self.saved else "Loaded validated record — not saved by this session" if view.digest in self.loaded else "Completed record — UNSAVED"
            self.identity.setText(f"{view.kind} · source {view.data['implementation']['commit'][:12]} · digest {view.digest[:16]} · {state}\nDraft edits prepare a new run; recorded inputs stay unchanged.")

    def _cancelled(self):
        self._artifact_core_pending = False
        self.axial_panel.status.setText('Cancelled; previous completed axial cache retained')
        self.statusBar().showMessage("Cancelled; previous completed records preserved")

    def _failed(self, error):
        if error.get('operation') == 'passive_analysis': self.axial_panel.show_error(error.get('message', 'Worker failed'))
        if self._artifact_core_pending:
            from trioctagon_ui.artifact_loading import bounded_text
            self.artifacts.status.setText(bounded_text("Core artifact refused: " + error.get("message", "")))
        self._artifact_core_pending = False
        if self.sweep_controller.handles(error.get("request_id")): return
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
        if self._artifact_context_active(): return
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

    def _local_error(self, exc, operation):
        self._failed({"exception_class": type(exc).__name__, "message": str(exc), "operation": operation})

    def _omega_widgets(self, count):
        while self.omega_form.rowCount(): self.omega_form.removeRow(0)
        self.omega_edits = []
        for i in range(count):
            pair = []
            for part in ("re", "im"):
                edit = QLineEdit(); edit.setAccessibleName(f"Omega{i} {part} authoritative input")
                edit.textChanged.connect(lambda _: self._edited("omega"))
                self.omega_form.addRow(f"Omega{i}.{part}", edit); pair.append(edit)
            self.omega_edits.append(pair)

    def _resize_rows(self, q):
        if self._setting: return
        draft = self._gather(); old_q = len(draft["omega"]) // 3
        try:
            resized = requests.resize_ring(draft, q)
        except ValueError:
            if QMessageBox.question(self, "Discard scientific input rows?", f"Reducing q from {old_q} to {q} discards nonblank Omega values. Confirm this explicit draft edit?") != QMessageBox.StandardButton.Yes:
                self.q_spin.blockSignals(True); self.q_spin.setValue(old_q); self.q_spin.blockSignals(False); return
            resized = requests.resize_ring(draft, q, discard_confirmed=True)
        self.draft = resized; self.checkpoint = None; self.checkpoint_reset.setVisible(False)
        self._render_draft()

    def _add_observer(self, descriptor):
        self.draft = self._gather(); self.draft["observers"].append(deepcopy(descriptor))
        self._refresh_observers(len(self.draft["observers"]) - 1); self._validity()

    def _refresh_observers(self, index=None):
        if index is None: index = self.observer_list.currentRow()
        self.observer_list.blockSignals(True); self.observer_list.clear()
        for value in self.draft["observers"]:
            self.observer_list.addItem("HISTORICAL PRESET " + value["name"] if value["mode"] == "preset" else "CUSTOM " + (value["observer_id"] or "(ID required)"))
        index = min(max(0, index), len(self.draft["observers"]) - 1)
        self.observer_list.setCurrentRow(index); self.observer_list.blockSignals(False)
        self._observer_selected(index)

    def _observer_selected(self, index):
        self._observer_rendering = True
        try:
            while self.observer_form.rowCount(): self.observer_form.removeRow(0)
            self.observer_fields = {}
            if not 0 <= index < len(self.draft["observers"]):
                self.convert_observer.setEnabled(False); return
            original = self.draft["observers"][index]
            preset = original["mode"] == "preset"
            value = deepcopy(self.help["observer_presets"][original["name"]]) if preset else original
            self.convert_observer.setEnabled(preset)
            self.observer_form.addRow(QLabel(("HISTORICAL PRESET — read-only" if preset else "CUSTOM / USER-SUPPLIED") + "; variant=" + value["variant"]))
            self.observer_form.addRow(QLabel("Origin: " + str(value["origin"] or "manual")))
            paths = [("observer_id",), ("initialization",), ("dt",)]
            paths += [("clock", k) for k in ("q", "N", "t", "q_step")]
            paths += [("config", k) for k in requests.CONFIG_FIELDS[value["variant"]]]
            if value["memory"] is not None: paths.append(("memory", "m"))
            paths += [("provenance", k) for k in ("source_id", "source_revision", "locator", "notes")]
            for path in paths:
                text = value[path[0]] if len(path) == 1 else value[path[0]][path[1]]
                name = ".".join(path)
                if name == "initialization":
                    edit = QComboBox(); edit.addItems(["Choose initialization", "recomputed", "historical_constructor_zero"])
                    edit.setCurrentIndex(0 if not text else edit.findText(text)); edit.setEnabled(not preset)
                    edit.currentTextChanged.connect(lambda v, p=path: self._observer_edit(p, "" if v == "Choose initialization" else v))
                else:
                    edit = QLineEdit(text or ""); edit.setReadOnly(preset)
                    edit.textChanged.connect(lambda v, p=path: self._observer_edit(p, v))
                edit.setAccessibleName("Observer " + name + (" historical read-only" if preset else " authoritative input"))
                self.observer_fields[name] = edit; self.observer_form.addRow(name, edit)
            self.observer_form.addRow(QLabel("constructor-zero requires update_index=0 and EMA m=0. EMA requires |m|<=1. Kernel validation remains final. No theta wrapping."))
        finally: self._observer_rendering = False

    def _observer_edit(self, path, value):
        if self._observer_rendering: return
        index = self.observer_list.currentRow()
        if not 0 <= index < len(self.draft["observers"]): return
        observer = self.draft["observers"][index]
        if observer["mode"] != "custom": return
        if path == ("provenance", "source_revision") and not value: value = None
        if len(path) == 1: observer[path[0]] = value
        else: observer[path[0]][path[1]] = value
        self.observer_list.item(index).setText("CUSTOM " + (observer["observer_id"] or "(ID required)"))
        self._validity()

    def _convert_observer(self):
        index = self.observer_list.currentRow()
        if 0 <= index < len(self.draft["observers"]):
            self.draft["observers"][index] = requests.preset_to_custom(self.draft["observers"][index])
            self._refresh_observers(index); self._validity()

    def _remove_observer(self):
        index = self.observer_list.currentRow()
        if 0 <= index < len(self.draft["observers"]):
            self.draft["observers"].pop(index); self._refresh_observers(index); self._validity()

    def _clear_passive(self):
        self.draft = self._gather()
        for field in ("observers", "readouts", "diagnostics"): self.draft[field] = []
        self._render_draft()

    def _geometry_envelope(self):
        if self.geometry_combo.currentIndex() == 1:
            return requests.geometry_request("C01", {"section_heights": [self.section_heights.item(i).text() for i in range(self.section_heights.count())]})
        if self.geometry_combo.currentIndex() == 2:
            construction = self.construction_combo.currentText()
            return requests.geometry_request("D03", {"construction": construction, **{k: self.geometry_fields[k].text() for k in requests.D03_FIELDS.get(construction, ())}})
        raise ValueError("Choose a geometry definition explicitly")

    def _add_section(self):
        item = QListWidgetItem(self.section_input.text()); item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
        self.section_heights.addItem(item); self._validity()

    def _remove_section(self):
        index = self.section_heights.currentRow()
        if index >= 0: self.section_heights.takeItem(index)
        self._validity()

    def _play(self):
        if self.current_run is None or self.reduced_motion.isChecked(): return
        self.play_timer.start(round(1000 / self.playback_rate.value()))

    def _play_tick(self):
        if self.sample.value() >= self.sample.maximum(): self.play_timer.stop()
        else: self.sample.setValue(self.sample.value() + 1)

    def _precision_changed(self, *_):
        if self.current_run is not None: self._sample_changed(self.sample.value())
        if self.analysis_current is not None: self._select_analysis(self.analysis_history.currentIndex())
        if self.comparison is not None: self._comparison_table()

    def _analysis_template(self):
        if self.analysis_kind.currentIndex() > 0:
            self.analysis_inputs.setPlainText(json.dumps(requests.analysis_template(self.analysis_kind.currentText()), indent=2))
        else: self.analysis_inputs.clear()
        self._validity()

    def _analysis_context(self, *_):
        if not hasattr(self, "analysis_source"): return
        if self.analysis_source.currentIndex() == 0:
            self.analysis_source_label.setText("Explicit scratchpad; no selected sample is used")
        elif self.current is not None and self.current.kind == "KERNEL_RUN_RECORD":
            self.analysis_source_label.setText(f"EXPLICIT STORED SOURCE: parent {self.current.digest}; sample ordinal {self.sample.value()}. Stored Omega/index override the scratchpad state; other fields remain explicit.")
        else: self.analysis_source_label.setText("Stored source selected, but no RunRecord is selected. Analysis will be refused.")

    def _copy_analysis_dynamics(self):
        try:
            inputs = json.loads(self.analysis_inputs.toPlainText()); draft = self._gather()
            if "omega" in inputs: inputs["omega"] = draft["omega"]
            if "state" in inputs: inputs["state"] = {"omega": draft["omega"], "update_index": draft["update_index"]}
            if "parameters" in inputs: inputs["parameters"] = {k: draft[k] for k in ("eps", "g", "phase_strength", "k")}
            if "topology" in inputs: inputs["topology"] = draft["topology"]
            self.analysis_inputs.setPlainText(json.dumps(inputs, indent=2))
        except (ValueError, TypeError) as exc: self._local_error(exc, "scratchpad copy")

    def _copy_analysis_observer(self):
        try:
            index = self.observer_list.currentRow()
            if not 0 <= index < len(self.draft["observers"]): raise ValueError("Select an observer explicitly")
            observer = self.draft["observers"][index]
            if observer["mode"] == "preset": observer = requests.preset_to_custom(observer)
            inputs = json.loads(self.analysis_inputs.toPlainText())
            for field in ("clock", "config", "memory", "dt"):
                if field in inputs: inputs[field] = deepcopy(observer[field])
            self.analysis_inputs.setPlainText(json.dumps(inputs, indent=2))
        except (ValueError, TypeError) as exc: self._local_error(exc, "scratchpad observer copy")

    def _analysis_source_record(self):
        if self._artifact_context_active(): raise ValueError('Select a Core RunRecord explicitly in Records first')
        if self.current is None or self.current.kind != "KERNEL_RUN_RECORD": raise ValueError("Explicitly select a RunRecord first")
        return {"mode": "record", "record_json": self.current.canonical_json, "sample_index": str(self.sample.value())}

    def _request_analysis(self):
        try:
            source = self._analysis_source_record() if self.analysis_source.currentIndex() == 1 else {"mode": "explicit"}
            self._submit(requests.analysis_request(self.analysis_kind.currentText(), json.loads(self.analysis_inputs.toPlainText()), source=source))
        except (ValueError, TypeError) as exc: self._local_error(exc, "passive_analysis")

    def _step_preview(self):
        draft = self._gather()
        inputs = {"state": {"omega": draft["omega"], "update_index": draft["update_index"]}, "parameters": {k: draft[k] for k in ("eps", "g", "phase_strength", "k")}, "topology": draft["topology"]}
        self._submit(requests.analysis_request("step_preview", inputs))

    def _request_history(self):
        try:
            kind = self.history_kind.currentText()
            if self.history_observer.currentIndex() <= 0: raise ValueError("Choose a recorded observer explicitly")
            inputs = {"observer_id": self.history_observer.currentText()}
            if kind == "direct_history_coordinates": inputs["key"] = self.history_key.currentText()
            else:
                inputs.update(kappa_source=self.kappa_source.currentText(), N=self.history_fields["N"].text())
                if kind == "history_torus_coordinates": inputs.update(R=self.history_fields["R"].text(), r_max=self.history_fields["r_max"].text())
            self._submit(requests.analysis_request(kind, inputs, source=self._analysis_source_record()))
        except ValueError as exc: self._local_error(exc, "history display")

    def _accept_axial_saved(self, view):
        self.analysis_cache.append(view)
        self.artifacts.add_session('AXIAL UNAUTHENTICATED SAVED OBSERVATION', view)
        self.analysis_history.addItem(view.result['analysis_type'] + ' · unauthenticated saved observation')
        self.analysis_history.setCurrentIndex(len(self.analysis_cache) - 1)
        self._select_analysis(len(self.analysis_cache) - 1)

    def _select_analysis(self, index):
        if not 0 <= index < len(self.analysis_cache): return
        view = self.analysis_cache[index]; self.analysis_current = view
        self.analysis_table.setVisible(not isinstance(view, AxialAnalysisView))
        if isinstance(view, AxialAnalysisView):
            self.axial_panel.show_view(view)
            self.history_plot.set_analysis(view)
            fill_tree(self.analysis_tree, {'axial_observation': view.artifact['content_sha256'],
                'location': 'Observers & Diagnostics / Axial Observables', 'evidence': 'UNAUTHENTICATED SAVED OBSERVATION' if view.saved_import else 'FLOATING_OBSERVATION'})
            return
        fill_tree(self.analysis_tree, view.result, self.precision.value())
        rows = view.rows(self.precision.value()); self.analysis_table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row): self.analysis_table.setItem(i, j, QTableWidgetItem(value))
        self.analysis_table.resizeColumnsToContents()
        self.history_plot.set_analysis(view)
        if self.current is not None and view.result["parent_digest"] == self.current.digest:
            self.history_plot.select_sample(self.sample.value())

    def _dataset_panel(self):
        page = QWidget(); layout = QVBoxLayout(page)
        layout.addWidget(QLabel("Finite parameter cases; fixed State/topology/updates/outputs. Enumeration only; no scientific ranking."))
        self.sweep_dimensions = QPlainTextEdit("{}"); self.sweep_dimensions.setMaximumHeight(110)
        self.sweep_dimensions.setAccessibleName("Explicit sweep dimensions JSON; eps, g, phase_strength, k0, k1, k2")
        self.sweep_dimensions.setPlaceholderText('{"g":{"values":["0.1","0.2"]}} or {"eps":{"start":"0.01","stop":"0.05","count":"3"}}')
        layout.addWidget(self.sweep_dimensions)
        policy = QHBoxLayout(); layout.addLayout(policy)
        self.sweep_guard = QSpinBox(); self.sweep_guard.setRange(1, 100000); self.sweep_guard.setValue(sweeps.DEFAULT_CASE_GUARD)
        self.sweep_guard.setAccessibleName("UI RESOURCE GUARD case count; not a scientific domain")
        policy.addWidget(QLabel("UI RESOURCE GUARD")); policy.addWidget(self.sweep_guard)
        self.sweep_override = QCheckBox("Explicitly allow larger resource guard"); self.sweep_override.setAccessibleName("Acknowledge larger sweep UI resource guard")
        self.sweep_stop_failure = QCheckBox("Stop after first failed case"); self.sweep_stop_failure.setAccessibleName("Sweep failure policy; unchecked continues later cases")
        policy.addWidget(self.sweep_override); policy.addWidget(self.sweep_stop_failure)
        self.sweep_build = button("Rebuild sweep plan from current draft", "Freeze explicit current draft and expand sweep values", self._build_sweep)
        layout.addWidget(self.sweep_build)
        self.sweep_preview = readonly_text("Frozen sweep base, fixed outputs, ordered decimal and binary64 values")
        self.sweep_preview.setMaximumHeight(190); layout.addWidget(self.sweep_preview)
        self.dataset_directory = QLineEdit(); self.dataset_directory.setAccessibleName("Chosen dataset directory; new datasets require an empty directory")
        row = QHBoxLayout(); layout.addLayout(row); row.addWidget(self.dataset_directory)
        self.dataset_choose = button("Choose dataset directory", "Choose empty dataset directory", self._choose_dataset)
        row.addWidget(self.dataset_choose)
        actions = QHBoxLayout(); layout.addLayout(actions)
        self.sweep_start = button("Start frozen sweep", "Start finite sequential sweep", self._start_sweep)
        self.sweep_load = button("Load dataset manifest", "Load dataset for explicit validation and continuation", self._load_dataset)
        self.sweep_continue = button("Continue dataset", "Validate saved cases and continue dataset", self._continue_sweep)
        self.sweep_cancel = button("Cancel sweep", "Cancel active case and preserve complete records", self.sweep_controller.cancel)
        for item in (self.sweep_start, self.sweep_load, self.sweep_continue, self.sweep_cancel): actions.addWidget(item)
        self.dataset_progress = QLabel("No frozen dataset plan"); self.dataset_progress.setWordWrap(True)
        self.dataset_progress.setAccessibleName("Completed case count, total cases and active case; individual run indeterminate")
        layout.addWidget(self.dataset_progress)
        self.dataset_table = QTableWidget(0, 5)
        self.dataset_table.setHorizontalHeaderLabels(["Case / request identity", "Explicit values / binary64", "Status", "Record digest / path", "Error / rerun reason"])
        self.dataset_table.setAccessibleName("Every dataset case, including failed, cancelled and not-run cases")
        layout.addWidget(self.dataset_table)
        self.repro_tabs.addTab(page, "Datasets")

    def _build_sweep(self):
        try:
            if self.sweep_controller.active: raise ValueError("Cancel or finish the active dataset before rebuilding its plan")
            if self.checkpoint: raise ValueError("Use an explicit new-run draft for a sweep, not checkpoint transport")
            self.sweep_plan = sweeps.make_plan(self._gather(), json.loads(self.sweep_dimensions.toPlainText()), self.lock,
                stop_after_failure=self.sweep_stop_failure.isChecked(), case_guard=self.sweep_guard.value(), override_ack=self.sweep_override.isChecked())
            self._show_dataset(self.sweep_plan)
        except Exception as exc: self._local_error(exc, "sweep preview")

    def _choose_dataset(self):
        path = QFileDialog.getExistingDirectory(self, "Choose empty directory for a new dataset")
        if path: self.dataset_directory.setText(path)

    def _confirm_sweep(self, manifest):
        return not manifest["confirmation_required"] or QMessageBox.question(self, "Application sweep safeguard",
            f"{manifest['case_count']:,} cases; {manifest['total_requested_samples']:,} requested samples. Above 100 cases or 100,000 samples requires confirmation. These are application safeguards. Continue?") == QMessageBox.StandardButton.Yes

    def _start_sweep(self):
        try:
            if self.sweep_plan is None: raise ValueError("Build an explicit frozen sweep plan first")
            if not self.dataset_directory.text().strip(): raise ValueError("Choose an empty dataset directory")
            if not self._confirm_sweep(self.sweep_plan): return
            self.sweep_controller.create(self.sweep_plan, self.dataset_directory.text())
            self.sweep_controller.start(confirmed=True)
        except Exception as exc: self._local_error(exc, "start dataset")

    def _load_dataset(self):
        path, _ = QFileDialog.getOpenFileName(self, "Load application sweep manifest", "", "JSON (*.json)")
        if not path: return
        try:
            self.sweep_controller.load(path); self.dataset_directory.setText(str(Path(path).parent))
            self.sweep_plan = None
        except Exception as exc: self._local_error(exc, "load dataset")

    def _continue_sweep(self):
        try:
            manifest = self.sweep_controller.manifest
            if manifest is None: raise ValueError("Load a dataset first")
            if self._confirm_sweep(manifest): self.sweep_controller.start(confirmed=True)
        except Exception as exc: self._local_error(exc, "continue dataset")

    def _show_dataset(self, manifest):
        completed = sum(case["status"] == "completed" for case in manifest["cases"])
        current = self.sweep_controller.index
        self.dataset_progress.setText(f"{completed} / {manifest['case_count']} cases completed; total requested samples={manifest['total_requested_samples']}; active case={current + 1 if current is not None else 'none'}. Individual run progress is indeterminate.")
        self.sweep_preview.setPlainText(json.dumps({k: v for k, v in manifest.items() if k != "cases"}, indent=2, ensure_ascii=False))
        self.dataset_table.setRowCount(len(manifest["cases"]))
        for i, case in enumerate(manifest["cases"]):
            values = [case["case_id"] + "\n" + case["request_sha256"], json.dumps({"text": case["substituted_values"], "f64": case["resolved_values"]}),
                case["status"], str(case["record_digest"]) + "\n" + str(case["record_path"]), json.dumps(case["error"]) if case["error"] else case["requires_rerun_reason"] or ""]
            for j, text in enumerate(values): self.dataset_table.setItem(i, j, QTableWidgetItem(text))

    def _dataset_changed(self):
        if self.sweep_controller.manifest: self._show_dataset(self.sweep_controller.manifest)
        self._validity()

    def _dataset_record(self, response):
        if not any(v.digest == response["result"]["deterministic_sha256"] for v in self.records): self._completed(response, dataset=True)

    def _cancel_job(self):
        if self.sweep_controller.active: self.sweep_controller.cancel()
        else: self.jobs.cancel()

    def _comparison_panel(self):
        page = QWidget(); layout = QVBoxLayout(page)
        layout.addWidget(QLabel("Two immutable records; descriptive stored differences only. Exact update-index alignment, no interpolation or resampling. Separate geometry frames/cameras."))
        self.compare_a = QComboBox(); self.compare_b = QComboBox()
        self.compare_a.setAccessibleName("Comparison record A from completed, loaded or dataset records")
        self.compare_b.setAccessibleName("Comparison record B from completed, loaded or dataset records")
        row = QHBoxLayout(); layout.addLayout(row); row.addWidget(self.compare_a); row.addWidget(self.compare_b)
        self.compare_channels = QLineEdit(); self.compare_channels.setPlaceholderText("Explicit shared channel indices, e.g. [0,1,2]; blank compares metadata/passive paths")
        self.compare_channels.setAccessibleName("Explicit shared Omega channels as JSON indices; no ring-sector inference")
        layout.addWidget(self.compare_channels)
        self.compare_button = button("Compare selected records", "Compare exactly two immutable records", self._compare_records)
        layout.addWidget(self.compare_button)
        self.compare_tree = tree("Side-by-side record metadata, selections, incidence and provenance")
        layout.addWidget(self.compare_tree, 1)
        self.compare_table = QTableWidget(0, 5); self.compare_table.setHorizontalHeaderLabels(["Stored update_index", "Path", "A", "B", "B - A: display only"])
        self.compare_table.setAccessibleName("Exact aligned stored values and display-only deltas; not recorded fields stay missing")
        layout.addWidget(self.compare_table, 1)
        self.compare_plot = ComparisonPlot(); layout.addWidget(self.compare_plot, 1)
        geometry = QHBoxLayout(); layout.addLayout(geometry)
        self.compare_geometry_a = GeometryView(); self.compare_geometry_b = GeometryView()
        self.compare_geometry_a.setAccessibleName("Geometry A in independent frames and camera")
        self.compare_geometry_b.setAccessibleName("Geometry B in independent frames and camera")
        geometry.addWidget(self.compare_geometry_a); geometry.addWidget(self.compare_geometry_b)
        self.compare_geometry_a.hide(); self.compare_geometry_b.hide()
        self.repro_tabs.addTab(page, "Compare")

    def _comparison_choices(self):
        for combo in (self.compare_a, self.compare_b):
            old = combo.currentIndex(); combo.blockSignals(True); combo.clear(); combo.addItem("Choose record explicitly")
            combo.addItems([f"{i + 1}: {v.kind} {v.digest[:16]}" for i, v in enumerate(self.records)])
            combo.setCurrentIndex(max(0, old)); combo.blockSignals(False)

    def _compare_records(self):
        try:
            indices = [combo.currentIndex() - 1 for combo in (self.compare_a, self.compare_b)]
            if any(i < 0 for i in indices): raise ValueError("Explicitly choose record A and record B")
            channels = json.loads(self.compare_channels.text() or "[]")
            if not isinstance(channels, list): raise ValueError("Shared channels require a JSON list")
            self.comparison = ComparisonView(*(self.records[i] for i in indices), tuple(channels))
            fill_tree(self.compare_tree, {k: v for k, v in self.comparison.result.items() if k != "rows"}, self.precision.value())
            is_run = self.comparison.a.kind == "KERNEL_RUN_RECORD"
            self.compare_plot.setVisible(is_run); self.compare_table.setVisible(is_run)
            for widget, record in ((self.compare_geometry_a, self.comparison.a), (self.compare_geometry_b, self.comparison.b)):
                widget.setVisible(not is_run)
                if not is_run: widget.set_record(record)
            if is_run: self.compare_plot.set_comparison(self.comparison)
            self._comparison_table()
        except Exception as exc: self._local_error(exc, "record comparison")

    def _comparison_table(self):
        rows = self.comparison.rows(self.precision.value()); self.compare_table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, text in enumerate(row): self.compare_table.setItem(i, j, QTableWidgetItem(text))

    def _export_panel(self):
        page = QWidget(); layout = QVBoxLayout(page)
        label = QLabel(exports.QUALIFICATION); label.setWordWrap(True); layout.addWidget(label)
        self.csv_groups = {}
        row = QHBoxLayout(); layout.addLayout(row)
        for name in exports.FIELD_GROUPS:
            check = QCheckBox(name); check.setAccessibleName("CSV stored field group " + name); row.addWidget(check); self.csv_groups[name] = check
        self.csv_selection = QComboBox(); self.csv_selection.addItems(["all", "range", "ordinals"])
        self.csv_selection.setAccessibleName("CSV sample selection: all, inclusive range, or explicit ordinals")
        self.csv_ordinals = QLineEdit(); self.csv_ordinals.setPlaceholderText('range: {"start":0,"stop":2}; ordinals: [0,2]')
        self.csv_ordinals.setAccessibleName("Explicit CSV range or sample ordinal JSON; no automatic decimation")
        layout.addWidget(self.csv_selection); layout.addWidget(self.csv_ordinals)
        self.csv_button = button("Export selected RunRecord as CSV + sidecar", "Export stored sample CSV with exact hex companions and provenance", self._export_csv)
        layout.addWidget(self.csv_button)
        self.export_view = QComboBox(); self.export_view.addItems(["Stored time series", "Stored complex planes", "Stored raw chirality", "Stored geometry", "Detached history", "Comparison series", "Comparison geometry A", "Comparison geometry B"])
        self.export_view.setAccessibleName("Already-created cached view to export with provenance")
        layout.addWidget(self.export_view)
        self.png_button = button("Export current view as PNG + sidecar", "Export cached PNG with provenance", lambda: self._export_image("png"))
        self.svg_button = button("Export current view as SVG + sidecar", "Export cached SVG with provenance", lambda: self._export_image("svg"))
        layout.addWidget(self.png_button); layout.addWidget(self.svg_button)
        self.export_result = QLabel("No derived export written"); self.export_result.setWordWrap(True)
        self.export_result.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse); self.export_result.setAccessibleName("Derived export artifact and provenance sidecar paths")
        layout.addWidget(self.export_result); layout.addStretch()
        self.repro_tabs.addTab(page, "Exports")

    def _export_csv(self):
        if self._artifact_context_active(): return
        try:
            if self.current is None or self.current.kind != "KERNEL_RUN_RECORD": raise ValueError("Select a RunRecord explicitly for CSV")
            mode = self.csv_selection.currentText(); selection = {"mode": mode}
            if mode == "range": selection.update(json.loads(self.csv_ordinals.text()))
            elif mode == "ordinals": selection["ordinals"] = json.loads(self.csv_ordinals.text())
            groups = [key for key, check in self.csv_groups.items() if check.isChecked()]
            path, _ = QFileDialog.getSaveFileName(self, "Derived CSV and mandatory provenance sidecar", "samples.csv", "CSV (*.csv)")
            if path: self._export_done(exports.export_csv(self.current, path, groups, selection, precision=self.precision.value(), kernel_identity=self.lock))
        except Exception as exc: self._local_error(exc, "CSV export")

    def _image_source(self):
        if self._artifact_context_active(): raise ValueError("Artifacts have no figure export source")
        name = self.export_view.currentText()
        context = {"view_type": name, "parents": [], "display_precision": self.precision.value(), "visible_series": [], "selection": None}
        if name in ("Stored time series", "Stored complex planes", "Stored raw chirality"):
            if self.current_run is None: raise ValueError("Create or load a RunRecord first")
            index = ("Stored time series", "Stored complex planes", "Stored raw chirality").index(name)
            context.update(self.plots.export_state()); context["selection"] = {"sample_ordinal": self.sample.value(), "update_index": self.current_run.samples[self.sample.value()]["update_index"], "plotted_samples": "all stored samples"}
            context["parents"] = [exports.parent_identity(self.current_run)]
            if index == 2: context["visible_series"] = ["Cx", "Cy", "Cz"] if "chirality0" in self.current_run.series else []
            figure = self.plots.figures[index]
        elif name == "Stored geometry":
            if self.current_geometry is None: raise ValueError("Create or load geometry first")
            figure = self.geometry_view.figure; context.update(self.geometry_view.export_state()); context["parents"] = [exports.parent_identity(self.current_geometry)]
        elif name == "Detached history":
            if self.analysis_current is None or self.analysis_current.coordinates is None: raise ValueError("Explicitly create/select a coordinate analysis first")
            figure = self.history_plot.figure; context["analysis_lineage"] = plain(self.analysis_current.result)
            result = self.analysis_current.result
            if result["parent_digest"]: context["parents"] = [{"digest": result["parent_digest"], "source_commit": result["parent_source_commit"], "record_type": "KERNEL_RUN_RECORD"}]
            context["selection"] = {"supplied_history": "entire cached history", "highlighted_sample_ordinal": self.sample.value() if self.current_run and result["parent_digest"] == self.current_run.digest else None}
        else:
            if self.comparison is None: raise ValueError("Create a two-record comparison first")
            context["parents"] = [exports.parent_identity(v) for v in (self.comparison.a, self.comparison.b)]
            if name == "Comparison series":
                if self.comparison.a.kind != "KERNEL_RUN_RECORD": raise ValueError("Select a run comparison")
                figure = self.compare_plot.figure; context["visible_series"] = [self.compare_plot.selector.currentText()]; context["selection"] = {"exact_common_update_indices": plain(self.comparison.result["indices_common"])}
            else:
                if self.comparison.a.kind != "GEOMETRY_RECORD": raise ValueError("Select a geometry comparison")
                widget = self.compare_geometry_a if name.endswith("A") else self.compare_geometry_b
                figure = widget.figure; context.update(widget.export_state())
        return figure, context

    def _export_image(self, extension):
        try:
            figure, context = self._image_source()
            path, _ = QFileDialog.getSaveFileName(self, "Derived presentation and mandatory provenance sidecar", "view." + extension, extension.upper() + " (*." + extension + ")")
            if path: self._export_done(exports.export_image(figure, path, context))
        except Exception as exc: self._local_error(exc, "image export")

    def _export_done(self, result):
        self.export_result.setText("Derived export complete:\n" + result["artifact"] + "\n" + result["sidecar"])

    def closeEvent(self, event):
        self.play_timer.stop()
        if self.sweep_controller.active: self.sweep_controller.cancel()
        if self.jobs.busy:
            self.jobs.cancel()
            event.ignore()
            self.jobs.cancelled.connect(self.close)
            return
        event.accept()
