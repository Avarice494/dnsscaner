# # 作者：Sceva
# # 日期：2021/8/7 15:25
# # 工具：PyCharm
# # Python版本：3.6.3
#
# from dns import resolver
# import dns
#
# # resolver = resolver.Resolver()
# # resolver.lifetime = 5
#
# #
# # domain = 'baidu.com'
# # TXT = resolver.query(domain,"TXT")
# # for i in TXT.response.answer:
# #     print(i)
# # # print(TXT)
# #
# #
# # A = resolver.query(domain, 'TXT')
# # for i in A.response.answer:
# #     # for j in i:
# #     #     print(j.address)
# #     print(i)
#
#
# #
# # TXT = resolver.query("163.com", 'TXT')
# # for i in TXT.response.answer:
# #     print( i)
# # dname = "163.com"
# # TXT = resolver.query(dname, "TXT")
# # for i in TXT.response.answer:
# #     print(dname + ":"+str(i) )
# #     print(i)
# # for i in Cname:
# #     print("163.com" + ":" + i)
#
#
#
# # import getopt, sys
# #
# # def main():
# #     try:
# #         opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
# #     except getopt.GetoptError as err:
# #         # print help information and exit:
# #         print(err)  # will print something like "option -a not recognized"
# #         usage()
# #         sys.exit(2)
# #     output = None
# #     verbose = False
# #     for o, a in opts:
# #         if o == "-v":
# #             verbose = True
# #         elif o in ("-h", "--help"):
# #             usage()
# #             sys.exit()
# #         elif o in ("-o", "--output"):
# #             output = a
# #         else:
# #             assert False, "unhandled option"
# #     # ...
# #
# # if __name__ == "__main__":
# #     main()
# #
# import requests
# #
# # proxy = {
# #     'http': '218.244.147.59:3128'
# # }
# #
# # response = requests.get("http://账号:密码@proxycn2.huawei.com:8080",proxies=proxy)
# # print(response.text)
# # import  requests
# #
# # reponse = requests.get("http://google.com")
# # print(reponse.text)
# #
# #
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
# # }
# # proxies = {'http': 'http://127.0.0.1:1080' , 'https': 'http://127.0.0.1:1080'}
# # url = 'https://www.google.com'
# # res = requests.get(url, proxies=proxies, verify=False)
# # print(res.text)
#
# # import sys
# # import getopt
# #
# # arg = sys.argv[1:]
# # try:
# #     opthons,s= getopt.getopt(arg,"at:")
# #     print (opthons)
# # except getopt.GetoptError as e :
# #     opthons, s = getopt.getopt(arg, "a:")
# #     print(opthons)
# # else:
# #     pass
# # for o,v in opthons:
# #     print(o)
# #     list = []
# #     if o in ("-t"):
# #         filename = v
# #
# #         with open(filename, "r", encoding="utf-8") as lines:
# #             line = str(lines.read())
# #             line = line.strip()
# #             list = line.split("\n")
# #         # print(list)
# #
# #     else:
# #         list=[v]
# #     print (list)
#
# #
# # a = [(1,2),(3,4),(5,6)]
# # a.pop(0)
# # print(a)
# import urllib3
# # from requests.packages.urllib3.contrib import pyopenssl as reqs
# #
# # ip='220.181.38.148'
# # port='443'
# # try:
# #     x509 = reqs.OpenSSL.crypto.load_certificate(
# #         reqs.OpenSSL.crypto.FILETYPE_PEM,
# #         reqs.ssl.get_server_certificate((ip, port))
# #     )
# #     domain = x509.get_subject().CN
# #     print(domain)
# # except:
# #     print(ip+'>Get CN failed')
# #
# # a = "123456789"
# #
# # print(a[-1][:-1])
#
# #!/usr/bin/python3
# #-*- coding:UTF-8 -*-
# import dns.resolver
# import os
# import httplib2
# iplist = []
# #appdomain = '.xn--zfr164b'
# appdomain = 'xn--zfr54hdx6e.xn--zfr164b'
# def get_iplist(domain = ''):
#   try:
#     A = dns.resolver.query(domain,'A')
#   except Exception as e:
#     print("dns resolver error %s" % str(e))
#     return
#   for i in A.response.answer:
#     for j in i.items:
#       iplist.append(j.address)
#   return True
#
# def checkip(ip):
#   #for ip in iplist:
#   checkurl =ip+":80"
#   getcontent = ""
#   httplib2.socket.setdefaulttimeout(5)
#   #conn = httplib2.HTTPConnection(checkurl) #httplib和httplib2的区别
#   conn = httplib2.Http()
#   try:
#     #conn.request("GET","/",header = {"Host":appdomain})
#     resp,getcontent = conn.request("http://"+checkurl)
#     #print("resp is %s" % resp)
#     #getcontent = resp.read(15)
#   finally:
#     #if getcontent == "<!doctype html>":#httplib2和httplib的区别
#     if resp['status'] == '200':
#       print("%s is OK!" % ip)
#     else:
#       print("%s is ERROR!" % ip)
# if __name__ == "__main__":
#   if get_iplist(appdomain) and len(iplist) >0 :
#     for ip in iplist:
#       checkip(ip)
#   else:
#     print("dns resolver error.")
# import xlwt
#
# def write_excel():
#     f = xlwt.Workbook() #创建工作簿
#
#     '''
#     创建第一个sheet:
#         sheet1
#     '''
#     sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
#     row0 = [u'业务',u'状态',u'北京',u'上海',u'广州',u'深圳',u'状态小计',u'合计']
#     column0 = [u'机票',u'船票',u'火车票',u'汽车票',u'其它']
#     status = [u'预订',u'出票',u'退票',u'业务小计']
#
#     #生成第一行
#     for i in range(0,len(row0)):
#         sheet1.write(0,i,row0[i])
#
#     #生成第一列和最后一列(合并4行)
#     i, j = 1, 0
#     while i < 4*len(column0) and j < len(column0):
#         sheet1.write_merge(i,i+3,0,0,column0[j]) #第一列
#         sheet1.write_merge(i,i+3,7,7) #最后一列"合计"
#         i += 4
#         j += 1
#
#     sheet1.write_merge(21,21,0,1,u'合计')
#
#     #生成第二列
#     i = 0
#     while i < 4*len(column0):
#         for j in range(0,len(status)):
#             sheet1.write(j+i+1,1,status[j])
#         i += 4
#
#     f.save('cases.xlsx') #保存文件
#
# if __name__ == '__main__':
#     #generate_workbook()
#     #read_excel()
#     write_excel()

# import xlrd
# import  openpyxl
# formdate=[]
# read = xlrd.open_workbook("cases.xlsx")
# table = read.sheets()[0]
# r = table.nrows
# c = table.ncols
# for i in range(r):
#     for j in range(c):
#         formdate.append(table.cell_value(i, j))
#
#
# print(formdate)
# import xlrd
# from xlutils.filter import process, XLRDReader, XLWTWriter
# def copy2(wb):
#     w = XLWTWriter()
#     process(XLRDReader(wb, 'unknown.xls'), w)
#     return w.output[0][1], w.style_list
#
# rb = xlrd.open_workbook('1.xls')
# wb, s = copy2(rb)
# wbs = wb.get_sheet(0)
# rbs = rb.get_sheet(0)
# styles = s[rbs.cell_xf_index(0, 0)]
# rb.release_resources()  #关闭模板文件
#
# wbs.write(0, 0, 'aa', styles)
# wb.save("2.xls")



#
# import xlrd
# def out_style(mode,value,outfile):
#     # value =[(1.0, '', '', '', ''), (2.0, 3.0, '', '', 5.0), ('', '', '', '', ''), ('', 4.0, '', 6.0, '') ,('', '', '', '', ''),( '', '', '', '', ''), ('', '', '', '', ''), (1.0, '', '', '', '')]
#     from xlutils.filter import process, XLRDReader, XLWTWriter
#
#     rb = xlrd.open_workbook(mode, formatting_info=True)
#
#     # 参考xlutils.copy库内的用法 参考xlutils.filter内的参数定义style_list
#
#     w = XLWTWriter()
#
#
#     process(XLRDReader(rb, 'unknown.xls'), w)
#
#     wb = w.output[0][1]
#
#     style_list = w.style_list
#
#     #n表id   sheet 表内容
#     for n, sheet in enumerate(rb.sheets()):
#         sheet2 = wb.get_sheet(n)
#         for r in range(sheet.nrows):
#
#             for c, cell in enumerate(sheet.row_values(r)):
#
#                 style = style_list[sheet.cell_xf_index(r, c)]
#
#                 sheet2.write(r, c, value[r][c], style)
#
#     wb.save(outfile)
#
#
# a= [1,2,3]
# b=[]
#
# b.append(a)
# print(b)

import socket
import dns.query
import dns.zone
import dns.resolver
from qqwry import QQwry
from ipwhois import IPWhois
import whois

# ip = socket.gethostbyname(domain);"给domain返回IP"
# domain = 'baidu.com'
# domain_prefix = 'www'
domain_prefix = ''
mx_a=[]
query_ip_add = QQwry()
query_ip_add.load_file('qqwry.dat')

# s=socks.socksocket()
# s.set_proxy(socks.SOCKS5,'127.0.0.1',1080)
# s.connect(("202.91.35.158",443))
# s.send(b"GET / HTTP/1.1...")
# print(s.recv(4006)) #读回复的包

def Get_ip_add(ip):
    try:
        country, region = query_ip_add.lookup(ip)
        return country, region
    except Exception:
        pass

def A(domain_prefix,domain):
    print('A:')
    try:
        A = dns.resolver.resolve(domain_prefix + domain,'A')
        ip = socket.gethostbyname(domain_prefix+domain)
        for i in A.response.answer:
            print (f'A text {i}')
        ip_add = Get_ip_add(ip)
        print(f'[+]{ip}:{domain_prefix}{domain}:{ip_add}')
    except Exception:
        pass
    print('--------------------------------------------')
def NS(domain_prefix,domain):
    domain_prefix=''
    print('NS:')
    try:
        NS=dns.resolver.resolve(domain,'NS')
        NS_info=[str(i).split('\n') for i in NS.response.answer] #将返回值用换行切为数组
        domainfo={} #设定一个字典用来存放最终的信息
        for i in NS_info[0]:
            domain=i.split()[-1][:-1] #？？？
            ipsinfo = socket.gethostbyname_ex(domain)[2] #解析获取域名的多个IP,获取数组格式
            ipsinfo = [f'{ip}:{Get_ip_add(ip)}' for ip in ipsinfo] #用ipsinfo中的ip来获取ip的地理位置并打印
            domainfo[domain]=ipsinfo #将全部信息存入字典中
        print(f"目标域名服务器共有{len(domainfo)}个域名{' | '.join(domainfo.keys())},每个域名信息如下")
        for key,values in domainfo.items(): #使用list的视图对象（只读），用keyalues键值对来遍历字典
            print(f'域名{key}有如下信息：')
            for v in values:
                print(v)
    except Exception:
        pass
    print('--------------------------------------------')
def MX(domain_prefix,domain):
    domain_prefix=''
    print('MX:')
    try:
        MX = dns.resolver.resolve(domain,'MX')
        MX_info = [str(i).split('\n') for i in MX.response.answer]  # 将返回值用换行切为数组
        domainfo = {}  # 设定一个字典用来存放最终的信息
        for i in MX_info[0]:
            domain = i.split()[-1][:-1]  # ？？？
            ipsinfo = socket.gethostbyname_ex(domain)[2]  # 解析获取域名的多个IP,获取数组格式
            ipsinfo = [f'{ip}:{Get_ip_add(ip)}' for ip in ipsinfo]  # 用ipsinfo中的ip来获取ip的地理位置并打印
            domainfo[domain] = ipsinfo  # 将全部信息存入字典中
        print(f"目标邮件服务器共有{len(domainfo)}个域名{' | '.join(domainfo.keys())},每个域名信息如下")
        for key, values in domainfo.items():  # 使用list的视图对象（只读），用keyalues键值对来遍历字典
            print(f'域名{key}有如下信息：')
            for v in values:
                print(v)
    except Exception:
        pass
    print('--------------------------------------------')

def TXT(domain_prefix,domain):
    domain_prefix=''
    txtinfo=[]
    print('TXT:')
    try:
        TXT = dns.resolver.resolve(domain_prefix + domain, 'TXT')
        TXT_info=[str(i).split('\n') for i in TXT.response.answer]
        for i in TXT_info[0]:
            TXTs = i.split(' "')[-1][:-1]
            txtinfo.append(TXTs)
        print(txtinfo)
    except Exception:
        pass
    print('--------------------------------------------')

def whoiS(domain_prefix,domain):
    domain_prefix=''
    ip = socket.gethostbyname(domain_prefix + domain)
    print('IPwhois:')
    obj = IPWhois(ip)
    try:
        print(obj.lookup_whois())
    except Exception:
        pass
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('whois:')
    obj = whois.whois(domain)
    try:
        print(obj)
    except Exception:
        pass
    print('--------------------------------------------')

def dns_query(path,*operation,domain_prefix=''):
    ip = ''
    with open(path,'r') as f:
        domain =f.readline()
        domain=domain.strip('\n')
        Oplist=[*operation]

        while domain != "":
            dnsdict = {
                'A':A,
                'NS':NS,
                'MX':MX,
                'TXT':TXT,
                'whois':whoiS
            }
            for i in Oplist:
                run = dnsdict.get(i,A)(domain_prefix,domain)
            domain = f.readline()
            domain = domain.strip("\n")
    f.close()

dns_query('./domain.txt','A','NS','MX','TXT','whois')

