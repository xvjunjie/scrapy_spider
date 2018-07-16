# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name1 = scrapy.Field
    Introduction = scrapy.Field

class TencentSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field
    position = scrapy.Field
    publish_date = scrapy.Field
    content = scrapy.Field
    content_img = scrapy.Field


class SunSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field
    href = scrapy.Field
    publish_date = scrapy.Field