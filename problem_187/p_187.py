import useful_functions

number_semi_primes = 0

max_n = (10**8)

primes_to_choose = useful_functions.rwh_primes(max_n//2)

primes_to_choose.append(10**9)

max_i = max_n//2

i = 0

i_prime = primes_to_choose[i]

while i_prime < max_i:
    max_j = max_n // i_prime
    j = i
    j_prime = primes_to_choose[j]
    while j_prime <= max_j:
        number_semi_primes += 1
        j += 1
        j_prime = primes_to_choose[j]
    i += 1
    i_prime = primes_to_choose[i]

print(i, j)
print(len(primes_to_choose))
print(number_semi_primes)