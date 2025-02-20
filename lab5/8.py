import re
def splitString(text):
    v1=re.split(r'([A-Z])', text)
    v2=["".join(v1[i:i+2]) for i in range(1, len(v1), 2)]
    return v2
text1="DoYouKnowTheWay?"
print(text1)
print(splitString(text1))