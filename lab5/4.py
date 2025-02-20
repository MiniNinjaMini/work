import re 
def text_match(text):
        patterns = '^[A-Z]{1}+[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aabcbbbc"))
print(text_match("aabAbbbc"))
print(text_match("Aaab"))