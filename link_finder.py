import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
from tabulate import tabulate

from time import sleep
from time import time
from random import randint

def getpage(url):
    try:
        page = urlopen(url)
    except HTTPError as e:
        return None
    except ValueError as e:
        return None        
    
    return page
    
baseUrl = "https://en.wikipedia.org/"
page = getpage("https://en.wikipedia.org/wiki/Burbank,_California")
html = page.read()

bsObj= bs(html , "lxml")
tags = bsObj.select("a")

for tag in tags:
    if 'href' in tag.attrs:
        url = urljoin(baseUrl , tag['href'])
        print(url)
        
        
        
        
        
        
    

