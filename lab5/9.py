import re
def splitter(match):
    return match.group(0)[0]+' '+match.group(0)[1]
def splitString(text):
    return re.sub(r'[a-z][A-Z]',splitter,text)
text1="DoYouKnowTheWay?"
print(text1)
print(splitString(text1))