from dns import resolver
from qqwry import updateQQwry
from qqwry import QQwry
import whois
import socket
from ipwhois import IPWhois

#查询dns信息

class dnsinfo:
    """
    初始化对象
    """
    def __init__(self,domain):
        self.domain = domain
        self.A_list = []
        self.NS_list = []
        self.MX_list = []
        self.SOA_list = []
        self.TXT_list = []
        self.Cname_list = []
        self.SRV_list = []
        self.PTR_list = []
    """
    1.查询网站的A记录，获得其ip地址
    2.使用其ip地址和纯真数据库获得其真实地址
    3.如果能够查到就返回一个  ---->   [[ip,{city:city,isp:value}],[ip,{city:city,isp:value}]....]
      如果没有查到就返回一个  ---->   ['163NO A text!']
    """
    def A(self):
        wry = QQwry()
        wry.load_file("qqwry.dat")
        try:
            A = resolver.resolve(self.domain, 'A')
            for i in A.response.answer:
                for j in i.items:
                    tmp = []
                    tmp.append(str(j))
                    info = wry.lookup(str(j))
                    res = {"city": info[0], "isp": info[1]}
                    tmp.append(res)
                    self.A_list.append(tmp)
        except:
            tmp =self.domain+"NO A text!"
            self.A_list.append(tmp)
        return self.A_list


    """
    1.查询网站的NS记录
    2.如果能够查到就返回一个  ---->   ['163.com. 1435 IN NS ns2.166.com.', '163.com. 1435 IN NS ns4.nease.net.'........]
      如果没有查到就返回一个  ---->   ['{domain}NO NS text!']
    """
    def NS(self):
        try:
            NS = resolver.resolve(self.domain,"NS")
            for i in NS.response.answer:
                self.NS_list = str(i).split("\n")
        except:
            self.NS_list.append(self.domain + " NO NS text!")
        return self.NS_list

    """
    1.查询网站的MX记录
    3.如果能够查到就返回一个  ---->   ['MX preference =10mail exchanger =163mx01.mxmail.netease.com.', 'MX preference =10mail exchanger =163mx02.mxmail.netease.com.'......]
      如果没有查到就返回一个  ---->   ['{domain}NO MX text!']
    """
    def MX(self):
        try:
            MX =resolver.resolve(self.domain, 'MX')
            for i in MX:
                tmp = 'MX preference =' + str(i.preference) + 'mail exchanger =' + str(i.exchange)
                self.MX_list.append(tmp)
        except:
            print(self.domain+" NO MX text")
        return self.MX_list
    """
    1.查询网站的TXT记录
    2.如果能够查到就返回一个  ---->   ['163.com. 699 IN TXT "v=spf1 include:spf.163.com -all"', '163.com. 699 IN TXT "google-site-verification=hRXfNWRtd9HKlh-ZBOuUgGrxBJh526R8Uygp0jEZ9wY"',........]
      如果没有查到就返回一个  ---->   ['163NO MX text!']
    """
    def TXT(self):
        try:
            TXT = resolver.resolve(self.domain,"TXT")
            for i in TXT.response.answer:
                self.TXT_list = str(i).split("\n")
        except:
            self.TXT_list.append(self.domain + " NO TXT text")
        return self.TXT_list

    """
    1.查询网站的TXT记录
    2.如果能够查到就返回一个  ---->   ["xxx","xxx","xxx"..]
      如果没有查到就返回一个  ---->   ['163NO Cname text!']
    """
    def Cname(self):
        try:
            Cname =resolver.resolve(self.domain,'CNAME')
            for i in  Cname:
               self.Cname_list =  str(i).split("\n")
        except:
            self.Cname_list.append(self.domain+" NO CNAME text")
        return self.Cname_list

    """
    1.查询网站的TXT记录
    2.如果能够查到就返回一个  ---->   ['dns.baidu.com.', 'sa.baidu.com.', '2012144815', '300', '300', '2592000', '7200']
      如果没有查到就返回一个  ---->   ['163NO SOA text!']
    """
    def SOA(self):
        S = " "
        try:
            SOA = resolver.resolve(self.domain,"SOA")
            for i in SOA:
                self.SOA_list = str(i).split(" ")
        except:
            self.SOA_list.append(self.domain+"NO SOA text")
        return self.SOA_list

    def SRV(self):
        pass


    def PTR(self,dname):
        pass

#查询whois信息
class whoisinfo:
    def __init__(self,domain):
        self.domain = domain
        self.Whois_dic = {}
        self.Ipwhoid_dic = {}


    def Update(self):
        updateQQwry('qqwry.dat')
    """
    1.查询网站的whois记录
    2.如果能够查到就返回一个  ---->  {
                                      "domain_name": [
                                        "BAIDU.COM",
                                        "baidu.com"
                                      ],
                                      "registrar": "MarkMonitor, Inc.",
                                      "whois_server": "whois.markmonitor.com",
                                      "referral_url": null,
                                      "updated_date": [
                                        "2020-12-09 04:04:41",
                                        "2021-04-07 19:52:21+00:00"
                                      ],
                                      "creation_date": [
                                        "1999-10-11 11:05:17",
                                        "1999-10-11 11:05:17+00:00"
                                      ],
                                      "expiration_date": [
                                        "2026-10-11 11:05:17",
                                        "2026-10-11 07:00:00+00:00"
                                      ],
                                      "name_servers": [
                                        "NS1.BAIDU.COM",
                                        "NS2.BAIDU.COM",
                                        "NS3.BAIDU.COM",
                                        "NS4.BAIDU.COM",
                                        "NS7.BAIDU.COM",
                                        "ns1.baidu.com",
                                        "ns3.baidu.com",
                                        "ns4.baidu.com",
                                        "ns2.baidu.com",
                                        "ns7.baidu.com"
                                      ],
                                      "status": [
                                        "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited",
                                        "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
                                        "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited",
                                        "serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited",
                                        "serverTransferProhibited https://icann.org/epp#serverTransferProhibited",
                                        "serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited",
                                        "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)",
                                        "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)",
                                        "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)",
                                        "serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)",
                                        "serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)",
                                        "serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)"
                                      ],
                                      "emails": [
                                        "abusecomplaints@markmonitor.com",
                                        "whoisrequest@markmonitor.com"
                                      ],
                                      "dnssec": "unsigned",
                                      "name": null,
                                      "org": "Beijing Baidu Netcom Science Technology Co., Ltd.",
                                      "address": null,
                                      "city": null,
                                      "state": "Beijing",
                                      "zipcode": null,
                                      "country": "CN"
                                    }

      如果没有查到就返回一个  ---->  指点的所有字段都返回null
    """
    def Whois(self):
        obj = whois.whois(self.domain)
        try:
            self.Whois_dic=obj
        except :
            pass
        return self.Whois_dic
    """
    1.查询网站的whois记录
    2.如果能够查到就返回一个  ---->  {
                                    'nir': None, 
                                    'asn_registry': 'apnic', 
                                    'asn': '23724', 
                                    'asn_cidr': '220.181.32.0/19', 
                                    'asn_country_code': 'CN', 
                                    'asn_date': '2002-10-30', 
                                    'asn_description': 'CHINANET-IDC-BJ-AP IDC, 
                                    China Telecommunications Corporation, CN', 
                                    'query': '220.181.38.251', 
                                    'nets': [{'cidr': '220.181.0.0/16', 
                                    'name': 'CHINANET-IDC-BJ', 
                                    'handle': 'CH93-AP', 
                                    'range': 
                                    '220.181.0.0 - 220.181.255.255', 
                                    'description': 'CHINANET Beijing province network\nChina Telecom\nNo.31,
                                    jingrong street\nBeijing 100032', 
                                    'country': 'CN', 
                                    'state': None, 'city': None, 
                                    'address': 'No.31 ,j
                                    ingrong street,beijing\n100032', 
                                    'postal_code': None, 
                                    'emails': ['anti-spam@ns.chinanet.cn.net', 
                                    'bjnic@bjtelecom.net'], 
                                    'created': None,
                                    'updated': None}], 
                                    'raw': None, 
                                    'referral': None, 
                                    'raw_referral': None}
      如果没有查到就返回一个  ---->  {'baidu': 'ipwhois 查询错误'}
    """
    def Ipwhois(self):
        domain_prefix = ''
        try:
            ip = socket.gethostbyname(domain_prefix + self.domain)
            obj = IPWhois(ip)
            self.Ipwhoid_dic = obj.lookup_whois()
        except :
            self.Ipwhoid_dic = {self.domain:"ipwhois 查询错误"}
        return self.Ipwhoid_dic
