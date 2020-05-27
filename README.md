# General-spider-for-news-website
使用scrapy 对新闻门户网站进行通用化爬虫，实现不同新闻平台间的爬虫迁移

### 使用步骤

1. 修改配置文件json文件和rules.py文件
 
2. 运行```python run.py json配置文件名```

### 注意：配置文件的修改主要包括以下几点：

1. json文件主要用于输入所抓取站点的基本信息，比如域名和爬虫起始页

2. rules.py 文件包含链接提取规则（在rules字典中）、构建要抓取的数据结构（在NewsItem类中）、网页解析规则（在extract_rules函数中）
