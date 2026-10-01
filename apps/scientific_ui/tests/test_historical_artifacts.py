"""P2 inert Historical inspection. All scientific fixtures are retained bytes."""
from contextlib import ExitStack
from dataclasses import FrozenInstanceError
import hashlib
from importlib import metadata
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from trioctagon_ui import artifact_loading as loading
from trioctagon_ui.historical_loading import (LoadedHistoricalResult, LoadedHistoricalReceipt,
    RESULT_FAMILY, RECEIPT_FAMILY, parse_historical)
from trioctagon_ui.historical_identity import historical_lock, verify_installed_historical, verify_historical_wheel
from trioctagon_ui.historical_views import HistoricalResultView, HistoricalReceiptView, stored_rows
from trioctagon_ui.artifact_views import DerivedArtifactView, AttemptReceiptView

FIXTURES = Path(__file__).parent / "fixtures/historical"


class HistoricalLoadingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="historical-view-")
        self.root = Path(self.temp.name)
        self.library = loading.ArtifactLibrary()

    def tearDown(self):
        self.temp.cleanup()

    def load(self, name="TEST_ONLY_result_0.json"):
        return self.library.load(FIXTURES / name)

    def test_exact_protocol_archive_and_installed_pin(self):
        identity = verify_installed_historical()
        self.assertEqual(identity.version, "0.1.0")
        self.assertEqual(identity.approved_archive_sha256, "734ae5d2734ce9b42301b851e23d57c4b9db37ac02b32b0fadff328d4724952f")
        wheel = Path(os.environ["TRIOCTAGON_UI_HISTORICAL_WHEEL"])
        self.assertEqual(verify_historical_wheel(wheel, historical_lock()), identity.approved_archive_sha256)
        changed = self.root / wheel.name; changed.write_bytes(wheel.read_bytes() + b"changed")
        with self.assertRaises(ValueError): verify_historical_wheel(changed, historical_lock())
        with self.assertRaises(metadata.PackageNotFoundError): metadata.distribution("trioctagon-historical-kernel")
        requires = metadata.requires("trioctagon-scientific-ui")
        self.assertIn("trioctagon-historical-protocol==0.1.0", requires)
        self.assertFalse(any("historical-kernel" in v for v in requires))

    def test_protocol_content_closure_origin_fail_before_parser(self):
        dist = metadata.distribution("trioctagon-historical-protocol")
        target = Path(dist.locate_file("trioctagon_historical_protocol/records.py"))
        original = Path.read_bytes
        with patch.object(Path, "read_bytes", lambda p: b"changed" if p == target else original(p)):
            with self.assertRaisesRegex(ValueError, "content mismatch"): self.load()
        with patch.object(Path, "rglob", return_value=iter(())):
            with self.assertRaisesRegex(ValueError, "closure mismatch"): verify_installed_historical()
        with patch("trioctagon_ui.historical_identity.find_spec", return_value=None):
            with self.assertRaisesRegex(ValueError, "import path"): verify_installed_historical()

    def test_immutable_fixture_identities_and_all_five_real_operations(self):
        for row in json.loads((FIXTURES / "manifest.json").read_bytes()):
            with self.subTest(file=row["file"]):
                raw = (FIXTURES / row["file"]).read_bytes()
                self.assertEqual(hashlib.sha256(raw).hexdigest(), row["sha256"])
                self.assertEqual(len(raw), row["bytes"])
        for i in range(5):
            with self.subTest(operation=i):
                item = self.load(f"H6B_admitted_{i}.json")
                view = HistoricalResultView(item)
                self.assertEqual(item.raw, (FIXTURES / f"H6B_admitted_{i}.json").read_bytes())
                self.assertIn("HISTORICAL MATHEMATICAL RECONSTRUCTION", view.heading)
                self.assertEqual(view.panels["Historical identity"]["issuance_class"], "UNATTESTED_HISTORICAL_RECONSTRUCTION")
                with self.assertRaises(FrozenInstanceError): item.sha256 = "changed"
                with self.assertRaises(TypeError): view.payload["operation"] = "changed"

    def test_N34_claims_observations_and_all_qualification_fields(self):
        for i in range(5):
            item = self.load(f"H6B_admitted_{i}.json"); view = HistoricalResultView(item)
            self.assertIn("ORIGINAL ARTIFACT CLAIMS", view.panels)
            observations = view.panels["CURRENT VIEWER OBSERVATIONS"]
            self.assertFalse(observations["equations_replayed"])
            self.assertFalse(observations["historical_authorship_authenticated"])
            self.assertEqual(observations["producer_execution_attestation"], "UNAVAILABLE")
            self.assertEqual(observations["physical_validation"], "NONE")
            self.assertFalse(observations["production_attestation_enabled"])
            self.assertIn("LOCAL_CHECK_PASSED is not VERIFIED", view.qualification)
            self.assertIn("WINDOWS EXECUTION BINDING = NOT PROVEN", view.qualification)
            self.assertEqual(set(view.qualification_fields), {"historical_status", "formula_survival_scope", "current_reuse",
                "operational_production_scope", "mathematical_reconstruction", "numerical_differences", "physical_validation", "harmonic_qualification", "text"})
            self.assertEqual(item.raw, (FIXTURES / f"H6B_admitted_{i}.json").read_bytes())

    def test_all_cross_family_loaders_and_inspectors_are_closed(self):
        from trioctagon_analysis.codec import ParseLimits
        from trioctagon_analysis.records import DerivedAnalysisRecord, AttemptReceipt
        limits = ParseLimits(loading.MAX_INPUT_FILE_BYTES, loading.MAX_JSON_DEPTH)
        for name in ("TEST_ONLY_core_result.json", "TEST_ONLY_core_receipt.json", "TEST_ONLY_core_catalogue.json", "TEST_ONLY_core_request.json"):
            for family in (RESULT_FAMILY, RECEIPT_FAMILY):
                with self.subTest(name=name, family=family), self.assertRaises(ValueError):
                    parse_historical((FIXTURES / name).read_bytes(), family, "1.0.0", limits)
        for name in ("TEST_ONLY_result_0.json", "TEST_ONLY_receipt_refused.json"):
            for owner in (DerivedAnalysisRecord, AttemptReceipt):
                with self.subTest(owner=owner, name=name), self.assertRaises(ValueError):
                    owner.from_bytes((FIXTURES / name).read_bytes(), limits)
        result = self.load(); receipt = self.load("TEST_ONLY_receipt_refused.json")
        for inspector, item in ((HistoricalResultView, receipt), (HistoricalReceiptView, result),
                (DerivedArtifactView, result), (DerivedArtifactView, receipt), (AttemptReceiptView, result), (AttemptReceiptView, receipt)):
            with self.subTest(inspector=inspector), self.assertRaises(TypeError): inspector(item)
        for name in ("derived.json", "receipt.json"):
            item = self.library.load(FIXTURES.parent / name)
            for inspector in (HistoricalResultView, HistoricalReceiptView):
                with self.assertRaises(TypeError): inspector(item)
        for legacy in (b'{"result_kind":"analysis","data":{}}', b'{"family":"LEGACY_CACHE","schema":"1.0.0"}'):
            with self.assertRaises(ValueError): parse_historical(legacy, RESULT_FAMILY, "1.0.0", limits)

    def test_schema_family_context_digest_and_noncanonical_fail_closed(self):
        original = (FIXTURES / "TEST_ONLY_result_0.json").read_bytes()
        cases = [original + b"\n", b'\xef\xbb\xbf'+original, b'{"family":"X",'+original[1:]]
        for path, value in [(('schema',),'9.0.0'), (('family',),'TRIOCTAGON_HISTORICAL_CATALOGUE'),
                (('profile',),'CORE'), (('semantic_result_digest','sha256'),'0'*64),
                (('payload','operation'),'historical.unknown'), (('payload','output_omega',0,'real','f64'),'0x1.0000000000000p+1'),
                (('assurance','producer_execution_attestation','state'),'VERIFIED')]:
            data = json.loads(original); at = data
            for part in path[:-1]: at = at[part]
            at[path[-1]] = value
            cases.append(json.dumps(data,sort_keys=True,separators=(",", ":")).encode())
        for i, raw in enumerate(cases):
            file = self.root / f"bad-{i}.json"; file.write_bytes(raw)
            with self.subTest(i=i), self.assertRaises(ValueError): self.library.load(file)
        for i in range(5):
            with self.assertRaises(ValueError): self.load(f"TEST_ONLY_request_{i}.json")
        for family in ("TRIOCTAGON_HISTORICAL_CATALOGUE", "TRIOCTAGON_HISTORICAL_PROVIDER_BUILD"):
            file = self.root / "envelope.json"; file.write_text(json.dumps(dict(family=family,schema="1.0.0")))
            with self.assertRaises(ValueError): self.library.load(file)
        self.assertEqual(self.library.items, ())

    def test_copy_snapshot_no_replace_external_identity_and_shared_quotas(self):
        item = self.load(); destination = self.root / "copy.json"
        loading.copy_artifact(item, destination)
        self.assertEqual(destination.read_bytes(), item.raw)
        with self.assertRaises(FileExistsError): loading.copy_artifact(item, destination)
        with self.assertRaises(FileExistsError): loading.copy_artifact(item, item.source)
        with self.assertRaises(ValueError): self.library.load(item.source,expected_sha256="0"*64,identity_source="test")
        self.assertIs(self.load(), item)
        with patch.object(loading, "MAX_LOADED_ANALYSIS_ARTIFACTS", 1):
            with self.assertRaisesRegex(ValueError,"RESOURCE_LIMIT"): self.load("TEST_ONLY_receipt_refused.json")
        with patch.object(loading, "MAX_RETAINED_ANALYSIS_BYTES", len(item.raw)):
            with self.assertRaisesRegex(ValueError,"RESOURCE_LIMIT"): self.load("TEST_ONLY_receipt_refused.json")
        changed = self.root / "source.json"; changed.write_bytes(item.raw)
        snapshot = self.library.load(changed); changed.write_bytes(b"changed after load")
        self.assertEqual(snapshot.raw,item.raw)

    def test_depth_and_input_size_limits_apply_to_historical(self):
        deep=self.root/'deep.json';deep.write_bytes(b'{"family":"TRIOCTAGON_HISTORICAL_DERIVED_ANALYSIS_RECORD","schema":"1.0.0","x":'+b'['*33+b'0'+b']'*33+b'}')
        with self.assertRaises(ValueError): self.library.load(deep)
        large=self.root/'large.json'
        with large.open('wb') as f:f.truncate(loading.MAX_INPUT_FILE_BYTES+1)
        with self.assertRaises(ValueError):self.library.load(large)

    def test_step_exact_signed_zero_and_precision_is_presentation_only(self):
        item = self.load(); view=HistoricalResultView(item)
        rows=tuple(stored_rows(view.values)); short=tuple(stored_rows(view.values,3))
        self.assertEqual([r[:2] for r in rows],[r[:2] for r in short])
        self.assertIn(("input_omega[1].imag","-0x0.0p+0","-0"),rows)
        self.assertEqual(view.values['update_count'],1)
        for field in ('t','q','z','clock','geometry'):self.assertNotIn(field,view.values)
        for precision in (0,18,True):
            with self.assertRaises(ValueError):tuple(stored_rows(view.values,precision))

    def test_run_rows_terminal_constructor_zero_and_N0(self):
        view=HistoricalResultView(self.load('H6B_admitted_1.json'))
        self.assertEqual(len(view.run_rows),1024)
        self.assertEqual([r['row_ordinal'] for r in view.run_rows],list(range(1024)))
        self.assertNotIn('row_ordinal',view.terminal)
        self.assertEqual(view.terminal['update_index'],1024)
        self.assertEqual(view.run_rows[0]['readout']['initialization'],'HISTORICAL_CONSTRUCTOR_ZERO')
        self.assertEqual(view.run_rows[1]['readout']['initialization'],'RECOMPUTED')
        for name in ('H6B_measurement_0.json','H6B_measurement_2.json'):
            view=HistoricalResultView(self.load(name))
            self.assertEqual(view.run_rows,())
            self.assertEqual(view.terminal['update_index'],0)
            self.assertEqual(view.terminal['initialization'],'CONSTRUCTOR_INITIAL')
            self.assertIn('N=0',view.note)

    def test_staged_raw_pair_order_supplied_clock_and_constants(self):
        view=HistoricalResultView(self.load('H6B_admitted_2.json'))
        self.assertEqual(view.values['initialization'],'RECOMPUTED')
        self.assertEqual(view.values['clock_qualification'],'USER_SUPPLIED_CLOCK')
        fields=[r[0] for r in stored_rows(view.values)]
        self.assertEqual([f for f in fields if f.startswith('C[')],['C[23]','C[31]','C[12]'])
        self.assertIn('resolved_constants.readout.harmonic',fields)

    def test_ema_memory_not_advanced(self):
        view=HistoricalResultView(self.load('H6B_admitted_3.json'))
        self.assertEqual(view.values['memory_input'],view.values['memory_output'])
        self.assertEqual(view.values['memory_update_count'],0)
        self.assertEqual(view.values['memory_qualification'],'SUPPLIED_MEMORY_NOT_HISTORY_VERIFIED')
        self.assertIn('NO MEMORY ADVANCE OCCURRED',view.note)
        self.assertIn('Detached numeric EMA variable',view.note)

    def test_chart_exact_order_flags_and_small_values_retained(self):
        for name in ('H6B_admitted_4.json','H6B_measurement_63.json','H6B_measurement_67.json'):
            item=self.load(name);view=HistoricalResultView(item)
            fields=[r[0] for r in stored_rows(view.values)]
            self.assertEqual([f for f in fields if f.startswith('chart[')],['chart[cu]','chart[cx]','chart[cy]'])
            self.assertEqual(view.values['chart_order'],('cu','cx','cy'))
            self.assertIn('underflow_flags',view.values)
            self.assertIn('zero_classification',view.values)
            self.assertIn('basis_digest',view.values)
            self.assertEqual(item.raw,(FIXTURES/name).read_bytes())

    def test_N18_receipt_cannot_expose_result_or_terminal(self):
        for name in ('TEST_ONLY_receipt_refused.json','TEST_ONLY_receipt_cancelled.json','H6B_receipt_68.json'):
            view=HistoricalReceiptView(self.load(name))
            self.assertIn('NOT A SCIENTIFIC RESULT',view.heading)
            self.assertFalse(hasattr(view,'payload'))
            self.assertFalse(hasattr(view,'terminal'))
            self.assertEqual(set(view.values),{'outcome','stage','category','argument_field','updates_completed','diagnostic','provider','checks','staging','request_digest'})
            self.assertLessEqual(len(view.values['diagnostic'].encode()),loading.MAX_DISPLAY_DIAGNOSTIC_BYTES)

    def test_import_order_and_absent_scientific_provider_closure(self):
        for core_first in (True,False):
            result=subprocess.run([sys.executable,'-I','-B','-c',INERT_CHILD,str(FIXTURES),str(core_first)],
                cwd=self.root,capture_output=True,text=True,encoding='utf-8',timeout=90)
            self.assertEqual(result.returncode,0,result.stdout+result.stderr)
            self.assertIn('PASS',result.stdout)


INERT_CHILD = r'''
import sys,pathlib,importlib,importlib.abc,importlib.metadata,json
network=[]
def audit(event,args):
 if (event.startswith('socket.') and event!='socket.gethostname') or event=='urllib.Request':
  network.append(event);raise AssertionError('network access in viewer')
sys.addaudithook(audit)
class Deny(importlib.abc.MetaPathFinder):
 def find_spec(self,fullname,path=None,target=None):
  if fullname.split('.')[0] in {'kernel_physics','kernel_TO','torment_service','trioctagon_historical_kernel','numpy','sympy'} or fullname in {'trioctagon_analysis.coordinator','trioctagon_analysis.b2a_worker','trioctagon_analysis.b2a_windows'}:raise AssertionError('execution dependency: '+fullname)
sys.meta_path.insert(0,Deny())
try:importlib.metadata.distribution('trioctagon-historical-kernel')
except importlib.metadata.PackageNotFoundError:pass
else:raise AssertionError('Historical kernel installed')
order=['trioctagon_analysis.records','trioctagon_historical_protocol.records']
if sys.argv[2]=='False':order.reverse()
for n in order:importlib.import_module(n)
from trioctagon_analysis import provider
def denied(*a,**kw):raise AssertionError('Core provider invoked')
provider.copy_recorded=denied
from trioctagon_ui.artifact_loading import ArtifactLibrary,copy_artifact
from trioctagon_ui.historical_views import HistoricalResultView,HistoricalReceiptView
from trioctagon_ui.historical_loading import LoadedHistoricalResult
from trioctagon_analysis.codec import ParseLimits
from trioctagon_analysis.records import DerivedAnalysisRecord
from trioctagon_ui.historical_loading import parse_historical,RESULT_FAMILY,RECEIPT_FAMILY
fixtures=pathlib.Path(sys.argv[1]);limits=ParseLimits(16777216,32)
for owner,name in [(DerivedAnalysisRecord,'TEST_ONLY_result_0.json')]:
 try:owner.from_bytes((fixtures/name).read_bytes(),limits)
 except ValueError:pass
 else:raise AssertionError('Historical bytes entered Core owner')
for family,name in [(RESULT_FAMILY,'TEST_ONLY_core_result.json'),(RECEIPT_FAMILY,'TEST_ONLY_core_receipt.json'),(RESULT_FAMILY,'TEST_ONLY_receipt_refused.json'),(RECEIPT_FAMILY,'TEST_ONLY_result_0.json')]:
 try:parse_historical((fixtures/name).read_bytes(),family,'1.0.0',limits)
 except ValueError:pass
 else:raise AssertionError('cross-family routing broadened by import order')
for i,name in enumerate(['H6B_admitted_0.json','H6B_admitted_1.json','H6B_admitted_2.json','H6B_admitted_3.json','H6B_admitted_4.json','TEST_ONLY_receipt_refused.json']):
 item=ArtifactLibrary().load(pathlib.Path(sys.argv[1])/name)
 view=(HistoricalResultView if type(item) is LoadedHistoricalResult else HistoricalReceiptView)(item)
 target=pathlib.Path.cwd()/('copy-'+sys.argv[2]+'-'+str(i)+'.json');copy_artifact(item,target)
 assert target.read_bytes()==item.raw
assert not any(n.split('.')[0] in {'kernel_physics','kernel_TO','torment_service','trioctagon_historical_kernel','numpy','sympy'} for n in sys.modules)
assert not network
print('PASS: inert Historical route; no scientific imports or provider invocation')
'''


class HistoricalWidgetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from trioctagon_ui.qt_runtime import prepare_qt
        prepare_qt()
        from PySide6.QtWidgets import QApplication
        cls.qt=QApplication.instance() or QApplication([])

    def setUp(self):
        from trioctagon_ui.app import MainWindow
        self.w=MainWindow();self.w.tabs.setCurrentIndex(3);self.w.repro_tabs.setCurrentWidget(self.w.artifacts)

    def tearDown(self):
        self.w.close();self.w.deleteLater();self.qt.processEvents()

    def test_all_views_readonly_and_no_execution_controls(self):
        from PySide6.QtWidgets import QPushButton,QAbstractItemView,QPlainTextEdit
        panel=self.w.artifacts
        for name in [f'H6B_admitted_{i}.json' for i in range(5)]+['TEST_ONLY_receipt_refused.json']:
            item=panel.load_path(FIXTURES/name);self.assertIsNotNone(item,panel.status.text())
            inspector=panel.historical
            self.assertTrue(panel.result_area.isHidden())
            self.assertFalse(inspector.isHidden())
            self.assertEqual(inspector.value_table.editTriggers(),QAbstractItemView.EditTrigger.NoEditTriggers)
            self.assertEqual([b.text() for b in panel.findChildren(QPushButton)],['Load Artifact','Copy canonical artifact bytes'])
            self.assertIn('UNAVAILABLE',panel.qualification.text())
            self.assertIn('Analysis loader: independent installed pin 0.1.1',self.w.identity.text())
            self.assertIn('PRODUCTION ATTESTATION = NOT ENABLED',panel.qualification.text())
            if type(item) is LoadedHistoricalResult:
                qualifications=next(inspector.widget(i) for i in range(inspector.count()) if inspector.tabText(i)=='Frozen qualifications')
                self.assertIsInstance(qualifications,QPlainTextEdit);self.assertTrue(qualifications.isReadOnly())
                self.assertIn('physical_validation: NONE',qualifications.toPlainText())
            else:
                self.assertIn('NOT A SCIENTIFIC RESULT',panel.heading.text())
                self.assertIsNone(inspector.run_table);self.assertIsNone(inspector.terminal_table)

    def test_rows_and_terminal_distinct_and_empty_run(self):
        panel=self.w.artifacts;panel.load_path(FIXTURES/'H6B_admitted_1.json')
        inspector=panel.historical
        self.assertEqual(inspector.row_selector.maximum(),1023)
        self.assertIn('HISTORICAL_CONSTRUCTOR_ZERO',[inspector.run_table.item(i,1).text() for i in range(inspector.run_table.rowCount())])
        inspector.row_selector.setValue(1)
        self.assertIn('RECOMPUTED',[inspector.run_table.item(i,1).text() for i in range(inspector.run_table.rowCount())])
        self.assertIsNot(inspector.run_table,inspector.terminal_table)
        before=[inspector.terminal_table.item(i,1).text() for i in range(inspector.terminal_table.rowCount())]
        inspector.precision.setValue(3)
        self.assertEqual(before,[inspector.terminal_table.item(i,1).text() for i in range(inspector.terminal_table.rowCount())])
        panel.load_path(FIXTURES/'H6B_measurement_2.json')
        self.assertEqual(panel.historical.run_table.rowCount(),0)
        self.assertFalse(panel.historical.row_selector.isEnabled())
        self.assertGreater(panel.historical.terminal_table.rowCount(),0)

    def test_N21_selection_and_jobs_remain_inert_all_operations_and_receipt(self):
        from test_worker_contract import run_child
        from test_requests import example
        from trioctagon_ui import requests
        from kernel_physics import api
        child,response=run_child(requests.run_request(example('1')))
        self.assertEqual(child.returncode,0,child.stderr);self.w._completed(response)
        w=self.w
        before=(w.current,w.current_run,w.current_geometry,w.analysis_current,len(w.records),w.compare_a.count(),w.compare_b.count())
        with ExitStack() as stack,tempfile.TemporaryDirectory() as directory:
            traps=[stack.enter_context(patch.object(w.jobs,'start',side_effect=AssertionError('job invoked')))]
            traps.append(stack.enter_context(patch.object(w.artifacts,'core_requested')))
            for name in ('run','step','get_geometry'):
                traps.append(stack.enter_context(patch.object(api,name,side_effect=AssertionError('Core science invoked'))))
            for i,name in enumerate([f'H6B_admitted_{i}.json' for i in range(5)]+['TEST_ONLY_receipt_refused.json']):
                item=w.artifacts.load_path(FIXTURES/name);self.assertIsNotNone(item,w.artifacts.status.text())
                self.assertFalse(w.resume_button.isEnabled());self.assertFalse(w.checkpoint_button.isEnabled())
                w._resume();w._prepare_checkpoint();w._save_record();w._export_csv()
                self.assertIsNotNone(w.artifacts.copy_to(Path(directory)/f'copy-{i}.json'))
            for trap in traps:trap.assert_not_called()
        self.assertEqual(before,(w.current,w.current_run,w.current_geometry,w.analysis_current,len(w.records),w.compare_a.count(),w.compare_b.count()))
        w.repro_tabs.setCurrentIndex(0);self.assertFalse(w.checkpoint_button.isEnabled())
        w._history_selected(0);self.assertTrue(w.checkpoint_button.isEnabled())
        w.artifacts.load_path(FIXTURES.parent/'derived.json')
        self.assertTrue(w.artifacts.historical.isHidden());self.assertEqual(w.artifacts.table.rowCount(),20)
