# import requests
# import re
# from ShangWuBu.spiders.shangwubu import ShangwubuSpider
# url_dlist = ['http://www.mofcom.gov.cn/article/ae/ldhd/',
#              'http://www.mofcom.gov.cn/article/ae/ai/',
#              'http://www.mofcom.gov.cn/article/ae/ag/',
#              'http://www.mofcom.gov.cn/article/ae/sjjd/',
#              'http://www.mofcom.gov.cn/article/ae/slfw/',
#              'http://www.mofcom.gov.cn/article/ae/ztfbh/',
#              'http://www.mofcom.gov.cn/article/b/c/',
#              'http://www.mofcom.gov.cn/article/b/fwzl/',
#              'http://www.mofcom.gov.cn/article/b/d/',
#              'http://www.mofcom.gov.cn/article/b/bf/',
#              ]
#
#
# def parse(self, response):
#     try:
#         # print("=======================1====================")
#         url_list = response.xpath('//ul[@class="u-newsList01 f-mt10"]//li/a/@href').extract()[0]
#         title = response.xpath('//ul[@class="u-newsList01 f-mt10"]//li/a/@title').extract()[0]
#         url = "http://www.mofcom.gov.cn" + url_list
#         # print(url)
#         #
#         # print(title)
#         # print("======================2====================")
#         print("==================1=======================")
#
#         yield scrapy.Request(url=url, callback=self.parse1)
#     except:
#         pass
#
#
#
# for i in url_dlist:
#     try:
#         test=requests.get(url=i).content.decode('utf-8')
#         # print(test)
#         url = re.findall(r"href='(.*?)'",str(test),re.S)
#         # print(url)
#         url=url[0]
#         requests.get(url).content.decode('utf-8')
#         ss = ShangwubuSpider()
#         urlll= ss.url
#         testt=requests.get(url=urlll).content.decode('utf-8')
#         print(testt)
#         url123 = re.findall(r"href='(.*?)'",str(testt),re.S)
#         url1234 =url123[0]
#         requests.get(url1234).content.decode('utf-8')
#     except:
#         pass
