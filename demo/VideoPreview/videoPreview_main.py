import functools
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from demo.HikSDK.HCNetSDK import netsdkdllpath
from demo.HikSDK.PlayCtrl import playM4dllpath
from demo.VideoPreview.VideoOperationBar import VideoOperationBar
from demo.VideoPreview.deviceTree import DeviceTree
from demo.VideoPreview.videoView import VideoView
from demo.VideoPreview.logger import Logger

from demo.VideoPreview.videoWidget import VideoWidget
from demo.VideoPreview.machineOperationBar import OperationBar


import ctypes


class VideoPreview(QtWidgets.QMainWindow):
    """
    主窗口类，用于显示视频预览和设备树。
    """

    def __init__(self):
        super(VideoPreview, self).__init__()

        self.initialize_UI()


    def initialize_UI(self):
        self.resize(1500, 1000)
        self.Objdll = ctypes.cdll.LoadLibrary(netsdkdllpath)
        self.Playctrldll = ctypes.cdll.LoadLibrary(playM4dllpath)
        self.Objdll.NET_DVR_Init()
        # 创建设备树
        self.device_tree = DeviceTree()
        #self.device_tree.add_device({'name': "打印机1"})
        self.device_tree.add_device("打印机1")

        # 创建视频视图
        self.video_view = VideoView()
        self.VideooperationBar = VideoOperationBar(self.Objdll,self.Playctrldll,self.video_view)
        # 创建日志记录器
        self.logger = Logger()
        self.OperationBar = OperationBar()

        # 创建主布局和容器
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addWidget(self._create_device_tree_container())
        self.main_layout.addWidget(self._create_center_container())
        self.main_layout.addWidget(self._create_operation_container())
        # 设置中心部件
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)



    def _create_device_tree_container(self):
        """
        创建并配置设备树的容器。
        """
        container = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(container)
        container.setFixedWidth(250)
        layout.addWidget(self.device_tree)
        return container

    def _create_center_container(self):
        """
        创建并配置中心容器，包含视频视图和日志记录器。
        """
        container = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.video_view)
        layout.addWidget(self.VideooperationBar)

        layout.addWidget(self.logger)
        self.VideooperationBar.selectWidNumComboBox.currentIndexChanged.connect(self.updateVideoLayout)
        self.updateVideoLayout()
        self.logger.setFixedHeight(150)
        return container

    def _create_operation_container(self):
        container = QtWidgets.QWidget()

        layout = QtWidgets.QVBoxLayout(container)
        container.setFixedWidth(280)
        container.setStyleSheet("QWidget { background-color: white; }")
        layout.addWidget(self.OperationBar)
        return container

    def updateVideoLayout(self, index=0):
        num_windows = int(self.VideooperationBar.widNums[index])  # 获取用户选择的窗口数
        n = int(num_windows ** 0.5)  # 计算 n 的值，即行数和列数

        # 清除当前布局中的所有视频窗口小部件
        for widget in self.video_view.video_widgets:
            widget.deleteLater()
        self.video_view.video_widgets.clear()

        while self.video_view.layout.count():
            child = self.video_view.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        for i in range(n):
            HLayout = QtWidgets.QHBoxLayout()
            HLayout.setContentsMargins(0, 0, 0, 0)
            container = QtWidgets.QWidget()
            container.setLayout(HLayout)
            for j in range(n):
                video_widget = VideoWidget()
                video_widget.index = i*n+j
                HLayout.addWidget(video_widget)
                self.video_view.addVideoWidget(video_widget)  # 连接信号
                if video_widget not in self.video_view.video_widgets:
                    self.video_view.video_widgets.append(video_widget)
            self.video_view.layout.addWidget(container)
        #print(self.video_view.video_widgets)
        self.video_view.adjustSize()