"""Shell-only export authority and destination guard, reusing repaired publisher."""
from contextlib import contextmanager
import ctypes
from ctypes import wintypes
import hashlib
import os
import re
from pathlib import Path, PureWindowsPath
import stat
import sys
from trioctagon_ui._export_publication import publication, text_writer
from trioctagon_ui.shell_reference import canonical, plain, implementation_identity
from trioctagon_ui.shell_observer import Observation

FAMILY='TRIOCTAGON_SPHERICAL_EDGE_OBSERVATION'


def artifact(reference, observation, view):
    if not isinstance(observation,Observation): raise TypeError('Completed immutable observation required')
    result={'family':FAMILY,'schema_version':'1.0.0','component':'SHELL_OBSERVER_V1','policy':'SHELL_NUMERIC_V1',
        'implementation':implementation_identity(),'source':plain(reference.manifest),
        'observation':plain(observation.data),'view':plain(view),
        'qualification':'Static numerical application observation; not a kernel record, execution attestation or physical boundary.'}
    result['content_sha256']=hashlib.sha256(canonical(result)).hexdigest()
    return result


def validate_destination(raw, protected_roots=()):
    text=os.fspath(raw); p=PureWindowsPath(text)
    if os.name!='nt': raise OSError('Shell exports require the supported Windows lane')
    if not p.is_absolute() or text.startswith(('\\\\','//')) or any(x in ('.','..') for x in re.split(r'[\\/]',text)) or '\x00' in text: raise ValueError('Choose an absolute local destination without traversal')
    reserved={'CON','PRN','AUX','NUL',*(f'COM{i}' for i in range(1,10)),*(f'LPT{i}' for i in range(1,10))}
    for component in p.parts[1:]:
        if component.endswith((' ','.')) or ':' in component or component.split('.')[0].upper() in reserved or any(c in component for c in '<>"|?*'): raise ValueError('Ambiguous Windows destination')
    dest=Path(text)
    if not dest.parent.is_dir(): raise ValueError('Choose an existing destination directory')
    ancestors=[dest.parent,*dest.parent.parents]
    for ancestor in ancestors:
        info=ancestor.lstat()
        if getattr(info,'st_file_attributes',0)&stat.FILE_ATTRIBUTE_REPARSE_POINT: raise ValueError('Reparse destinations are refused')
        if ancestor.name.lower() in ('papers','research','trioctagon_ui','.git') or (ancestor/'.git').exists(): raise ValueError('Source/research/package destinations are protected')
        if ancestor.name.lower()=='records' and (ancestor.parent/'sweep-manifest.json').exists(): raise ValueError('Authoritative dataset records are protected')
    resolved=dest.resolve()
    for root in (Path(__file__).resolve().parent,*map(Path,protected_roots)):
        if resolved.is_relative_to(root.resolve()): raise ValueError('Protected export destination')
    if dest.exists() or dest.is_symlink(): raise FileExistsError('Exports never overwrite existing files')
    return resolved,tuple((str(a),a.stat().st_dev,a.stat().st_ino) for a in ancestors)


@contextmanager
def guarded_destination(destination, sidecar=None, protected_roots=()):
    target,before=validate_destination(destination,protected_roots)
    if sidecar is not None: validate_destination(sidecar,protected_roots)
    # Hold ancestors against rename/deletion for the complete two-publication operation.
    api=ctypes.WinDLL('kernel32',use_last_error=True)
    api.CreateFileW.argtypes=[wintypes.LPCWSTR,wintypes.DWORD,wintypes.DWORD,ctypes.c_void_p,wintypes.DWORD,wintypes.DWORD,wintypes.HANDLE]
    api.CreateFileW.restype=wintypes.HANDLE
    api.CloseHandle.argtypes=[wintypes.HANDLE]; api.CloseHandle.restype=wintypes.BOOL
    handles=[]
    try:
        for name,_,_ in before:
            # Attribute-only access does not participate in Windows sharing
            # exclusion. Directory read access makes denial of DELETE effective.
            h=api.CreateFileW(name,0x80000000,3,None,3,0x02200000,None)
            if h==ctypes.c_void_p(-1).value: raise ctypes.WinError(ctypes.get_last_error())
            handles.append(h)
        def recheck():
            _,now=validate_destination(target,protected_roots)
            if now!=before: raise ValueError('Destination ancestry changed')
            if sidecar is not None: validate_destination(sidecar,protected_roots)
        recheck()
        yield target,recheck
    finally:
        for h in reversed(handles): api.CloseHandle(h)


def export_json(reference, observation, view, destination, *, protected_roots=()):
    if not str(destination).lower().endswith('.shell.json'): raise ValueError('Choose .shell.json')
    result=artifact(reference,observation,view); raw=canonical(result)+b'\n'
    with guarded_destination(destination,protected_roots=protected_roots) as (dest,recheck):
        with publication(dest) as (item,):
            item.stream.write(raw)
            if item.read()!=raw: raise OSError('Shell export byte readback mismatch')
            recheck(); item.publish()
    return {'artifact':str(dest),'content_sha256':result['content_sha256'],'sha256':hashlib.sha256(raw).hexdigest()}


def export_image(reference, observation, view, figure, destination, *, protected_roots=()):
    suffix=Path(destination).suffix.lower()
    if suffix not in ('.png','.svg'): raise ValueError('Choose PNG or SVG')
    observed=artifact(reference,observation,view)
    companion=Path(destination).with_suffix(suffix+'.provenance.json')
    with guarded_destination(destination,companion,protected_roots) as (dest,recheck):
        with publication(dest,companion) as (item,side):
            if suffix=='.svg':
                with text_writer(item.stream,newline=None) as f: figure.savefig(f,format='svg')
            else: figure.savefig(item.stream,format='png')
            image=item.read()
            metadata={'family':FAMILY+'_FIGURE','schema_version':'1.0.0','filename':dest.name,
                'image_sha256':hashlib.sha256(image).hexdigest(),'observation_digest':observed['content_sha256'],
                'cached_observation':observed,'rendered_state':plain(view),'pair_atomic':False,
                'qualification':'Numerical presentation; no exact symbolic geometry or physical boundary claim.',
                'rasterized_layers_detected':b'<image' in image if suffix=='.svg' else True}
            side.stream.write(canonical(metadata)+b'\n'); side.read()
            recheck(); item.publish(); side.publish()
    return {'artifact':str(dest),'sidecar':str(companion),'image_sha256':metadata['image_sha256'],'observation_digest':observed['content_sha256']}
