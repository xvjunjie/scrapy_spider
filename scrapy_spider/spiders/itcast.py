# -*- coding: utf-8 -*-
import scrapy
from scrapy_spider.items import ScrapySpiderItem
import logging

logger = logging.getLogger(__name__)


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        li_lsit = response.xpath("//div[@class='tea_con']//li")

        item = ScrapySpiderItem()
        for li in li_lsit:
            item["name1"] = li.xpath(".//h3/text()").extract_first()
            # print(item["name"])
            yield item


