from PySide6.QtWidgets import QLineEdit, QLabel

from Widgets.AbstractWidget import AbstractWidget


class ChartWidget(AbstractWidget):

    def __init__(self):
        super().__init__()

        self.symbol_line_edit = QLineEdit()

        self.layout.addWidget(self.symbol_line_edit, 0, 0)

        self.label = QLabel("test")
        self.layout.addWidget(self.label)
