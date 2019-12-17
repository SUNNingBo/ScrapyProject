# -*- coding: utf-8 -*-
import scrapy
from Scrapy_EtcData.Scrapy_EtcData.items import ScrapyEtcdataItem

class EtcdataSpiderSpider(scrapy.Spider):
    #爬虫名字
    name = 'etcdata_spider'
    #允许的域名
    allowed_domains = ['movie.douban.com']
    #入口url
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for movie in movie_list:
            douban_item = ScrapyEtcdataItem()
            douban_item['serial_number'] = movie.xpath("")