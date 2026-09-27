"""Plot stored sample columns. No kernel calls, scientific formulas or mutation."""
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel, QTabWidget, QListWidget, QListWidgetItem


class ViewToolbar(NavigationToolbar2QT):
    """Presentation navigation only; provenance-aware export belongs to K4d."""
    toolitems = tuple(item for item in NavigationToolbar2QT.toolitems if item[0] != "Save")

    def save_figure(self, *args):
        return None  # Also disable Matplotlib's keyboard export shortcut.


def series_style(index):
    return {"linestyle": ("-", "--", "-.", ":")[index % 4], "marker": ("o", "s", "^", "x", "+", "d")[index % 6], "markersize": 3}


class StoredPlots(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAccessibleName("Stored-sample plots; exact table alternative below")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Channel/observer coordinates — not physical placement"))
        self.visibility_label = QLabel("No stored channels")
        layout.addWidget(self.visibility_label)
        self.channels = QListWidget(); self.channels.setMaximumHeight(90)
        self.channels.setAccessibleName("Stored channel visibility; hidden channels remain in the sample table")
        layout.addWidget(self.channels)
        self.channels.itemChanged.connect(lambda _: self._draw_record())
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        self.figures = []
        self.canvases = []
        for name in ("Omega Re/Im", "Complex planes", "Raw chirality"):
            page = QWidget(); box = QVBoxLayout(page)
            figure = Figure(figsize=(7, 3), layout="constrained")
            canvas = FigureCanvasQTAgg(figure)
            canvas.setAccessibleName(name + " plot; values also available in sample table")
            box.addWidget(ViewToolbar(canvas, page)); box.addWidget(canvas)
            self.tabs.addTab(page, name)
            self.figures.append(figure); self.canvases.append(canvas)
        self.record = None
        self.markers = []
        self.sample_index = 0

    def set_record(self, record):
        self.record = record
        self.sample_index = 0
        self.channels.blockSignals(True); self.channels.clear()
        for i in range(int(record.data["state_size"])):
            item = QListWidgetItem(f"Omega{i} Re/Im and complex plane")
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Checked if i < 3 else Qt.CheckState.Unchecked)
            self.channels.addItem(item)
        self.channels.blockSignals(False)
        self._draw_record()

    def _draw_record(self):
        record = self.record
        if record is None: return
        selected = [i for i in range(self.channels.count()) if self.channels.item(i).checkState() == Qt.CheckState.Checked]
        self.visibility_label.setText(f"Showing channels {', '.join(map(str, selected)) or 'none'} of {record.data['state_size']}; all components remain in the table.")
        self.markers = []
        series = record.series
        for figure in self.figures:
            figure.clear()
        axes = self.figures[0].subplots(2, 1, sharex=True)
        for i in selected:
            for j, part in enumerate(("re", "im")):
                axes[j].plot(series["indices"], series[f"omega{i}.{part}"], label=f"Omega{i}.{part}", **series_style(i))
        for j, part in enumerate(("Re", "Im")):
            axes[j].set_ylabel(part)
            if selected: axes[j].legend(loc="best", fontsize="small")
            self.markers.append(axes[j].axvline(series["indices"][0], color="black", linestyle="--", linewidth=0.7))
        axes[-1].set_xlabel("update_index")
        planes = self.figures[1].subplots(1, max(1, len(selected)), squeeze=False)[0]
        for i, ax in zip(selected, planes):
            ax.plot(series[f"omega{i}.re"], series[f"omega{i}.im"], **series_style(i))
            ax.set(xlabel="Re", ylabel="Im", title=f"Omega{i}")
        ax = self.figures[2].subplots()
        if "chirality0" in series:
            for i, label in enumerate(("Cx (BC)", "Cy (CA)", "Cz (AB)")):
                ax.plot(series["indices"], series[f"chirality{i}"], label=label, **series_style(i))
            ax.legend(); ax.set(xlabel="update_index", ylabel="raw chirality")
            self.markers.append(ax.axvline(series["indices"][0], color="black", linestyle="--", linewidth=0.7))
        else:
            message = "Raw chirality not recorded / not a supported ring run selection." if record.data["topology"] == "ring" else "Raw chirality: not recorded"
            ax.text(0.5, 0.5, message, ha="center", va="center", transform=ax.transAxes)
        for canvas in self.canvases:
            canvas.draw_idle()
        self.select_sample(self.sample_index)


    def select_sample(self, index):
        if self.record is None:
            return
        self.sample_index = index
        value = self.record.series["indices"][index]
        for marker in self.markers:
            marker.set_xdata([value, value])
        for canvas in self.canvases:
            canvas.draw_idle()


    def export_state(self):
        return {"sample_ordinal": self.sample_index, "visible_series": [f"Omega{i}" for i in range(self.channels.count()) if self.channels.item(i).checkState() == Qt.CheckState.Checked],
            "plot_tab": self.tabs.tabText(self.tabs.currentIndex())}


class ComparisonPlot(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        from PySide6.QtWidgets import QComboBox
        layout = QVBoxLayout(self)
        self.selector = QComboBox(); self.selector.setAccessibleName("Stored comparison scalar path; exact common update indices only")
        layout.addWidget(self.selector)
        self.figure = Figure(figsize=(6, 3), layout="constrained"); self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setAccessibleName("Comparison A and B; distinct line styles and markers; full comparison table alongside")
        layout.addWidget(ViewToolbar(self.canvas, self)); layout.addWidget(self.canvas)
        self.values = {}; self.selector.currentTextChanged.connect(self.redraw)

    def set_comparison(self, view):
        self.values = view.series(); self.selector.blockSignals(True); self.selector.clear(); self.selector.addItems(list(self.values)); self.selector.blockSignals(False)
        self.redraw()

    def redraw(self, *_):
        self.figure.clear(); ax = self.figure.subplots()
        values = self.values.get(self.selector.currentText(), [])
        if values:
            for side, label in ((1, "A"), (2, "B")):
                ax.plot([v[0] for v in values], [v[side] for v in values], label=label, **series_style(side - 1))
            ax.legend(); ax.set(xlabel="exact common stored update_index", ylabel=self.selector.currentText())
        else: ax.text(.5, .5, "No shared recorded numeric values selected", ha="center", transform=ax.transAxes)
        self.canvas.draw_idle()


class HistoryPlot(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Observer-vector coordinates — not physical placement. No interpolation; parent history stays unchanged."))
        self.figure = Figure(figsize=(6, 3), layout="constrained")
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setAccessibleName("Detached CPU history coordinates; complete coordinate table alongside")
        layout.addWidget(ViewToolbar(self.canvas, self)); layout.addWidget(self.canvas)
        self.analysis = None; self.marker = None

    def set_analysis(self, view):
        self.analysis = view; self.figure.clear(); self.marker = None
        coordinates = view.coordinates
        if coordinates and coordinates[0]:
            ax = self.figure.add_subplot(111, projection="3d")
            ax.plot(*coordinates, marker=".")
            self.marker, = ax.plot([coordinates[0][0]], [coordinates[1][0]], [coordinates[2][0]], marker="o", color="red")
            ax.set(xlabel="returned x", ylabel="returned y", zlabel="returned z", title=view.result["analysis_type"])
        self.canvas.draw_idle()

    def select_sample(self, ordinal):
        if self.analysis is None or self.marker is None: return
        values = self.analysis.coordinates
        if 0 <= ordinal < len(values[0]):
            self.marker.set_data_3d([values[0][ordinal]], [values[1][ordinal]], [values[2][ordinal]])
            self.canvas.draw_idle()
