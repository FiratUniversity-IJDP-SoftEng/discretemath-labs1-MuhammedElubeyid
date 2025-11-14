def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the polynomial n^2 + n + 41
for n in range(0, 41):
    value = n*n + n + 41
    if is_prime(value):
        print(f"n={n:2d}, value={value} → PRIME")
    else:
        print(f"n={n:2d}, value={value} → NOT PRIME")

