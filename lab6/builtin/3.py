def is_palindrome(s):
    return s == s[::-1]  


# testo
text = "madam"
if is_palindrome(text):
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')