import threading
from queue import Queue
from spider import spider
from urlparsing import *
from crawler1 import *

PROJECT_NAME = 'Flipkart'
HOMEPAGE = 'https://www.flipkart.com'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
queue = Queue()
spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

    
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()

crawl()
