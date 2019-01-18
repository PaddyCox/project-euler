import collections
import numpy as np

def primesfrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)//3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def flatten(l):
    # requires collections
    # potentially tripped up by strings
    output = []
    for el in l:
        if isinstance(el, collections.Iterable):
            for sub in flatten(el):
                output.append(sub)
        else:
            output.append(el)
    return output


def find_factors(n):
    # requires is_prime(n)
    output = []
    for i1 in range(2, int(n**0.5+1)):
        i2 = n/i1
        if i2 == int(i2):
            output.append(i1)
            output.append(i2)

def num_divisors(n):
    """Return number of divisors of integer 'n' based on prime of factors of n"""
    set_pf = set(n)
    n_div = 1
    for pf in set_pf:
        x = n.count(pf)
        n_div *= (1 + x)
    return n_div


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


def find_p_factors(n):
    # requires is_prime(), flatten()
    output = []
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            j = int(n/i)
            output.append(i)
            output.append(j)
            break
    for f in output:
        if is_prime(f) is False:
            output.remove(f)
            pf = find_p_factors(f)
            output += pf
    if is_prime(n) is True:
        output.append(n)
    return flatten(output)


def find_p_factors_ii(n):
    """Returns prime factors of n"""
    n_copy = n
    p_factors = []
    count = 2
    while count < (int(n_copy**0.5) + 1):
        if n_copy % count == 0:
            p_factors.append(count)
            n_copy = n_copy // count
            count = 2
            if n_copy == 1:
                break
        else:
            count += 1
    p_factors.append(n_copy)

    return p_factors
