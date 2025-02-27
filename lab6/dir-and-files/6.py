import string
def alphabet(directory):
    for letter in string.ascii_uppercase:
        filename=f"{directory}/{letter}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"{letter}")
alphabet("lab6/dir-and-files")