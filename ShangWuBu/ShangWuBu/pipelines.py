# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class ShangwubuPipeline(object):
    def __init__(self):
        #链接本地数据库：
        self.client=pymongo.MongoClient('localhost')
        #数据库：
        self.db = self.client['xinwen']
        #集合：
        self.xinxi =self.db['xinxi']
        print("_________________________")

    def process_item(self, item, spider):
        print('###################')
        self.xinxi.insert(dict(item))


        return item
