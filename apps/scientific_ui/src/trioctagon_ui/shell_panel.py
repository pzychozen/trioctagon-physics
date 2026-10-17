"""Panel-local static observation and explicit, stale-safe exports."""
from dataclasses import replace
import json
from trioctagon_ui.qt_runtime import prepare_qt
prepare_qt()
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget,QVBoxLayout,QHBoxLayout,QFormLayout,QLabel,QPushButton,
    QLineEdit,QComboBox,QCheckBox,QPlainTextEdit,QSplitter,QScrollArea,QFileDialog)
from trioctagon_ui.shell_reference import load_reference,ReferenceError,plain,canonical
from trioctagon_ui.shell_observer import Request,evaluate,NumericError
from trioctagon_ui.shell_view import ShellView,LAYERS,DEFAULT_LAYERS
from trioctagon_ui import shell_exports


class ShellPanel(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.reference=None; self.observation=None; self.pending=True; self.revision=0
        self.value_dirty=False; self.setting=False; self.awaiting_value=False
        self.validity_reason='Loading pinned reference'; self.operation_notice=''; self.reference_error=None
        root=QVBoxLayout(self)
        title=QLabel('Spherical Edge Observer · unreleased application component\nA: whole chord C/w = 1.  B: each end’s addition ell/w = 1.\nStatic geometry only; width is a similarity scale. No physical boundary or kernel feedback.')
        title.setWordWrap(True); root.addWidget(title)
        self.status=QLabel('Loading pinned reference'); self.status.setWordWrap(True)
        self.status.setAccessibleName('Shell observation validity and provenance'); self.status.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        root.addWidget(self.status)
        split=QSplitter(); root.addWidget(split,1)
        scroll=QScrollArea(); scroll.setWidgetResizable(True); scroll.setMinimumWidth(410); scroll.setMaximumWidth(430)
        controls=QWidget(); left=QVBoxLayout(controls); scroll.setWidget(controls); split.addWidget(scroll)
        row=QHBoxLayout(); left.addLayout(row); self.presets={}
        for key,label in [('original','Original'),('A','A · first meeting'),('B','B · last meeting')]:
            button=QPushButton(label); button.setAccessibleName('Shell exact '+label); button.clicked.connect(lambda checked=False,k=key:self.choose_preset(k))
            row.addWidget(button); self.presets[key]=button
        self.comparisons=QComboBox(); self.comparisons.addItem('Assigned comparisons (not events)',None)
        for key,label in [('R_equals_w','Assigned R/w = 1'),('t_equals_w','Assigned t/w = 1'),('assigned_R10','Assigned R/w = 10'),('assigned_RT','Assigned R/w = pi*e*phi')]: self.comparisons.addItem(label,key)
        self.comparisons.setAccessibleName('Shell assigned comparison'); self.comparisons.activated.connect(lambda i:self.choose_preset(self.comparisons.itemData(i)) if i else None); left.addWidget(self.comparisons)
        form=QFormLayout(); left.addLayout(form)
        self.mode=QComboBox(); self.mode.addItems(['R','C','ell']); self.mode.setAccessibleName('Shell normalized input mode'); form.addRow('Input quantity / w',self.mode)
        self.value=QLineEdit(); self.value.setAccessibleName('Shell normalized decimal input'); form.addRow('Value',self.value)
        self.width=QLineEdit('1'); self.width.setAccessibleName('Shell similarity width'); form.addRow('Width (similarity)',self.width)
        self.unit=QComboBox(); self.unit.addItems(['width','edge','chord','extension']); self.unit.setAccessibleName('Shell display unit'); form.addRow('Display unit',self.unit)
        self.frame=QComboBox(); self.frame.addItems(['centered','paper_c_global']); self.frame.setAccessibleName('Shell coordinate frame'); form.addRow('Frame',self.frame)
        self.apply_button=QPushButton('Apply observer input'); self.apply_button.setAccessibleName('Apply explicit shell input'); left.addWidget(self.apply_button)
        self.layers={}
        for key,label in LAYERS.items():
            check=QCheckBox(label); check.setChecked(DEFAULT_LAYERS[key]); check.setAccessibleName('Shell layer '+label)
            check.toggled.connect(lambda checked,k=key:self.layer_changed(k,checked)); left.addWidget(check); self.layers[key]=check
        camera=QHBoxLayout(); left.addLayout(camera)
        for name in ('oblique','axial','side','reset'):
            button=QPushButton(name.title()); button.setAccessibleName('Shell camera '+name); button.clicked.connect(lambda checked=False,k=name:self.camera(k)); camera.addWidget(button)
        focus=QPushButton('Focus original shell (may clip outer points)'); focus.clicked.connect(lambda:self.camera('original focus')); left.addWidget(focus)
        self.branch=QComboBox(); self.branch.addItems([f'E{i:02}{s}' for i in range(1,22) for s in ('-','+')]); self.branch.setAccessibleName('Inspect shell branch and coincident dot'); left.addWidget(self.branch)
        self.inspector=QPlainTextEdit(); self.inspector.setReadOnly(True); self.inspector.setMinimumHeight(190); self.inspector.setAccessibleName('Shell branch exact text and incidence inspector'); left.addWidget(self.inspector)
        exportrow=QHBoxLayout(); left.addLayout(exportrow); self.export_buttons={}
        for kind in ('json','png','svg'):
            button=QPushButton('Export '+kind.upper()); button.setAccessibleName('Export shell '+kind); button.clicked.connect(lambda checked=False,k=kind:self.export(k)); exportrow.addWidget(button); self.export_buttons[kind]=button
        self.view=ShellView(); split.addWidget(self.view); split.setStretchFactor(1,1)
        self.view.view_changed.connect(self._status)
        self.value.textChanged.connect(self.edited); self.width.textChanged.connect(self.width_edited)
        self.mode.currentTextChanged.connect(self.mode_changed)
        self.unit.currentTextChanged.connect(self.presentation_changed); self.frame.currentTextChanged.connect(self.presentation_changed)
        self.apply_button.clicked.connect(self.apply); self.value.returnPressed.connect(self.apply); self.width.returnPressed.connect(self.apply)
        self.branch.currentTextChanged.connect(self.inspect)
        try: self.reference=load_reference()
        except ReferenceError as exc:
            self.reference_error=str(exc); controls.setEnabled(False); self._status(); self._export_enabled(False); return
        self.choose_preset('A')

    def _export_enabled(self,enabled):
        for button in self.export_buttons.values(): button.setEnabled(enabled)

    def invalidate(self,message):
        self.pending=True; self.revision+=1; self._export_enabled(False)
        self.validity_reason=message; self.operation_notice=''; self._status()

    def edited(self,*unused):
        if not self.setting:
            self.value_dirty=True; self.awaiting_value=False; self.invalidate('Input edited; apply to validate.')

    def width_edited(self,*unused):
        if not self.setting: self.invalidate('Width edited; apply to validate.')

    def mode_changed(self,*unused):
        if self.setting or self.observation is None: return
        if self.value_dirty:
            # An unvalidated normalized edit has no accepted conversion to another
            # mode. Require fresh text instead of reinterpreting the old display.
            self.setting=True; self.value.clear(); self.setting=False
            self.awaiting_value=True
            self.invalidate('Input mode changed after a normalized edit; enter a fresh value in '+self.mode.currentText()+'.'); return
        self.setting=True; self.value.setText(str(self.observation.data[{'R':'R_over_w','C':'C_over_w','ell':'ell_over_w'}[self.mode.currentText()]])); self.setting=False
        # Changing the editor's presentation never reparses its rounded contents.
        self.revision+=1

    def choose_preset(self,preset):
        if self.reference is None: return
        self._evaluate(Request(preset=preset,mode=self.mode.currentText(),width=self.width.text(),unit=self.unit.currentText(),frame=self.frame.currentText()))

    def apply(self):
        if self.reference is None: return
        if self.awaiting_value:
            self.invalidate('Enter a fresh normalized value in '+self.mode.currentText()+' before Apply.'); return
        if self.value_dirty or self.observation is None:
            req=Request(preset=None,mode=self.mode.currentText(),value=self.value.text(),width=self.width.text(),unit=self.unit.currentText(),frame=self.frame.currentText())
        else: req=replace(self.observation.origin,width=self.width.text(),unit=self.unit.currentText(),frame=self.frame.currentText())
        self._evaluate(req)

    def presentation_changed(self,*unused):
        if self.setting or self.reference is None or self.observation is None: return
        if self.pending: self.invalidate('Presentation changed with pending input; apply to validate.'); return
        self._evaluate(replace(self.observation.origin,width=self.width.text(),unit=self.unit.currentText(),frame=self.frame.currentText()))

    def _evaluate(self,req):
        self.invalidate('Resolving explicit input.')
        try: observation=evaluate(self.reference,req)
        except NumericError as exc:
            self.validity_reason=str(exc); self._status()
            if exc.diagnostics: self.inspector.setPlainText(json.dumps(exc.diagnostics,indent=2))
            return
        self.observation=observation; self.pending=False; self.value_dirty=False; self.awaiting_value=False; self.revision+=1
        d=observation.data; self.setting=True
        self.value.setText(str(d[{'R':'R_over_w','C':'C_over_w','ell':'ell_over_w'}[self.mode.currentText()]]))
        self.unit.setCurrentText(d['unit'])
        self.unit.model().item(self.unit.findText('extension')).setEnabled(d['ell_over_w']>0)
        self.setting=False
        self.view.set_observation(observation)
        for key in ('hull_edges','hull_faces'): self.layers[key].setEnabled(d['event'] is not None)
        self._status(); self.inspect(); self._export_enabled(True)

    def _status(self):
        if self.reference is None:
            self.status.setText('Shell unavailable: '+(self.reference_error or self.validity_reason)+'\nExisting C01/D03 remains available. Export disabled.')
            return
        validity=(('STALE — retained previous view. ' if self.observation else 'No valid observation. ')+self.validity_reason+' Export disabled.\n') if self.pending else ''
        notice='\n'+self.operation_notice if self.operation_notice else ''
        if self.observation is None:
            self.status.setText(validity+notice); return
        d=self.observation.data
        meaning=('Exact '+d['event']+' · 18 accepted positions / 42 branches') if d['event'] else ('Endpoint-adjusted numeric input · 42 branch identities, no certified position count' if d['adjustments'] else 'Generic numeric input · 42 branch identities, no coincidence certification')
        note='\nExplicit adjustment: '+json.dumps(plain(d['adjustments']),ensure_ascii=False) if d['adjustments'] else ''
        clipping='\nVIEW CLIPS OUTER POINTS — use Reset for the observer sphere.' if self.view.state()['outer_points_clipped'] else ''
        self.status.setText(validity+('Last valid: ' if self.pending else '')+f'{meaning}\nR/w={d["R_over_w"]:.12g}   C/w={d["C_over_w"]:.12g}   ell/w={d["ell_over_w"]:.12g}'+note+clipping+notice)

    def _operation_status(self,message):
        self.operation_notice=message; self._status()

    def inspect(self,*unused):
        if self.observation is None: return
        d=self.observation.data; label=self.branch.currentText(); self.view.selected_branch=label
        branch=next(b for b in d['branches'] if b['branch']==label); dot=next(q for q in d['dots'] if label in q['branches'])
        edge=next(e for e in d['original_edges'] if e['id']==branch['edge'])
        self.inspector.setPlainText(json.dumps(plain({'branch':branch,'dot':dot,'source_edge':edge,
            'event':d['event'],'event_origin':d['event_origin'],'graph_counts':{k:d['graph'][k] for k in ('V','E','cycle_rank')} if d['graph'] else None,
            'hull_counts':{k:d['hull'][k] for k in ('V','E','F')} if d['hull'] else None}),indent=2))
        self.view.redraw()

    def layer_changed(self,key,checked):
        self.view.layers[key]=checked; self.view.redraw()
        self._status()

    def camera(self,name):
        if self.observation:
            self.view.camera(name)
            self._status()

    def closeEvent(self,event):
        self.view.disconnect_view_callback()
        super().closeEvent(event)

    def export(self,kind):
        if self.pending or self.observation is None or self.reference is None: return
        snapshot=self.observation; revision=self.revision; state=self.view.state(); state_bytes=canonical(state)
        suffix='.shell.json' if kind=='json' else '.'+kind
        path,_=QFileDialog.getSaveFileName(self,'Export static shell observation','observation'+suffix,kind.upper()+' (*'+suffix+')')
        if not path:
            self._operation_status('Export cancelled; no file written.'); return
        if self.pending or self.reference is None or self.observation is not snapshot or self.revision!=revision or canonical(self.view.state())!=state_bytes:
            self._operation_status('Export cancelled: observation or view changed while the dialog was open.'); return
        try:
            if kind=='json': result=shell_exports.export_json(self.reference,snapshot,state,path)
            else: result=shell_exports.export_image(self.reference,snapshot,state,self.view.figure,path)
        except (ValueError,OSError) as exc:
            self._operation_status('Export failed; observation retained: '+str(exc)); return
        self._operation_status('Shell export complete: '+result['artifact']+'\nStatic observation only; existing records unchanged.')
