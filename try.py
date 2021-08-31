from qqwry import  QQwry
from dns import resolver
def A(self, dname):
    ipaddress = " "
    local = " "
    ec = "\r\n"
    wry = QQwry()
    wry.load_file("qqwry.dat")
    try:
        A = resolver.resolve(dname, 'A')
        for i in A.response.answer:
            for j in i.items:
                print("     A:" + str(j))
                ipaddress += str(j) + ec
                print(ipaddress)
                info = wry.lookup(str(j))
                res = {"city": info[0], "isp": info[1]}
                print("     地理位置:" + str(res))
                local += str(res) + ec
    except:
        print(dname + " NO A text!")
    return ipaddress, local
A("self","163.com")