def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
arr = []

for num in countdown(n):
    arr.append(num)

print(arr)