import os            #This program generates a file which alphabetically sorts the authors and all their books, run this
import csv           #before testing the corpora. WARNING, this will generate the file in the same folder as program


path = '/home/macaire/Bureau/test/' #ONLY thing for you to do is specify the path where the books you want to use are

def  loadbooks(path,completlist,lister):       #Loads all the books from a specified path and extracts name and author
    keeper=''
    templist=[]

    for f in os.walk(path):
          if __name__ == "__main__":
                for name in os.listdir(path):
                    templist.append(name)
    templist.sort()

    for name in templist:
        sameauth=False
        x = name.rfind("_") #Find the _that splits the author and title
        y = name.find("_")
        author=(name[y+1:x])
        if author==keeper: 
            sameauth=True
            
        keeper=author
        z=(len(name))
        booktitle=(name[x+1:z])
        if sameauth==False:
            lister.append(author)
            completlist.append(author)
            
        lister.append(booktitle)

def assignwrite(completlist,lister):          #Finds each author and marks them, then saves them to a file
    for x in range(0,len(completlist)):        #author list
        for val1 in range(0,len(lister)):       #complete list   
            if completlist[x]==lister[val1]:
                lister[val1]='$A' + lister[val1]

    with open('Profile list', 'w') as f:
        for x in range(0,len(lister)):
            f.write(lister[x]+'\n')
        


def Makefile(path):              #Extract the names and based on them make a file
    completlist=[]
    lister=[]
    loadbooks(path,completlist,lister)
    completlist = list(dict.fromkeys(completlist))     #clear duplicates
    assignwrite(completlist,lister)
    
Makefile(path)
    
