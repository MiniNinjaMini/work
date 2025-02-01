# 1. Convert grams to ounces
def grams_to_ounces(grams):
    return grams * 28.3495231

# 2. Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# 3. Chicken and Rabbit Puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None

# 4. Filter Prime Numbers
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

# 5. String Permutations
from itertools import permutations
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

# 6. Reverse Sentence
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

# 7. Check for 3 next to 3
def has_33(nums):
    return any(nums[i] == 3 and nums[i + 1] == 3 for i in range(len(nums) - 1))

import random

# 8. Function to check if the list contains 0, 0, 7 in order
def spy_game(nums):
    code = [0, 0, 7]
    code_index = 0
    for num in nums:
        if num == code[code_index]:
            code_index += 1
        if code_index == len(code):
            return True
    return False

# 9. Function to compute the volume of a sphere
def volume(radius):
    pi = 3.141592653589793
    return (4/3) * pi * (radius ** 3)

# 10. Function to return unique elements from a list
def uniq(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# 11. Function to check if a word or phrase is a palindrome
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

# 12. Function to print a histogram
def histogram(lst):
    for num in lst:
        print('*' * num)

# 13. Guess the number game
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    number_to_guess = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break


# 14.Example usages
print(grams_to_ounces(100))
print(fahrenheit_to_celsius(98.6))
print(solve(35, 94))
print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(string_permutations("abc"))
print(reverse_sentence("We are ready"))
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print(spy_game([1,2,4,0,0,7,5]))  # True
print(spy_game([1,0,2,4,0,5,7]))  # True
print(spy_game([1,7,2,0,4,5,0]))  # False
print(volume(3))  # 113.097....
print(uniq([1,2,2,3,4,4,5]))  # [1, 2, 3, 4, 5]
print(is_palindrome("roaddaor"))  # true
print(is_palindrome("a some words"))  # false
histogram([4, 9, 7])

#guess_the_number()