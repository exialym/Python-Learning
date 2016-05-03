# -*- coding: utf-8 -*-
from time import sleep
from lxml import html
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
titleXpath = "//div[@class='slide01_items']/a/@href"
url = "http://blog.sina.com.cn"
page = requests.get(url)
page.encoding = "utf-8"
print page.text
tree = html.fromstring(page.text)
title = tree.xpath(titleXpath)
print title

