import Opener
import connection as Project
import GetName as In
from bs4 import BeautifulSoup
def AryNews():
    OpenUrl =Opener.myUrlOpener()
    HtmlPage =OpenUrl.open("https://arynews.tv/en/category/pakistan/")
    # driver.get("https://arynews.tv/en/")
    # Html = driver.page_source
    soup = BeautifulSoup(HtmlPage,'html.parser')
    section_tag = soup.find('div',{"class":"listing listing-blog listing-blog-1 clearfix columns-1"})
    article_tag = section_tag.find_all('article')
    for index in range(0,10):
        article_link = article_tag[index].h2.a.get('href')
        response = OpenUrl.open(article_link)
        soup1 = BeautifulSoup(response,'html.parser')
        next_link_div = soup1.find('div',{"class":"post-header post-tp-1-header"})
        next_link_div_img_src = next_link_div.img.get('data-src')
        if next_link_div_img_src is not None:
            next_link_div_h1 = next_link_div.h1.text
            description_div = soup1.find('div',{"class":"entry-content clearfix single-post-content"})
            description_text = description_div.p.text
            img_name = In.AddUrl_and_Get_Name(next_link_div_img_src)
            print(article_link)
            print(next_link_div_h1)
            print(next_link_div_img_src)
            print(description_text)
            Project.News(next_link_div_h1,description_text,article_link,img_name,"ARY")