from useful_functions import rwh_primes

primes_to_check = rwh_primes(300000)

print(primes_to_check)

print(len(primes_to_check))

p_test = primes_to_check[7036]

def check_123(n):
    p_n = primes_to_check[n - 1]
    multiple = (p_n + 1)**n + (p_n - 1)**n
    r = multiple % (p_n**2)
    # print(n, p_n, r, p_n**2, multiple)
    return r

print(p_test, ((p_test + 1)**7037 + (p_test - 1)**7037)%(p_test**2))

print(check_123(7037))

n_max = 0

for n in range(20999, 22000):
    r_n = check_123(n)
    if r_n > n_max:
        n_max = r_n
        print(n, r_n)