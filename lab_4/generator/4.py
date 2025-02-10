def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Starting number: "))
b = int(input("Ending number: "))
for square in squares(a, b):
    print(square, end=" ")
