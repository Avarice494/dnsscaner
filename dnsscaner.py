# 作者：Sceva
# 日期：2021/8/7 1:17
# 工具：PyCharm
# Python版本：3.6.3
from dns import resolver
from qqwry import updateQQwry
from qqwry import QQwry
import qqwry
import sys
import getopt
#
# filename = "domain.txt"
# with open(filename,"r",encoding="utf-8") as lines:
#     line = lines.read()
#
#     print(line)
#
# def A(name):
#     A = resolver.query(name,"A")
class dnsinfo:

    def A(self,dname):
        A= resolver.query(dname,'A')
        for i in A.response.answer:
            dir(i)
            print(i)


    def NS(self,dname):
        NS = resolver.query(dname,"NS")
        for i in NS.response.answer:
            print(i)


    def MX(self,dname):
        MX =resolver.query(dname, 'MX')
        for i in MX:
            print('MX preference =', i.preference, 'mail exchanger =', i.exchange)

    def TXT(self,dname):
        TXT = resolver.query(dname,"TXT")
        for i in TXT.response.answer:
            print(i)


    def Cname(self,dname):
        Cname = resolver.query(dname,'CNAME')
        for i in  Cname:
            print(i)

    def SOA(self,dname):
        SOA = resolver.query(dname,"SOA")
        for i in SOA:
            # print(i.serial)
            print(i.rname)
            # print(i.refresh)
            # print(i.retry)
            # print(i.expire)
            # print(i.minimum)
    def SRV(self):
        pass
    def PTR(self):
        pass

class whoisinfo:
    def update(self):
        ret = updateQQwry('qqwryupdate.dat')

    def whois(self,dname):
        wry = QQwry()
        wry.load_file("qqwryupdate.dat")
        info = wry.lookup('127.0.0.1')
        res= {"city":info[0],"isp":info[1]}
        print (res)
if __name__ == '__main__':
    option_arg = sys.argv();
    option,s = getopt.getopt(option_arg,"a:mx:","help=")
    resolver = resolver.Resolver()
    # resolver.timeout = 5
    resolver.lifetime = 5
    #
    #
    a=dnsinfo()
    a.TXT("baidu.com")
    # # a.TXT("baidu.com")
    # a.NS("a.shifen.com")
    #
    # w= whoisinfo()
    # w.whois(1)
