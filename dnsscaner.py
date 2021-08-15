# 作者：Sceva
# 日期：2021/8/7 1:17
# 工具：PyCharm
# Python版本：3.6.3
import json

from dns import resolver
from qqwry import updateQQwry
from qqwry import QQwry
import sys
import getopt
import whois
import socket
from ipwhois import IPWhois
# import os
# os.environ["http_proxy"] = "http://127.0.0.1:1080"
# os.environ["https_proxy"] = "http://127.0.0.1:1080"
#查询dns信息

ec = "\r\n"
class dnsinfo:
    #
    def A(self,dname):
        ipaddress=" "
        local =" "
        wry = QQwry()
        wry.load_file("qqwry.dat")
        try:
            A= resolver.query(dname,'A')
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
            NS = resolver.query(dname,"NS")
            for i in NS.response.answer:
                print("       NS:"+str(i))
                N += "NS:"+str(i)+ec
        except:
            print(dname + " NO NS text!")
        return N
    def MX(self,dname):
        M = " "
        try:
            MX =resolver.query(dname, 'MX')
            for i in MX:
                print('     MX preference =', i.preference, 'mail exchanger =', i.exchange)
                M += 'MX preference ='+i.preference+'mail exchanger ='+i.exchange+ec
        except:
            print(dname+" NO MX text")
        return M

    def TXT(self,dname):
        T = " "
        try:
            TXT = resolver.query(dname,"TXT")
            for i in TXT.response.answer:
                print("     TXT:"+str(i))
                T +="TXT:"+str(i)+ec
        except:
            print(dname + " NO TXT text")
        return T
    def Cname(self,dname):
        C =" "
        try:
            Cname = resolver.query(dname,'CNAME')
            for i in  Cname:
                print("     Cname:"+str(i))
                C += "Cname:"+str(i)+ec
        except:
            print(dname+" NO CNAME text")
        return C

    def SOA(self,dname):
        S = " "
        try:
            SOA = resolver.query(dname,"SOA")
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

class out():
    def str(self,o,v):
        # print(domain+":")
        # print(type)
        # try:
        #     eval("cl."+type[1:].upper()+"('"+domain+"')")
        # except:
        #     eval("cl."+type[2:].upper()+"('"+domain+"')")
        # except:
        #     eval("wh." + type[2:].upper() + "()")
        # except:
        #     eval("wh."+type[2:].upper()+"()")

        if o in ("-a","-A"):
            print(v)
            cl.A(v)
        elif o in ("-m","-M"):
            print(v)
            cl.M(v)
        elif o in ("-n","-N"):
            print(v)
            cl.NS(v)
        elif o in ("-c","-C"):
            print(v)
            cl.Cname(v)
        elif o in ("-s","-S"):
            print(v)
            cl.SOA(v)
        elif o in ("--all","--ALL"):
            print(v)
            cl.A(v)
            cl.Cname(v)
            cl.MX(v)
            print(v)
            cl.NS(v)
            print(v)
            cl.TXT(v)
            cl.SOA(v)
            print(v)
            wh.Whois(v)
        elif o in ("-w","-W"):
            print(v)
            wh.Whois(v)
        elif o in ("--update","--UPDATE"):
            print()
            wh.Update()
        else:
            pass

    def txt(self,o,v):
        pass
    def excel(self):
        pass

if __name__ == '__main__':
    dname =""
    resolver = resolver.Resolver()
    resolver.lifetime = 5


    #读取命令行的选项
    # sys.argv = [['1','1'],['--all', '163.com']]
    option_arg = sys.argv[1:]
    try:
        option, s = getopt.getopt(option_arg, "a:m:n:s:t:w:", ["ALL=", "all=", "UPDATE=", "update=","proxy="])
        print(option)
    except getopt.GetoptError as e:
        option,s = getopt.getopt(option_arg,"f:amnsw",["ALL","all","UPDATE","update","proxy="])
    except BaseException as e:
        print (e)
    #读取文件

    print (option)
    #实例化对象
    cl = dnsinfo()
    wh = whoisinfo()
    ou = out()


    #参数列表
    list = []
    for o, v in option:
        if o in ("-f"):
            filename = v
            with open(filename, "r", encoding="utf-8") as lines:
                line = str(lines.read())
                line = line.strip()
                list = line.split("\n")
                option.pop(0)
        else:
            list = [v]

    #结果输出
    for o, v in option:
        for i in list:
                 ou.str(o,i)