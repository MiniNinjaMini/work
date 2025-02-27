import os
def dlist(path):
    dir_list=os.listdir(path)
    print(f"Files and directories in {path} :")
    print(dir_list)
dlist("lab6")