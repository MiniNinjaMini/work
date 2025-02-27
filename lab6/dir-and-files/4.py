import os
def count_lines(filename):
        with open(filename, "r", encoding="utf-8") as file:
                return sum(1 for line in file)
print(count_lines("lab6/dir-and-files/test.txt"))
