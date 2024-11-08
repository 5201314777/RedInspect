import functools

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
from demo.utils.tool_bar import *
from demo.utils.QtTool import *
class VideoOperationBar(QtWidgets.QToolBar):
    def __init__(self, parent=None):
        super(VideoOperationBar, self).__init__(parent)
        self.setStyleSheet("QToolBar { background-color: white; }")
        self.setOrientation(Qt.Horizontal)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        action = functools.partial(newAction, self)
        # 创建一个QWidgetAction来包含窗口数选择的组合框
        selectWidNum = QtWidgets.QWidgetAction(self)
        widNumWidget = QWidget()  # 创建一个QWidget作为action的默认小部件
        selectWidNum.setDefaultWidget(widNumWidget)

        # 创建一个水平布局管理器
        widNumLayout = QtWidgets.QHBoxLayout(widNumWidget)

        # 创建标签并设置对齐方式
        selectWidNumLabel = QtWidgets.QLabel("窗口数:")
        selectWidNumLabel.setAlignment(Qt.AlignCenter)
        widNumLayout.addWidget(selectWidNumLabel)

        # 创建组合框并添加选项
        self.selectWidNumComboBox = QtWidgets.QComboBox()
        self.widNums = ['1', '4', '9', '16', '25', '36', '49', '64', '81']
        self.selectWidNumComboBox.addItems(self.widNums)
        self.selectWidNumComboBox.setCurrentIndex(0)
        #self.selectWidNumComboBox.currentIndexChanged.connect(self.updateVideoLayout)
        widNumLayout.addWidget(self.selectWidNumComboBox)

        startVideo = action(
            "播放",
            self.startVideo,
        )
        record = action(
            "录像",
            self.record
        )
        grabbing = action(
            "抓图",
            self.grabbing
        )
        inforce = action(
            "强制帧",
            self.inforce
        )
        self.actions = struct(
            startVideo=startVideo,
            record=record,
            grabbing=grabbing,
            inforce=inforce,
            selectWidNum=selectWidNum,
            videoOperationBar=(
                startVideo,
                record,
                grabbing,
                None,
                inforce,
                selectWidNum
            ),

        )
        addActions(self, self.actions.videoOperationBar)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)
    def startVideo(self):
        pass

    def record(self):
        pass

    def grabbing(self):
        pass

    def inforce(self):
        pass

    def WidNumChanged(self):
        pass



