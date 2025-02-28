from demo.HikSDK.HCNetSDK import *
from demo.HikSDK.PlayCtrl import *
import ctypes
class DeviceController:
    def __init__(self, Objdll, Playctrl):
        self.Objdll = Objdll
        self.playctrldll = Playctrl
        print("load dll successfully")
        self.Objdll.NET_DVR_Init()
        print("init device successfully ")
        self.PlayCtrl_Port = c_long(-1)

    def login_device(self, ip, port, username, password):
        struLoginInfo = NET_DVR_USER_LOGIN_INFO()
        struLoginInfo.bUseAsynLogin = 0
        struLoginInfo.sDeviceAddress = bytes(ip, "ascii")
        struLoginInfo.wPort = port
        struLoginInfo.sUserName = bytes(username, "ascii")
        struLoginInfo.sPassword = bytes(password, "ascii")
        struLoginInfo.byLoginMode = 0
        struDeviceInfoV40 = NET_DVR_DEVICEINFO_V40()
        UserID = self.Objdll.NET_DVR_Login_V40(byref(struLoginInfo), byref(struDeviceInfoV40))
        return UserID, struDeviceInfoV40

    def open_preview(self, UserID, callbackFun):
        preview_info = NET_DVR_PREVIEWINFO()
        preview_info.hPlayWnd = 0
        preview_info.lChannel = 1
        preview_info.dwStreamType = 0
        preview_info.dwLinkMode = 0
        preview_info.bBlocked = 1
        preview_info.dwDisplayBufNum = 15
        lRealPlayHandle = self.Objdll.NET_DVR_RealPlay_V40(UserID, byref(preview_info), callbackFun, None)
        return lRealPlayHandle

    def cleanup(self):
        self.Objdll.NET_DVR_Cleanup()