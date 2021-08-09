# 作者：Sceva
# 日期：2021/8/7 1:17
# 工具：PyCharm
# Python版本：3.6.3
from dns import resolver
from qqwry import updateQQwry
from qqwry import QQwry
import sys
import getopt

class dnsinfo:
    #
    def A(self,dname):
        try:
            A= resolver.query(dname,'A')
            for i in A.response.answer:
                print(i)
        except:
            print(dname+" NO A text!")


    def NS(self,dname):
        try:
            NS = resolver.query(dname,"NS")
            for i in NS.response.answer:
                print(dname+":"+str(i))
        except:
            print(dname + " NO NS text!")

    def MX(self,dname):
        try:
            MX =resolver.query(dname, 'MX')
            for i in MX:
                print('MX preference =', i.preference, 'mail exchanger =', i.exchange)
        except:
            print(dname+" NO MX text")


    def TXT(self,dname):
        try:
            TXT = resolver.query(dname,"TXT")
            for i in TXT.response.answer:
                print(dname+":"+str(i))
        except:
            print(dname + " NO TXT text")

    def Cname(self,dname):
        try:
            Cname = resolver.query(dname,'CNAME')
            for i in  Cname:
                print(dname+":"+str(i))
        except:
            print(dname+" NO CNAME text")


    def SOA(self,dname):
        try:
            SOA = resolver.query(dname,"SOA")
            for i in SOA:
                print(" "+"SOA:"+str(i))
        except:
            print(" NO SOA text")


    def SRV(self,dname):
        pass


    def PTR(self,dname):
        pass

class whoisinfo:
    def update(self):
        ret = updateQQwry('qqwryupdate.dat')

    def whois(self,dname):
        wry = QQwry()
        wry.load_file("qqwryupdate.dat")
        try:
            A = resolver.query(dname,'A')
            for i in A.response.answer:
                for j in i.items:
                    info = wry.lookup(str(j))
                    res = {"city": info[0], "isp": info[1]}
                    print(res)
        except:
            print(dname+" NO A text!")




if __name__ == '__main__':
    dname =""
    resolver = resolver.Resolver()
    resolver.lifetime = 5

    # filename = "domain.txt"
    # with open(filename, "r", encoding="utf-8") as lines:
    #     dname = lines.read()


    option_arg = sys.argv[1:]

    try:
        option,s = getopt.getopt(option_arg,"A:M:N:T:C:S:a:m:n:t:c:s:W:w:t:T:",["ALL=","all=","UPDATE=","update="])
    except:
        print("请输入合法参数!!")

    print (option)
    cl = dnsinfo()
    wh = whoisinfo()
    for o,v in option:
        if o in ("-a","-A"):
            print(v)
            cl.A(v)
        elif o in ("-m","-M"):
            print(o)
            cl.M(v)
        elif o in ("-n","-N"):
            print(o)
            cl.NS(v)
        elif o in ("-t","-T"):
            print(o)
            cl.TXT(v)
        elif o in ("-c","-C"):
            print(o)
            cl.Cname(v)
        elif o in ("-s","-S"):
            print(o)
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
        elif o in ("-w","-W"):
            print(o)
            wh.whois(v)
        elif o in ("--update","--UPDATE"):
            print(o)
            wh.update()
        else:
            pass

