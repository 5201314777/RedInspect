import ctypes
from ctypes import *

# 加载海康SDK的库文件
# 假设HCNetSDK.dll在项目的根目录下
lib_path = './HCNetSDK.dll'

hcnetsdk = ctypes.CDLL(lib_path)

# 调用SDK函数
# 假设SDK中定义为 BOOL NET_DVR_Init();
hcnetsdk.NET_DVR_Init.restype = c_bool  # 设置返回类型
success = hcnetsdk.NET_DVR_Init()
if success:
    print("SDK 初始化成功")
else:
    print("SDK 初始化失败")

# 其他函数调用和参数设置类似
hcnetsdk.NET_DVR_Cleanup()