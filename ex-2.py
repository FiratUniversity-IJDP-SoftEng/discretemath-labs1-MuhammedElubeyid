def list_primes_upto(N):
    primes = []
    for num in range(2, N + 1):
        if is_prime(num):
            primes.append(num)
    return primes
print(list_primes_upto(50))
