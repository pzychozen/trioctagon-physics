"""Native shell state boundaries; no scientific execution or token orchestration."""
import unittest
from dataclasses import replace
from itertools import permutations
from unittest.mock import patch
from trioctagon_ui.qt_runtime import prepare_qt
prepare_qt()
from PySide6.QtCore import QCoreApplication,QEvent
from PySide6.QtTest import QSignalSpy,QTest
from PySide6.QtWidgets import QApplication
from trioctagon_ui import shell_panel
from trioctagon_ui.shell_reference import ReferenceError, canonical


class ShellPanelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.qt=QApplication.instance() or QApplication([])

    def setUp(self): self.panel=shell_panel.ShellPanel()
    def tearDown(self): self.panel.close(); self.panel.deleteLater(); self.qt.processEvents()

    def test_modes_preserve_origin_until_real_edit(self):
        p=self.panel; original=p.observation.origin
        for mode in ('ell','C','R','C','ell','R'):
            p.mode.setCurrentText(mode); p.apply()
            self.assertEqual(p.observation.origin,original); self.assertEqual(p.observation.data['event'],'A')
        p.mode.setCurrentText('C'); p.value.setText('1.00000000000000001')
        self.assertTrue(p.pending); self.assertTrue(all(not b.isEnabled() for b in p.export_buttons.values()))
        p.apply(); self.assertFalse(p.pending); self.assertIsNone(p.observation.data['event'])
        self.assertIsNone(p.observation.data['hull']); self.assertIsNone(p.observation.data['graph'])
        self.assertFalse(p.layers['hull_edges'].isEnabled())

    def test_pending_invalid_and_unit_transitions(self):
        p=self.panel; last=p.observation
        p.value.setText('NaN'); self.assertIn('STALE',p.status.text()); p.apply()
        self.assertIs(p.observation,last); self.assertTrue(p.pending)
        p.choose_preset('B'); p.unit.setCurrentText('extension'); p.choose_preset('original')
        self.assertEqual(p.unit.currentText(),'width'); self.assertIn('adjustment',p.status.text())
        self.assertFalse(p.unit.model().item(p.unit.findText('extension')).isEnabled())
        p.choose_preset('B'); p.unit.setCurrentText('extension'); p.mode.setCurrentText('ell'); p.value.setText('0'); p.apply()
        self.assertEqual(p.unit.currentText(),'width'); self.assertEqual(p.observation.data['event'],'original')
        p.choose_preset('B'); p.unit.setCurrentText('extension'); p.mode.setCurrentText('R'); p.value.setText('0.6133730937584284'); p.apply()
        self.assertTrue(p.pending); self.assertIn('unit',p.status.text().lower())

    def test_layers_camera_frame_scale_and_inspection(self):
        p=self.panel; p.camera('side'); before=p.view.state()['camera']
        for box in p.layers.values(): box.setChecked(not box.isChecked())
        self.assertEqual(p.view.state()['camera'],before)
        p.branch.setCurrentText('E21+'); self.assertIn('E21+',p.inspector.toPlainText())
        p.frame.setCurrentText('paper_c_global'); p.width.setText('2'); p.apply()
        self.assertEqual(p.observation.data['frame'],'paper_c_global')
        for key in ('R_equals_w','t_equals_w','assigned_R10','assigned_RT'):
            p.choose_preset(key); self.assertIsNone(p.observation.data['event'])
        p.camera('original focus'); self.assertTrue(p.view.state()['outer_points_clipped']); self.assertIn('CLIPS',p.status.text())
        p.camera('reset'); self.assertFalse(p.view.state()['outer_points_clipped'])
        limits=[p.view.ax.get_xlim(),p.view.ax.get_ylim(),p.view.ax.get_zlim()]
        self.assertLess(max(b-a for a,b in limits)-min(b-a for a,b in limits),1e-12)

    def test_dialog_cancel_and_stale_snapshot(self):
        p=self.panel
        with patch.object(shell_panel.QFileDialog,'getSaveFileName',return_value=('','')), patch.object(shell_panel.shell_exports,'export_json') as exporter:
            p.export('json'); exporter.assert_not_called()
        def edit(*args): p.value.setText('invalid'); return ('C:/unused.shell.json','')
        with patch.object(shell_panel.QFileDialog,'getSaveFileName',side_effect=edit), patch.object(shell_panel.shell_exports,'export_json') as exporter:
            p.export('json'); exporter.assert_not_called()
        self.assertTrue(p.pending); self.assertIn('cancelled',p.status.text())
        p.choose_preset('A')
        def camera(*args): p.camera('side'); return ('C:/unused.shell.json','')
        with patch.object(shell_panel.QFileDialog,'getSaveFileName',side_effect=camera), patch.object(shell_panel.shell_exports,'export_json') as exporter:
            p.export('json'); exporter.assert_not_called()

    def test_export_uses_observed_snapshot_and_failure_is_local(self):
        p=self.panel; snapshot=p.observation
        with patch.object(shell_panel.QFileDialog,'getSaveFileName',return_value=('C:/unused.shell.json','')), patch.object(shell_panel.shell_exports,'export_json',side_effect=OSError('injected disk failure')) as exporter:
            p.export('json'); self.assertIs(exporter.call_args.args[1],snapshot)
        self.assertIs(p.observation,snapshot); self.assertFalse(p.pending); self.assertIn('failed',p.status.text())

    def test_missing_reference_disables_only_shell(self):
        with patch.object(shell_panel,'load_reference',side_effect=ReferenceError('injected missing package resource')):
            other=shell_panel.ShellPanel()
        try:
            self.assertIsNone(other.reference); self.assertIsNone(other.observation)
            self.assertTrue(all(not b.isEnabled() for b in other.export_buttons.values()))
            self.assertIn('C01/D03',other.status.text()); self.assertEqual(self.panel.observation.data['event'],'A')
        finally: other.close(); other.deleteLater()

    def test_width_pending_mode_pairs_preserve_exact_and_generic_origins(self):
        p=self.panel
        origins=[('A',None,None),('B',None,None),('original',None,None),
            (None,'R','0.763762615825973334431341198954'),
            (None,'C','1.00000000000000001'),(None,'C','0.99999999999999999'),
            (None,'ell','1.00000000000000001'),(None,'ell','0.99999999999999999')]
        stable=('event','event_origin','preset_id','raw_value','parsed_decimal','input_mode',
            'input_binary64_hex','resolved_decimal','resolved_binary64_hex','certified_unique_count')
        for preset,origin_mode,raw in origins:
            for first,second in permutations(('R','C','ell'),2):
                for invalid_width in (False,True):
                    with self.subTest(preset=preset,raw=raw,first=first,second=second,invalid_width=invalid_width):
                        p.width.setText('1'); p.unit.setCurrentText('width'); p.frame.setCurrentText('centered'); p.choose_preset(preset or 'A')
                        if raw:
                            p.mode.setCurrentText(origin_mode); p.value.clear(); p.value.setText(raw); p.apply()
                            self.assertIsNone(p.observation.data['event'])
                        original=p.observation; expected={k:original.data[k] for k in stable}
                        p.mode.setCurrentText(first); p.width.setText('invalid' if invalid_width else '2')
                        if invalid_width:
                            p.apply(); self.assertTrue(p.pending); self.assertIs(p.observation,original)
                        with patch.object(shell_panel,'evaluate',side_effect=AssertionError('Presentation must not evaluate pending input')):
                            p.mode.setCurrentText(second); p.frame.setCurrentText('paper_c_global'); p.unit.setCurrentText('edge')
                            for mode in ('R','C','ell',second): p.mode.setCurrentText(mode)
                        self.assertTrue(p.pending); self.assertFalse(p.value_dirty)
                        self.assertTrue(all(not b.isEnabled() for b in p.export_buttons.values()))
                        self.assertIn('STALE',p.status.text())
                        if invalid_width: p.width.setText('2')
                        p.apply(); self.assertFalse(p.pending)
                        self.assertEqual(p.observation.origin,replace(original.origin,width='2',unit='edge',frame='paper_c_global'))
                        self.assertEqual({k:p.observation.data[k] for k in stable},expected)
                        self.assertEqual(p.observation.data['width'],2)

    def test_dirty_normalized_mode_transition_requires_fresh_entry(self):
        p=self.panel
        for old,new in permutations(('R','C','ell'),2):
            with self.subTest(old=old,new=new):
                p.width.setText('1'); p.choose_preset('A'); p.mode.setCurrentText(old)
                accepted=p.observation; p.value.setText('1.7'); p.width.setText('2'); p.mode.setCurrentText(new)
                self.assertTrue(p.awaiting_value); self.assertEqual(p.value.text(),'')
                with patch.object(shell_panel,'evaluate',side_effect=AssertionError('Fresh normalized entry required')): p.apply()
                self.assertIs(p.observation,accepted); self.assertIn('fresh normalized',p.status.text())
                self.assertTrue(all(not b.isEnabled() for b in p.export_buttons.values()))
                entered='1.2' if new=='R' else '1'
                QTest.keyClicks(p.value,entered); p.apply()
                self.assertFalse(p.pending); self.assertFalse(p.awaiting_value)
                self.assertIsNone(p.observation.origin.preset); self.assertEqual(p.observation.origin.mode,new)
                self.assertEqual(p.observation.origin.value,entered); self.assertEqual(p.observation.origin.width,'2')
                self.assertEqual(p.observation.data['event'],{'R':None,'C':'A','ell':'B'}[new])

    def test_modal_pending_retains_validity_with_view_callbacks(self):
        p=self.panel
        for field in ('value','width'):
            for kind in ('json','png','svg'):
                with self.subTest(field=field,kind=kind):
                    p.width.setText('1'); p.choose_preset('A'); p.camera('reset'); snapshot=p.observation
                    def edit(*unused):
                        getattr(p,field).setText('invalid')
                        p.view.ax.set(xlim=(-.2,.2),ylim=(-.2,.2),zlim=(-.2,.2)); p.view.canvas.draw()
                        return ('C:/unused.'+kind,'')
                    with patch.object(shell_panel.QFileDialog,'getSaveFileName',side_effect=edit),patch.object(shell_panel.shell_exports,'export_json') as js,patch.object(shell_panel.shell_exports,'export_image') as image:
                        p.export(kind); js.assert_not_called(); image.assert_not_called()
                    self.assertIs(p.observation,snapshot); self.assertTrue(p.pending)
                    for text in ('STALE','retained previous view','Export disabled','cancelled','CLIPS'): self.assertIn(text,p.status.text())
                    self.assertTrue(all(not b.isEnabled() for b in p.export_buttons.values()))
                    with patch.object(shell_panel,'evaluate',side_effect=AssertionError('View callback must not evaluate')):
                        p.view.canvas.draw(); p.camera('reset'); p.view.canvas.draw()
                    self.assertIn('STALE',p.status.text()); self.assertIn('cancelled',p.status.text()); self.assertNotIn('CLIPS',p.status.text())

    def test_export_notices_cannot_hide_current_clipping(self):
        p=self.panel; p.view.ax.set(xlim=(-.2,.2),ylim=(-.2,.2),zlim=(-.2,.2)); p.view.canvas.draw()
        for kind in ('json','png','svg'):
            for failure in (False,True):
                with self.subTest(kind=kind,failure=failure):
                    fn='export_json' if kind=='json' else 'export_image'
                    with patch.object(shell_panel.QFileDialog,'getSaveFileName',return_value=('C:/unused.'+kind,'')),patch.object(shell_panel.shell_exports,fn,side_effect=OSError('injected refusal') if failure else None,return_value={'artifact':'example.'+kind}): p.export(kind)
                    self.assertIn('CLIPS',p.status.text()); self.assertIn('failed' if failure else 'export complete',p.status.text())
                    self.assertFalse(p.pending); p.view.canvas.draw(); self.assertIn('CLIPS',p.status.text())
        p.camera('reset'); p.view.canvas.draw(); self.assertNotIn('CLIPS',p.status.text())
        self.assertIn('failed',p.status.text())

    def test_toolbar_history_pan_and_zoom_draw_status(self):
        p=self.panel; view=p.view; view.canvas.draw(); accepted=p.observation
        toolbar=view.toolbar; toolbar.push_current(); full=view.state()['camera']
        with patch.object(shell_panel,'evaluate',side_effect=AssertionError('Navigation must not evaluate')):
            # Real Axes limit updates and the real native toolbar history route.
            view.ax.set(xlim=(-.2,.2),ylim=(-.2,.2),zlim=(-.2,.2)); view.canvas.draw(); toolbar.push_current()
            self.assertIn('CLIPS',p.status.text())
            toolbar.back(); view.canvas.draw(); self.assertNotIn('CLIPS',p.status.text())
            self.assertEqual(view.state()['camera'],full)
            toolbar.forward(); view.canvas.draw(); self.assertIn('CLIPS',p.status.text())
            toolbar.home(); view.canvas.draw(); self.assertNotIn('CLIPS',p.status.text())
            limits=view.ax.get_xlim(); view.ax.set_xlim(limits[0]+3,limits[1]+3); view.canvas.draw()
            self.assertIn('CLIPS',p.status.text())
            toolbar.home(); view.canvas.draw(); self.assertNotIn('CLIPS',p.status.text())
        self.assertIs(p.observation,accepted)

    def test_one_canvas_callback_survives_redraw_and_tears_down(self):
        p=self.panel; view=p.view; spy=QSignalSpy(view.view_changed); cid=view._draw_cid
        for i in range(6):
            p.layers['panels'].setChecked(not p.layers['panels'].isChecked()); p.branch.setCurrentText('E02+' if i%2 else 'E01-')
            p.choose_preset('A' if i%2 else 'B')
            view.ax.set(xlim=(-.2,.2),ylim=(-.2,.2),zlim=(-.2,.2))
            before=spy.count(); view.canvas.draw(); self.assertEqual(spy.count(),before+1)
            self.assertEqual(view._draw_cid,cid); self.assertIn('CLIPS',p.status.text())
        p.close(); before=spy.count(); status=p.status.text(); view.canvas.draw()
        self.assertEqual(spy.count(),before); self.assertEqual(p.status.text(),status)
        self.assertNotIn(cid,view.canvas.callbacks.callbacks.get('draw_event',{}))
        # Parent destruction also disconnects without requiring closeEvent on a child.
        other=shell_panel.ShellPanel(); registry=other.view.canvas.callbacks; other_cid=other.view._draw_cid
        other.deleteLater(); QCoreApplication.sendPostedEvents(None,QEvent.Type.DeferredDelete)
        self.assertNotIn(other_cid,registry.callbacks.get('draw_event',{}))

    def test_unavailable_status_survives_late_notification(self):
        with patch.object(shell_panel,'load_reference',side_effect=ReferenceError('injected invalid reference')): other=shell_panel.ShellPanel()
        try:
            other.operation_notice='Old operation completed'; other.view.view_changed.emit()
            self.assertIn('unavailable',other.status.text()); self.assertIn('invalid reference',other.status.text())
            self.assertNotIn('Old operation completed',other.status.text())
            self.assertTrue(all(not b.isEnabled() for b in other.export_buttons.values()))
        finally: other.close(); other.deleteLater()
