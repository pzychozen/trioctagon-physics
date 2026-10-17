import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from trioctagon_ui import shell_reference as r


class ReferenceTests(unittest.TestCase):
    def test_pins_and_event_mapping(self):
        ref=r.load_reference()
        self.assertEqual(ref.manifest['resource']['sha256'],r.RESOURCE_SHA)
        for i,k in enumerate(r.EVENTS): self.assertEqual(ref.data['events'][k],ref.data['geometry']['coincidence_events'][i])
        self.assertEqual(tuple(p['id'] for p in ref.data['presets']),r.PRESETS)

    def test_deep_immutable(self):
        ref=r.load_reference()
        with self.assertRaises(TypeError): ref.data['geometry']['vertices'][0]['id']=100
        with self.assertRaises(TypeError): r.Reference({}, {})

    def test_missing_corrupt_resource_and_manifest(self):
        package=r.resources.files('trioctagon_ui')
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            with patch.object(r.resources,'files',return_value=root):
                with self.assertRaises(r.ReferenceError): r.load_reference()
            for name in (r.RESOURCE,r.MANIFEST): (root/name).write_bytes(package.joinpath(name).read_bytes())
            for name in (r.RESOURCE,r.MANIFEST):
                old=(root/name).read_bytes(); (root/name).write_bytes(old+b' ')
                with patch.object(r.resources,'files',return_value=root):
                    with self.assertRaises(r.ReferenceError): r.load_reference()
                (root/name).write_bytes(old)

    def test_strict_json_and_structural_rejections(self):
        for raw in (b'{"a":1,"a":2}',b'{"a":NaN}',b'{"a":Infinity}'):
            with self.assertRaises(r.ReferenceError): r.strict_json(raw)
        ref=r.load_reference(); original=r.plain(ref.data); manifest=r.plain(ref.manifest)
        mutations=[lambda d:d['geometry']['vertices'][0].update(id=99),
            lambda d:d['geometry']['edges'][0].update(vertices=[1,0]),
            lambda d:d['events']['A']['groups'][0].update(branches=['E99+']),
            lambda d:d['hulls']['B']['faces'][0].update(vertices=[0,0,1]),
            lambda d:d['graphs']['A']['edges'][0].update(vertices=[0,999]),
            lambda d:d['presets'][0].update(id='invented')]
        for mutate in mutations:
            value=copy.deepcopy(original); mutate(value)
            with self.assertRaises(r.ReferenceError): r.validate(value,manifest)

    def test_eight_lineage_paths_and_no_executable_resource(self):
        ref=r.load_reference()
        self.assertEqual(len(ref.manifest['section_mappings']),8)
        for row in ref.manifest['section_mappings']:
            self.assertTrue(row['canonical_repository_path'].startswith('research/spherical_edge_extensions/'))
            self.assertEqual(len(row['sha256']),64)
        self.assertEqual(set(ref.data),{'geometry','presets','events','graphs','hulls','source_identities'})


if __name__=='__main__': unittest.main()
