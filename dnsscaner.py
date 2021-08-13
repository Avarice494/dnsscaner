# 作者：Sceva
# 日期：2021/8/7 1:17
# 工具：PyCharm
# Python版本：3.6.3
from dns import resolver
from qqwry import updateQQwry
from qqwry import QQwry
import sys
import getopt

# import os
# os.environ["http_proxy"] = "http://127.0.0.1:1080"
# os.environ["https_proxy"] = "http://127.0.0.1:1080"
#查询dns信息
class dnsinfo:
    #
    def A(self,dname):
        try:
            A= resolver.query(dname,'A')
            for i in A.response.answer:
                for j in i.items:
                    print("     A:"+str(j))
        except:
            print(dname+" NO A text!")


    def NS(self,dname):
        try:
            NS = resolver.query(dname,"NS")
            for i in NS.response.answer:
                print("       NS:"+str(i))
        except:
            print(dname + " NO NS text!")

    def MX(self,dname):
        try:
            MX =resolver.query(dname, 'MX')
            for i in MX:
                print('     MX preference =', i.preference, 'mail exchanger =', i.exchange)
        except:
            print(dname+" NO MX text")


    def TXT(self,dname):
        try:
            TXT = resolver.query(dname,"TXT")
            for i in TXT.response.answer:
                print("     TXT:"+str(i))
        except:
            print(dname + " NO TXT text")

    def Cname(self,dname):
        try:
            Cname = resolver.query(dname,'CNAME')
            for i in  Cname:
                print("     Cname:"+str(i))
        except:
            print(dname+" NO CNAME text")


    def SOA(self,dname):
        try:
            SOA = resolver.query(dname,"SOA")
            for i in SOA:
                print("     SOA:"+str(i))
        except:
            print(" NO SOA text")


    def SRV(self,dname):
        pass


    def PTR(self,dname):
        pass

#查询whois信息
class whoisinfo:
    def Update(self):
        ret = updateQQwry('qqwryupdate.dat')

    def Whois(self,dname):
        wry = QQwry()
        wry.load_file("qqwryupdate.dat")
        try:
            A = resolver.query(dname,'A')
            for i in A.response.answer:
                for j in i.items:
                    info = wry.lookup(str(j))
                    res = {"city": info[0], "isp": info[1]}
                    print("     WHOIS:"+str(res))
        except:
            print(dname+" NO A text!")

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