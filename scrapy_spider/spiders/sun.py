# -*- coding: utf-8 -*-
import scrapy
from scrapy_spider.items import SunSpiderItem


class SunSpider(scrapy.Spider):
    """
        阳光热线
    """
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        tr_list = response.xpath("//div[class='ctitle']/table[2]/tr/td/table/tr")

        item = SunSpiderItem()
        for tr in tr_list:
            item["title"] = tr.xpath("./td[2]/a[@class='news14']/@title").extract_first()
            item["href"] = tr.xpath("./td[2]/a[@class='news14']/@href").extract_first()
            item["publish_date"] = tr.xpath("./td[last()]/text()").extract_first()


            yield scrapy.Request(
                item["href"],
                callback=self.parse_detail,
                meta={"item":item}
            )


        # 下一页
        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )


    #页面详情
    def parse_detail(self,response):
        item = response.meta("item")
        item["content"] = response.xpath("//div[@class='c1 text14_2']/text()")
        item["content_img"] = response.xpath("//div[@class='c1 text14_2']//img/@src/extract()")

        item["content_img"] = ["http://wz.sun0769.com" + i for i in item["content_img"]]
        print(item)
        yield item
