def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime():
    numbers = list(map(int, input().split()))
    primes = [num for num in numbers if is_prime(num)]
    print(primes)

filter_prime()
