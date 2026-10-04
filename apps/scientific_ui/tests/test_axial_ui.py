"""Real Qt cache/export/reference boundary and visual evidence for APP-G."""
import ast
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

os.environ.setdefault('QT_QPA_PLATFORM','offscreen')
os.environ.setdefault('QT_OPENGL','software')
from trioctagon_ui.qt_runtime import prepare_qt
prepare_qt()
from PySide6.QtCore import Qt
from PySide6.QtTest import QTest
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtWidgets import QApplication
from trioctagon_ui.app import MainWindow
from trioctagon_ui import requests as r, worker, axial_artifacts as codec, axial_exports
from trioctagon_ui.axial_reference import load_reference, RESOURCE_SHA256
from test_axial_transport import explicit, source, result
from test_requests import example
from test_worker_contract import record


class AxialReferenceTests(unittest.TestCase):
    def test_static_identity_and_exact_bounds(self):
        ref=load_reference();m3=ref['m3']
        self.assertEqual(m3['sufficient_entry_index'],301);self.assertEqual(m3['entrance_squared_norm'],3)
        self.assertEqual(m3['two_step_contraction_bound'],{'numerator':4789,'denominator':5000,'display':'0.9578'})
        self.assertIn('separate interval Krawczyk',m3['statement']);self.assertIn('nonzero and reverse',m3['statement'])
        self.assertIn('outer image enclosure',m3['outer_image_qualification']);self.assertIsNone(ref['reference_comparison'])
        self.assertEqual(len(ref['authorities']),5)

    def test_tampered_norm_n_q_lambda_and_resource_refused(self):
        from trioctagon_ui.axial_artifacts import plain
        mutations=(lambda v:v['m3'].update(entrance_squared_norm=9),lambda v:v['m3'].update(sufficient_entry_index=300),
            lambda v:v['m3']['two_step_contraction_bound'].update(numerator=4790),
            lambda v:v['m3']['model'].update(lambda_c='0.3674763946042135'),lambda v:v.update(reference_comparison='M3 CERTIFIED'))
        for mutate in mutations:
            value=plain(load_reference());mutate(value)
            with self.subTest(mutation=mutate),self.assertRaisesRegex(ValueError,'identity'):load_reference(json.dumps(value).encode())
        with self.assertRaises(ValueError):load_reference(b'{}')

    def test_no_run_matching_or_strengthened_theorem(self):
        from trioctagon_ui.axial_artifacts import plain
        ref=plain(load_reference());text=json.dumps(ref)
        for phrase in ('first entry','global basin','all mu','lambda=0.5','M2->M3 branch continuation'):
            self.assertNotIn(phrase,text)
        self.assertIn('not a physical field',text)
        # Norm nine and rounded inputs remain ordinary observations, never matched.
        values=explicit();values['omega']=[['3','0'],['0','0'],['0','0']]
        for inputs in (values,explicit()):
            a=result(r.analysis_request('axial_snapshot',inputs))['data']
            self.assertIsNone(a['reference_comparison']);self.assertEqual(a['evidence_class'],'FLOATING_OBSERVATION')


class AxialUITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.qt=QApplication.instance() or QApplication([])
        # Windows offscreen QPA has no system font discovery. Load an installed
        # OS font for honest readable screenshots; no font is redistributed.
        if os.environ.get('QT_QPA_PLATFORM') == 'offscreen':
            font = Path(os.environ.get('WINDIR', 'C:/Windows'))/'Fonts/segoeui.ttf'
            index = QFontDatabase.addApplicationFont(str(font))
            families = QFontDatabase.applicationFontFamilies(index)
            if not families: raise AssertionError('Visual review requires a readable installed system font')
            cls.qt.setFont(QFont(families[0], 10))
        cls.parent=record(r.run_request(example('3')))

    def setUp(self):
        self.w=MainWindow();self.w.resize(1600,1100);self.w.tabs.setCurrentIndex(1);self.w.observer_tabs.setCurrentWidget(self.w.axial_panel)
        self.w.show();QApplication.processEvents()

    def tearDown(self):
        self.w.close();self.w.deleteLater();QApplication.processEvents()

    def show(self,envelope):
        response=worker.respond(envelope)
        self.assertEqual(response['status'],'completed',response.get('error'))
        self.w._completed(response);QApplication.processEvents()
        return self.w.axial_panel.view

    def screen(self,name):
        if os.environ.get('TRIOCTAGON_UI_EVIDENCE'):
            path=Path(os.environ['TRIOCTAGON_UI_EVIDENCE'])/'axial-visual';path.mkdir(exist_ok=True)
            QApplication.processEvents();self.w.grab().save(str(path/(name+'.png')))

    def test_empty_explicit_action_keyboard_and_reduced_motion(self):
        p=self.w.axial_panel;self.assertIn('NOT ANALYZED',p.evidence.text());self.screen('01-empty')
        mode,edit,button=p.forms['axial_snapshot'];edit.setPlainText(json.dumps(explicit()))
        with patch.object(self.w.jobs,'start') as start:
            button.setFocus();QTest.keyClick(button,Qt.Key.Key_Space);QApplication.processEvents()
            self.assertEqual(start.call_count,1);self.assertEqual(start.call_args.args[0]['operation'],'passive_analysis')
        button.setFocus();QTest.keyClick(button,Qt.Key.Key_Tab);self.assertIsNotNone(self.qt.focusWidget())
        self.w.reduced_motion.setChecked(True);self.assertFalse(self.w.play_timer.isActive())
        self.assertFalse(self.w.jobs.busy)

    def test_state_all_values_exact_tokens_and_no_renderer_science(self):
        view=self.show(r.analysis_request('axial_snapshot',explicit()))
        p=self.w.axial_panel;self.assertIn('CURRENT BINARY64 EXPERIMENT',p.evidence.text())
        fields=[p.tables['axial_snapshot'].item(i,0).text() for i in range(p.tables['axial_snapshot'].rowCount())]
        for field in ('snapshot.Gamma','snapshot.C_norm','snapshot.W_norm','snapshot.intensity','snapshot.W[0]','snapshot.C_parallel[0]','snapshot.C_perp[0]'):
            self.assertIn(field,fields)
        self.assertEqual(p.raw.toPlainText(),view.canonical_json);self.screen('02-state')
        from kernel_physics import api
        with patch.object(api,'axial_snapshot',side_effect=AssertionError('renderer calculation')):
            p.show_view(view)

    def test_sparse_history_signed_values_and_planar_aspect(self):
        view=self.show(r.analysis_request('axial_history',{'sample_indices':['0','2','3']},source=source(self.parent)))
        p=self.w.axial_panel;plots=p.history_plot
        self.assertEqual(list(plots.figures[0].axes[0].lines[0].get_xdata()),[0,2,3])
        for ax,field in zip(plots.figures[0].axes,('W_x','W_y','Gamma')):self.assertIn(field,ax.get_ylabel())
        self.assertEqual(plots.figures[1].axes[0].get_aspect(),1.0)
        self.screen('03-history');plots.tabs.setCurrentIndex(1);self.screen('04-planar')
        with patch.object(self.w.jobs,'start') as start,patch.object(worker,'execute') as execute:
            p.select_sample(view.result['parent_digest'],1);self.assertEqual(p.labels['axial_snapshot'].text(),'NOT ANALYZED')
            self.screen('05-not-analyzed');p.select_sample(view.result['parent_digest'],2)
            self.assertIn('ordinal 2',p.labels['axial_snapshot'].text());start.assert_not_called();execute.assert_not_called()

    def test_budget_prediction_and_recorded_adjacent_views(self):
        view=self.show(r.analysis_request('axial_source_budget',explicit('axial_source_budget')))
        p=self.w.axial_panel;self.assertIn('PREDICTION',p.labels['axial_source_budget'].text());self.assertEqual(p.terms.rowCount(),7)
        self.assertIsNone(view.artifact['data']['budget']['comparison_residuals']);self.screen('06-prediction')
        self.show(r.analysis_request('axial_source_budget',{'after_sample_index':'1'},source=source(self.parent)))
        self.assertIn('RECORDED ADJACENT COMPARISON',p.labels['axial_source_budget'].text());self.screen('07-adjacent')

    def test_error_cancelled_failed_keep_cache(self):
        view=self.show(r.analysis_request('axial_snapshot',explicit()));p=self.w.axial_panel
        p.forms['axial_snapshot'][1].setPlainText('{"omega":[]}');p.analyze('axial_snapshot')
        self.assertIs(p.view,view);self.assertIn('REFUSED',p.status.text());self.screen('09-refusal')
        self.w._failed({'operation':'passive_analysis','exception_class':'ValueError','message':'test refusal'})
        self.assertIs(p.view,view);self.w._cancelled();self.assertIs(p.view,view)
        self.assertEqual(len(self.w.analysis_cache),1)

    def test_real_worker_completion_failure_and_cancellation_preserve_cache(self):
        from test_ui import spin_until
        p=self.w.axial_panel
        p.forms['axial_snapshot'][1].setPlainText(json.dumps(explicit()))
        p.forms['axial_snapshot'][2].click();spin_until(lambda: not self.w.jobs.busy)
        self.assertEqual(self.w.jobs.state,'completed');view=p.view;self.assertIsNotNone(view)
        invalid=explicit();invalid['omega'][0][0]='1e200'
        p.forms['axial_snapshot'][1].setPlainText(json.dumps(invalid));p.forms['axial_snapshot'][2].click()
        spin_until(lambda:not self.w.jobs.busy)
        self.assertEqual(self.w.jobs.state,'failed');self.assertIs(p.view,view)
        p.forms['axial_snapshot'][1].setPlainText(json.dumps(explicit()));p.forms['axial_snapshot'][2].click()
        self.w.jobs.cancel();spin_until(lambda:not self.w.jobs.busy)
        self.assertEqual(self.w.jobs.state,'cancelled');self.assertIs(p.view,view)

    def test_plot_class_contains_only_presentation_calls(self):
        from trioctagon_ui import plots
        tree=ast.parse(Path(plots.__file__).read_text())
        owner=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='AxialHistoryPlot')
        for node in ast.walk(owner):
            if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute):
                self.assertNotIn(node.func.attr,('cross','dot','norm','step','axial_snapshot','axial_source_budget','sin','cos','sqrt'))

    def test_static_reference_and_tampered_resource_display(self):
        p=self.w.axial_panel;p.sections.setCurrentIndex(3);self.screen('08-reference')
        self.assertIn('N=301',p.reference_text.toPlainText());self.assertIn('4789/5000',p.reference_text.toPlainText())
        with patch.object(worker,'execute') as execute:
            p.sections.setCurrentIndex(0);p.sections.setCurrentIndex(3);execute.assert_not_called()

    def test_cached_exports_saved_import_no_recompute_or_overwrite(self):
        view=self.show(r.analysis_request('axial_history',{'sample_indices':['0','2']},source=source(self.parent)))
        from kernel_physics import api
        with tempfile.TemporaryDirectory() as directory,patch.object(api,'axial_snapshot',side_effect=AssertionError('export recompute')),patch.object(api,'axial_source_budget',side_effect=AssertionError('export recompute')),patch.object(self.w.jobs,'start') as start:
            root=Path(directory)
            axial_exports.export_json(view,root/'x.axial.json');axial_exports.export_csv(view,root/'x.csv')
            for ext in ('png','svg'):axial_exports.export_plot(view,self.w.axial_panel.history_plot.figures[0],root/('x.'+ext))
            self.assertEqual((root/'x.axial.json').read_text(),view.canonical_json)
            for ext in ('csv','png','svg'):
                meta=json.loads((root/('x.'+ext+'.provenance.json')).read_text())
                self.assertEqual(meta['axial_observation']['content_sha256'],view.artifact['content_sha256'])
                self.assertEqual(meta['axial_observation']['selection'],codec.plain(view.artifact['selection']))
            with self.assertRaises(FileExistsError):axial_exports.export_json(view,root/'x.axial.json')
            loaded=self.w.axial_panel.load_path(root/'x.axial.json');self.assertTrue(loaded.saved_import)
            self.assertIn('UNAUTHENTICATED SAVED OBSERVATIONS',self.w.axial_panel.evidence.text());start.assert_not_called()
            self.screen('10-saved-import')
