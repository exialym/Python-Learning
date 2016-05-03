# These are the xpaths we determined from snooping 
next_button_xpath = "//a[@id='key_nextpage']/@href"
headline_xpath = "//div[@class='picbox']/dl/dt/a/text()"

# We'll use sleep to add some time in between requests
# so that we're not bombarding Gawker's server too hard. 
from time import sleep
from lxml import html
# Now we'll fill this list of gawker titles by starting
# at the landing page and following "More Stories" links
titles = []
base_url = 'http://www.mtime.com/hotest/{}'
next_page = "http://www.mtime.com/hotest/"
while len(titles) < 50 and next_page:
    dom = html.parse(next_page)
    headlines = dom.xpath(headline_xpath)
    print "Retrieved {} titles from url: {}".format(len(headlines), next_page)
    titles += headlines
    next_pages = dom.xpath(next_button_xpath)
    if next_pages: 
        next_page = base_url.format(next_pages[0]) 
    else:
        print "No next button found"
        next_page = None
    sleep(3)
with open('mtime_titles.txt', 'wb') as out:
    out.write('\n'.join(titles).encode('utf-8'))
with open('mtime_titles.txt') as f:
    titles_ = f.readlines()
    
print "Well, we got {} Hot Movies!".format(len(titles_))
for title in titles_:
    print title
