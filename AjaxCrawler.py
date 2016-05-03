# -*- coding: utf-8 -*-
nextButtonXpath = "//li[@class='next']/a/@href"
headlineXpath = "//li[@class='item']/div[@class='info']/div[@class='title']/a/text()"
subtitleXpath = "//li[@class='item'][{}]//p[@class='subtitle']/text()"
authorXpath = "//li[@class='item'][{}]//a[@class='author-item']/text()"
categoryXpath = "//li[@class='item'][{}]//span[@class='labeled-text']/span/text()"
rateXpath = "//li[@class='item'][{}]//span[@class='rating-average']/text()"
translatorXpath = "//li[@class='item'][{}]//span[@class='meta-item']//a[@class='author-item']/text()"
reviewXpath = "//li[@class='item'][{}]//a[@class='ratings-link']/span/text()"
introduceXpath = "//li[@class='item']//div[@class='article-desc-brief']/text()"
 
from time import sleep
from lxml import html
import requests
headers = {'X-Requested-With': ' XMLHttpRequest'}
page = requests.get('http://list.jd.com/list.html?cat=9987,653,655')
tree = html.fromstring(page.text)
jd_names = tree.xpath("//div[@class='p-name']/a/em/text()")
for jd_name in jd_names[:5]:
    print jd_name
jd_ids = tree.xpath("//div[@class='gl-i-wrap j-sku-item']/@data-sku")
# for jd_id in jd_ids:
#     print jd_id.attrib['data-sku']
for ids_groups in [jd_ids[i:i+5] for i in range(0,len(jd_ids),5)]:
    skuIds = '%2C'.join(map(lambda x: 'J_%s' % x, [ids_group for ids_group in ids_groups]))
    page = requests.get('http://p.3.cn/prices/mgets?callback=jQuery8870889&type=1&area=1&skuIds=%s' % skuIds)
    print page.content

