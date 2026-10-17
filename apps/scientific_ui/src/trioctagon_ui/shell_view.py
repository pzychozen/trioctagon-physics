"""Native presentation of a completed shell observation; no scientific actions."""
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout
from trioctagon_ui.plots import ViewToolbar

LAYERS = {'panels':'Original panels', 'edges':'Original edges', 'framework':'Added lines / exact split framework',
          'tangent':'Edge-tangent sphere', 'vertex':'Original vertex sphere', 'observer':'Observer sphere',
          'dots':'Outer points', 'hull_edges':'Convex envelope edges', 'hull_faces':'Filled convex envelope (optional)'}
DEFAULT_LAYERS = {key:key not in ('hull_faces','hull_edges') for key in LAYERS}


class ShellView(QWidget):
    view_changed=Signal()

    def __init__(self,parent=None):
        super().__init__(parent)
        self.figure=Figure(figsize=(7,6),layout='constrained'); self.canvas=FigureCanvasQTAgg(self.figure)
        self.canvas.setAccessibleName('Spherical Edge Observer equal-scale 3D view; drag to rotate, toolbar to zoom')
        layout=QVBoxLayout(self); layout.setContentsMargins(0,0,0,0)
        self.toolbar=ViewToolbar(self.canvas,self); layout.addWidget(self.toolbar); layout.addWidget(self.canvas)
        self.ax=self.figure.add_subplot(projection='3d'); self.observation=None
        self.layers=DEFAULT_LAYERS.copy(); self.focus='observer'; self.selected_branch='E01-'
        # Canvas ownership survives Axes.clear(). One draw notification covers
        # native pan/zoom and toolbar Home/Back/Forward without resetting limits
        # or requesting another draw. The receiver only composes status text.
        self._draw_cid=self.canvas.mpl_connect('draw_event',self._view_drawn)
        registry=self.canvas.callbacks; cid=self._draw_cid
        self.destroyed.connect(lambda *unused:registry.disconnect(cid))

    def _view_drawn(self,event):
        if self._draw_cid is not None and self.observation is not None: self.view_changed.emit()

    def disconnect_view_callback(self):
        if self._draw_cid is not None:
            self.canvas.mpl_disconnect(self._draw_cid); self._draw_cid=None

    def closeEvent(self,event):
        self.disconnect_view_callback(); super().closeEvent(event)

    def set_observation(self,observation):
        old=self.observation; self.observation=observation
        if old:
            ratio=old.data['unit_over_w']/observation.data['unit_over_w']
            c0=old.data['sphere_center']; c1=observation.data['sphere_center']
            for i,(getter,setter) in enumerate(((self.ax.get_xlim,self.ax.set_xlim),(self.ax.get_ylim,self.ax.set_ylim),(self.ax.get_zlim,self.ax.set_zlim))):
                setter(tuple((v-c0[i])*ratio+c1[i] for v in getter()))
        self.redraw(reset=old is None)

    def redraw(self,reset=False):
        if self.observation is None: return
        d=self.observation.data; a=self.ax
        camera=(a.elev,a.azim,getattr(a,'roll',0),a.get_xlim(),a.get_ylim(),a.get_zlim())
        a.clear(); a.set_box_aspect((1,1,1))
        xyz=[v['display_xyz'] for v in d['original_vertices']]
        if self.layers['panels']:
            a.add_collection3d(Poly3DCollection([[xyz[i] for i in f] for f in d['panels']],facecolors='#98b4c7',alpha=.13,edgecolors='none'))
        if self.layers['edges']:
            a.add_collection3d(Line3DCollection([[xyz[i] for i in e['vertices']] for e in d['original_edges']],colors='#172d40',linewidths=1.7))
        if self.layers['framework']:
            if d['graph']:
                verts=d['graph']['vertices']
                segments=[[verts[i]['display_xyz'] for i in e['vertices']] for e in d['graph']['edges'] if e['segment_kind']=='added']
            else:
                segments=[[xyz[int(b['original_endpoint'][1:])],b['display_xyz']] for b in d['branches']]
            if segments: a.add_collection3d(Line3DCollection(segments,colors='#bc493a',linewidths=1.1))
        if d['hull']:
            hv=[v['display_xyz'] for v in d['hull']['vertices']]
            if self.layers['hull_faces']:
                a.add_collection3d(Poly3DCollection([[hv[i] for i in f['vertices']] for f in d['hull']['faces']],facecolors='#daaf47',alpha=.16,edgecolors='none'))
            if self.layers['hull_edges']:
                a.add_collection3d(Line3DCollection([[hv[i] for i in e['vertices']] for e in d['hull']['edges']],colors='#ac7f16',linewidths=1.3))
        centre=d['sphere_center']
        for layer,name,color in [('tangent','edge_tangent','#41856a'),('vertex','vertex','#7496bb'),('observer','observer','#b58cb1')]:
            if not self.layers[layer]: continue
            radius=d['spheres'][name]; curves=[]
            for lat in (-math.pi/3,-math.pi/6,0,math.pi/6,math.pi/3):
                curves.append([[centre[0]+radius*math.cos(lat)*math.cos(j*math.pi/24),centre[1]+radius*math.cos(lat)*math.sin(j*math.pi/24),centre[2]+radius*math.sin(lat)] for j in range(49)])
            for longitude in range(0,12,2):
                curves.append([[centre[0]+radius*math.sin(j*math.pi/24)*math.cos(longitude*math.pi/6),centre[1]+radius*math.sin(j*math.pi/24)*math.sin(longitude*math.pi/6),centre[2]+radius*math.cos(j*math.pi/24)] for j in range(49)])
            a.add_collection3d(Line3DCollection(curves,colors=color,linewidths=.45,alpha=.35))
        if self.layers['dots']:
            points=[x['display_xyz'] for x in d['dots']]
            a.scatter(*zip(*points),s=16,c='#34345e',depthshade=False)
        selected=next(b for b in d['branches'] if b['branch']==self.selected_branch)
        if self.layers['dots']:
            dot=next(q for q in d['dots'] if self.selected_branch in q['branches'])
            a.scatter(*[[x] for x in dot['display_xyz']],s=42,c='#d5711e',depthshade=False)
            a.text(*dot['display_xyz'],self.selected_branch,fontsize=8)
        a.set(xlabel='x / '+d['unit'],ylabel='y / '+d['unit'],zlabel='z / '+d['unit'])
        if reset: self.reset_limits()
        else:
            a.view_init(camera[0],camera[1],camera[2]); a.set(xlim=camera[3],ylim=camera[4],zlim=camera[5])
        a.set_title((d['event'] or 'Generic numeric input')+' · '+d['frame']+'\nStatic observation — no physical boundary',fontsize=10)
        self.canvas.draw_idle()

    def reset_limits(self):
        d=self.observation.data
        radius=d['spheres']['vertex' if self.focus=='original' else 'observer']*1.12
        center=d['sphere_center']
        self.ax.set(xlim=(center[0]-radius,center[0]+radius),ylim=(center[1]-radius,center[1]+radius),zlim=(center[2]-radius,center[2]+radius))
        self.ax.set_box_aspect((1,1,1))

    def camera(self,name):
        if name=='original focus': self.focus='original'; self.reset_limits()
        elif name=='reset': self.focus='observer'; self.reset_limits(); self.ax.view_init(25,-55,0)
        else:
            elev,azim={'oblique':(25,-55),'axial':(90,-90),'side':(0,-90)}[name]
            self.ax.view_init(elev,azim,0)
        self.canvas.draw_idle()

    def state(self):
        d=self.observation.data
        limits=[list(self.ax.get_xlim()),list(self.ax.get_ylim()),list(self.ax.get_zlim())]
        clipping=any(any(x<limits[i][0] or x>limits[i][1] for i,x in enumerate(q['display_xyz'])) for q in d['dots'])
        effective=self.layers.copy()
        if not d['event']: effective['hull_edges']=effective['hull_faces']=False
        return {'camera':{'elevation':self.ax.elev,'azimuth':self.ax.azim,'roll':getattr(self.ax,'roll',0),'limits':limits},
            'layers':effective,'layer_preferences':self.layers.copy(),'selected_branch':self.selected_branch,
            'focus':self.focus,'outer_points_clipped':clipping,'frame':d['frame'],'unit':d['unit'],
            'framework_mode':'accepted split framework' if d['event'] else 'unsplit added line portions',
            'geometry_claim':'numerical presentation, no exact symbolic SVG claim'}
