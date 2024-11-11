# from scapy.all import ARP, Ether, srp
#
# #在同一个局域网内搜索设备
# #写一个ARP脚本来执行代码
# def arp_scan(network, timeout=2):
#     # Create an ARP request packet
#     arp_request = ARP(pdst=network)
#     ether_request = Ether(dst="ff:ff:ff:ff:ff:ff")
#     packet = ether_request / arp_request
#
#     # Send the packet and receive the response
#     result = srp(packet, timeout=timeout, verbose=False)[0]
#
#     # Parse the responses
#     devices = []
#     for sent, received in result:
#         devices.append({'ip': received.psrc, 'mac': received.hwsrc})
#
#     return devices

######################################################################

import socket
import threading
from concurrent.futures import ThreadPoolExecutor

# 摄像头可能使用的端口列表
# 这里给出端口列表，需要从读取设备中获取，使用SDK函数来获取
# SDK中给定了一个范围，我们可以在范围内读取端口号：NET_DVR_LOCAL_TCP_PORT_BIND_CFG
CAMERA_PORTS = [80, 8080, 554, 10554]

# 扫描单个IP地址和端口的函数
def scan_ip_port(ip, port):
    try:
        # 创建一个socket对象
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置socket超时时间
        sock.settimeout(1)
        # 尝试连接指定的IP地址和端口
        result = sock.connect_ex((ip, port))
        # 如果连接成功（返回0），则打印该IP地址和端口
        if result == 0:
            print(f"IP: {ip}, Port: {port} - Open")
        # 关闭socket连接
        sock.close()
    except Exception as e:
        # 捕获异常并打印错误信息（可选）
        print(f"Error scanning {ip}:{port} - {e}")

# 扫描单个IP地址的所有端口
def scan_ip(ip):
    with ThreadPoolExecutor(max_workers=len(CAMERA_PORTS)) as executor:
        # 使用线程池并发扫描端口
        futures = [executor.submit(scan_ip_port, ip, port) for port in CAMERA_PORTS]
        # 等待所有线程完成（可选）
        for future in futures:
            future.result()

# 扫描整个局域网的函数
def scan_network(subnet):
    # 遍历子网内的所有IP地址
    for i in range(1, 255):  # 假设子网为192.168.1.x，
        ip = f"{subnet}.{i}"
        # 打印正在扫描的IP地址
        print(f"Scanning {ip}...")
        # 扫描该IP地址的所有端口
        scan_ip(ip)

# if __name__ == "__main__":
#     # 设置局域网子网
#     subnet = "192.168.1"
#     # 开始扫描网络
#     scan_network(subnet)


##########################################################################

# from hikvisionapi import  Client
#
# #设备的IP地址、用户名和密码
# ip = "192.168.1.100"
# username = "admin"
# passward = "123456"
#
# #创建客户端实例并连接到设备
# client = Client(ip,username,passward)
# client.connect()
#
# #获取设备信息
# params = client.get_camera_params()
#
# #打印分辨率和帧率作为示例
# resolution = params["Resolution"]
# framerate = params["Framerate"]
# print("分辨率",resolution)
# print("帧率",framerate)