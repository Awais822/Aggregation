from requests_html import HTMLSession
from bs4 import BeautifulSoup
'''session = HTMLSession()
urlToAccess = 'https://support.foxtrotalliance.com/hc/en-us'
htmlPage = session.get(urlToAccess)
soup = BeautifulSoup(htmlPage,'html.parser')
print(soup.prettify())
htmlPage.close()
session.close()
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())
print(soup.title)
paraWithClassStory = soup.findAll("p",{"class":"story"})
print(paraWithClassStory.a)'''

# Using AsynchHtmlSession() for grabbing data from more websites at a time

'''ASession = AsyncHTMLSession()

async def getGoogle():
    r = await ASession.get('https://google.com/')
    print(r.html.links)
async def getReddit():
    r = await ASession.get('https://reddit.com/')
async def getPython():
    r = await ASession.get('https://python.org/')

print(ASession.run(getPython,getGoogle,getReddit))

session = HTMLSession()
def getPython():
       htmlPage = session.get('https://python.org/')
       # print(htmlPage.html.absolute_links)
       about = htmlPage.html.find('#about',first=True)
       soup = BeautifulSoup(about.html ,'html.parser')
       print(soup.prettify())
session = HTMLSession()
def getSupportFoxTrot():
    PageToStore = session.get('https://support.foxtrotalliance.com/hc/en-us')
    PageHtmlDataOfSpecifiedTag = PageToStore.html.find('body',first=True)
    soup = BeautifulSoup(PageHtmlDataOfSpecifiedTag.html,'html.parser')
    print(soup.find('h1',{'class':'welcome_text'}).text)
    container = soup.find('ul',{'class':'blocks-list'})

getSupportFoxTrot()'''
session = HTMLSession()
url = 'https://support.foxtrotalliance.com/hc/en-us'
Page = session.get(url)
Page.close()
session.close()



