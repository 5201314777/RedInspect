import cv2
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage


class VideoWidget(QtWidgets.QWidget):
    selectionChanged = QtCore.pyqtSignal(int)  # 添加一个信号

    def __init__(self, parent=None):
        super(VideoWidget, self).__init__(parent)
        self.setStyleSheet("QWidget {background-color: white;}")
        self.widget = QtWidgets.QLabel(self)
        self.index = -1
        self.selected = False
        self.setContentsMargins(0,0,0,0)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.widget)
        self.setLayout(self.layout)
    def show_frame(self, image):
        """显示视频帧"""
        qImg = self.convert_cv_qt(image)
        self.widget.setPixmap(qImg)

    def convert_cv_qt(self, cv_img):
        """将OpenCV图像转换为Qt可以显示的格式"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.widget.width(), self.widget.height(), QtCore.Qt.KeepAspectRatio)
        return QtWidgets.QPixmap.fromImage(p)
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