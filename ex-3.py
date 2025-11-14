def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Checking Mersenne numbers for prime p ≤ 100:\n")

for p in range(2, 101):
    if is_prime(p):
        m = (2**p) - 1
        if is_prime(m):
            print(f"Mersenne number for p = {p}: 2^{p} - 1 = {m} → PRIME")
        else:
            print(f"Mersenne number for p = {p}: 2^{p} - 1 = {m} → NOT PRIME")
