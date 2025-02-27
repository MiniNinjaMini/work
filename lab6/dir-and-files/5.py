import json
def writer(filename, data_list):
    with open(filename, "w", encoding="utf-8") as file:
        for item in data_list:
            file.write(str(item) + '\n')
  

#testo
data = ["apple","juice"]
writer("lab6/dir-and-files/test.txt", data)

