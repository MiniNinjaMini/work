import re 
def text_match(text):
        patterns = 'a.*b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aabcbbbc"))
print(text_match("aabAbbbc"))
print(text_match("aab"))
print(text_match("aabAbbbb"))
print(text_match("daaaaaaaaaaaaaaaAAAABbab"))

