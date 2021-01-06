# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure


class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure(figsize=(9,4.5), dpi=None, facecolor='lightgrey', edgecolor=None, linewidth=1, frameon=None, subplotpars=None, tight_layout=None, constrained_layout=None))# =fig

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        #self.canvas.width = self.canvas.figure(figsize=(6,8))
        self.setLayout(vertical_layout)

