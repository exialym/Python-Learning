# -*- coding: utf-8 -*-
from time import sleep
from lxml import html
import requests
nextButtonXpath = "//button[@id='showNextPage']"
titleXpath = "//a[@class='forumTitleLink wrapWord']/text()"
categoryXpath = "//p[@class='forumListProperties'][1]/text()"
infoXpath = "//p[@class='forumListProperties'][1]"
info2Xpath = "//p[@class='forumListProperties'][2]"
url = "http://answers.microsoft.com/zh-hans/forum/forumthreadlist?forumId=cacb25ef-5e2a-e011-8a67-d8d385dcbb12&sort=LastReplyDate&dir=Desc&tab=Threads&meta=windows_10&status=all&mod=&modAge=&advFil=&postedAfter=&postedBefore=&page={}&threadType=All&tm=1444898609931"
pageNo = 1
headers = {'X-Requested-With': ' XMLHttpRequest'}
problems = []
tip = u"从微软Windows 10官方技术论坛获取不多于100条帖子，并获得帖子类别，浏览次数等详细信息。\n"
print tip
while len(problems)<100 and url:
	tempUrl = url.format(pageNo)
	page = requests.get(tempUrl,headers=headers)
	print page.encoding
	tree = html.fromstring(page.text)
	titles = tree.xpath(titleXpath)
	categorys = tree.xpath(categoryXpath)
	infos = tree.xpath(infoXpath)
	print infos
	infos2 = tree.xpath(info2Xpath)
	for i in range(0,len(titles)):
		infoThis = infos[i].xpath("span[@class='text-nowrap']/text()")
		infoThis += infos[i].xpath("span/span[@class='forumListCountPos']/text()")
		infoThis += infos[i].xpath("span/span[@class='forumAnswerCountLabel']/text()")
		infoFinal = ""
		infoThis2 = infos2[i].xpath("span[@class='text-nowrap'][1]/text()") 
		infoThis2 += infos2[i].xpath("span[@class='text-nowrap'][1]/a/text()") 
		infoThis3 = infos2[i].xpath("span[@class='text-nowrap'][2]/a/text()")
		infoFinal2 = ""
		infoFinal3 = ""  
		for info in infoThis:
			infoFinal += info.strip() + " "
		for info in infoThis2:
			infoFinal2 += info.strip().replace('\n','')
		for info in infoThis3:
			infoFinal3 += info.strip()
		problems.append(u"题目：" + titles[i]  + "\n" + infoFinal + "\n" + infoFinal2 + "\n" + infoFinal3 + "\n")
		#+ u"\n类别:" + categorys[i]
	nextButton = tree.xpath(nextButtonXpath)
	print u"从第{}页获得了{}个帖子（URL：{}）\n".format(pageNo, len(titles),tempUrl)
	if nextButton:
		pageNo += 1
	else:
		url = none
	sleep(3)
with open('problemList.txt', 'wb') as out:
    out.write("\n".join(problems).encode('utf-8'))
with open('problemList.txt') as f:
    problems_ = f.readlines()
    
print "共获取了{}个帖子".format(len(problems_))
for problem in problems_:
    print problem

