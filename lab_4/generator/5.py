def generate_squares(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input())
for square in generate_squares(n):
    print(square, end=" ")
