import Opener
import connection as Project
import GetName as In
from bs4 import BeautifulSoup
Previous_Url = []
def AlJazeeraNews():
    OpenUrl = Opener.myUrlOpener()
    response = OpenUrl.open("https://www.aljazeera.com")
    soup = BeautifulSoup(response,'html.parser')
    editorPicks = soup.find('div',{'class':'editors-picks-wrapper'})
    moreTopStories = soup.find('section',{'id':'more-top-stories'})
    # EditorPicsMethod(editorPicks)
    MoreTopStoriesFunction(moreTopStories)
    # d_img.image_download(Previous_Url)
    '''title_h2 = soup.find_all('h1',{'class':'mts-article-title'})
    # time.sleep(1)
    # driver.quit()
    for a_tag in title_h2:
        link = a_tag.a.get('href')
        text = a_tag.a.text
        print(text)
        Link = "https://www.aljazeera.com" + link
        print(Link)
        GetLinkValue(Link)
        Project.News(text,link,"Aljazeera News")
def GetLinkValue(LinkPageDate):
    OpenUrl =Opener.myUrlOpener()
    response = OpenUrl.open(LinkPageDate)
    soup = BeautifulSoup(response,'html.parser')
    print(soup.prettify())'''

def EditorPicsMethod(link):
    '''div = editorPics.find('div',{'class':'cards-wrap'})
    div_child = div.find_all('div',{'class':'ep4-default-card'})
    for element in div_child:
        div_thumbnail = element.find('div',{'class':'ep4-thumbnail'})'''

def MoreTopStoriesFunction(moretopstories):
    '''story_articles = moretopstories.find_all('article')
    for index in range(0,1):#Replace range with story articles
        story_link =story_articles[index].a.get('href')'''
    story_articles = moretopstories.find_all('article')
    for x in story_articles:
        story_link = story_articles[x].a.get('href')
    OpenUrl1 = Opener.myUrlOpener()
    response = OpenUrl1.open(moretopstories) #"https://www.aljazeera.com" + story_link
    soup = BeautifulSoup(response,'html.parser')
    heading = soup.find('div',{"class":"topics-sec-block"})
    article_section = heading.find_all('div',{"class":"row topics-sec-item default-style"})
    print(article_section)
    print(len(article_section))
    for article in range(0,10):
        div_p = article_section[article].find('div',{"class":"col-sm-7 topics-sec-item-cont"})
        p = div_p.find('p',{"class":"topics-sec-item-p"})
        h2 =div_p.find('h2')
        h2_text = h2.text
        p_text = p.text
        print(p_text)
        print(h2_text)
        div_img = article_section[article].find('div',{"class":"col-sm-5 topics-sec-item-img"})
        div_img_a_src = div_img.a.get('href')
        article_link ="https://www.aljazeera.com" + div_img_a_src
        response1 = OpenUrl1.open(article_link)
        soup1 = BeautifulSoup(response1, 'html.parser')
        image = soup1.find('img', {'class': 'main-article-media-img'})
        if image is not None:
            heading = soup1.find('div', {'class': 'article-heading'})
            heading_text = heading.p.text
            heading_disc = heading.h1.text
            image_link = "https://www.aljazeera.com" + image.get('src')
            img_name = In.AddUrl_and_Get_Name(image_link)
            print(image_link)
            print(heading_disc)
            print(heading_text)
            print(img_name)
            # Project.News(heading_text,heading_disc,article_link,img_name,"Aljazeera")

        '''
        image = soup.find('img',{'class':'main-article-media-img'})
        heading_text = heading.p.text
        heading_disc = heading.h1.text
        image_link = "https://www.aljazeera.com" + image.get('src')
        Previous_Url.append(image_link)
        print(image_link)'''
