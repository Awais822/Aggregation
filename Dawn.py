import Opener
import connection as Project
from bs4 import BeautifulSoup
import GetName as In
def DawnNews():
    # driver.get("https://www.dawn.com")
    # Html = driver.page_source

    OpenUrl =Opener.myUrlOpener()
    response =OpenUrl.open("https://www.dawn.com")
    soup = BeautifulSoup(response,'html.parser')
    top_stories = soup.find('div',{"class":"mb-4 pr-0 sm-pr-2 sm-border-r sm-border-r-solid sm-border-r-grey-lighter"})
    articles = top_stories.find_all('article')
    print(len(articles))
    # driver.quit()
    for article in articles:
        article_link = article.h2.a.get('href')
        article_heading = article.h2.a.text
        article_img_src = article.figure.img.get('src')
        article_div_text = article.find('div',{'class':'story__excerpt'})
        article_div_description = article_div_text.text
        print(article_heading)
        print(article_link)
        print(article_img_src)
        article_img_name = In.AddUrl_and_Get_Name(article_img_src)
        print(article_div_text.text)
        Project.News(article_heading,article_div_description,article_link,article_img_name,"DAWN")