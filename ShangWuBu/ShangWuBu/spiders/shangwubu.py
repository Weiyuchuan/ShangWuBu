# -*- coding: utf-8 -*-
import scrapy
import re
import time

from ShangWuBu import UA
from ShangWuBu.items import ShangwubuItem


class ShangwubuSpider(scrapy.Spider):
    name = 'shangwubu'
    allowed_domains = ['mofcom.gov.cn']
    start_urls = []
    url_dlist=['http://www.mofcom.gov.cn/article/ae/?wscckey=3fb1abb2a4ccdb62_1552997120']

    # url_dlist=['http://www.mofcom.gov.cn/article/ae/ldhd/',
    #               'http://www.mofcom.gov.cn/article/ae/ai/',
    #               'http://www.mofcom.gov.cn/article/ae/ag/',
    #               'http://www.mofcom.gov.cn/article/ae/sjjd/',
    #               'http://www.mofcom.gov.cn/article/ae/slfw/',
    #               'http://www.mofcom.gov.cn/article/ae/ztfbh/',
    #               'http://www.mofcom.gov.cn/article/b/c/',
    #               'http://www.mofcom.gov.cn/article/b/fwzl/',
    #               'http://www.mofcom.gov.cn/article/b/d/',
    #               'http://www.mofcom.gov.cn/article/b/bf/',
    #               ]
    for url in url_dlist:
        start_urls.append(url)
    # print(start_urls)


    def parse(self, response):


            # print(response.body.decode('utf-8'))
            # with open('页面.html','a',encoding='utf-8')as fp:
            #     fp.write(response.body.decode('utf-8'))
            url_list = response.xpath('//section[@class="w1200 m-con-01"]//li')
            # print(url_list)
            with open('测试.txt', 'a', encoding='utf-8')as fp:
                for i in url_list:
                    item=ShangwubuItem()
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11")
                    url_1 = i.xpath('.//a/@href').extract()[0]
                    title = i.xpath('.//a/text()').extract()[0]
                    # time = i.xpath('.//ul/li/span/text()').extract()[0]
                    url ='http://www.mofcom.gov.cn'+url_1
                    # print('@@@@@@@@@@@@@@@@@@@@@@222')
                    # print('路径：'+url)
                    # print('表头：'+title)
                    # print('时间：'+time)
                    fp.write(title+'\n')
                    item['title'] = title


                    yield scrapy.Request(url=url,callback=self.parse1,meta={"item":item})

    def parse1(self,response):
        item = response.meta["item"]

        # print("==================0=======================")
        count = response.body.decode('utf-8')
        time1 = re.findall(r'var tm.*?"(.*?)"',count)
        # print(time)

        item['time1'] = time1[0]
        source =re.findall(r'var source.*?"(.*?)"',count)
        item["source"] =source[0]
        info = response.xpath('//p[@style="TEXT-INDENT: 2em"]//text()').extract()
        info = "".join(info).replace("\n","")
        # print(info)
        with open('测试.txt', 'a', encoding='utf-8')as fp:
            fp.write(info+'\n\n')
            item['info']=info
        sj =time.time()
        xzsj = time.localtime(sj)
        pqsj = time.strftime("%Y--%m--%d %H:%M:%S",xzsj)
        item["pqsj"] =pqsj


        yield item







