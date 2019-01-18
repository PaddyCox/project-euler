from useful_functions import rwh_primes
from useful_functions import primesfrom2to
import inspect
import time
import collections


t_1 = time.time()

all_primes = primesfrom2to(1000000)

t_2 = time.time()

def prime_check(n):
    max_i = int(n**0.5)
    for i in all_primes:
        if i > max_i:
            break
        if n % i == 0:
            return False
    return True

max_repeat_digit = [0 for x_0 in range(1, 11)]
repeat_digit_primes = [list() for x_1 in range(1, 11)]

for p in range(10**6 + 1, 10**7, 2):
    string_p = str(p)
    length_num = len(string_p)

    if len(set(list(string_p))) == 1:
        continue

    most_common_two = collections.Counter(string_p).most_common(2)

    d_1, c_1 = int(most_common_two[0][0]), most_common_two[0][1]
    if length_num - len(str(d_1)) >= (length_num // 2):
        d_2, c_2 = int(most_common_two[1][0]), most_common_two[1][1]

    if max_repeat_digit[d_1] < c_1:
        prime_boolean =  prime_check(p)
        if prime_boolean:
            max_repeat_digit[d_1] = c_1
            repeat_digit_primes[d_1] = [p]

    elif max_repeat_digit[d_1] == c_1:
        prime_boolean = prime_check(p)
        if prime_boolean:
            repeat_digit_primes[d_1].append(p)

    if max_repeat_digit[d_2] < c_2:
        prime_boolean = prime_check(p)
        if prime_boolean:
            max_repeat_digit[d_2] = c_2
            repeat_digit_primes[d_2] = [p]

    elif max_repeat_digit[d_2] == c_2:
        prime_boolean = prime_check(p)
        if prime_boolean:
            repeat_digit_primes[d_2].append(p)

total = 0

for i, list_p in enumerate(repeat_digit_primes):
    sub_total =  sum(list_p)
    total += sub_total
    print(i, sub_total)

t_3 = time.time()

print(repeat_digit_primes[1:][0])
print(total)
print(t_3 - t_1, t_2 - t_1)