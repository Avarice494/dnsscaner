# 作者：Sceva
# 日期：2021/8/13 23:22
# 工具：PyCharm
# Python版本：3.6.3
import dnsscaner
import local_ip
import struct
import socket
from typing import Tuple, Union
import logging
# wry = local_ip.QQwry()
# wry.load_file("qqwry.dat")
#
# logger = logging.getLogger(__name__)

# def lookup(ip_str: str) -> Union[Tuple[str, str], None]:
#     '''查找IP地址的归属地。
#        找到则返回一个含有两个字符串的元组，如：('国家', '省份')
#        没有找到结果，则返回一个None。'''
#
#
#     try:
#         return self.__fun(ip)
#     except:
#         if not self.is_loaded():
#             logger.error('Error: qqwry.dat not loaded yet.')
#         else:
#             raise
#

a = "北京"
a= a.encode(encoding="utf-8")
print (a)

ip = struct.unpack(">I", socket.inet_aton("192.168.1.1"))[0]
print(ip)
# info = wry.lookup("110.242.68.3")
# res = {"city": info[0], "isp": info[1]}
# print("     地理位置:" + str(res))