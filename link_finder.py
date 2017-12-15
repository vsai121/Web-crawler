from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs


def getpage(url):
    try:
        page = urlopen(url)
    except HTTPError as e:
        return None
    except ValueError as e:
        return None        
    
    return page
    
def getLinks(bsObj , baseUrl):
    tags = bsObj.select("a")
    links = set()
    for tag in tags:
        if 'href' in tag.attrs:
            url = urljoin(baseUrl , tag['href'])
            #print(url)
            links.add(url)

    return links 
            
            
    

#print(links)

        
        
        
        
        
    

