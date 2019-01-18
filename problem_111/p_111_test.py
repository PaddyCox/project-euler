import itertools
import time
import timeit
from useful_functions import primesfrom2to

time_0 = time.time()

all_primes = primesfrom2to(1000000)

def prime_check(n):
    max_i = int(n**0.5)
    for i in all_primes:
        if i > max_i:
            break
        if n % i == 0:
            return False
    return True

t_1 = time.time()

def repeat_digit_num_generator(num_digits, repeated_digit):
    solution_list = []
    all_digits = set([i for i in range(0, 10)])
    non_repeated_digits = list(all_digits - set([repeated_digit]))
    digit_position = [j for j in range(0, num_digits)]
    num_non_repeated_digits = 1

    while len(solution_list) == 0:
        insert_digits = itertools.product(non_repeated_digits, repeat=num_non_repeated_digits)
        for i_d in insert_digits:
            digit_position_i = itertools.combinations(digit_position, num_non_repeated_digits)
            for d_p in digit_position_i:
                prime_i = [repeated_digit] * num_digits
                zipped_digits = zip(i_d, d_p)
                for z in zipped_digits:
                    prime_i[z[1]] = z[0]
                prime_j = int(''.join(map(str, prime_i)))
                if len(str(prime_j)) == num_digits:
                    if prime_check(prime_j):
                        solution_list.append(prime_j)
        num_non_repeated_digits += 1
    return solution_list

total = 0

t_2 = time.time()

for i in range(0, 10):
    sol_i = repeat_digit_num_generator(10, i)
    t_3 = time.time()
    sub_total = sum(sol_i)
    print(t_3 - t_2, sub_total, sol_i)
    t_2 = t_3
    total += sum(sol_i)


print(total)