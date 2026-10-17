"""Shell-format destination, identity and owned-publication failures (Windows)."""
import hashlib
import ctypes
from ctypes import wintypes
import json
import os
from pathlib import Path
import tempfile
import stat
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from trioctagon_ui import shell_exports as exports, _export_publication as publication
from trioctagon_ui.shell_reference import load_reference, canonical
from trioctagon_ui.shell_observer import Request, evaluate
from matplotlib.figure import Figure
from test_export_publication import alias_fixture, native_aliases, native_record, file_identity


class ShellExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reference=load_reference(); cls.observation=evaluate(cls.reference,Request()); cls.view={'camera':{},'numeric_view':True}
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='shell-export-'); self.root=Path(self.temp.name)
    def tearDown(self): self.temp.cleanup()
    def export(self,path): return exports.export_json(self.reference,self.observation,self.view,path)

    def test_json_identity_branch_labels_and_roundtrip(self):
        path=self.root/'result.shell.json'; result=self.export(path); raw=path.read_bytes(); data=json.loads(raw)
        digest=data.pop('content_sha256'); self.assertEqual(digest,hashlib.sha256(canonical(data)).hexdigest())
        self.assertEqual(result['sha256'],hashlib.sha256(raw).hexdigest())
        self.assertEqual(data['family'],'TRIOCTAGON_SPHERICAL_EDGE_OBSERVATION')
        self.assertEqual(len({b['branch'] for b in data['observation']['branches']}),42)
        self.assertEqual(data['implementation']['status'],'UNRELEASED_UNCOMMITTED_CANDIDATE')
        self.assertFalse(list(self.root.glob('.trioctagon-*')))

    def test_png_svg_sidecars(self):
        fig=Figure(); fig.add_subplot().plot([0,1],[0,1])
        for suffix in ('png','svg'):
            with self.subTest(suffix=suffix):
                path=self.root/('view.'+suffix)
                exports.export_image(self.reference,self.observation,self.view,fig,path)
                side=json.loads(path.with_suffix('.'+suffix+'.provenance.json').read_bytes())
                self.assertEqual(side['image_sha256'],hashlib.sha256(path.read_bytes()).hexdigest())
                cached=side['cached_observation']; digest=cached.pop('content_sha256')
                self.assertEqual(side['observation_digest'],digest); self.assertEqual(digest,hashlib.sha256(canonical(cached)).hexdigest())
                self.assertEqual(side['rendered_state'],self.view); self.assertFalse(side['pair_atomic'])

    def test_raw_hazards_and_protected_roots(self):
        for raw in ('relative.shell.json',r'\\server\share\x.shell.json',r'C:\a\..\x.shell.json',r'C:\a\.\x.shell.json',r'C:\a\x:stream.shell.json',r'C:\a\CON.shell.json',r'C:\a\bad.\x.shell.json'):
            with self.subTest(raw=raw), self.assertRaises(ValueError): exports.validate_destination(raw)
        with self.assertRaises(ValueError): exports.validate_destination(self.root/'x.shell.json',[self.root])
        for name in ('research','papers','trioctagon_ui'):
            folder=self.root/name; folder.mkdir()
            with self.assertRaises(ValueError): exports.validate_destination(folder/'x.shell.json')
        dataset=self.root/'dataset'; dataset.mkdir(); (dataset/'sweep-manifest.json').write_text('{}'); (dataset/'records').mkdir()
        with self.assertRaises(ValueError): exports.validate_destination(dataset/'records/x.shell.json')

    def test_existing_and_racing_primary_sidecars(self):
        path=self.root/'taken.shell.json'; path.write_bytes(b'other writer')
        with self.assertRaises(FileExistsError): self.export(path)
        self.assertEqual(path.read_bytes(),b'other writer')
        fig=Figure(); side=self.root/'image.png.provenance.json'; side.write_bytes(b'other sidecar')
        with self.assertRaises(FileExistsError): exports.export_image(self.reference,self.observation,self.view,fig,self.root/'image.png')
        self.assertFalse((self.root/'image.png').exists()); self.assertEqual(side.read_bytes(),b'other sidecar')
        real=publication._OwnedFile.publish; target=self.root/'race.shell.json'
        hits=[]
        def race(item): hits.append(1); target.write_bytes(b'racer'); return real(item)
        with patch.object(publication._OwnedFile,'publish',race), self.assertRaises(OSError): self.export(target)
        self.assertEqual(hits,[1])
        self.assertEqual(target.read_bytes(),b'racer'); self.assertFalse(list(self.root.glob('.trioctagon-*')))

    def test_write_flush_publish_and_cleanup_faults(self):
        for method in ('read','flush','publish'):
            with self.subTest(method=method), patch.object(publication._OwnedFile,method,side_effect=OSError('injected '+method)) as fault:
                with self.assertRaisesRegex(OSError,'injected '+method): self.export(self.root/(method+'.shell.json'))
                self.assertEqual(fault.call_count,1)
                native_record('shell-fault',method=method,hits=fault.call_count)
            self.assertFalse(list(self.root.iterdir()))
        fig=Figure()
        with patch.object(fig,'savefig',side_effect=OSError('injected image write')) as fault:
            with self.assertRaisesRegex(OSError,'injected image write'): exports.export_image(self.reference,self.observation,self.view,fig,self.root/'failed.png')
            self.assertEqual(fault.call_count,1)
        self.assertFalse(list(self.root.iterdir()))
        real=publication._OwnedFile.publish
        hits=[]
        def second(item):
            if item.destination.name.endswith('.provenance.json'): hits.append(1); raise OSError('injected second publication')
            return real(item)
        with patch.object(publication._OwnedFile,'publish',second), self.assertRaises(OSError): exports.export_image(self.reference,self.observation,self.view,fig,self.root/'pair.png')
        self.assertEqual(hits,[1])
        self.assertFalse(list(self.root.iterdir()))
        # Cleanup failure is reported, never disguised as successful publication.
        real_discard=publication._OwnedFile.discard
        cleanups=[]
        def noisy(item): cleanups.append(1); real_discard(item); raise OSError('injected cleanup diagnostic after owned deletion')
        with patch.object(publication._OwnedFile,'publish',side_effect=OSError('primary')) as fault, patch.object(publication._OwnedFile,'discard',noisy):
            with self.assertRaisesRegex(OSError,'cleanup incomplete') as caught: self.export(self.root/'cleanup.shell.json')
            self.assertEqual(fault.call_count,1); self.assertEqual(cleanups,[1]); self.assertIn('primary',str(caught.exception.__cause__))
        self.assertFalse(list(self.root.iterdir()))

    def test_ancestry_change_and_nonfinite_refused(self):
        real=exports.validate_destination; calls=[]
        def changed(*args,**kwargs):
            path,identity=real(*args,**kwargs); calls.append(1)
            return path,identity if len(calls)==1 else identity+(('injected',0,0),)
        with patch.object(exports,'validate_destination',changed), self.assertRaisesRegex(ValueError,'ancestry'): self.export(self.root/'change.shell.json')
        self.assertFalse(list(self.root.iterdir()))
        with self.assertRaises(ValueError): exports.artifact(self.reference,self.observation,{'bad':float('nan')})

    def test_sidecar_race_and_ancestor_rename_refused(self):
        fig=Figure(); primary=self.root/'race.png'; side=primary.with_suffix('.png.provenance.json'); real=publication._OwnedFile.publish
        expected=side.resolve(); hits=[]; identities=[]
        def race(item):
            if item.destination==expected: hits.append(1); side.write_bytes(b'independent sidecar'); identities.append(file_identity(side))
            return real(item)
        with patch.object(publication._OwnedFile,'publish',race), self.assertRaises(OSError): exports.export_image(self.reference,self.observation,self.view,fig,primary)
        self.assertEqual(hits,[1]); self.assertEqual(file_identity(side),identities[0])
        self.assertFalse(primary.exists()); self.assertEqual(side.read_bytes(),b'independent sidecar')
        self.assertFalse(list(self.root.glob('.trioctagon-*')))
        folder=self.root/'ancestor'; folder.mkdir()
        with exports.guarded_destination(folder/'p.shell.json'):
            with self.assertRaises(PermissionError): folder.rename(self.root/'changed')
        self.assertTrue(folder.is_dir())
        folder.rename(self.root/'changed'); self.assertTrue((self.root/'changed').is_dir())

    def test_native_alias_guards_exports_and_observation_contract(self):
        fig=Figure(); fig.add_subplot().plot([0,1],[0,1])
        for spelling in (0,1):
            with self.subTest(spelling=spelling), alias_fixture() as aliases:
                root=aliases[spelling]
                for paired in (False,True):
                    path=root/'guard.png'; side=path.with_suffix('.png.provenance.json') if paired else None
                    with exports.guarded_destination(path,side) as (admitted,recheck):
                        self.assertEqual(admitted,path.resolve()); recheck()
                for mode,request in (('exact',Request(unit='edge',frame='paper_c_global')),('generic',Request(preset=None,mode='R',value='0.9',unit='chord'))):
                    obs=evaluate(self.reference,request); target=root/(mode+'.shell.json')
                    result=exports.export_json(self.reference,obs,self.view,target)
                    raw=target.read_bytes(); data=json.loads(raw); digest=data.pop('content_sha256')
                    self.assertEqual(digest,hashlib.sha256(canonical(data)).hexdigest()); self.assertEqual(result['sha256'],hashlib.sha256(raw).hexdigest())
                    expected=exports.artifact(self.reference,obs,self.view); expected.pop('content_sha256')
                    self.assertEqual(data,expected)
                    self.assertEqual(len({b['branch'] for b in data['observation']['branches']}),42)
                    self.assertEqual(data['implementation'],exports.implementation_identity())
                    for suffix in ('png','svg'):
                        image=root/(mode+'.'+suffix); exports.export_image(self.reference,obs,self.view,fig,image)
                        side=json.loads(image.with_suffix('.'+suffix+'.provenance.json').read_bytes())
                        self.assertEqual(side['image_sha256'],hashlib.sha256(image.read_bytes()).hexdigest())
                        cached=side['cached_observation']; self.assertEqual(cached.pop('content_sha256'),digest)
                        self.assertEqual(cached,data); self.assertEqual(side['observation_digest'],digest)
                    native_record('shell-alias-exports',spelling=spelling,mode=mode,request=request.__dict__,implementation=data['implementation'],branches=42,content_sha256=digest,formats=['json','png','svg'])
                self.assertFalse(list(root.glob('.trioctagon-*')))

    def test_alias_protection_and_simulated_reparse(self):
        with alias_fixture() as aliases:
            for target_root in aliases:
                for protected_root in aliases:
                    with self.assertRaisesRegex(ValueError,'Protected'): exports.validate_destination(target_root/'x.shell.json',[protected_root])
            for name in ('research','papers','trioctagon_ui','dataset','repository'):
                folder=aliases[1]/name; folder.mkdir()
                if name=='dataset':
                    (folder/'sweep-manifest.json').write_text('{}'); folder=folder/'records'; folder.mkdir()
                if name=='repository': (folder/'.git').mkdir()
                for root in native_aliases(folder):
                    with self.assertRaisesRegex(ValueError,'protected'): exports.validate_destination(root/'x.shell.json')
            real=Path.lstat; selected=aliases[0]
            def reparse(path,*args,**kwargs):
                info=real(path,*args,**kwargs)
                if path==selected: return SimpleNamespace(st_file_attributes=info.st_file_attributes|stat.FILE_ATTRIBUTE_REPARSE_POINT)
                return info
            with patch.object(Path,'lstat',reparse), self.assertRaisesRegex(ValueError,'Reparse'): exports.validate_destination(selected/'x.shell.json')
            native_record('protections',raw_and_long=True,explicit_roots_both_spellings=True,synthetic_named_roots=True,reparse='SIMULATED')

    def test_real_replacement_between_guard_stages_refused(self):
        for stage in ('after-raw-inspection','before-handle-acquisition'):
            with self.subTest(stage=stage), alias_fixture() as aliases:
                folder=aliases[1]/'victim'; folder.mkdir(); target=folder/'x.shell.json'; moved=aliases[1]/'moved'
                before=file_identity(folder); hits=[]
                def swap():
                    folder.rename(moved); folder.mkdir(); hits.append(1)
                    self.assertNotEqual(file_identity(folder),before)
                name='_ancestry' if stage=='after-raw-inspection' else 'validate_destination'
                real=getattr(exports,name)
                def changed(*args,**kwargs):
                    result=real(*args,**kwargs)
                    if not hits: swap()
                    return result
                with patch.object(exports,name,changed), patch.object(publication._OwnedFile,'publish') as publish:
                    with self.assertRaisesRegex(ValueError,'ancestry'): self.export(target)
                    publish.assert_not_called()
                self.assertEqual(hits,[1]); self.assertEqual(list(folder.iterdir()),[]); self.assertEqual(list(moved.iterdir()),[])
                native_record('real-replacement',stage=stage,hits=len(hits),before=before,after=file_identity(folder),publications=0)

    def test_prepublication_gate_refuses_changed_identity_and_cleans_owned(self):
        with alias_fixture() as aliases:
            folder=aliases[1]/'gate'; folder.mkdir(); target=folder/'gate.shell.json'
            read=publication._OwnedFile.read; validate=exports.validate_destination; hits=[]; blocked=[]
            def inspected(item):
                result=read(item)
                with self.assertRaises(PermissionError): folder.rename(aliases[1]/'renamed')
                blocked.append(1); hits.append(1)
                return result
            def changed(*args,**kwargs):
                path,chain=validate(*args,**kwargs)
                return path,chain+(('simulated changed identity',0,0),) if hits else chain
            with patch.object(publication._OwnedFile,'read',inspected), patch.object(exports,'validate_destination',changed), patch.object(publication._OwnedFile,'publish') as publish:
                with self.assertRaisesRegex(ValueError,'ancestry'): self.export(target)
                publish.assert_not_called()
            self.assertEqual(hits,[1]); self.assertEqual(blocked,[1]); self.assertEqual(list(folder.iterdir()),[])
            folder.rename(aliases[1]/'renamed')
            native_record('prepublication-gate',identity_change='SIMULATED',real_rename_blocked=1,read_hits=1,publications=0,owned_cleanup=True)

    def test_held_ancestry_gate_and_all_handle_cleanup(self):
        for outcome in ('success','partial-open-failure','held-identity-mismatch','pre-yield-recheck','pre-publication-recheck'):
            with self.subTest(outcome=outcome), alias_fixture() as aliases:
                folder=aliases[1]/'held'; folder.mkdir(); target=folder/'x.shell.json'
                api=ctypes.WinDLL('kernel32',use_last_error=True)
                api.CreateFileW.argtypes=[wintypes.LPCWSTR,wintypes.DWORD,wintypes.DWORD,ctypes.c_void_p,wintypes.DWORD,wintypes.DWORD,wintypes.HANDLE]; api.CreateFileW.restype=wintypes.HANDLE
                api.CloseHandle.argtypes=[wintypes.HANDLE]; api.CloseHandle.restype=wintypes.BOOL
                api.GetFileInformationByHandle.argtypes=[wintypes.HANDLE,ctypes.POINTER(exports._FileInformation)]; api.GetFileInformationByHandle.restype=wintypes.BOOL
                api.GetHandleInformation.argtypes=[wintypes.HANDLE,ctypes.POINTER(wintypes.DWORD)]; api.GetHandleInformation.restype=wintypes.BOOL
                opened=[]; closed=[]; calls=[]; injected=[]
                def acquire(*args):
                    calls.append(1)
                    if outcome=='partial-open-failure' and len(calls)==2:
                        injected.append(1); ctypes.set_last_error(5); return ctypes.c_void_p(-1).value
                    h=api.CreateFileW(*args)
                    if h!=ctypes.c_void_p(-1).value: opened.append(h)
                    return h
                def close(h): closed.append(h); return api.CloseHandle(h)
                proxy=SimpleNamespace(CreateFileW=acquire,CloseHandle=close,GetFileInformationByHandle=api.GetFileInformationByHandle)
                real_identity=exports._held_identity; real_validate=exports.validate_destination; validations=[]
                def identity(*args):
                    result=real_identity(*args)
                    if outcome=='held-identity-mismatch' and not injected: injected.append(1); return result[0],result[1]+1
                    return result
                def validate(*args,**kwargs):
                    result=real_validate(*args,**kwargs); validations.append(1)
                    threshold=2 if outcome=='pre-yield-recheck' else 3
                    if outcome in ('pre-yield-recheck','pre-publication-recheck') and len(validations)==threshold:
                        injected.append(1); return result[0],result[1]+(('simulated identity change',0,0),)
                    return result
                with patch.object(exports.ctypes,'WinDLL',return_value=proxy), patch.object(exports,'_held_identity',identity), patch.object(exports,'validate_destination',validate):
                    def operation():
                        with exports.guarded_destination(target) as (_,recheck):
                            with self.assertRaises(PermissionError): folder.rename(aliases[1]/'renamed')
                            recheck()
                    if outcome=='success': operation()
                    else:
                        with self.assertRaises((OSError,ValueError)): operation()
                        self.assertEqual(injected,[1])
                self.assertTrue(opened); self.assertEqual(closed,list(reversed(opened)))
                for h in opened:
                    flags=wintypes.DWORD(); self.assertFalse(api.GetHandleInformation(h,ctypes.byref(flags))); self.assertEqual(ctypes.get_last_error(),6)
                folder.rename(aliases[1]/'renamed'); self.assertFalse(target.exists())
                native_record('held-ancestry',outcome=outcome,opened=len(opened),closed=len(closed),all_invalid_handle_6=True,injection_hits=len(injected),post_exit_rename=True,
                              simulated=outcome in ('held-identity-mismatch','pre-yield-recheck','pre-publication-recheck'))


def access_writer(config):
    """Explicit external token lane only; never called by unittest discovery."""
    import test_windows_export_access as access
    identity=access.token_identity(); elevated=identity['is_elevated']
    if not elevated: access.require_medium(identity)
    else: assert identity['integrity_sid']=='S-1-16-12288'
    ref=load_reference(); obs=evaluate(ref,Request()); figure=Figure(); figure.add_subplot().plot([0,1],[0,1]); rows=[]
    for destination in config['destinations']:
        folder=Path(destination)/('elevated' if elevated else 'normal'); folder.mkdir()
        with patch.object(os,'link',side_effect=AssertionError('hard links forbidden')):
            exports.export_json(ref,obs,{},folder/'observation.shell.json')
            for kind in ('png','svg'): exports.export_image(ref,obs,{},figure,folder/('view.'+kind))
        published=sorted(folder.iterdir()); assert len(published)==5
        for path in published:
            sibling=folder/('direct-'+path.name); sibling.write_bytes(path.read_bytes())
            assert access.security(path)==access.security(sibling)
        with tempfile.TemporaryDirectory(prefix='private-control-',dir=folder) as temporary:
            private=Path(temporary)/'payload.json'; private.write_bytes(b'{"negative":"private rename"}\n'); os.rename(private,folder/'negative-private-rename.json')
        assert not list(folder.glob('.trioctagon-*'))
        for path in sorted(folder.iterdir()):
            rows.append({'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'security':access.security(path),'links':path.stat().st_nlink,'negative':path.name.startswith('negative-'),'writer_elevated':elevated})
        assert all(r['links']==1 for r in rows)
    return {'status':'PASS','pid':os.getpid(),'token':identity,'files':rows,'formats':['shell.json','png','svg'],'direct_sibling_security_equal':True,'pair_atomic':False}
