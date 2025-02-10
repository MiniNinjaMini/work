def generate_evens(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i

N = int(input("Enter a number: "))

even_numbers = ', '.join(str(num) for num in generate_evens(N))
print("Even numbers:", even_numbers)
