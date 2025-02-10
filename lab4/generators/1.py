def generate_squares(N):
    for i in range(N + 1):
        yield i ** 2

# Example usage:
N = 5
for square in generate_squares(N):
    print(square)
