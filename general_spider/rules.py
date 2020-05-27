from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
#from general_spider.items import NewsItem
from scrapy import Field,Item
import re

#页面链接提取规则
rules={
    'sina':(
        Rule(LinkExtractor(allow='world\/.*\.shtml',restrict_xpaths='//div[@class="fixList"]//li'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="_function_code_page"]//a[contains(.,"下一页")]'))
    ),
    'micai':(
        Rule(LinkExtractor(allow='article\/.*\.html',restrict_xpaths='//div[@class="list_title"]'),callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="nav_left"]//a[contains(.,"下一页")]'))
    )
}

#要提取的页面数据结构
class NewsItem(Item):
    title=Field()
    datetime=Field()
    text=Field()
    keyWord=Field()
    source = Field()
    website=Field()


#页面数据提取规则
def extract_rules(response):
    item=NewsItem()
    item['title']=''
    item['datetime']=''
    item['text']=''
    item['keyWord']=''
    item['source']=''
    item['website']=''
    return item

"""
def sina_extract_item(response):
    item = NewsItem()
    item['title'] = response.xpath('//h1[@class="main-title"]/text()').extract_first()
    item['datetime'] = response.xpath('//div[@class="date-source"]//span[@class="date"]/text()').extract_first()
    item['text'] = re.sub('\s|\t|\n', '',
                          ''.join(response.xpath('//div[@id="article"]//text()').extract()).strip().replace(u'\u3000',
                                                                                                            u'').replace(
                              u'\xa0', u''))
    item['keyWord'] = response.xpath('//div[@class="keywords"]//a/text()').extract_first()
    item['source'] = response.xpath('//div[@class="date-source"]//a/text()').extract_first()
    item['website'] = '新浪军事'
    return item

def micai_extract_item(response):
    item = NewsItem()
    item['title'] = response.xpath('//div[@class="nav_left"]//h1/text()').extract_first()
    item['datetime'] = response.xpath('//div[@class="nav_zuoze"]/text()').extract_first()
    item['text'] = re.sub('\s|\t|\n', '',
                          ''.join(response.xpath('//div[@class="nav_main content"]//p//text()').extract()).strip().replace(u'\u3000',
                                                                                                            u'').replace(
                              u'\xa0', u''))
    item['keyWord'] = '无'
    item['source'] = '无'
    item['website'] = '迷彩虎军事'
    return item
"""