"""Inert stored fixtures only: no step/run/resume or new scientific trajectories."""
from contextlib import ExitStack
import hashlib
import json
import os
from pathlib import Path
import pickle
import random
import unittest
from unittest.mock import patch
import numpy as np
from trioctagon_ui.qt_runtime import prepare_qt
prepare_qt()
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QWidget
from trioctagon_ui.app import MainWindow
from trioctagon_ui import shell_panel, requests, jobs
from trioctagon_ui.record_views import RecordView
from trioctagon_ui.shell_reference import canonical, ReferenceError

FIXTURES=Path(__file__).parent/'fixtures'


def rng(): return pickle.dumps((random.getstate(),np.random.get_state()),protocol=4)


def state(window):
    # Entire canonical samples contain Omega, coefficients, observer clocks and memory.
    values={'draft':window.draft,'checkpoint':window.checkpoint,
        'records':[(id(v),v.canonical_json) for v in window.records],
        'current':id(window.current),'current_run':id(window.current_run),'current_geometry':id(window.current_geometry),
        'analysis':[id(v) for v in window.analysis_cache],'analysis_current':id(window.analysis_current),
        'loaded':sorted(window.loaded),'saved':window.saved,'resumed':sorted(window.resumed),
        'artifact_ids':[id(v) for _,v in window.artifacts.entries],
        'artifact_raw':[v.raw.hex() for _,v in window.artifacts.entries if hasattr(v,'raw')],
        'artifact_current':id(window.artifacts.current),'artifact_row':window.artifacts.history.currentRow(),
        'record_row':window.history.currentIndex(),'sample':window.sample.value(),
        'job':(window.jobs.state,window.jobs.request,window.jobs.process,window.jobs.timer.isActive()),
        'playback':window.play_timer.isActive(),'geometry':window.geometry_combo.currentIndex(),
        'geometry_fields':{k:v.text() for k,v in window.geometry_fields.items()},
        'requested_samples':window.requested_samples}
    return canonical(values)


def forbidden(include_completed=True):
    from kernel_physics import api
    from trioctagon_ui import worker
    stack=ExitStack(); mocks=[]
    targets=[(api,n) for n in ('step','run','resume','axial_snapshot','axial_source_budget')]
    targets += [(jobs.JobManager,'start'),(worker,'execute'),(MainWindow,'_submit'),(MainWindow,'_select_record'),(MainWindow,'_select_analysis'),(QTimer,'start')]
    if include_completed: targets.append((MainWindow,'_completed'))
    for obj,name in targets: mocks.append(stack.enter_context(patch.object(obj,name,side_effect=AssertionError('Shell forbidden call '+name))))
    return stack,mocks


class ShellIsolationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.qt=QApplication.instance() or QApplication([])
    def close(self,w): w.close(); w.deleteLater(); self.qt.processEvents()

    def test_first_construction_and_reference_failure_have_no_scientific_calls(self):
        context,mocks=forbidden(); before=rng()
        with context:
            w=MainWindow()
            self.assertEqual(w.tabs.count(),4); self.assertEqual(w.tabs.currentIndex(),0)
            self.assertEqual(w.geometry_combo.currentIndex(),0); self.assertEqual(w.geometry_tabs.currentIndex(),0)
            self.assertEqual(w.shell_panel.observation.data['event'],'A'); self.close(w)
            with patch.object(shell_panel,'load_reference',side_effect=ReferenceError('injected corrupt reference')):
                w=MainWindow()
            self.assertEqual(w.geometry_combo.count(),3); self.assertIsNone(w.shell_panel.reference)
            w.geometry_combo.setCurrentIndex(1); self.assertEqual(w.geometry_combo.currentText(),'C01 — explicit sections'); self.close(w)
        self.assertEqual(before,rng()); self.assertTrue(all(m.call_count==0 for m in mocks))

    def test_repeated_interactions_preserve_core_historical_and_rng(self):
        w=MainWindow(); raw=(FIXTURES/'axial_old_run.json').read_text(encoding='utf-8'); core=RecordView(raw)
        w.records.append(core); w._select_record(core)
        historical=w.artifacts.load_path(FIXTURES/'historical/H6B_admitted_0.json'); self.assertIsNotNone(historical)
        w.checkpoint={'record_json':core.canonical_json,'sample_index':'0'}
        before=state(w); before_rng=rng(); context,mocks=forbidden(); p=w.shell_panel
        try:
            with context:
                for _ in range(2):
                    w.tabs.setCurrentIndex(2); w.geometry_tabs.setCurrentIndex(1)
                    for name in ('original','A','B','R_equals_w','t_equals_w','assigned_R10','assigned_RT'): p.choose_preset(name)
                    for name in ('R','C','ell'): p.mode.setCurrentText(name)
                    p.value.setText('bad'); p.apply(); self.assertTrue(p.pending); p.choose_preset('B')
                    for unit in ('edge','chord','extension','width'): p.unit.setCurrentText(unit)
                    for frame in ('paper_c_global','centered'): p.frame.setCurrentText(frame)
                    p.width.setText('2'); p.apply(); p.width.setText('1'); p.apply()
                    p.choose_preset('A'); p.mode.setCurrentText('C'); origin=p.observation.origin
                    p.width.setText('invalid'); p.mode.setCurrentText('ell'); p.apply(); self.assertTrue(p.pending)
                    p.frame.setCurrentText('paper_c_global'); p.unit.setCurrentText('edge')
                    p.width.setText('2'); p.mode.setCurrentText('R'); p.apply()
                    self.assertEqual(p.observation.data['event'],'A'); self.assertEqual(p.observation.origin.preset,origin.preset)
                    p.value.setText('0.763762615825973334431341198954'); p.apply()
                    p.mode.setCurrentText('C'); p.width.setText('3'); p.mode.setCurrentText('ell'); p.apply()
                    self.assertIsNone(p.observation.data['event']); self.assertEqual(p.observation.origin.mode,'R')
                    self.assertEqual(p.observation.origin.value,'0.763762615825973334431341198954')
                    p.value.setText('1.7'); p.mode.setCurrentText('C'); p.apply(); self.assertTrue(p.pending)
                    p.value.setText('1'); p.apply(); self.assertEqual(p.observation.data['event'],'A')
                    for layer in p.layers.values(): layer.setChecked(not layer.isChecked())
                    for camera in ('oblique','axial','side','reset','original focus'): p.camera(camera)
                    p.branch.setCurrentText('E21+'); p.branch.setCurrentText('E01-')
                    p.view.canvas.draw(); p.view.toolbar.push_current()
                    for _redraw in range(2):
                        p.view.redraw(); p.view.ax.set(xlim=(-.2,.2),ylim=(-.2,.2),zlim=(-.2,.2)); p.view.canvas.draw()
                        self.assertIn('CLIPS',p.status.text())
                    p.view.toolbar.push_current(); p.view.toolbar.back(); p.view.canvas.draw()
                    p.view.toolbar.forward(); p.view.canvas.draw(); self.assertIn('CLIPS',p.status.text())
                    def pending_dialog(*unused):
                        p.width.setText('invalid'); p.view.canvas.draw(); return ('C:/unused.shell.json','')
                    with patch.object(shell_panel.QFileDialog,'getSaveFileName',side_effect=pending_dialog),patch.object(shell_panel.shell_exports,'export_json',side_effect=AssertionError('Stale export forbidden')): p.export('json')
                    p.camera('reset'); p.view.canvas.draw(); self.assertIn('STALE',p.status.text())
                    p.width.setText('1'); p.apply()
                    with patch.object(shell_panel.QFileDialog,'getSaveFileName',return_value=('','')):
                        for kind in ('json','png','svg'): p.export(kind)
                    with patch.object(shell_panel.QFileDialog,'getSaveFileName',return_value=('C:/unused.shell.json','')), patch.object(shell_panel.shell_exports,'export_json',side_effect=OSError('injected refusal')): p.export('json')
                    w.geometry_tabs.setCurrentIndex(0); w.tabs.setCurrentIndex(0)
                self.assertEqual(before,state(w)); self.assertEqual(before_rng,rng())
                self.assertTrue(all(m.call_count==0 for m in mocks))
                if os.environ.get('TRIOCTAGON_UI_EVIDENCE'):
                    (Path(os.environ['TRIOCTAGON_UI_EVIDENCE'])/'shell-isolation.json').write_text(json.dumps({'status':'PASS','fixture_only':True,'core_digest':core.digest,'historical_sha256':hashlib.sha256(historical.raw).hexdigest(),'state_before_sha256':hashlib.sha256(before).hexdigest(),'state_after_sha256':hashlib.sha256(state(w)).hexdigest(),'rng_before_sha256':hashlib.sha256(before_rng).hexdigest(),'rng_after_sha256':hashlib.sha256(rng()).hexdigest(),'forbidden_calls':[m.call_count for m in mocks],'state_reset':False,'p1r1_routes':['width-pending mode changes','invalid-width recovery','generic rounded presentation','fresh-entry requirement','repeated redraw callbacks','toolbar history','modal pending status']},indent=2),encoding='utf-8')
        finally: self.close(w)

    def test_legitimate_record_completion_matches_control_without_shell(self):
        # Deliver the recorded result of a legitimate load, with no worker execution.
        raw=(FIXTURES/'axial_old_run.json').read_text(encoding='utf-8'); data=json.loads(raw)
        response={'request_id':'recorded-load-completion','operation':'load_record','result':{'result_kind':'record','canonical_json':raw,'produced_current':False,'source_commit':data['implementation']['commit']}}
        w=MainWindow()
        with patch('trioctagon_ui.app.ShellPanel',QWidget): control=MainWindow()
        p=w.shell_panel; p.mode.setCurrentText('C'); p.width.setText('2'); p.mode.setCurrentText('ell'); p.apply()
        p.width.setText('invalid'); p.view.ax.set(xlim=(-.2,.2),ylim=(-.2,.2),zlim=(-.2,.2)); p.view.canvas.draw()
        status=p.status.text()
        snapshot=w.shell_panel.observation; camera=canonical(w.shell_panel.view.state())
        try:
            with patch.object(jobs.JobManager,'start',side_effect=AssertionError('No worker execution in fixture delivery')):
                w._completed(response); control._completed(response)
            for item in (w,control):
                self.assertEqual(len(item.records),1); self.assertEqual(item.current.canonical_json,raw.strip())
                self.assertIn(data['deterministic_sha256'],item.loaded); self.assertEqual(item.sample.value(),0)
            self.assertEqual(w.current.canonical_json,control.current.canonical_json)
            self.assertEqual(w.draft,control.draft); self.assertEqual(w.raw_json.toPlainText(),control.raw_json.toPlainText())
            self.assertIs(w.shell_panel.observation,snapshot); self.assertEqual(canonical(w.shell_panel.view.state()),camera)
            p.view.canvas.draw(); self.assertEqual(p.status.text(),status); self.assertTrue(p.pending)
        finally: self.close(w); self.close(control)
