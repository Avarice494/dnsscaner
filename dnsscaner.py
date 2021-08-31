# 作者：Sceva
# 日期：2021/8/7 1:17
# 工具：PyCharm
# Python版本：3.6.3
import json

from dns import resolver
from qqwry import updateQQwry
from qqwry import QQwry
import whois
import socket
from ipwhois import IPWhois
# import os
# os.environ["http_proxy"] = "http://127.0.0.1:1080"
# os.environ["https_proxy"] = "http://127.0.0.1:1080"
#查询dns信息

ec = "\r\n"
class dnsinfo:
    def A(self,dname):
        ipaddress=" "
        local =" "
        wry = QQwry()
        wry.load_file("qqwry.dat")
        try:
            A = resolver.resolve(dname, 'A')
            for i in A.response.answer:
                for j in i.items:
                    print("     A:"+str(j))
                    ipaddress += str(j)+ec
                    print(ipaddress)
                    info = wry.lookup(str(j))
                    res = {"city": info[0], "isp": info[1]}
                    print("     地理位置:"+str(res))
                    local += str(res)+ec
        except:
            print(dname+" NO A text!")
        return ipaddress,local

    def NS(self,dname):
        N = " "
        try:
            NS = resolver.resolve(dname,"NS")
            for i in NS.response.answer:
                print("       NS:"+str(i))
                N += "NS:"+str(i)+ec
        except:
            print(dname + " NO NS text!")
        return N
    def MX(self,dname):
        M = " "
        try:
            MX =resolver.resolve(dname, 'MX')
            for i in MX:
                print('     MX preference =', i.preference, 'mail exchanger =', i.exchange)
                M += 'MX preference ='+i.preference+'mail exchanger ='+i.exchange+ec
        except:
            print(dname+" NO MX text")
        return M

    def TXT(self,dname):
        T = " "
        try:
            TXT = resolver.resolve(dname,"TXT")
            for i in TXT.response.answer:
                print("     TXT:"+str(i))
                T +="TXT:"+str(i)+ec
        except:
            print(dname + " NO TXT text")
        return T
    def Cname(self,dname):
        C =" "
        try:
            Cname =resolver.resolve(dname,'CNAME')
            for i in  Cname:
                print("     Cname:"+str(i))
                C += "Cname:"+str(i)+ec
        except:
            print(dname+" NO CNAME text")
        return C

    def SOA(self,dname):
        S = " "
        try:
            SOA = resolver.resolve(dname,"SOA")
            for i in SOA:
                print("     SOA:"+str(i))
                S += "SOA:"+str(i)+ec
        except:
            print(" NO SOA text")
        return S

    def SRV(self,dname):
        pass


    def PTR(self,dname):
        pass

#查询whois信息
class whoisinfo:
    def Update(self):
        ret = updateQQwry('qqwry.dat')

    def Whois(self,dname):
        # print('whois:')
        w=" "
        obj = whois.whois(dname)

        try:
            # print(obj)
            for i in obj:
                print(i + ":" + str(obj[i]))
                w +=i + ":" + str(obj[i])
            pass
        except Exception:
            pass
        # print('--------------------------------------------')
        return w
    def Ipwhoid(self,dname):
        domain_prefix = ''
        ip = socket.gethostbyname(domain_prefix + dname)
        print('IPwhois:')
        obj = IPWhois(ip)
        try:
            print(obj.lookup_whois())
        except Exception:
            pass
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')



if __name__ == '__main__':
    dname ="163.com"
    resolver = resolver.Resolver()
    resolver.lifetime = 5

    dns = dnsinfo()
    who = whoisinfo()

    dns.NS(dname)
    dns.A(dname)
    dns.SOA(dname)
    dns.Cname(dname)
    dns.MX(dname)
    dns.TXT(dname)
    dns.PTR(dname)

    who.Whois(dname)
    who.Ipwhoid(dname)
