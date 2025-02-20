import re
def upperCaser(letters):
        return letters.group(0)[1].upper()
def snakeToCamel(text):
        return re.sub(r'_[a-zA-Z]',upperCaser,text)
text1="do_you_like_a_snakes?"
print(text1)
print(snakeToCamel(text1))