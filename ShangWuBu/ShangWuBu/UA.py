import random
import urllib.request,requests
from lxml import etree
# UA池   亲测稳定可用    如有异常请查看网络连接或者尝试指定本地UA！
            #ps 某些网站可能会拒绝特定浏览器
def UserAgent():
    USER_AGENTS = [
        # opera  速度慢信号差，保留备用使用。
        # 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        # 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
        # firefox
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        # chrome  很强！首推
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        # 360   第一个凑合   第二个速度微慢
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        # taobao
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
        # 猎豹
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
        # UC浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    ]
    USER_AGENTS = random.choice(USER_AGENTS)
    UA = {"User-Agent": USER_AGENTS}
    return UA

#随机选取UA池一个User-Agent进行模拟
# 使用的时候格式如下：
# headers = {'User-Agent':UserAgent()，}
#最下面为测试文本。


#get_IP,从快代理获取首页最新ip进行挑选测试并返回可用ip
def GetProxies():
    proxy = []
    page= 1
                                         #构建请求———加入headers
    req = urllib.request.Request("https://www.kuaidaili.com/free/inha/" + str(page),headers=UserAgent())
    html = urllib.request.urlopen(req).read()
       #爬取页面信息并赋给html
    # print(html)
    content = etree.HTML(html)                          #XPath解析对象并对HTML文本进行自动修正。
    ip = content.xpath('//td[@data-title="IP"]/text()') #XPath ：可用来在XML文档中对元素和属性进行遍历
    port = content.xpath('//td[@data-title="PORT"]/text()')     #XML的设计宗旨是传输数据，而不是显示数据。

    for i in range(len(ip)):
        for p in range(len(port)):
            if i == p:                                      #循环添加到空列表中
                if ip[i] + ':' + port[p] not in proxy:
                    proxy.append(ip[i] + ':' + port[p])

    proxy_ran=random.choice(proxy)
    proxy_list = {'http': proxy_ran}
    url_all = ['https://www.baidu.com'
                'https://maoyan.com/board',
                'https://fanyi.baidu.com/sug',
                'http://www.renren.com/PLogin.do',
                ]
    url = random.choice(url_all)
    try:
        html = requests.request('get', url=url, proxies=proxy_list).content.decode('utf-8')
    except:
        pass
    if not html:
        GetProxies()
    else:
        print(proxy_list)
        print("已经成功获取代理")
        return proxy_list



def requests_html(base_url):
    try:
        html = requests.get(url=base_url, headers=UserAgent(), proxies=GetProxies()).content.decode('utf-8')
        return html
    except:
        requests_html(base_url)

def requests_tree(base_url):
    try:
        html = requests.get(url = base_url,headers = UserAgent()).content.decode('utf-8')
        tree = etree.HTML(html)
        return tree
    except:
        requests_tree(base_url)

def req_wudaili(base_url):
    try:
        html = requests.get(url=base_url,headers= UserAgent()).content.decode('utf-8')
        return html
    except:
        req_wudaili(base_url)

'''测试内容(请放在同级目录下进行测试)'''
# from UA import GetProxies,UserAgent
# import requests
# url = "https://hr.tencent.com/position.php?keywords=python&start=0"
# content = requests.request('get',url=url,headers= UserAgent(),proxies=GetProxies()).content.decode('utf-8')
# print(content)



#微型架构测试中
# import requests,random
# from lxml import etree
# # from UA import requests_url
# class Lx_test():
#     def __init__(self,base_url):
#         self.html = requests_tree(base_url)
#         self.parse_html()
#     def parse_html(self):
#         group_num = self.html.xpath('xxx')
# base_url = "xxx"
# Lx_test(base_url)


