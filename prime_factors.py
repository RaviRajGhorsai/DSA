import math


def prime_factors(n: int) -> list[int]:
    prime_factor = []

    while n % 2 == 0:
        prime_factor.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n = n // i
            prime_factor.append(i)

    if n > 2:
        prime_factor.append(n)

    return prime_factor


print(prime_factors(33))
