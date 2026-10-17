"""Pure static numerical observer. No model, clock, random or GUI dependency."""
from dataclasses import dataclass, replace
from decimal import (Decimal, Context, localcontext, ROUND_HALF_EVEN, InvalidOperation,
                     DivisionByZero, Overflow, Underflow, Clamped)
import math
import re
from trioctagon_ui.shell_reference import Reference, freeze, plain, PRESETS

POLICY = 'SHELL_NUMERIC_V1'
CONTEXT = Context(prec=80, rounding=ROUND_HALF_EVEN, Emin=-999, Emax=999, capitals=1, clamp=0,
                  flags=[], traps=[InvalidOperation, DivisionByZero, Overflow, Underflow, Clamped])
GRAMMAR = re.compile(r'[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE]([+-]?[0-9]{1,3}))?\Z')
MIN_POSITIVE = Decimal('1e-50')
MAX_INPUT = Decimal('1e12')
FRAMES = ('centered', 'paper_c_global')
UNITS = ('width', 'edge', 'chord', 'extension')


class NumericError(ValueError):
    def __init__(self, message, diagnostics=None):
        super().__init__(message)
        self.diagnostics = diagnostics or {}


@dataclass(frozen=True)
class Request:
    preset: str | None = 'A'
    mode: str = 'R'
    value: str = ''
    width: str = '1'
    unit: str = 'width'
    frame: str = 'centered'


@dataclass(frozen=True)
class Observation:
    origin: Request
    data: object


def parse(text, name):
    if not isinstance(text,str) or len(text)>128: raise NumericError(name+': at most 128 text characters')
    match=GRAMMAR.fullmatch(text)
    if not match or (match[1] is not None and abs(int(match[1]))>80): raise NumericError(name+': finite decimal, exponent -80..80 required')
    value=Decimal(text)
    if len(value.as_tuple().digits)>64: raise NumericError(name+': at most 64 significant digits')
    diagnostic={'raw':text,'parsed_decimal':str(value)}
    if value and abs(value)<MIN_POSITIVE: raise NumericError(name+': unsupported positive magnitude below 1e-50',diagnostic)
    if abs(value)>MAX_INPUT: raise NumericError(name+': magnitude exceeds 1e12',diagnostic)
    return value


def _as_float(value):
    result=float(value)
    if not math.isfinite(result) or (value!=0 and result==0): raise NumericError('Unsupported binary64 resolution',{'decimal':str(value)})
    return result


def evaluate(reference, request):
    if not isinstance(reference,Reference) or not isinstance(request,Request): raise TypeError('Immutable Reference and Request required')
    if request.mode not in ('R','C','ell') or request.unit not in UNITS or request.frame not in FRAMES: raise NumericError('Unknown input mode, frame or unit')
    if request.preset is not None and request.preset not in PRESETS: raise NumericError('Unknown preset')
    with localcontext(CONTEXT.copy()) as ctx:
        ctx.clear_flags()
        w=parse(request.width,'Width')
        if not Decimal('1e-12')<=w<=Decimal('1e12'): raise NumericError('Width must lie in [1e-12,1e12]')
        D=Decimal; h=(D(2).sqrt()-1)/2; a=D(1)/D(3).sqrt(); rho2=D(13)/12-D(2).sqrt()/2
        adjustments=[]; event=None; event_origin=None; entered=None; hex_input=None
        source=reference.data; preset=next((p for p in source['presets'] if p['id']==request.preset),None)
        if preset is not None:
            event=preset['exact_event']; event_origin='validated_exact_preset' if event else None
            if event=='original': t=h; ell=D(0)
            elif event=='A': t=D('0.5'); ell=t-h
            elif event=='B': ell=D(1); t=h+ell
            elif request.preset=='t_equals_w': t=D(1); ell=t-h
            else:
                R=D(str(preset['numeric']['R_over_w'])); t=(R*R-D(1)/3).sqrt(); ell=t-h
            R=(D(1)/3+t*t).sqrt(); C=2*t
        else:
            entered=parse(request.value,request.mode); hex_input=_as_float(entered).hex()
            if request.mode=='C' and entered==1: event='A'
            elif request.mode=='ell' and entered==0: event='original'
            elif request.mode=='ell' and entered==1: event='B'
            if event: event_origin='exact_decimal_length_identity'
            if request.mode in ('R','C'):
                pin=source['geometry']['rho'] if request.mode=='R' else source['presets'][0]['numeric']['C_over_w']
                numeric=_as_float(entered)
                if numeric<pin: raise NumericError('Below the admitted '+request.mode+' endpoint',{'raw':request.value,'parsed_decimal':str(entered),'binary64_hex':hex_input})
                if numeric==pin:
                    t=h; ell=D(0); R=rho2.sqrt(); C=2*h
                    adjustments.append({'kind':'lower_endpoint_representation','mode':request.mode,'raw':request.value,
                        'parsed_decimal':str(entered),'binary64_hex':hex_input,
                        'source_pointer':'/geometry/rho' if request.mode=='R' else '/presets/0/numeric/C_over_w',
                        'resolved_algebraic':'sqrt(13/12-sqrt(2)/2)' if request.mode=='R' else 'sqrt(2)-1',
                        'resolved_decimal':str(R if request.mode=='R' else C)})
                elif request.mode=='R':
                    R=entered; delta=R*R-rho2
                    if delta<=0: raise NumericError('Radius outside mathematical domain after decimal resolution')
                    t=(h*h+delta).sqrt(); ell=delta/(t+h); C=2*t
                else:
                    C=entered; t=C/2; ell=t-h
                    if ell<=0: raise NumericError('Chord outside mathematical domain after decimal resolution')
                    R=(D(1)/3+t*t).sqrt()
            else:
                if entered<0: raise NumericError('Extension cannot be negative')
                ell=entered; t=h+ell; C=2*t; R=(D(1)/3+t*t).sqrt()
                if ell>0 and t==h: raise NumericError('Positive extension lost at supported Decimal resolution',{'parsed_decimal':str(entered)})
        if ell<0: raise NumericError('Negative resolved extension')
        unit=request.unit
        if unit=='extension' and ell==0:
            if event=='original':
                unit='width'; adjustments.append({'kind':'zero_extension_unit_transition','from':'extension','to':'width','reason':'Exact Original has zero extension'})
            else: raise NumericError('Zero extension: select width, edge or chord units')
        U={'width':D(1),'edge':2*h,'chord':C,'extension':ell}[unit]
        lengths={'R_over_w':R,'t_over_w':t,'C_over_w':C,'ell_over_w':ell,'s_over_w':2*h}
        values={k:_as_float(v) for k,v in lengths.items()}
        shift=(D(0),D(3).sqrt()/6,D(0))
        def coordinates(point):
            p=tuple(D(str(x)) for x in point)
            glob=tuple(x+o for x,o in zip(p,shift)); selected=p if request.frame=='centered' else glob
            return {'centered_over_w':[_as_float(x) for x in p],'global_over_w':[_as_float(x) for x in glob],
                'centered_scaled':[_as_float(x*w) for x in p],'global_scaled':[_as_float(x*w) for x in glob],
                'display_xyz':[_as_float(x/U) for x in selected]}
        groups=source['events'][event]['groups'] if event else ()
        memberships={label:f'{event}:P{i+1:02}' for i,g in enumerate(groups) for label in g['branches']}
        branches=[]
        for edge in source['geometry']['edges']:
            for sign in (-1,1):
                label=edge['id']+('+' if sign==1 else '-')
                p=[D(str(m))+sign*t*D(str(u)) for m,u in zip(edge['midpoint'],edge['unit_direction'])]
                branches.append({'branch':label,'edge':edge['id'],'sign':sign,'class':edge['class'],
                    'original_endpoint':'V'+str(edge['vertices'][1 if sign==1 else 0]),
                    'outward_direction':[sign*x for x in edge['unit_direction']],
                    'dot_id':memberships.get(label,'branch:'+label),**coordinates(p)})
        dots=[{'dot_id':f'{event}:P{i+1:02}','branches':list(g['branches']),
               'coordinates_exact':list(g['coordinates_exact']),**coordinates(g['coordinates'])} for i,g in enumerate(groups)] if event else [
               {'dot_id':b['dot_id'],'branches':[b['branch']],**{k:b[k] for k in ('centered_over_w','global_over_w','centered_scaled','global_scaled','display_xyz')}} for b in branches]
        geometry=source['geometry']
        original=[{'id':'V'+str(v['id']),'coordinates_exact':list(v['centered_exact']),**coordinates(v['centered'])} for v in geometry['vertices']]
        graph=plain(source['graphs'][event]) if event else None; hull=plain(source['hulls'][event]) if event else None
        for obj in (graph,hull):
            if obj:
                for v in obj['vertices']: v.update(coordinates(v['xyz']))
        result={'policy':POLICY,'preset_id':request.preset,'input_mode':request.mode,'raw_value':request.value,
            'parsed_decimal':str(entered) if entered is not None else None,'input_binary64_hex':hex_input,
            'raw_width':request.width,'width_decimal':str(w),'width':_as_float(w),
            'resolved_decimal':{k:str(v) for k,v in lengths.items()},'resolved_binary64_hex':{k:v.hex() for k,v in values.items()},**values,
            'adjustments':adjustments,'event':event,'event_origin':event_origin,'certified_unique_count':18 if event else None,
            'marker_count':len(dots),'grouping':'accepted exact incidences' if event else 'independent branch identities; visual overlaps are not certified coincidences',
            'frame':request.frame,'requested_unit':request.unit,'unit':unit,'unit_over_w':_as_float(U),'unit_length':_as_float(w*U),
            'translation_over_w':[_as_float(x) for x in shift],'sphere_center':coordinates((0,0,0))['display_xyz'],
            'spheres':{'edge_tangent':_as_float(a/U),'vertex':_as_float(rho2.sqrt()/U),'observer':_as_float(R/U)},
            'original_vertices':original,'original_edges':plain(geometry['edges']),'panels':plain(geometry['faces']),
            'branches':branches,'dots':dots,'graph':graph,'hull':hull,
            'exact_source':plain(source['events'][event]) if event else None,
            'numeric_status':'finite numerical application evaluation; not whole-domain certification'}
        return Observation(request,freeze(result))


def present(reference, observation, *, width=None, unit=None, frame=None):
    """Retain originating request, including raw text and exact/generic authority."""
    origin=observation.origin
    return evaluate(reference,replace(origin,width=origin.width if width is None else width,
        unit=origin.unit if unit is None else unit,frame=origin.frame if frame is None else frame))
