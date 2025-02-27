import os
def check_path_access(doroga):
    print(f"checking access for:{doroga}")
    print(f"exists:{os.path.exists(doroga)}")
    print(f"readable:{os.access(doroga,os.R_OK)}")
    print(f"writable:{os.access(doroga,os.W_OK)}")
    print(f"executable:{os.access(doroga,os.X_OK)}")
check_path_access("lab6")
