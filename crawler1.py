import os
import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
from tabulate import tabulate

from time import sleep
from time import time
from random import randint


def create_project_directory(directory):
    if not os.path.exists(directory):
        print('Creating Project ' + directory)
        os.makedirs(directory)

def write_file(filename , data):
    f = open(filename , 'w')
    f.write(data)
    f.close()

def create_datafiles(directory , url):
    queue = directory + "/queue" + url +  ".txt"  #List of links waiting to be crawled
    crawled = directory + "/crawled" + url + ".txt"
    
    if not os.path.isfile(queue):
        write_file(queue , url)
        
    if not os.path.isfile(crawled):
        write_file(crawled , "") 

def append_to_file(filename , data):
    f = open(filename , 'a')
    f.write(data + "\n")
    f.close()      
    
def del_file(filename):
    f = open(filename , 'w')
    
        
        
          
        
             
        
        
