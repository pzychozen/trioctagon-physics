"""Display adaptation of returned Exact Codec 1 nodes and returned incidence."""
import math
from fractions import Fraction
from collections.abc import Mapping
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from trioctagon_ui.plots import ViewToolbar
from matplotlib.figure import Figure
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QPushButton, QLabel, QCheckBox


def exact_float(node, depth=0):
    if depth > 100 or not isinstance(node, Mapping) or len(node) != 1:
        raise ValueError("Exact display expression exceeds the UI depth guard or is malformed")
    kind, value = next(iter(node.items()))
    recurse = lambda item: exact_float(item, depth + 1)
    if kind == "integer":
        result = float(int(value))
    elif kind == "rational":
        result = float(Fraction(int(value["numerator"]), int(value["denominator"])))
    elif kind == "pi":
        result = math.pi
    elif kind == "add":
        result = math.fsum(recurse(v) for v in value)
    elif kind == "mul":
        result = math.prod(recurse(v) for v in value)
    elif kind == "pow":
        result = recurse(value["base"]) ** recurse(value["exponent"])
    elif kind in ("sin", "cos"):
        result = (math.sin if kind == "sin" else math.cos)(recurse(value))
    else:
        raise ValueError("Unknown exact expression node in display adapter")
    if not isinstance(result, (int, float)) or not math.isfinite(result):
        raise ValueError("Exact value cannot be shown at binary64 display precision; use the exact inspector")
    return result


def geometry_lines(record):
    """Return object/frame-labelled polylines, using only returned order/edges."""
    point = lambda value: tuple(exact_float(v) for v in value)
    result = []
    for obj in record.data["objects"]:
        data = obj["data"]; lines = []
        if obj["kind"] == "oriented_mesh":
            vertices = [point(v) for v in data["vertices"]]
            lines = [(vertices[int(a)], vertices[int(b)]) for a, b in data["edges"]]
        elif obj["kind"] == "section_curve":
            lines = [tuple(point(p) for p in segment) for segment in data["segments"]]
        elif "outline" in data:
            lines = [tuple(point(p) for p in segment) for segment in data["outline"]]
        elif "vertices" in data:
            vertices = [point(v) for v in data["vertices"]]
            lines = [tuple(vertices + vertices[:1])]
        result.append((obj["object_id"], obj["frame_id"], tuple(lines)))
    return tuple(result)


class GeometryView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Independent geometry — no dynamic attachment"))
        layout.addWidget(QLabel("Derived binary64 wireframe; exact values remain in the inspector. Separate coordinate frames have separate axes."))
        row = QHBoxLayout(); layout.addLayout(row)
        self.objects = QListWidget(); self.objects.setMaximumWidth(210)
        self.objects.setAccessibleName("Geometry object visibility; Space toggles the selected object")
        row.addWidget(self.objects)
        self.figure = Figure(figsize=(8, 4), layout="constrained")
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setAccessibleName("CPU geometry wireframe; exact object table alternative below")
        right = QVBoxLayout(); row.addLayout(right)
        right.addWidget(ViewToolbar(self.canvas, self)); right.addWidget(self.canvas)
        self.show_axes = QCheckBox("Show geometry axes"); self.show_axes.setChecked(True)
        self.show_axes.setAccessibleName("Geometry axes visibility; presentation only")
        right.addWidget(self.show_axes); self.show_axes.toggled.connect(lambda _: self.redraw())
        self.reset = QPushButton("Reset camera"); self.reset.setAccessibleName("Reset geometry camera")
        right.addWidget(self.reset)
        self.reset.clicked.connect(lambda: self.redraw(reset=True))
        self.objects.itemChanged.connect(lambda _: self.redraw())
        self.lines = (); self.axes = {}

    def set_record(self, record):
        self.lines = geometry_lines(record)
        self.objects.blockSignals(True); self.objects.clear()
        for oid, frame, lines in self.lines:
            item = QListWidgetItem(f"{oid} [{frame}]")
            item.setData(Qt.ItemDataRole.UserRole, oid)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Checked)
            self.objects.addItem(item)
        self.objects.blockSignals(False)
        self.redraw(reset=True)

    def redraw(self, reset=False):
        cameras = {} if reset else {k: (a.elev, a.azim, a.get_xlim(), a.get_ylim(), a.get_zlim()) for k, a in self.axes.items()}
        self.figure.clear(); self.axes = {}
        frames = list(dict.fromkeys(frame for _, frame, _ in self.lines))
        visible = {self.objects.item(i).data(Qt.ItemDataRole.UserRole) for i in range(self.objects.count()) if self.objects.item(i).checkState() == Qt.CheckState.Checked}
        for j, frame in enumerate(frames):
            ax = self.figure.add_subplot(1, len(frames), j + 1, projection="3d")
            self.axes[frame] = ax
            for oid, object_frame, lines in self.lines:
                if oid not in visible or object_frame != frame:
                    continue
                for line in lines:
                    xyz = [tuple(p) if len(p) == 3 else (*p, 0.0) for p in line]
                    ax.plot(*zip(*xyz), linewidth=0.9)
            ax.set(title=frame, xlabel="x", ylabel="y", zlabel="z")
            if not self.show_axes.isChecked(): ax.set_axis_off()
            if frame in cameras:
                elev, azim, xlim, ylim, zlim = cameras[frame]
                ax.view_init(elev=elev, azim=azim); ax.set(xlim=xlim, ylim=ylim, zlim=zlim)
            else:
                ax.view_init(elev=25, azim=-55)
        self.canvas.draw_idle()
