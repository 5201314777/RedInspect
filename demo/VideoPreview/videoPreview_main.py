import functools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from demo.VideoPreview.deviceTree import DeviceTree
from demo.VideoPreview.videoView import VideoView
from demo.VideoPreview.logger import Logger
from demo.VideoPreview.operation_bar import OperationBar
class VideoPreview(QtWidgets.QMainWindow):
    """
    主窗口类，用于显示视频预览和设备树。
    """

    def __init__(self):
        super(VideoPreview, self).__init__()

        self.initialize_UI()


    def initialize_UI(self):
        self.resize(1500, 1000)

        # 创建设备树
        self.device_tree = DeviceTree()
        #self.device_tree.add_device({'name': "打印机1"})
        self.device_tree.add_device("打印机1")

        # 创建视频视图
        self.video_view = VideoView()
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
        layout = QtWidgets.QVBoxLayout(container)  # 使用 container 的 layout

        layout.addWidget(self.video_view)
        layout.addWidget(self.logger)
        self.logger.setFixedHeight(150)
        return container

    def _create_operation_container(self):
        container = QtWidgets.QWidget()

        layout = QtWidgets.QVBoxLayout(container)
        container.setFixedWidth(280)
        container.setStyleSheet("QWidget { background-color: white; }")
        layout.addWidget(self.OperationBar)
        return container


