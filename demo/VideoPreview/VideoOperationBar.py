import functools
import sys
from ctypes import c_long

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
from _ctypes import byref

from demo.utils.tool_bar import *
from demo.utils.QtTool import *
from demo.VideoPreview.DeviceController import *
funcRealDataCallBack_V30 = None  # 实时预览回调函数，需要定义为全局的

PlayCtrl_Port = c_long(-1)  # 播放句柄
FuncDecCB = None   # 播放库解码回调函数，需要定义为全局的
class VideoOperationBar(QtWidgets.QToolBar):
    def __init__(self,Objdll,Playctrl,video_view):
        super(VideoOperationBar, self).__init__()
        self.setStyleSheet("QToolBar { background-color: white; }")
        self.setOrientation(Qt.Horizontal)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.device_controller = DeviceController(Objdll, Playctrl)
        self.video_view=video_view
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
        if not self.device_controller.playctrldll.PlayM4_GetPort(byref(self.device_controller.PlayCtrl_Port)):
            print(u'获取播放库句柄失败')
            return
        self.lUserId, _ = self.device_controller.login_device("192.168.0.63", 8000, "admin", "abcd1234")
        self.funcRealDataCallBack_V30 = REALDATACALLBACK(self.RealDataCallBack_V30)
        self.lRealPlayHandle = self.device_controller.open_preview(self.lUserId, self.funcRealDataCallBack_V30)

    def RealDataCallBack_V30(self, lPlayHandle, dwDataType, pBuffer, dwBufSize, pUser):
        # 码流回调函数
        #print("调用回调函数")
        if dwDataType == NET_DVR_SYSHEAD:
            self.device_controller.playctrldll.PlayM4_SetStreamOpenMode(self.device_controller.PlayCtrl_Port, 0)
            if self.device_controller.playctrldll.PlayM4_OpenStream(self.device_controller.PlayCtrl_Port, pBuffer,
                                                                    dwBufSize, 1024 * 1024):
                global FuncDecCB
                # FuncDecCB = DECCBFUNWIN(DecCBFun)
                self.device_controller.playctrldll.PlayM4_SetDecCallBackExMend(self.device_controller.PlayCtrl_Port,
                                                                               None, None, 0, None)
                if self.device_controller.playctrldll.PlayM4_Play(self.device_controller.PlayCtrl_Port,
                                                                  int(self.video_view.winId())):
                    print(u'播放库播放成功')
                else:
                    print(u'播放库播放失败')
            else:
                print(u'播放库打开流失败')
        elif dwDataType == NET_DVR_STREAMDATA:
            self.device_controller.playctrldll.PlayM4_InputData(self.device_controller.PlayCtrl_Port, pBuffer,
                                                                dwBufSize)
        else:
            print(u'其他数据,长度:', dwBufSize)

    def record(self):
        pass

    def grabbing(self):
        pass

    def inforce(self):
        pass

    def WidNumChanged(self):
        pass
