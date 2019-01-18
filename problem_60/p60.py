import time


def is_prime(n):

    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    else:
        return True

t_1 = time.time()

primes_large = [x for x in range(30000) if is_prime(x)]

print("Time taken to process primes under 10^6:", str(time.time() - t_1)[0:5] + 's')

set_primes = set(primes_large)


def b_t_f_2(j, a_list_2):

    # j: a prime number
    # a_list_2: a list of primes

    for n in a_list_2:
        c_1 = int(str(n) + str(j))
        c_2 = int(str(j) + str(n))
        if c_1 not in set_primes or c_2 not in set_primes:
            print(c_1, c_2)
            return False

    return True

def my_funk(p, l_p):

    for n in l_p:
        c_1 = int(str(n) + str(p))
        c_2 = int(str(p) + str(n))

        if not is_prime(c_1) or not is_prime(c_2):
            return l_p

    return l_p + [p]


t_2 = time.time()

print(b_t_f_2(7, [109, 3, 673]))

print("Time taken to run solution:", time.time() - t_2)

print(my_funk(7, [109, 3, 673]))

"""for a in range(1, 100):
    list_p = [primes_large[a]]
    current_length = 1
    for b in range(a+3, len(primes_large)):
        b_p = primes_large[b]
        check = my_funk(b_p, list_p)
        if len(check) > current_length:
            current_length += 1
            list_p.append(b_p)
            if current_length > 2:
                print(list_p)"""

"""for a_2 in range(1, 100):
    list_p = [primes_large[a_2]]
    current_length = 1
    for b in range(len(primes_large)-1, a_2, -1):
        b_p = primes_large[b]
        check = my_funk(b_p, list_p)
        if len(check) > current_length:
            current_length += 1
            list_p.append(b_p)
            print(list_p)"""

for a in range(1, 100):
    current_length = 1
    for c in range(a, 1000):
        list_p = [primes_large[a]]
        v_1 = int(str(primes_large[a]) + str(primes_large[c]))
        v_2 = int(str(primes_large[c]) + str(primes_large[a]))
        if is_prime(v_1) and is_prime(v_2):
            list_p = [primes_large[a], primes_large[c]]
            for b in range(c, len(primes_large)):
                b_p = primes_large[b]
                check_1 = my_funk(4, list_p)
                check_2 = my_funk(b_p, list_p)
                if len(check_2) > len(check_1):
                    list_p.append(b_p)
                    if len(list_p) > 3:
                        print(list_p, a, c, b)
