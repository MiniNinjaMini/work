def copypaste(path1,path2):
    with open(path1, "r", encoding="utf-8") as file1:
            with open(path2, "w", encoding="utf-8") as file2:
                  for line in file1:
                    file2.write(line)
copypaste("lab6/dir-and-files/test.txt","lab6/dir-and-files/test2.txt")

