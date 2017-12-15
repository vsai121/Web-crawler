import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
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


page = getpage("https://en.wikipedia.org/wiki/Federal_Communications_Commission")
html = page.read()

bsObj= bs(html , "lxml")
links = bsObj.select("a")

for link in links:
    if 'href' in link.attrs:
        print(link['href'])
        print("\n")
        
        
    

