# 作者：Sceva
# 日期：2021/8/15 14:01
# 工具：PyCharm
# Python版本：3.6.3
import dnsscaner
import output
import config
# import port
# ip_address= "目标IP"
# ip_local="IP位置"
# ip_auther="其他关联IP"
# port = "开放端口"
# web_server="Web 应用服务器"
# lang_data="开发语言数据库"
# web_cms="Web框架"
# app="对应App"
# who="域名Whois"
# user_acc="社交媒体账号"
# user_info="人员信息"
mode_file = "big.xls"
domain= "elections.org.za"

a = output.read_exceal(mode_file)

ip_address=[]
for i,r in enumerate(a):
    for j,rc in enumerate(r):
        if rc == config.ip_address :
            a[i][j+1]=dnsscaner.dnsinfo.A("self",domain)[0]
            print(dnsscaner.dnsinfo.A("self",domain)[0])
            print(type(dnsscaner.dnsinfo.A("self",domain)[0]))
        elif rc == config.ip_local:
            a[i][j + 1] = dnsscaner.dnsinfo.A("self",domain)[1]
        elif rc == config.who:
            a[i][j + 1] =dnsscaner.whoisinfo.Whois("self", domain)
            a[i][j + 1] += dnsscaner.dnsinfo.NS("self",domain)
            a[i][j + 1] += dnsscaner.dnsinfo.MX("self", domain)
            a[i][j + 1] += dnsscaner.dnsinfo.Cname("self", domain)
            a[i][j + 1] += dnsscaner.dnsinfo.SOA("self", domain)
            a[i][j + 1] += dnsscaner.dnsinfo.TXT("self", domain)
        # elif rc == config.port:
        #     a[i][j + 1] = port.main(dnsscaner.dnsinfo.A("self",domain)[0])

print(a)
output.write_exceal(mode_file,a,"qweqeqweqweqeqew.xls")
