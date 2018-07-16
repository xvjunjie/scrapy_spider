# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import re

from pymongo import MongoClient

logger = logging.getLogger(__name__)

client = MongoClient()
db = client["python_database"]


class ScrapySpiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "itcast":
            pass
        return item


class TencentSpiderPipeline(object):
    def __init__(self):
        self.hr_cllection = db["hr_cllection"]

    def process_item(self, item, spider):
        if spider.name == "hr_tencent":
            self.hr_cllection.insert(dict(item))

        return item


class SunSpiderPipeline(object):
    def open_spider(self, spider):
        # spider.hello = "world"
        client = MongoClient()
        self.collection = client["test"]["test"]

    def process_item(self, item, spider):
        spider.settings.get("MONGO_HOST")
        item["content"] = self.process_content(item["content"])
        print(item)

        self.collection.insert(dict(item))
        return item

    def process_content(self, content):
        content = [re.sub(r"\xa0|\s", "", i) for i in content]
        content = [i for i in content if len(i) > 0]  # 去除列表中的空字符串
        return content


