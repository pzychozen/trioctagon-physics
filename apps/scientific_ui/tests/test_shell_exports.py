"""Shell-format destination, identity and owned-publication failures (Windows)."""
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from trioctagon_ui import shell_exports as exports, _export_publication as publication
from trioctagon_ui.shell_reference import load_reference, canonical
from trioctagon_ui.shell_observer import Request, evaluate
from matplotlib.figure import Figure


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
        def race(item): target.write_bytes(b'racer'); return real(item)
        with patch.object(publication._OwnedFile,'publish',race), self.assertRaises(OSError): self.export(target)
        self.assertEqual(target.read_bytes(),b'racer'); self.assertFalse(list(self.root.glob('.trioctagon-*')))

    def test_write_flush_publish_and_cleanup_faults(self):
        for method in ('read','flush','publish'):
            with self.subTest(method=method), patch.object(publication._OwnedFile,method,side_effect=OSError('injected '+method)), self.assertRaises(OSError): self.export(self.root/(method+'.shell.json'))
            self.assertFalse(list(self.root.iterdir()))
        fig=Figure()
        with patch.object(fig,'savefig',side_effect=OSError('injected image write')), self.assertRaises(OSError):
            exports.export_image(self.reference,self.observation,self.view,fig,self.root/'failed.png')
        self.assertFalse(list(self.root.iterdir()))
        real=publication._OwnedFile.publish
        def second(item):
            if item.destination.name.endswith('.provenance.json'): raise OSError('injected second publication')
            return real(item)
        with patch.object(publication._OwnedFile,'publish',second), self.assertRaises(OSError): exports.export_image(self.reference,self.observation,self.view,fig,self.root/'pair.png')
        self.assertFalse(list(self.root.iterdir()))
        # Cleanup failure is reported, never disguised as successful publication.
        real_discard=publication._OwnedFile.discard
        def noisy(item): real_discard(item); raise OSError('injected cleanup diagnostic after owned deletion')
        with patch.object(publication._OwnedFile,'publish',side_effect=OSError('primary')), patch.object(publication._OwnedFile,'discard',noisy), self.assertRaisesRegex(OSError,'cleanup incomplete'): self.export(self.root/'cleanup.shell.json')
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
        def race(item):
            if item.destination==side: side.write_bytes(b'independent sidecar')
            return real(item)
        with patch.object(publication._OwnedFile,'publish',race), self.assertRaises(OSError): exports.export_image(self.reference,self.observation,self.view,fig,primary)
        self.assertFalse(primary.exists()); self.assertEqual(side.read_bytes(),b'independent sidecar')
        self.assertFalse(list(self.root.glob('.trioctagon-*')))
        folder=self.root/'ancestor'; folder.mkdir()
        with exports.guarded_destination(folder/'p.shell.json'):
            with self.assertRaises(PermissionError): folder.rename(self.root/'changed')
        self.assertTrue(folder.is_dir())


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
