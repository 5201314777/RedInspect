from asyncio import sleep

from PyQt5.QtGui import QMouseEvent
from PyQt5 import QtWidgets

class VideoView(QtWidgets.QWidget):
    """
    视频视图类，用于显示视频内容。
    """

    def __init__(self, parent=None):
        super(VideoView, self).__init__(parent)
        # 视频
        self.video_widgets = []
        self.selected_widget = None
        self.currentVideoIndex = -1
        self.video_layout = QtWidgets.QVBoxLayout()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

    def addVideoWidget(self, video_widget):
        self.video_widgets.append(video_widget)
        video_widget.selectionChanged.connect(self.onSelectionChanged)  # 连接信号

    def onSelectionChanged(self,index):
        if index >=0 and index < len(self.video_widgets):
            if self.currentVideoIndex != -1:
                self.video_widgets[self.currentVideoIndex].selectCancle()
            self.selected_widget = self.video_widgets[index]
            self.currentVideoIndex = index
        print(self.currentVideoIndex)

