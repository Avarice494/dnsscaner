# 作者：Sceva
# 日期：2021/8/7 1:17
# 工具：PyCharm
# Python版本：3.6.3
from dns import resolver
a = resolver.query("www.baidu.com","A")
print(a)
print(1)
