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

titles = []
baseUrl = 'http://read.douban.com/tag/%E7%A7%91%E5%B9%BB/{}'
nextUrl = 'http://read.douban.com/tag/%E7%A7%91%E5%B9%BB/'
pageNo = 0
books = []

while len(books)<100 and nextUrl:
    pageNo += 1
    dom = html.parse(nextUrl)
    headLines = dom.xpath(headlineXpath)
    introduces = dom.xpath(introduceXpath)

    print "We got {} books from Page{}. url({})".format(len(headLines), pageNo, nextUrl)

    for i in range(0,len(headLines)):
        No = i + 1
        subtitle = dom.xpath(subtitleXpath.format(No))
        authors = dom.xpath(authorXpath.format(No))
        translators = dom.xpath(translatorXpath.format(No))
        category = dom.xpath(categoryXpath.format(No))
        rate = dom.xpath(rateXpath.format(No))
        review = dom.xpath(reviewXpath.format(No))

        if subtitle :
            subtitle = u'\n简介：' + subtitle[0]
        else:
            subtitle = ''

        if authors :
            authors = authors[0]
        else:
            authors = u"未知作者"

        if translators:
            authors += u"\n译者："
            for translator in translators:
                authors += translator + '  '

        if category :
            category = category[0]
        else:
            category = u"暂时未分类"

        if rate :
            rate = rate[0]
        else:
            rate = u"暂时没有评分"

        if review :
            review = review[0] + u"人评价"
        else:
            review = u"还没有人评价"

        books.append(headLines[i] + subtitle + u'\n作者：' + authors + u'\n类别：' + category + u'\n评分：' + rate + '\n' + review  + u"\n摘要：" + introduces[i] + '\n')
    nextUrl = dom.xpath(nextButtonXpath)
    if nextUrl:
        nextUrl = baseUrl.format(nextUrl[0])
    else:
        print('This is the last page')
        nextUrl = None
    sleep(3)
with open('bookList.txt', 'wb') as out:
    out.write('\n'.join(books).encode('utf-8'))
with open('bookList.txt') as f:
    books_ = f.readlines()
    
print "Well, we got {} Books!".format(len(books_))
for book in books_:
    print book
