import socket
import queue
import threading
import time
open = []
tmp=[]

class PortScanner():
    #初始化数据
    def __init__(self,listOrstr):
        self.ip = queue.Queue()
        self.ip_port = queue.Queue()
        self.open=[]
        if isinstance(listOrstr,list):
            for i in range(list):
                self.ip.put(i)
        elif isinstance(listOrstr,str):
            self.ip.put(listOrstr)
        else:
            print("参数类型错误！")

    #将得到的数据ip或iplist将其与其端口加入队列
    def ip_port_queue(self):
        while True:
            if self.ip.empty() != True:
                tmp = self.ip.get()
                for i in range(0,65535):
                    ip_port = tmp+":"+str(i)
                    self.ip_port.put(ip_port)
                    print(ip_port)


    #遍历出每个ip的port
    def  ip_port_scaner(self):

        while True:
            tmp1 = self.ip_port.get()
            tmp = tmp1.split(":")
            ip = tmp[0]
            port = tmp[1]
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            try:
                sock.connect((ip,int(port)))
                print(f"{ip}:{port} open")
                self.open.append(tmp1)
            except Exception as err:
                pass
            finally:
                sock.close()

    #防止还没传入数据就已经将数据输出
    def over(self,m_count):
        tmp_count = 0
        i = 0
        count = m_count
        while True:
            time.sleep(4)
            ac_count = threading.activeCount()
            if ac_count < count  and ac_count == tmp_count:
                i+=1
            else:
                i=0
            tmp_count = ac_count
            if (self.ip_port.empty() and threading.activeCount() <= 1) or i > 5:
                break

    #实现通过读取列表的方式实现多ip运行
if __name__ == '__main__':
    MaxThread = 500
    PS =  PortScanner("192.168.231.16")
    Thread_ip_port = threading.Thread(target=PS.ip_port_queue)

    for i in range(0,MaxThread):
        threading.Thread(target=PS.ip_port_scaner).start()

    Thread_ip_port.start()

    PS.over(10)
