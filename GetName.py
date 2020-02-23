Previous_Urls = []
counter = [1]
def AddUrl_and_Get_Name(url):
    Previous_Urls.append(url)
    name = counter[0]
    counter[0] = counter[0] + 1
    return str(name)+".jpg"
