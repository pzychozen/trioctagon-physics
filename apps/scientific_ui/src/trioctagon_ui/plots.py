"""Plot stored sample columns. No kernel calls, scientific formulas or mutation."""
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel, QTabWidget


class StoredPlots(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAccessibleName("Stored-sample plots; exact table alternative below")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Channel/observer coordinates — not physical placement"))
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        self.figures = []
        self.canvases = []
        for name in ("Omega Re/Im", "Complex planes", "Raw chirality"):
            page = QWidget(); box = QVBoxLayout(page)
            figure = Figure(figsize=(7, 3), layout="constrained")
            canvas = FigureCanvasQTAgg(figure)
            canvas.setAccessibleName(name + " plot; values also available in sample table")
            box.addWidget(NavigationToolbar2QT(canvas, page)); box.addWidget(canvas)
            self.tabs.addTab(page, name)
            self.figures.append(figure); self.canvases.append(canvas)
        self.record = None
        self.markers = []

    def set_record(self, record):
        self.record = record
        self.markers = []
        series = record.series
        for figure in self.figures:
            figure.clear()
        axes = self.figures[0].subplots(2, 1, sharex=True)
        for i in range(min(3, int(record.data["state_size"]))):
            for j, part in enumerate(("re", "im")):
                axes[j].plot(series["indices"], series[f"omega{i}.{part}"], label=f"Omega{i}.{part}")
        for j, part in enumerate(("Re", "Im")):
            axes[j].set_ylabel(part); axes[j].legend(loc="best", fontsize="small")
            self.markers.append(axes[j].axvline(series["indices"][0], color="black", linestyle="--", linewidth=0.7))
        axes[-1].set_xlabel("update_index")
        planes = self.figures[1].subplots(1, 3)
        for i, ax in enumerate(planes):
            ax.plot(series[f"omega{i}.re"], series[f"omega{i}.im"])
            ax.set(xlabel="Re", ylabel="Im", title=f"Omega{i}")
        ax = self.figures[2].subplots()
        if "chirality0" in series:
            for i, label in enumerate(("Cx (BC)", "Cy (CA)", "Cz (AB)")):
                ax.plot(series["indices"], series[f"chirality{i}"], label=label)
            ax.legend(); ax.set(xlabel="update_index", ylabel="raw chirality")
            self.markers.append(ax.axvline(series["indices"][0], color="black", linestyle="--", linewidth=0.7))
        else:
            ax.text(0.5, 0.5, "Raw chirality: not recorded", ha="center", va="center", transform=ax.transAxes)
        for canvas in self.canvases:
            canvas.draw_idle()

    def select_sample(self, index):
        if self.record is None:
            return
        value = self.record.series["indices"][index]
        for marker in self.markers:
            marker.set_xdata([value, value])
        for canvas in self.canvases:
            canvas.draw_idle()
