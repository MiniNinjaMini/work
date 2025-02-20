import re
def function(text):
    return re.sub('[ .,]', ':',text ,flags=re.IGNORECASE)
text1='there is a sentence, that we will check.'
print(function(text1))

