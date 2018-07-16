# -*- coding: utf-8 -*-
import re
from copy import deepcopy

import scrapy
from scrapy_spider.items import SltsSpiderItem


class SltsSpider(scrapy.Spider):
    """
        苏宁 图书
    """
    name = 'slts'
    allowed_domains = ['suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='ulwrap'/li]")
        for li in li_list:
            item = SltsSpiderItem()
            # 大分类标签
            item["b_cate"] = li.xpath(".//div[@class='second-sort']/a/text()").extract_first()

            # 小分类标签
            a_list = li.xpath(".//div[@class='three-sort']/a")
            for a in a_list:
                item["s_href"] = a.xpath("./@href").extract_first()
                item["s_cate"] = a.xpath("./text()").extract_first()

                if item["s_href"] is not None:
                    item["s_href"] = "http://snbook.suning.com/" + item["s_href"]

                yield scrapy.Request(
                    item["s_href"],
                    callback=self.parse_content_list,
                    meta={"item": deepcopy(item)}

                )

    def parse_content_list(self, response):
        item = deepcopy(response.meta["item"])
        li_list = response.xpath("//div[@class='filtrate-books list-filtrate-books']/ul/li")
        for li in li_list:
            item["book_name"] = li.xpath(".//div[@class='book-title']/a/text()").extract_first()  # 标题
            item["book_href"] = li.xpath(".//div[@class='book-title']/a/@href").extract_first()  # 描述

            item["book_img"] = li.xpath("./div[@class='book-img']//img/@src").extract_first()  # 图片
            if item["book_img"] is None:
                item["book_img"] = li.xpath(".//div[@class='book-img']//img/@src2").extract_first()
            item["book_desc"] = li.xpath(".//div[@class='book-descrip c6']/text()").extract_first()  # 描述

            yield scrapy.Request(
                item["book_href"],
                callback=self.parse_content_detail,
                meta={"item": deepcopy(item)}
            )

        # 下一页
        page_count = int(re.findall("var pagecount=(.*?);", response.body.decode())[0])
        current_page = int(re.findall("var currentPage=(.*?);", response.body.decode())[0])

        if current_page < page_count:
            next_url = item["s_href"] + "?pageNumber={}&sort=0".format(current_page + 1)
            yield scrapy.Request(
                next_url,
                callback=self.parse_book_list,
                meta={"item": response.meta["item"]}
            )

    def parse_content_detail(self, response):
        item = response.meta["item"]
        item["book_price"] = re.findall("\"bp\":'(.*?)',", response.body.decode())
        item["book_price"] = item["book_price"][0] if len(item["book_price"]) > 0 else None
        print(item)
