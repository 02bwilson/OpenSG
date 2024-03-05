from PySide6.QtWidgets import QMainWindow

from Widgets.MainWidget import MainWidget


class MainWindow(QMainWindow):
    __version__ = "24.3.4"

    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"OpenSG v{self.__version__}")

        self.widget = MainWidget()

        self.menuBar().addAction(self.widget.chart_dock_widget.toggleViewAction())
        self.menuBar().addAction(self.widget.chart_dock_widget2.toggleViewAction())

        # self.setCentralWidget(self.widget)
