# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from general_spider.utils import get_config
#from general_spider.rules import rules
#from general_spider.rules import sina_extract_item
from general_spider.rules import rules
from general_spider.rules import sina_extract_item
from general_spider.rules import micai_extract_item
from general_spider.rules import extract_rules


class UniversalSpider(CrawlSpider):
    name = 'universal'
    def __init__(self,name,*args,**kwargs):
        config=get_config(name)
        self.config=config
        self.rules=rules.get(config.get('rules'))
        self.start_urls=config.get('start_urls')
        self.allowed_domains=config.get('allowed_domains')
        super(UniversalSpider,self).__init__(*args,**kwargs)

    def parse_item(self, response):
        item=extract_rules(response)
        #item=micai_extract_item(response)
        yield item
