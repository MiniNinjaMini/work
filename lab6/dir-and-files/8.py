import os
def deleter(path1):
    if os.path.exists(path1):
        if os.access(path1,os.W_OK):
             os.remove(path1)
        else:
            print("Access denied")
    else:
        print("The file doesn't exist")
 
 #testo
deleter("lab6/dir-and-files/test2.txt")
