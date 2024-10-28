import functools

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from qtpy import QtWidgets
from demo.utils.tool_bar import ToolBar
from demo import utils
class VideoView(QtWidgets.QWidget):
    """
    视频视图类，用于显示视频内容。
    """
    def __init__(self, parent=None):
        super(VideoView, self).__init__(parent)
        # 视频
        self.video_widgets = []

        self.video_operation_bar = self.toolbar("视频操作")
        self.video_layout = QtWidgets.QVBoxLayout()  # 使用水平布局
        self.video_container = QWidget()
        #self.video_container.setFixedSize(512,384)
        self.video_container.setLayout(self.video_layout)

        action = functools.partial(utils.newAction, self)

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
        self.widNums = ['1' ,'4', '9', '16', '25', '36', '49', '64', '81']
        self.selectWidNumComboBox.addItems(self.widNums)
        self.selectWidNumComboBox.setCurrentIndex(0)
        self.selectWidNumComboBox.currentIndexChanged.connect(self.updateVideoLayout)
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
        self.actions = utils.struct(
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
        utils.addActions(self.video_operation_bar, self.actions.videoOperationBar)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.video_container)
        self.layout.addWidget(self.video_operation_bar)
        self.setLayout(self.layout)

        self.updateVideoLayout()
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

    def updateVideoLayout(self, index=0):
        num_windows = int(self.widNums[index])  # 获取用户选择的窗口数
        n = int(num_windows ** 0.5)  # 计算 n 的值，即行数和列数

        # 清除当前布局中的所有视频窗口小部件
        for widget in self.video_widgets:
            widget.deleteLater()
        self.video_widgets.clear()

        while self.video_layout.count():
            child = self.video_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for i in range(n):
            HLayout = QtWidgets.QHBoxLayout()
            HLayout.setContentsMargins(0,0,0,0)
            container =QWidget()
            container.setLayout(HLayout)
            for j in range(n):
                video_widget = QtWidgets.QWidget()
                video_widget.setStyleSheet("QWidget {background-color:white;}")
                HLayout.addWidget(video_widget)
                self.video_widgets.append(video_widget)
            self.video_layout.addWidget(container)

    def toolbar(self, title, actions=None,vertical=None):
        # 创建一个新的工具栏对象，title 参数是工具栏的标题。
        toolbar = ToolBar(title)
        toolbar.setStyleSheet("QToolBar { background-color: white; }")
        # 给工具栏设置一个对象名称，这通常用于在应用程序中唯一标识这个工具栏。
        toolbar.setObjectName("%sToolBar" % title)
        # 设置工具栏的方向为水平
        if vertical is not None:
            toolbar.setOrientation(Qt.Vertical)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # 如果提供了 actions 参数（一个动作列表），则将这些动作添加到工具栏中
        if actions:
            utils.addActions(toolbar, actions)
        return toolbar
