import os
def check_path(doroga):
    if os.path.exists(doroga):
        print(f"directory portion:{os.path.dirname(doroga)}")
        print(f"filename portion:{os.path.basename(doroga)}")
    else:
        print("directory does't exist")
check_path("lab6/dir-and-files/1.py")