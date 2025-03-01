from PyQt5.QtCore import QThread
from _ctypes import byref

from demo.HikSDK.HCNetSDK import *


class VideoThread(QThread):
    def __init__(self, device_controller, video_view):
        super().__init__()
        self.device_controller = device_controller
        self.video_view = video_view

    def run(self):
        # 获取播放库句柄
        if not self.device_controller.playctrldll.PlayM4_GetPort(byref(self.device_controller.PlayCtrl_Port)):
            print(u'获取播放库句柄失败')
            return

        # 登录设备
        lUserId, _ = self.device_controller.login_device("192.168.0.63", 8000, "admin", "abcd1234")

        # 设置回调函数并开启预览
        funcRealDataCallBack_V30 = REALDATACALLBACK(self.RealDataCallBack_V30)
        self.device_controller.open_preview(lUserId, funcRealDataCallBack_V30)

    def RealDataCallBack_V30(self, lPlayHandle, dwDataType, pBuffer, dwBufSize, pUser):
        # 码流回调函数
        if dwDataType == NET_DVR_SYSHEAD:
            self.device_controller.playctrldll.PlayM4_SetStreamOpenMode(self.device_controller.PlayCtrl_Port, 0)
            if self.device_controller.playctrldll.PlayM4_OpenStream(self.device_controller.PlayCtrl_Port, pBuffer,
                                                                    dwBufSize, 1024 * 1024):
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