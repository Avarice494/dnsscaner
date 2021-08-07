# 作者：Sceva
# 日期：2021/8/7 15:25
# 工具：PyCharm
# Python版本：3.6.3

from dns import resolver
import dns
domain = 'baidu.com'
TXT = resolver.query(domain,"A")
print(TXT)



