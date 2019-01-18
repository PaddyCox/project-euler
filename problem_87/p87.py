def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

optimus_primes_2 = []

optimus_primes_3 = []

optimus_primes_4 = []

for i in range(2, int(50000000 ** 0.5) + 1):
    if is_prime(i):
        optimus_primes_2.append(i)
        if i ** 3 < 50000000:
            optimus_primes_3.append(i)
        if i ** 4 < 50000000:
            optimus_primes_4.append(i)




print(len(optimus_primes_2), len(optimus_primes_3), len(optimus_primes_4))

opt2 = tuple(x ** 2 for x in optimus_primes_2)

opt3 = tuple(x ** 3 for x in optimus_primes_3)

opt4 = tuple(x ** 4 for x in optimus_primes_4)


all_numbers = []

for n in opt2:
    for m in opt3:
        for o in opt4:
            to_add = n + m + o
            if to_add < 50000000:
                all_numbers.append(to_add)

set_solutions = set(all_numbers)

print(len(set_solutions))

#print(opt2, opt3, opt4)