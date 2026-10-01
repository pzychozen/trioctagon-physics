"""Read-only artifact UI. No worker, coordinator or scientific execution controls."""
from collections.abc import Mapping
from dataclasses import dataclass
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (QAbstractItemView, QCheckBox, QFileDialog, QHBoxLayout, QLabel,
    QListWidget, QPlainTextEdit, QPushButton, QSpinBox, QTableWidget, QTableWidgetItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget, QTabWidget)
from .artifact_loading import (ArtifactLibrary, CoreArtifactCandidate, LoadedAttemptArtifact,
    LoadedDerivedArtifact, MAX_RAW_TEXT_PREVIEW_BYTES, bounded_text, copy_artifact)
from .artifact_views import AttemptReceiptView, DerivedArtifactView
from .historical_loading import LoadedHistoricalResult, LoadedHistoricalReceipt
from .historical_views import HistoricalResultView, HistoricalReceiptView, stored_rows


@dataclass(frozen=True)
class RejectedImport:
    selected_file: str
    diagnostic: str


class ArtifactTree(QTreeWidget):
    """Lazy, paginated nodes prevent large saved manifests exploding the widget."""
    def __init__(self):
        super().__init__()
        self.setHeaderLabels(["Field", "Stored value / claim"])
        self.setColumnWidth(0, 280)
        self.itemExpanded.connect(self.expand_node)

    def node(self, name, value):
        container = isinstance(value, (Mapping, tuple, list))
        node = QTreeWidgetItem([bounded_text(name), f"{len(value)} entries" if container else bounded_text(value)])
        if container and value:
            node.payload = value
            node.offset = 0
            node.addChild(QTreeWidgetItem(["Expand to inspect", ""]))
        return node

    def show_panels(self, panels):
        self.clear()
        for key, value in panels.items():
            self.addTopLevelItem(self.node(key, value))

    def expand_node(self, node):
        if not hasattr(node, "payload"):
            return
        value, start = node.payload, node.offset
        del node.payload
        node.takeChildren()
        # Iterate only the displayed page, including mappings, without copying it.
        import itertools
        entries = value.items() if isinstance(value, Mapping) else enumerate(value)
        for key, child in itertools.islice(entries, start, start + 128):
            node.addChild(self.node(key, child))
        if start + 128 < len(value):
            more = QTreeWidgetItem(["More entries (expand)", ""])
            more.payload, more.offset = value, start + 128
            more.addChild(QTreeWidgetItem(["Expand to inspect", ""]))
            node.addChild(more)


class HistoricalInspector(QTabWidget):
    """Separate result/receipt presentation; bounded row selection never adds terminal."""
    def __init__(self):
        super().__init__()
        self.view = None

    @staticmethod
    def table():
        table = QTableWidget(0, 3)
        table.setHorizontalHeaderLabels(["Stored field / ordered component", "Exact token / stored value", "Decimal display only"])
        table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        table.setMinimumHeight(180)
        return table

    @staticmethod
    def fill(table, value, precision):
        rows = tuple(stored_rows(value, precision))
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, text in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(text))
        table.resizeColumnsToContents()

    def show_view(self, view):
        while self.count():
            widget = self.widget(0); self.removeTab(0); widget.deleteLater()
        self.view = view
        self.run_table = self.terminal_table = self.row_selector = None
        values = QWidget(); layout = QVBoxLayout(values)
        self.summary = QLabel(view.summary); self.summary.setWordWrap(True)
        self.summary.setTextFormat(Qt.TextFormat.PlainText); layout.addWidget(self.summary)
        self.precision = QSpinBox(); self.precision.setRange(1, 17); self.precision.setValue(17)
        self.precision.setPrefix("Decimal display precision: "); layout.addWidget(self.precision)
        self.value_table = self.table(); layout.addWidget(self.value_table)
        self.addTab(values, "Stored result" if type(view) is HistoricalResultView else "Attempt receipt")
        self.precision.setVisible(type(view) is HistoricalResultView)
        if type(view) is HistoricalResultView:
            self.note = QLabel(view.note); self.note.setWordWrap(True)
            self.note.setTextFormat(Qt.TextFormat.PlainText); layout.insertWidget(1, self.note)
            if view.terminal is not None:
                rows = QWidget(); row_layout = QVBoxLayout(rows)
                self.row_selector = QSpinBox(); self.row_selector.setRange(0, max(0, len(view.run_rows)-1))
                self.row_selector.setPrefix("Historical row ordinal: ")
                self.row_selector.setEnabled(bool(view.run_rows)); row_layout.addWidget(self.row_selector)
                label = QLabel("Rows 0…N−1 only. Constructor readout caches are labelled HISTORICAL_CONSTRUCTOR_ZERO; later recorded readouts RECOMPUTED." if view.run_rows else "N=0 — empty rows; constructor terminal is in its separate tab.")
                label.setWordWrap(True); row_layout.addWidget(label)
                self.run_table = self.table(); row_layout.addWidget(self.run_table)
                self.addTab(rows, f"Historical rows ({len(view.run_rows)})")
                self.row_selector.valueChanged.connect(self.render)
                terminal = QWidget(); terminal_layout = QVBoxLayout(terminal)
                terminal_layout.addWidget(QLabel("HISTORICALLY UNSTORED TERMINAL STATE — separate from rows"))
                self.terminal_table = self.table(); terminal_layout.addWidget(self.terminal_table)
                self.addTab(terminal, "Historically unstored terminal state")
            qualifications = QPlainTextEdit(); qualifications.setReadOnly(True)
            qualifications.setPlainText("FROZEN HISTORICAL QUALIFICATIONS\n\n" + "\n".join(
                f"{k}: {', '.join(v) if isinstance(v, tuple) else v}" for k,v in view.qualification_fields.items()))
            self.addTab(qualifications, "Frozen qualifications")
        claims = ArtifactTree(); claims.show_panels(view.panels)
        self.addTab(claims, "Identity / claims / viewer observations")
        self.precision.valueChanged.connect(self.render)
        self.render()

    def render(self):
        precision = self.precision.value()
        self.fill(self.value_table, self.view.values, precision)
        if self.run_table is not None:
            row = self.view.run_rows[self.row_selector.value()] if self.view.run_rows else {}
            self.fill(self.run_table, row, precision)
            self.fill(self.terminal_table, self.view.terminal, precision)


class ArtifactsPanel(QWidget):
    selection_changed = Signal()
    core_requested = Signal(object)

    def __init__(self, help_text=""):
        super().__init__()
        self.library = ArtifactLibrary()
        self.entries = []
        self.current = None
        self.view = None
        layout = QVBoxLayout(self)
        actions = QHBoxLayout(); layout.addLayout(actions)
        self.load_button = QPushButton("Load Artifact")
        self.copy_button = QPushButton("Copy canonical artifact bytes")
        self.copy_button.setEnabled(False)
        actions.addWidget(self.load_button); actions.addWidget(self.copy_button)
        self.load_button.clicked.connect(self.choose_file)
        self.copy_button.clicked.connect(self.choose_copy)
        help_toggle = QCheckBox("Show artifact help")
        help_toggle.setAccessibleName("Show sourced artifact inspection help")
        actions.addWidget(help_toggle)
        self.help_text = QPlainTextEdit(); self.help_text.setReadOnly(True)
        self.help_text.setPlainText(help_text); self.help_text.setMaximumHeight(160)
        self.help_text.hide(); layout.addWidget(self.help_text)
        help_toggle.toggled.connect(self.help_text.setVisible)
        self.status = QLabel("Session library: Core Run / Core Geometry / Derived / Attempt Receipt / Legacy / Unknown or Unsupported")
        self.status.setTextFormat(Qt.TextFormat.PlainText); self.status.setWordWrap(True)
        layout.addWidget(self.status)
        self.history = QListWidget(); self.history.setMaximumHeight(140)
        self.history.setAccessibleName("Typed session artifact library")
        layout.addWidget(self.history)
        self.history.currentRowChanged.connect(self.select)
        self.heading = QLabel(); self.heading.setTextFormat(Qt.TextFormat.PlainText)
        self.qualification = QLabel(); self.qualification.setWordWrap(True)
        self.qualification.setTextFormat(Qt.TextFormat.PlainText)
        layout.addWidget(self.heading); layout.addWidget(self.qualification)
        self.inspector = ArtifactTree(); layout.addWidget(self.inspector)
        self.historical = HistoricalInspector(); self.historical.hide(); layout.addWidget(self.historical)
        self.result_area = QWidget(); results = QVBoxLayout(self.result_area)
        self.sample_summary = QLabel(); self.sample_summary.setTextFormat(Qt.TextFormat.PlainText)
        self.sample_summary.setWordWrap(True); results.addWidget(self.sample_summary)
        self.precision = QSpinBox(); self.precision.setRange(1, 17); self.precision.setValue(17)
        self.precision.setPrefix("Decimal display precision: ")
        self.precision.valueChanged.connect(self.render_rows); results.addWidget(self.precision)
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["Requested field", "Axis", "Stored source path", "Exact canonical f64 token", "Decimal display"])
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        results.addWidget(self.table); layout.addWidget(self.result_area); self.result_area.hide()
        self.raw = QPlainTextEdit(); self.raw.setReadOnly(True)
        self.raw.setAccessibleName("Bounded canonical raw text preview (1 MiB)")
        self.raw.setMaximumHeight(130); layout.addWidget(self.raw)

    def add_session(self, kind, value):
        # Background Core/legacy completion never steals artifact selection.
        self.entries.append((kind, value))
        self.history.blockSignals(True)
        self.history.addItem(kind)
        self.history.blockSignals(False)

    def load_path(self, path):
        try:
            item = self.library.load(path)
            if isinstance(item, CoreArtifactCandidate):
                self.status.setText("Core envelope hint — sent to the existing authoritative Core loader")
                self.core_requested.emit(item)
                return item
            kind = "ANALYSIS ATTEMPT RECEIPT" if isinstance(item, LoadedAttemptArtifact) else "DERIVED ANALYSIS RECORD"
            if type(item) is LoadedHistoricalResult:
                kind = "HISTORICAL MATHEMATICAL RECONSTRUCTION"
            elif type(item) is LoadedHistoricalReceipt:
                kind = "HISTORICAL ATTEMPT RECEIPT — NOT A SCIENTIFIC RESULT"
            index = next((i for i, (_, v) in enumerate(self.entries) if v is item), None)
            if index is None:
                index = len(self.entries)
                self.add_session(kind + " · " + item.sha256[:16], item)
            self.history.setCurrentRow(index)
            self.select(index)
            self.status.setText(kind + " — canonical structure valid; producer verification unavailable")
            return item
        except Exception as exc:
            diagnostic = bounded_text("UNKNOWN / UNSUPPORTED or refused import: " + type(exc).__name__ + ": " + str(exc))
            self.status.setText(diagnostic)
            # Retain only the most recent refusal; never select it on failure.
            prior = next((i for i, (_, v) in enumerate(self.entries) if isinstance(v, RejectedImport)), None)
            rejected = ("UNKNOWN / UNSUPPORTED — last refused import", RejectedImport(bounded_text(path), diagnostic))
            if prior is None:
                self.add_session(*rejected)
            else:
                self.entries[prior] = rejected
            return None

    def choose_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Inspect local artifact", "", "JSON (*.json);;All files (*)")
        if path:
            self.load_path(path)

    def select(self, index):
        if not 0 <= index < len(self.entries):
            return
        kind, self.current = self.entries[index]
        self.status.setText(kind)
        self.view = None; self.result_area.hide(); self.table.setRowCount(0)
        self.historical.hide(); self.inspector.show()
        self.raw.clear(); self.copy_button.setEnabled(False)
        views = {LoadedDerivedArtifact: DerivedArtifactView, LoadedAttemptArtifact: AttemptReceiptView,
                 LoadedHistoricalResult: HistoricalResultView, LoadedHistoricalReceipt: HistoricalReceiptView}
        if type(self.current) in views:
            self.view = views[type(self.current)](self.current)
            self.heading.setText(self.view.heading); self.qualification.setText(self.view.qualification)
            self.inspector.show_panels(self.view.panels)
            self.copy_button.setEnabled(True)
            raw = self.current.raw
            preview = raw[:MAX_RAW_TEXT_PREVIEW_BYTES].decode("utf-8", errors="ignore")
            if len(raw) > MAX_RAW_TEXT_PREVIEW_BYTES:
                preview = bounded_text(preview + "\n[UI preview truncated]", MAX_RAW_TEXT_PREVIEW_BYTES)
            self.raw.setPlainText(preview)
            if isinstance(self.view, DerivedArtifactView):
                self.sample_summary.setText(self.view.sample_summary)
                self.result_area.show(); self.render_rows()
            elif type(self.view) in (HistoricalResultView, HistoricalReceiptView):
                self.inspector.hide(); self.historical.show_view(self.view); self.historical.show()
        elif isinstance(self.current, RejectedImport):
            self.heading.setText("Unknown / unsupported or refused artifact")
            self.qualification.setText("No artifact accepted. No fallback, conversion or execution.")
            self.inspector.show_panels({"Selected file (unaccepted)": self.current.selected_file,
                "Bounded diagnostic": self.current.diagnostic})
        else:
            legacy = kind.startswith("LEGACY")
            self.heading.setText("Legacy detached analysis" if legacy else kind)
            self.qualification.setText("Producer not independently verified under the new analysis protocol. Existing validated session cache only." if legacy else "Validated Core record in session. Select it explicitly in Records to use Core actions.")
            self.inspector.show_panels({"Session identity": {"kind": kind, "digest": getattr(self.current, "digest", None)},
                "Stored legacy cache": self.current.result if legacy else "Inspect full Core record in Records",
                "Boundary": "No conversion, recomputation, comparison or export from this selection."})
        self.selection_changed.emit()

    def render_rows(self):
        if not isinstance(self.view, DerivedArtifactView):
            return
        rows = self.view.rows(self.precision.value())
        self.table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(value))
        self.table.resizeColumnsToContents()

    def copy_to(self, destination):
        try:
            observation = copy_artifact(self.current, destination)
            self.status.setText(f"Local UI copy verified: {observation.sha256}; {observation.bytes_written} bytes. No analysis attempt was executed.")
            return observation
        except Exception as exc:
            self.status.setText(bounded_text("Local UI copy failed: " + str(exc)))
            return None

    def choose_copy(self):
        if type(self.current) not in (LoadedDerivedArtifact, LoadedAttemptArtifact, LoadedHistoricalResult, LoadedHistoricalReceipt):
            return
        path, _ = QFileDialog.getSaveFileName(self, "Copy to a new file (existing destinations refused)", "artifact-copy.json", "JSON (*.json)", options=QFileDialog.Option.DontConfirmOverwrite)
        if path:
            self.copy_to(path)
