import random

# Miller-Rabin primality test
def is_probable_prime(n, k=10):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2

    # Write n-1 = d * 2^s
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Generate a random 100-digit odd number
def random_100_digit_number():
    n = random.randint(10**99, 10**100 - 1)
    if n % 2 == 0:
        n += 1
    return n

# Generate a 100-digit prime
def random_100_digit_prime():
    while True:
        n = random_100_digit_number()
        if is_probable_prime(n):
            return n

# Generate and print 10 primes
primes = []
for i in range(10):
    p = random_100_digit_prime()
    primes.append(p)
    print(f"Prime {i+1}: {p}\n")

