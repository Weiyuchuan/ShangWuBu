from lxml import etree
import requests


url ='http://www.mofcom.gov.cn/article/ae/ag/?7&wscckey=8843b090c41291ba_1552366505'




response = etree.HTML(url)
# print(response)
a=requests.get(url=url).content.decode('utf-8')
print(a)
# test = response.xpath('//text()')
# print(test)

# url_list = response.xpath('//text()')
# print(url_list)