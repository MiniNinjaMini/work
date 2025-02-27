import time
import math

def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000)  # milliseconds to seconds
    return math.sqrt(number)

# testo 
num = 25
delay = 2000  # 2000 milliseconds (2 seconds)

print(f"Calculating square root of {num} after {delay} milliseconds...")
result = delayed_sqrt(num, delay)
print(f"Square root of {num} is {result}")