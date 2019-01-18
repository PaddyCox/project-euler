import math
import time

start_time = time.time()

def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

primes_under_10_bil = rwh_primes(5000000)

print(len(primes_under_10_bil))

def foo_m(p, q, N):
    """ Returns largest multiple of p,q < N """
    if p * q > N:
        return 0

    n_p = int(math.log(N/q, p))
    answer = 0

    for a in range(1, n_p + 1):
        remainder = N/(p ** a)
        n_q = int(math.log(remainder, q))
        i_answer = ((p ** a) * (q ** n_q))
        temp_answer = max(i_answer, answer)
        answer = temp_answer
    return answer

sum_answers = 0

for a in range(0, len(primes_under_10_bil)):
    p_i = primes_under_10_bil[a]
    i = 0
    q_i = primes_under_10_bil[i]
    q_i_max = 10000000/p_i
    while q_i < q_i_max and i < a:
        sum_answers += foo_m(p_i, q_i, 10000000)
        i += 1
        q_i = primes_under_10_bil[i]



print(sum_answers)

print(time.time() - start_time)
