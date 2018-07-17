# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TtSpider(CrawlSpider):
    name = 'tencent1'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (

        # position_detail.php?id=42535&keywords=&tid=0&lid=0 详情页
        # position.php?keywords=&tid=0&start=10#a 下一页
        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'), follow=True),
    )

    def parse_item(self, response):
        """
            需要获取的数据在详情页
        :param response:
        :return:
        """
        item = {}
        item["title"] = response.xpath("//td[@id='sharetitle']/text()").extract_first()
        item["aquire"] = response.xpath("//div[text()='工作要求：']/../ul/li/text()").extract()
        # return i
        print(item)
