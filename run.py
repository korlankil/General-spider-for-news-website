import sys
from scrapy.utils.project import  get_project_settings
from general_spider.spiders.universal import UniversalSpider
from general_spider.utils import get_config
from scrapy.crawler import  CrawlerProcess

def run():
    #此处的name是配置文件json的名称
    name=sys.argv[1]
    custom_settings=get_config(name)

    #爬取时使用的spider的名称
    spider=custom_settings.get('spider')
    #建立一个配置对象project_settings,将其各个配置项转化成字典并传给settings
    project_settings=get_project_settings()
    settings=dict(project_settings.copy())

    #合并配置
    settings.update(custom_settings.get('settings'))
    process=CrawlerProcess(settings)

    #启动服务
    process.crawl(spider,**{'name':name})
    process.start()

if __name__=='__main__':
    run()
