import time

def v_p(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k

def val(k, p):
    r = 0
    while k > 0:
        r += 1
        k -= (1 + v_p(r, p))
    return p * r

def sieve_ff(n):
    l = [0] * (n + 1)
    for p in range(2, n + 1):
        if l[p] == 0:
            u = p
            k = 1
            while u <= n:
                s = val(k, p)
                j = 1
                while j * u <= n:
                    l[j * u] = max(l[j * u], s)
                    j += 1
                k += 1
                u *= p
    return l

def v_p(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k

def sieve_ff_ii(n):
    l = [0] * (n + 1)
    for p in range(2, n + 1):
        if l[p] == 0:
            u = p
            k = 1
            s = 0
            while u <= n:
                while k > 0:
                    s += p
                    k -= v_p(s, p)
                j = u
                while j <= n:
                    if s > l[j]:
                        l[j] = s
                    j += u
                k += 1
                u *= p
    return l

t_0 = time.time()

l = sieve_ff(10 ** 6)
print(sum(l[1:]))

print(time.time() - t_0)

t_1 = time.time()

L = sieve_ff_ii(10**6)
print(sum(L[1:]))

print(time.time() - t_1)