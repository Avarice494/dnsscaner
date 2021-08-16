import socket
import asyncio
import queue
import threading

open = []
tmp=[]
#遍历出每个ip的port
def  ip_port(ip,port):
    global open,tmp
    # for i in range(79,82):
    socket.setdefaulttimeout(5)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # print("ip_port:\r\n")
    try:
        sock.connect((ip,int(port)))
        print(f"{ip}:{port} open")
        tmp.append(port)
    except Exception as err:
        # print(f"{ip}:{port} close")
        # print(err)
        pass
    finally:
        sock.close()
# a = ip_port("123.58.180.8")
# print(a)
"""

import asyncio

async def count():
    for i in range(1,4000000):
        print(i)
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

asyncio.run(main())
"""
#防止还没传入数据就已经将数据输出
async def begin_port(ip):
    global open,tmp
    for i in range(1,65536):
        threading.Thread(target=ip_port, args=(ip, i)).start()

        # th =  threading.Thread(target=ip_port,args=(ip,i))
        # th.start()
        # th.join()
    await asyncio.sleep(1)
    open.append(tmp)
    tmp=[]
    return open
# begin_port("123.58.180.8")


async def asy(ip):
    a = await asyncio.gather(begin_port(ip))
    print(a)


#实现通过读取列表的方式实现多ip运行

def main(ip_list):
    global tmp
    for i  in ip_list:
        tmp.append(i)
        threading.Thread(asyncio.run(asy(i))).start()
        # asyncio.run(asy("123.58.180.8"))

list = ["192.168.231.16"]


main(list)



