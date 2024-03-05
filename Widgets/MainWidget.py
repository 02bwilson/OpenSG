from PySide6.QtWidgets import QMenuBar
from PySide6QtAds import CDockManager, CDockWidget, TopDockWidgetArea

from Widgets.AbstractWidget import AbstractWidget
from Widgets.ChartWidget import ChartWidget


class MainWidget(AbstractWidget):

    def __init__(self, *args, **kwargs):
        super().__init__()

        # Setup dock
        self.dock_manager = CDockManager(self)

        self.chart_dock_widget = CDockWidget("1")
        self.cw = ChartWidget()
        self.chart_dock_widget.setWidget(self.cw)
        self.chart_dock_widget2 = CDockWidget("2")
        self.chart_dock_widget2.setWidget(self.cw)

        self.dock_manager.addDockWidget(TopDockWidgetArea, self.chart_dock_widget)
        self.dock_manager.addDockWidget(TopDockWidgetArea, self.chart_dock_widget2)
