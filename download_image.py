from urllib.request import Request,urlopen
import requests
import Opener
import os
Path_name = "D:visualStudio\AFinalYearProject\AFinalYearProject\image"
def image_download(myList):
        os.chdir(Path_name)
        i = 1
        for url in myList:
            name = i
            image_file = open(str(name) + ".jpg","wb")
            req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
            image_file.write(urlopen(req).read())
            image_file.close()
            i = i+1