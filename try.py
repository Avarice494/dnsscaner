# 作者：Sceva
# 日期：2021/8/7 15:25
# 工具：PyCharm
# Python版本：3.6.3

from dns import resolver
import dns

# resolver = resolver.Resolver()
# resolver.lifetime = 5

#
# domain = 'baidu.com'
# TXT = resolver.query(domain,"TXT")
# for i in TXT.response.answer:
#     print(i)
# # print(TXT)
#
#
# A = resolver.query(domain, 'TXT')
# for i in A.response.answer:
#     # for j in i:
#     #     print(j.address)
#     print(i)


#
# TXT = resolver.query("163.com", 'TXT')
# for i in TXT.response.answer:
#     print( i)
# dname = "163.com"
# TXT = resolver.query(dname, "TXT")
# for i in TXT.response.answer:
#     print(dname + ":"+str(i) )
#     print(i)
# for i in Cname:
#     print("163.com" + ":" + i)



# import getopt, sys
#
# def main():
#     try:
#         opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
#     except getopt.GetoptError as err:
#         # print help information and exit:
#         print(err)  # will print something like "option -a not recognized"
#         usage()
#         sys.exit(2)
#     output = None
#     verbose = False
#     for o, a in opts:
#         if o == "-v":
#             verbose = True
#         elif o in ("-h", "--help"):
#             usage()
#             sys.exit()
#         elif o in ("-o", "--output"):
#             output = a
#         else:
#             assert False, "unhandled option"
#     # ...
#
# if __name__ == "__main__":
#     main()
#
# import  requests
#
# reponse = requests.get("http://httpbin.org/ip")
# print(reponse.text)
# import requests
#
# proxy = {
#     'http': '218.244.147.59:3128'
# }
#
# response = requests.get("http://httpbin.org/ip",proxies=proxy)
# print(response.text)
import sys
import getopt

arg = sys.argv[1:]
opthons = getopt.getopt(arg,"t:")
print (opthons)
for o,v in opthons:
    if o in ("-t"):
        filename = v
        with open(filename, "r", encoding="utf-8") as lines:
            line = lines.read()
            print(line)




