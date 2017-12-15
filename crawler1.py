import os



def create_project_directory(directory):
    if not os.path.exists(directory):
        print('Creating Project ' + directory)
        os.makedirs(directory)

def write_file(filename , data):
    f = open(filename , 'w')
    f.write(data)
    f.close()

def create_datafiles(directory , url):
    queue = directory + "/queue" +".txt"  #List of links waiting to be crawled
    crawled = directory + "/crawled" + ".txt"
    
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
    

def file_to_set(filename):
    result = set()
    f = open(filename , 'rt')
    
    for line in f:
        result.add(line.replace('\n' ,'')) #Removing newline from url

    return result
    
def set_to_file(result , filename):
    del_file(filename)
    for link in result:
        append_to_file(filename , link)
        
        
        
                 
           
        
          
        
             
        
        
