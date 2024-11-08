from PyQt5 import QtWidgets, QtCore

class VideoWidget(QtWidgets.QWidget):
    selectionChanged = QtCore.pyqtSignal(int)  # 添加一个信号

    def __init__(self, parent=None):
        super(VideoWidget, self).__init__(parent)
        self.setStyleSheet("QWidget {background-color: white;}")
        self.widget = QtWidgets.QWidget()
        self.index = -1
        self.selected = False
        self.setContentsMargins(0,0,0,0)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.widget)
        self.setLayout(self.layout)
    def select(self):
        self.selected = True
        self.setStyleSheet("QWidget { background-color: lightgreen; }")
    def selectCancle(self):
        self.selected = False
        self.setStyleSheet("QWidget { background-color: white; }")
    def mousePressEvent(self, event):
        if not self.selected:
            self.selectionChanged.emit(self.index)  # 发射信号
            self.select()
        else:
            self.selectionChanged.emit(-1)  # 发射信号
            self.selectCancle()