def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = 10
for number in countdown(n):
    print(number)
