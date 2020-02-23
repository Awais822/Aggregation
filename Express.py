import Opener
import connection as Project
import time
import GetName as In
from bs4 import BeautifulSoup
Express_Urls = []
def ScrapExpressTribune():

    OpenUrl =Opener.myUrlOpener()
    HtmlPage =OpenUrl.open("https://tribune.com.pk")

    '''driver.get("https://tribune.com.pk")
    time.sleep(2)
    Html = driver.page_source'''
    soup = BeautifulSoup(HtmlPage,'html.parser')
    LinkCollector(soup)
    SubCategoryCollector()
    '''top_stories = soup.find('div',{'class':'span-8 mobile-top-news-section'})
    stories = top_stories.find_all('div',{"class":"story"})
   # driver.quit()
    for story in stories:
        story_link = story.a.get('href')
        story_heading = story.a.text
        story_img_src = story.img.get('src')
        #story_img_name = In.AddUrl_and_Get_Name(story_img_src)
        story_text = story.find('p',{"class":"excerpt"})
        story_text_disc = story_text.text
        print(story_link)
        print(story_heading)
        print(story_img_src)
        #print(story_img_name)
        print(story_text_disc.strip())
        
        # Project.News(story_heading,story_text_disc.strip(),story_link,story_img_name,"Tribune")'''
def LinkCollector(webPage):
    Urls_of_Express_subcategory =webPage.find('ul',{'id':'sub-menu','class':"home subcategory"})
    Urls_of_Express_subcategory_link = Urls_of_Express_subcategory.find_all('a')
    for x in Urls_of_Express_subcategory_link:
        Express_Urls.append(x.get('href'))
def SubCategoryCollector():
    OpenUrl = Opener.myUrlOpener()
    for x in Express_Urls:
        response = OpenUrl.open(x)
        webpage = BeautifulSoup(response,'html.parser')
        Trending_stories = webpage.find('div',{'class':'primary'})
        if Trending_stories is not None:
            div_p = Trending_stories.find_all("div",{"class":"story"})
            for x in div_p:
                print(x)
                if x is not None:
                    div_h1_text = x.find('h2').text
                    div_p_text = x.find('p',{'class':'excerpt'})
                    print(div_h1_text)
                    print(div_p_text)