# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from pymongo import MongoClient

logger = logging.getLogger(__name__)

client = MongoClient()
collection = client["tencent"]["hr"]


class ScrapySpiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "itcast":
            pass
        return item


class TencentSpiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "hr_tencent":
            collection.insert(dict(item))

        return item
