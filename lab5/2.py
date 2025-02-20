import re

def text_match(text):
        patterns1 = 'abb.*'
        patterns2 = 'abbbb.*'
        if re.search(patterns1,  text) and not re.search(patterns2,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))
print(text_match("abbbc"))
print(text_match("abbbbc"))
print(text_match("abbbbbc"))