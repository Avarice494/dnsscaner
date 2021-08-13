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
import xlwt

def write_excel():
    f = xlwt.Workbook() #创建工作簿

    '''
    创建第一个sheet:
        sheet1
    '''
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    row0 = [u'业务',u'状态',u'北京',u'上海',u'广州',u'深圳',u'状态小计',u'合计']
    column0 = [u'机票',u'船票',u'火车票',u'汽车票',u'其它']
    status = [u'预订',u'出票',u'退票',u'业务小计']

    #生成第一行
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i])

    #生成第一列和最后一列(合并4行)
    i, j = 1, 0
    while i < 4*len(column0) and j < len(column0):
        sheet1.write_merge(i,i+3,0,0,column0[j]) #第一列
        sheet1.write_merge(i,i+3,7,7) #最后一列"合计"
        i += 4
        j += 1

    sheet1.write_merge(21,21,0,1,u'合计')

    #生成第二列
    i = 0
    while i < 4*len(column0):
        for j in range(0,len(status)):
            sheet1.write(j+i+1,1,status[j])
        i += 4

    f.save('cases.xlsx') #保存文件

if __name__ == '__main__':
    #generate_workbook()
    #read_excel()
    write_excel()




