from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
from link_finder import getpage
from link_finder import getLinks
from crawler1 import *

class spider:

    #Staic variables type
    directory = ""
    baseUrl = ""
    domainName = ""
    queueFile =""
    crawledFile =""
    queue = set()
    crawled = set()
    
    def __init__(self , directory , baseUrl , domainName=""):
    
        spider.directory = directory
        spider.baseUrl = baseUrl
        spider.domainName = domainName
        spider.queueFile = directory + '/' +  'queue.txt'
        spider.crawledFile = directory + '/' + 'crawled.txt'
        
        self.boot()  # to initialise directory , queue files and crawled files for spiders
        self.crawl('First spider' , spider.baseUrl)
        

    def boot(self):
        create_project_directory(spider.directory)
        create_datafiles(spider.directory , spider.baseUrl)
        spider.queue = file_to_set(spider.queueFile)
        spider.crawled = file_to_set(spider.crawledFile)
        

    def crawl(self ,thread_name , url):
        if url not in spider.crawled:
            print(thread_name + " now crawling "  + url)
            print(str(len(spider.queue)) + "links waiting to be crawled")
            print(str(len(spider.crawled)) + "links have been crawled")
            
            links = spider.gatherlinks(url , spider.baseUrl)
            if links== None:
                print("No links in current url" + url)
                
                
                
            spider.add_to_queue(links)
            spider.queue.remove(url)
            spider.crawled.add(url)
            
            spider.update_files()
            
   

    def gatherlinks(url , baseUrl):
        page = getpage(url)
        if not page==None:
            html = page.read()
        
            if not html==None:
                bsObj = bs(html , "lxml")
                links = getLinks(bsObj , baseUrl)
            
                return links
            return None                
            
        return None
        
    def add_to_queue(links): 
        if not links==None:
            for link in links:
            
                if link in spider.queue:
                    continue
                    
                if link in spider.crawled:
                    continue
                    
                if spider.domainName not in link:
                    continue    
                    
                spider.queue.add(link)   
            
    def update_files():
        set_to_file(spider.queue , spider.queueFile)
        set_to_file(spider.crawled , spider.crawledFile)
                                                                               
                        
"""if __name__ == "__main__":
    
    spider1 = spider('crawlers' , "https://en.wikipedia.org")"""
    
