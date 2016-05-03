import urllib.request
import re
import os
import time
from selenium import webdriver

folder=''
default_page=4

def get_page(a,b):
    if a>b:
        return b
    else:
        return a
    

def get_listurl(url):
    driver=webdriver.Chrome()
    driver.get(url)
    time.sleep(4)
    #driver.implicitly_wait(7)
    global folder
    temp=driver.find_element_by_id("blognamespan")
    folder=driver.find_element_by_id("blognamespan").text
    if folder.startswith("加载中..."):
        folder="佚名"
    print(folder,"=folder")
    page_s=driver.page_source
    listurl=re.findall(r'href="(.+?)">博文目录',page_s)
    driver.quit()
    return listurl[0]

def get_blog(listurl):
    urls=[]
    f1=urllib.request.urlopen(listurl)
    content1=f1.read().decode()
    f1.close()
    if re.search(r'共(\d+)页',content1):
        match=re.findall(r'共(\d+)页',content1)
        page_old=int(match[0])
    else:
        page_old=1
    print('共有'+str(page_old)+'页')
    page=get_page(page_old,default_page)
    print('下载'+str(page)+'页')
    m=re.split('_',listurl)
    for i in range(1,page+1):
        each_list_url=m[0]+'_'+m[1]+'_'+m[2]+'_'+str(i)+'.html'#获得每一页list的url
        print (each_list_url)
        f2=urllib.request.urlopen(each_list_url)
        content2=f2.read().decode()
        f2.close()
        blog_url=re.findall(r'a title.*?href="(.+?)"',content2)
        #print(blog_url)
        print('正在下载第'+str(i)+'页')
        driver=webdriver.Chrome()
        for j in blog_url:
            driver.get(j)
            time.sleep(1)
            page_s=driver.page_source
            if re.search(r'blogtitle.+?href="(.+?)"',page_s):
                #driver.implicitly_wait(5)
                title=driver.title
                title=re.sub(r'\*','',title)
                title=re.sub(r'\\','',title)
                title=re.sub(r'\/','',title)
                title=re.sub(r'\:','',title)
                title=re.sub(r'\?','',title)
                title=re.sub(r'\"','',title)
                title=re.sub(r'\<','',title)
                title=re.sub(r'\>','',title)
                title=re.sub(r'\|','',title)
                print(title)
                path1=folder+'/'+title+'.txt'
                newlist=re.findall(r'atcTitCell_tit SG_dot.+?href="(http://blog.sina.com.cn/s.+?)"',page_s,re.S)
               # newtitle=re.findall(r'atcTitCell_tit SG_dot.+?><.+?>(.+?)</a>',page_s,re.S)
                #for l in newtitle:
                 #   print(l)
                for k in newlist:
                    if k in urls:
                        pass
                    else:
                        urls.append(k)                                      
                if os.path.exists(path1):
                    driver.quit()
                    return '0'
                nums=driver.find_element_by_class_name("IL").find_elements_by_tag_name("span")
                content=driver.find_element_by_class_name("articalContent").text
                with open(folder+'/'+title+'.txt','w+') as f:
                    f.write("阅读：")
                    f.write(nums[0].text)
                    f.write('\n')
                    f.write("评论：")
                    f.write(nums[1].text)
                    f.write('\n')
                    f.write("收藏：")
                    f.write(nums[2].text)
                    f.write('\n')
                    if re.search(r"禁止转载",page_s):
                        f.write("禁止转载")
                        f.write('\n')
                    else:
                        data=driver.find_element_by_class_name("zznum").text
                        f.write("转载：")
                        f.write(data)
                        f.write('\n')
                    f.write(content)
            else:
                continue
        driver.quit()
        
def main():
    homepage='http://blog.sina.com.cn/'
    f_home=urllib.request.urlopen(homepage)
    content_home=f_home.read().decode('gbk')
    #content_home=content_home.decode('gb18030')
    f_home.close()
    urls=re.findall(r'"(http://blog.sina.com.cn/s/.+?\.html\?tj=1)"',content_home)
    #print(urls)
    for x in urls:
        f_0=urllib.request.urlopen(x)
        content_0=f_0.read().decode()
        f_0.close()
        if re.search(r'blogtitle.+?href="(.+?)"',content_0):
            listurl=get_listurl(x)
            path=folder
            print("f=",folder)
            if os.path.exists(path):
                get_blog(listurl)
            else:
                ff=os.makedirs(path)
                get_blog(listurl)
        else:
            continue

if __name__=="__main__":
    main()
