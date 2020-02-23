import Opener
import time
import connection as Project
from bs4 import BeautifulSoup
import download_image as imge
def BBCNews():
    # driver.get("https://www.bbc.com/news")
    # Html = driver.page_source
    OpenUrl =Opener.myUrlOpener()
    response = OpenUrl.open("https://www.bbc.com/news/")
    soup = BeautifulSoup(response,'html.parser')
    print(soup.prettify())
    """ tag_div = soup.find_all('div',{'class':'gs-o-media__body'})
    
    for div in tag_div:
        print(div.a.text)
        print("https://www.bbc.com"+div.a.get('href'))
     title_h2 = soup.find_all('h1',{'class':'mts-article-title'})
    # time.sleep(1)
    # driver.quit()
    for a_tag in title_h2:
        link = a_tag.a.get('href')
        text = a_tag.a.text
        print(text)
        print("https://www.bbc.com/news" + link)
        # Project.News(text,link,"BBC")"""
    seven_slice_div = soup.find_all('div',{'class':'gel-layout gel-layout--no-flex qa-seven-slice'})
    Seven_Slice(seven_slice_div)
    '''div_first = div.div
    div_first_image = div.div.find_next_sibling()
    print(div_first.a.text)
    print(div_first.a.get('href'))
    print(div_first.p.text)
    image_src = div_first_image.img.get('src')
    image_name = div_first_image.omg.get('alt')
    if image_name[:1] == "/":
        image_name = "https://www.bbc.com/news"+image_name
    else:
        img.image_download(image_src,image_name)
        image_src = image.get('src')

    print(image)
    print(image_src)
    image_name = image.get('alt')
    print(image_name)
    imagefile = open(image_name,"wb")
    imagefile.write(OpenUrl.open(image_src))
    imagefile.close()'''
def Seven_Slice(div_items):
    for item in div_items:
        siblings = item.find_all('div',{"class":"gel-layout__item"})
        for sibling in siblings:
            print(sibling)
            sibling_a_href = sibling.a.get('href')
            if sibling_a_href[:1] == "/":
                sibling_a_href = "https://www.bbc.com" + sibling_a_href
            print(sibling_a_href)

            # sibling_img_name = sibling.img.get('alt')