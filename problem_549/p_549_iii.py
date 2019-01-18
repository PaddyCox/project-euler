import psutil
import math
import sys
import inspect
from useful_functions import rwh_primes
from operator import itemgetter
import time

max_p = 10**5

def min_m(p, e):
    """Return min integer m for which m!%(p**e) == 0 """
    guess_m = e * (p - 1)
    a_max = max(int(math.log(guess_m, p)), 1)
    list_0 = [p**i for i in range(a_max, -1, -1)]
    list_1 = [sum(list_0[i:]) for i in range(a_max + 1)]
    m = 0
    total = 0
    remain = e
    x = 0
    while total < e:
        total += (remain//list_1[x]) * list_1[x]
        m += (remain//list_1[x]) * p**(a_max + 1 - x)
        remain = max(e - total, 0)
        if remain > (p - 1) * sum(list_1[x + 1:]):
            total += list_1[x]
            m += p**(a_max + 1 - x)
        x += 1
    return m, total

def min_m_ii(p, e):
    """Return min integer m for which m!%(p**e) == 0 """
    z = e
    a = 0
    while z > 0:
        a += p
        x = a
        while x % p == 0:
            x //= p
            z -= 1
    return a, "Nada"

def min_m_iii(p, e):
    """Return min integer m for which m!%(p**e) == 0 """
    g_0 = math.log(p**e, p)



class recursive_multiplier_ii:
    def __init__(self, p_max):
        self.max = p_max
        self.solutions = {}
        self.mp_exp = {'2_1': 2}
        self.primes_n = rwh_primes(p_max)
        self.l = len(self.primes_n)

    def recur(self, i, j, factors_i, m_i, p_i):
        count_j = factors_i.count(j)
        key_j = str(j) + '_' + str(count_j)
        if key_j in self.mp_exp:
            check_m = self.mp_exp[key_j]
        else:
            check_m = min_m(j, count_j)[0]
            self.mp_exp[key_j] = check_m
        new_m = max(m_i, check_m)
        self.solutions[i] = new_m
        for z in range(p_i, self.l):
            p_z = self.primes_n[z]
            new_i = i * p_z
            if new_i > self.max:
                return
            else:
                self.recur(i * p_z, p_z, factors_i + [p_z], new_m, z)

    def start_recur(self):
        t_0 = time.time()
        for e, p in enumerate(self.primes_n):
            if p > self.max:
                break
            else:
                self.recur(p, p, [p], p, e)
        print("Time taken for {} recur is {}".format('ii', time.time() - t_0))
        return self.solutions, self.mp_exp


class recursive_multiplier_iii:
    def __init__(self, p_max):
        self.name = str(self)
        self.max = p_max
        self.solutions = {}
        self.mp_exp = {'2_1': 2}
        self.primes_n = rwh_primes(p_max)
        self.l = len(self.primes_n)

    def recur(self, i, j, count_j, m_i, p_i):
        key_j = str(j) + '_' + str(count_j)
        if key_j in self.mp_exp:
            check_m = self.mp_exp[key_j]
        else:
            check_m = min_m(j, count_j)[0]
            self.mp_exp[key_j] = check_m
        new_m = max(m_i, check_m)
        self.solutions[i] = new_m
        for z in range(p_i, self.l):
            p_z = self.primes_n[z]
            new_i = i * p_z
            if new_i > self.max:
                return
            elif z == p_i:
                self.recur(i * p_z, p_z, count_j + 1, new_m, z)
            else:
                self.recur(i * p_z, p_z, 1, new_m, z)


    def start_recur(self):
        t_0 = time.time()
        for e, p in enumerate(self.primes_n):
            if p > self.max:
                break
            else:
                self.recur(p, p, 1, p, e)
        print("Time taken for {} recur is {}".format('iii', time.time() - t_0))
        return self.solutions, self.mp_exp

class recursive_multiplier_iv:
    def __init__(self, p_max):
        self.name = str(self)
        self.max = p_max
        self.solutions = {}
        self.mp_exp = {'2_1': 2}
        self.primes_n = rwh_primes(p_max)
        self.l = len(self.primes_n)

    def recur(self, i, j, count_j, m_i, p_i):
        if count_j * j > m_i:
            check_m = min_m(j, count_j)[0]
            new_m = max(m_i, check_m)
        else:
            new_m = m_i
        self.solutions[i] = new_m
        for z in range(p_i, self.l):
            p_z = self.primes_n[z]
            new_i = i * p_z
            if new_i > self.max:
                return
            elif z == p_i:
                self.recur(i * p_z, p_z, count_j + 1, new_m, z)
            else:
                self.recur(i * p_z, p_z, 1, new_m, z)


    def start_recur(self):
        t_0 = time.time()
        for e, p in enumerate(self.primes_n):
            if p > self.max:
                break
            else:
                self.recur(p, p, 1, p, e)
        print("Time taken for {} recur is {}".format('iv', time.time() - t_0))
        return self.solutions, self.mp_exp

class recursive_multiplier_v:
    def __init__(self, p_max):
        self.name = str(self)
        self.max = p_max
        self.solutions = 0
        self.mp_exp = {'2_1': 2}
        self.primes_n = rwh_primes(p_max)
        self.l = len(self.primes_n)

    def recur(self, i, j, count_j, m_i, p_i):
        if count_j * j > m_i:
            check_m = min_m(j, count_j)[0]
            new_m = max(m_i, check_m)
        else:
            new_m = m_i
        self.solutions  += new_m
        for z in range(p_i, self.l):
            p_z = self.primes_n[z]
            new_i = i * p_z
            if new_i > self.max:
                return
            elif z == p_i:
                self.recur(i * p_z, p_z, count_j + 1, new_m, z)
            else:
                self.recur(i * p_z, p_z, 1, new_m, z)


    def start_recur(self):
        t_0 = time.time()
        for e, p in enumerate(self.primes_n):
            if p > self.max:
                break
            else:
                self.recur(p, p, 1, p, e)
        print("Time taken for {} recur is {}".format('v', time.time() - t_0))
        return self.solutions, self.mp_exp

class recursive_multiplier_vi:
    def __init__(self, p_max):
        self.name = str(self)
        self.max = p_max
        self.solutions = 0
        self.primes_n = rwh_primes(p_max)
        self.l = len(self.primes_n)
        self.mp_exp = {str(i) + '_' + str(j): min_m(i, j)[0] for i in
                       self.primes_n for j in range(1, int(math.log(p_max, i)) + 1)}

    def recur(self, i, j, count_j, m_i, p_i):
        check_m = self.mp_exp[str(j) + '_' + str(count_j)]
        new_m = max(m_i, check_m)
        self.solutions  += new_m
        for z in range(p_i, self.l):
            p_z = self.primes_n[z]
            new_i = i * p_z
            if new_i > self.max:
                return
            elif z == p_i:
                self.recur(i * p_z, p_z, count_j + 1, new_m, z)
            else:
                self.recur(i * p_z, p_z, 1, new_m, z)


    def start_recur(self):
        t_0 = time.time()
        for e, p in enumerate(self.primes_n):
            if p > self.max:
                break
            else:
                self.recur(p, p, 1, p, e)
        print("Time taken for {} recur is {}".format('vi', time.time() - t_0))
        return self.solutions, self.mp_exp


class recursive_multiplier_vii:
    def __init__(self, p_max):
        self.name = str(self)
        self.max = p_max
        self.solutions = 0
        self.primes_n = rwh_primes(p_max)
        self.l = len(self.primes_n)
        self.mp_exp = {str(i) + '_' + str(j): min_m_ii(i, j)[0] for i in
                       self.primes_n for j in range(1, int(math.log(p_max, i)) + 1)}

    def recur(self, i, j, count_j, m_i, p_i):
        check_m = self.mp_exp[str(j) + '_' + str(count_j)]
        new_m = max(m_i, check_m)
        self.solutions  += new_m
        for z in range(p_i, self.l):
            p_z = self.primes_n[z]
            new_i = i * p_z
            if new_i > self.max:
                return
            elif z == p_i:
                self.recur(i * p_z, p_z, count_j + 1, new_m, z)
            else:
                self.recur(i * p_z, p_z, 1, new_m, z)


    def start_recur(self):
        t_0 = time.time()
        for e, p in enumerate(self.primes_n):
            if p > self.max:
                break
            else:
                self.recur(p, p, 1, p, e)
        print("Time taken for {} recur is {}".format('vii', time.time() - t_0))
        return self.solutions, self.mp_exp

def a_check(m, p):
    r = 0
    while m % p == 0:
        m //= p
        r += 1
    return r

def sieve_s(n):
    time_s0 = time.time()
    dict_p = {}
    n_primes = rwh_primes(n)
    n_list = [0] * (n + 1)
    for p in n_primes:
        p_a = p
        m = p
        while p_a < n:
            m_t = m
            while m_t % p == 0:
                dict_p[p_a] = m
                m_t //= p
                p_a *= p
            m += p
    sorted_d = sorted(dict_p.items(), key=lambda kv: kv[1])
    for i in sorted_d:
        a = n // i[0]
        n_list[i[0]:(a + 1)*i[0]:i[0]] = [i[1]] * a
    print("Sieve time:", time.time() - time_s0)
    return n_list[2:]




#print(solutions_i)

#print(m_p_exp)

t_0 = time.time()

for e in range(2, 9):
    #print(recursive_multiplier_vi(10 ** e).start_recur()[0])
    print(sum(sieve_s(10 ** e)))

print(time.time() - t_0)

