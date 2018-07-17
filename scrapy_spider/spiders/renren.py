# -*- coding: utf-8 -*-
import re

import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/327550029/profile']


    def start_requests(self):
        '''
            重写
        :return:
        '''
        cookies = "anonymid=jjp1qhb8ju6rfq; depovince=GW; jebecookies=7557f511-5010-476a-9cbf-30b33d8f634b|||||; _r01_=1; ick_login=50fb12c0-ba57-41e4-b549-e09ffcf0509c; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=ad64a71f9e689725929e8780c053d0ce9; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20180711/2125/main_SDYi_ae9c0000bf9e1986.jpg; t=37b8a6c221c07b6973d0dbfdabb1bb7a9; societyguester=37b8a6c221c07b6973d0dbfdabb1bb7a9; id=327550029; xnsid=5a043303; loginfrom=syshome; JSESSIONID=abczB9lf-uW3YgPW8_Lsw; jebe_key=5fec7697-1d9d-4cd3-82a7-c2708e02bb88%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1531793102512%7C1%7C1531793107471; Hm_lvt_966bff0a868cd407a416b4e3993b9dc8=1531793143; _ga=GA1.2.716872696.1531793143; _gid=GA1.2.890015324.1531793143; _ga=GA1.3.716872696.1531793143; _gid=GA1.3.890015324.1531793143; Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8=1531793201; wp_fold=0"

        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        # headers = {"Cookie":cookies}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
            # headers = headers
        )


    def parse(self, response):
        print(re.findall("毛兆军", response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/327550029/profile?v=info_timeline",
            callback=self.parse_detial
        )

    def parse_detial(self, response):
        print(re.findall("毛兆军", response.body.decode()))
