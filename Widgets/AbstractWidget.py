from PySide6.QtWidgets import QWidget, QGridLayout


class AbstractWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.__name__ = kwargs.get('name', "AbstractWidget")

        t_layout = kwargs.get('layout', QGridLayout)

        self.layout = t_layout()

        self.setLayout(self.layout)
