def recursive_prime_factors(n):
    p_factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            p_factors.append(i)
            p_factors += recursive_prime_factors(n // i)
            break
    if len(p_factors) == 0:
        p_factors.append(n)
    return p_factors


for n_b in range(1, 1000000):
    n = 2 * (n_b**2 - n_b)
    T = ((n + 0.25) ** 0.5) + 0.5
    if T % 1 == 0:
        print(int(T), n_b, int(T - n_b), 2 * (n_b**2 - n_b))
        print(recursive_prime_factors(int(T)), recursive_prime_factors(n_b), recursive_prime_factors(int(T - n_b)), recursive_prime_factors(2 * (n_b ** 2 - n_b)))
