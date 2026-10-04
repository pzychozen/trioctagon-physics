"""Passive axial controls and cached displays; no scientific kernel imports."""
import json
from itertools import islice
from pathlib import Path
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTabWidget, QComboBox,
    QPushButton, QPlainTextEdit, QTableWidget, QTableWidgetItem, QFileDialog, QSplitter)
from trioctagon_ui import requests, axial_exports
from trioctagon_ui.axial_artifacts import AxialAnalysisView, MAX_BYTES, plain
from trioctagon_ui.axial_reference import load_reference
from trioctagon_ui.record_views import flatten
from trioctagon_ui.plots import AxialHistoryPlot


def table(name):
    item = QTableWidget(0, 3); item.setHorizontalHeaderLabels(['Field', 'Display value', 'Exact binary64 / stored value'])
    item.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers); item.setAccessibleName(name)
    item.resizeColumnsToContents()
    return item


def fill_table(item, value):
    rows = list(islice(flatten(value, precision=17), 10001))
    if len(rows) > 10000: rows[-1] = ('DISPLAY LIMIT', 'First 10000 rows; complete data retained in JSON/CSV exports', '')
    item.setRowCount(len(rows))
    for i, row in enumerate(rows):
        for j, value in enumerate(row): item.setItem(i, j, QTableWidgetItem(value))
    item.resizeColumnsToContents()


def state_fields(value):
    order = ('C', 'W', 'Gamma', 'C_norm', 'W_norm', 'intensity', 'C_parallel', 'C_perp', 'residuals', 'chiral_area_accounting',
             'S', 'A', 'revision', 'source_definition', 'numeric_policy')
    return {'snapshot': {k: value[k] for k in order}}


class AxialPanel(QWidget):
    requested = Signal(dict)
    loaded = Signal(object)

    def __init__(self, source_provider, parent=None):
        super().__init__(parent); self.source_provider = source_provider
        self.view = None; self.views = {}; self.forms = {}; self.tables = {}; self.labels = {}; self.busy = False
        self.setAccessibleName('Axial Observables passive analysis')
        layout = QVBoxLayout(self)
        meaning = QLabel('C: channel-space area vector. W: geometry-attached planar axial observable. Gamma: complementary signed channel-area scalar.\nSquared-amplitude scale; not a physical field.')
        meaning.setWordWrap(True); layout.addWidget(meaning)
        self.evidence = QLabel('NOT ANALYZED — explicit Analyze action required'); self.evidence.setWordWrap(True)
        self.evidence.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse); layout.addWidget(self.evidence)
        self.sections = QTabWidget(); self.sections.setAccessibleName('Axial State, History, Source Accounting and Paper G Reference'); layout.addWidget(self.sections, 1)
        for kind, label in (('axial_snapshot', 'State'), ('axial_history', 'History'), ('axial_source_budget', 'Source Accounting')):
            page = QWidget(); box = QVBoxLayout(page)
            controls = QHBoxLayout(); box.addLayout(controls)
            mode = QComboBox(); mode.setAccessibleName(label + ' explicit or recorded input mode')
            if kind != 'axial_history': mode.addItem('Explicit inputs', 'explicit')
            mode.addItem('Selected stored triad sample', 'record'); controls.addWidget(mode)
            analyze = QPushButton('Analyze ' + label); analyze.setAccessibleName('Explicit Analyze ' + label); controls.addWidget(analyze)
            edit = QPlainTextEdit(); edit.setMaximumHeight(130); edit.setAccessibleName(label + ' inputs JSON; numbers as decimal strings')
            box.addWidget(edit)
            if kind == 'axial_history': hint = 'Enter strictly increasing stored sample ordinals. Source anchor must be the first selection. Missing updates remain missing.'
            elif kind == 'axial_source_budget': hint = 'Record mode binds parent parameters. Optional after_sample_index is from the same parent and must have actual index n+1. Null means prediction only.'
            else: hint = 'Choose explicit triad values or the selected stored sample. Enter numbers as decimal strings; no automatic presets.'
            note = QLabel(hint); note.setWordWrap(True); box.addWidget(note)
            status = QLabel('NOT ANALYZED'); status.setWordWrap(True); box.addWidget(status); self.labels[kind] = status
            results = QTabWidget(); box.addWidget(results, 1)
            if kind == 'axial_history':
                self.history_plot = AxialHistoryPlot(); results.addTab(self.history_plot, 'Signed plots')
            fields = table(label + ' scientific values; exact text alternative'); self.tables[kind] = fields
            results.addTab(fields, 'Values and exact tokens')
            if kind == 'axial_source_budget':
                self.terms = QTableWidget(7, 5); self.terms.setHorizontalHeaderLabels(['Source term', 'A', 'C', 'W', 'Gamma'])
                self.terms.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers); self.terms.setAccessibleName('All seven returned source terms A C W Gamma')
                results.insertTab(0, self.terms, 'Seven source terms'); results.setCurrentIndex(0)
            self.forms[kind] = (mode, edit, analyze)
            mode.currentIndexChanged.connect(lambda _, k=kind: self.reset_template(k))
            analyze.clicked.connect(lambda _, k=kind: self.analyze(k))
            self.reset_template(kind); self.sections.addTab(page, label)
        reference = QWidget(); ref_layout = QVBoxLayout(reference)
        self.reference_text = QPlainTextEdit(); self.reference_text.setReadOnly(True)
        self.reference_text.setAccessibleName('Static Paper G theorem and archived repaired M3 reference; not a run certificate')
        ref_layout.addWidget(self.reference_text)
        self.reference_raw = QPlainTextEdit(); self.reference_raw.setReadOnly(True); self.reference_raw.setAccessibleName('Exact archived reference receipts and authority hashes')
        ref_tabs = QTabWidget(); ref_tabs.addTab(self.reference_text, 'Statement and scope'); ref_tabs.addTab(self.reference_raw, 'Exact receipts / hashes')
        ref_layout.addWidget(ref_tabs)
        try:
            ref = load_reference()
            parts = [ref['title'], ref['theorem']['evidence_class'], ref['theorem']['statement'], ref['theorem']['zero_stratum'],
                ref['m3']['evidence_class'], 'Exact named model: ' + json.dumps(plain(ref['m3']['model']), ensure_ascii=False),
                'Entrance: ' + ', '.join(ref['m3']['entrance']) + '; squared norm = 3.',
                ref['m3']['statement'], ref['m3']['outer_image_qualification'], ref['m3']['chart_qualification'], *ref['limits'], ref['attribution']]
            self.reference_text.setPlainText('\n\n'.join(parts)); self.reference_raw.setPlainText(json.dumps(plain(ref), indent=2, ensure_ascii=False))
        except ValueError as exc: self.reference_text.setPlainText(str(exc))
        self.sections.addTab(reference, 'Paper G Reference')
        row = QHBoxLayout(); layout.addLayout(row); self.export_buttons = []
        for label, action in (('Load saved axial JSON', self.load_saved), ('Save strict JSON', lambda: self.export('json')),
                ('Export CSV + provenance', lambda: self.export('csv')), ('Export PNG + provenance', lambda: self.export('png')),
                ('Export SVG + provenance', lambda: self.export('svg'))):
            b = QPushButton(label); b.setAccessibleName(label); b.clicked.connect(action); row.addWidget(b)
            if label != 'Load saved axial JSON': self.export_buttons.append(b)
        self.raw = QPlainTextEdit(); self.raw.setReadOnly(True); self.raw.setMaximumHeight(80)
        self.raw.setAccessibleName('Accepted immutable axial artifact raw canonical JSON'); layout.addWidget(self.raw)
        self.status = QLabel('No axial result cached'); self.status.setWordWrap(True); layout.addWidget(self.status)
        self.sections.currentChanged.connect(lambda _: self.update_exports())
        self.update_exports()

    def reset_template(self, kind):
        mode, edit, _ = self.forms[kind]
        edit.setPlainText(json.dumps(requests.analysis_template(kind, mode.currentData()), indent=2))

    def analyze(self, kind):
        try:
            if self.busy: raise ValueError('A worker is already active')
            mode, edit, _ = self.forms[kind]
            source = self.source_provider() if mode.currentData() == 'record' else {'mode': 'explicit'}
            from trioctagon_ui.axial_artifacts import pairs
            envelope = requests.analysis_request(kind, json.loads(edit.toPlainText(), object_pairs_hook=pairs), source=source)
            self.status.setText('Analysis requested; previous completed cache retained')
            self.requested.emit(envelope)
        except (ValueError, TypeError) as exc: self.show_error(str(exc))

    def set_busy(self, busy):
        self.busy = busy
        for _, _, button in self.forms.values(): button.setEnabled(not busy)

    def show_error(self, message):
        self.status.setText('REFUSED / ERROR: ' + message + '\nPrevious completed cache retained')

    def show_view(self, view):
        if not isinstance(view, AxialAnalysisView): raise ValueError('Axial panel requires an axial cache')
        self.view = view; a = view.artifact; kind = a['analysis_kind']; self.views[kind] = view
        for other, item in self.tables.items():
            if other != kind: item.setRowCount(0); self.labels[other].setText('NOT ANALYZED in the selected cache; select a completed analysis from Records to inspect another cache')
        if kind != 'axial_history': self.history_plot.set_view(None)
        if kind != 'axial_source_budget': self.terms.clearContents()
        label = ('UNAUTHENTICATED SAVED OBSERVATIONS' if view.saved_import else
                 'PASSIVE RECOMPUTATION OF STORED SAMPLE' if a['parent'] else 'CURRENT BINARY64 EXPERIMENT')
        self.evidence.setText(label + '\nFLOATING_OBSERVATION · observation ' + a['content_sha256'][:16] +
            ' · kernel ' + a['implementation']['source_commit'][:12] + (('\nParent producer ' + a['parent']['source_commit'][:12] + ' · parent ' + a['parent']['deterministic_sha256'][:16]) if a['parent'] else ''))
        self.sections.setCurrentIndex(('axial_snapshot', 'axial_history', 'axial_source_budget').index(kind))
        fill_table(self.tables[kind], state_fields(a['data']['snapshot']) if kind == 'axial_snapshot' else a['data'])
        if kind == 'axial_history':
            self.history_plot.set_view(view); self.labels[kind].setText('Stored sparse selection (' + str(len(a['selection'])) + ' samples): ' + str(plain(a['selection'][:8])) + (' … full selection in retained JSON/CSV' if len(a['selection']) > 8 else ''))
        elif kind == 'axial_source_budget':
            data = a['data']; b = data['budget']
            heading = 'RECORDED ADJACENT COMPARISON' if data['comparison_status'] == 'RECORDED_ADJACENT_PAIR' else 'PREDICTION' if data['comparison_status'] == 'PREDICTION_ONLY' else 'SUPPLIED ADJACENT COMPARISON'
            self.labels[kind].setText(heading + ' · ' + data['comparison_availability'] + '\nPre-sync prediction is reconstructed, not stored trajectory evidence. Full values include before, predicted after, actual after and signed residuals.')
            labels = ('eps(DA+AD)', 'g(LA+AL)', 'eps² DAD', 'eps*g(DAL+LAD)', 'g² LAL', 'A_tilde(cos d - 1)', 'S_tilde sin d')
            for i, term in enumerate((*b['amplitude_terms'], *b['phase_terms'])):
                self.terms.setItem(i, 0, QTableWidgetItem(labels[i]))
                for j, field in enumerate(('A', 'C', 'W', 'Gamma'), 1):
                    if field == 'A': value = '\n'.join(', '.join(r[1] for r in flatten(row, precision=9)) for row in term[field])
                    else: value = '\n'.join(r[1] for r in flatten(term[field], precision=9))
                    self.terms.setItem(i, j, QTableWidgetItem(value))
            self.terms.resizeColumnsToContents(); self.terms.resizeRowsToContents()
        else: self.labels[kind].setText('Returned state snapshot · ' + str(plain(a['selection'])))
        self.raw.setPlainText(view.canonical_json[:65536] + ('\n[Raw preview truncated at 64 KiB; export retains all bytes]' if len(view.canonical_json)>65536 else ''))
        self.status.setText('Complete immutable observation cached; reference_comparison = null')
        self.update_exports()

    def select_sample(self, parent_digest, ordinal):
        self.history_plot.select_sample(parent_digest, ordinal)
        view = self.view if self.view and self.view.artifact['analysis_kind'] == 'axial_history' else None
        if view and view.artifact['parent']['deterministic_sha256'] == parent_digest:
            rows = {s['sample_ordinal']: i for i, s in enumerate(view.artifact['selection'])}
            if ordinal in rows:
                fill_table(self.tables['axial_snapshot'], state_fields(view.artifact['data']['snapshots'][rows[ordinal]]))
                self.labels['axial_snapshot'].setText('Cached history snapshot at stored ordinal ' + str(ordinal)); return
        view = self.view if self.view and self.view.artifact['analysis_kind'] == 'axial_snapshot' else None
        if view and view.artifact['parent'] and view.artifact['parent']['deterministic_sha256'] == parent_digest and view.artifact['selection'][0]['sample_ordinal'] == ordinal:
            fill_table(self.tables['axial_snapshot'], state_fields(view.artifact['data']['snapshot'])); self.labels['axial_snapshot'].setText('Cached selected snapshot'); return
        self.tables['axial_snapshot'].setRowCount(0); self.labels['axial_snapshot'].setText('NOT ANALYZED')

    def update_exports(self):
        active = self.sections.currentIndex()
        matches = self.view is not None and active < 3 and self.view.artifact['analysis_kind'] == ('axial_snapshot','axial_history','axial_source_budget')[active]
        for i, b in enumerate(self.export_buttons): b.setEnabled(matches and (i < 2 or active == 1))

    def load_path(self, path):
        try:
            path = Path(path)
            if path.stat().st_size > MAX_BYTES: raise ValueError('Axial artifact exceeds 16 MiB')
            view = AxialAnalysisView.from_saved(path.read_bytes()); self.loaded.emit(view); self.show_view(view)
            return view
        except (OSError, ValueError) as exc: self.show_error(str(exc)); return None

    def load_saved(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Load unauthenticated saved observation', '', 'Axial JSON (*.json)')
        if path: self.load_path(path)

    def export(self, extension):
        if self.view is None: return
        path, _ = QFileDialog.getSaveFileName(self, 'Export accepted axial cache', '', extension.upper() + ' (*.' + extension + ')')
        if not path: return
        try:
            if extension == 'json': axial_exports.export_json(self.view, path)
            elif extension == 'csv': axial_exports.export_csv(self.view, path)
            else: axial_exports.export_plot(self.view, self.history_plot.figures[self.history_plot.tabs.currentIndex()], path)
            self.status.setText('Exported retained values with provenance; no scientific recomputation')
        except (OSError, ValueError) as exc: self.show_error(str(exc))
