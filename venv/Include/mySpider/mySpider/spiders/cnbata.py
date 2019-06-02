# -*- coding: utf-8 -*-
import scrapy


class CnbataSpider(scrapy.Spider):
    name = 'cnbata'
    allowed_domains = ['cnbeta.com']
    start_urls = ['https://www.cnbeta.com/']

    def parse(self, response):
        select = response.xpath('//*[@id="J_all_item_853041"]/dl/dt/a/span/text()')
        # select = response.xpath('//*')
        print('爬取的内容为' ,select)
        print(type(select))
        filename = "cnbeta.html"
        with open(filename, mode='wb+') as file :
            print("a________________________")
            file.write(response.body)
            print("a________________________")

        pass
