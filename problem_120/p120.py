

def find_r(a, n):
    r = ((a - 1) ** n + (a + 1) ** n) % (a ** 2)
    return r

sum_r_max = 0

for a in range(3, 1001):
    a_r_max = 0
    n_max = 0
    for n in range((2 * a) + 2):
        i_r = (find_r(a, n))
        if i_r > a_r_max:
            a_r_max = i_r
            n_max = n
    print(a, n_max, a_r_max)
    sum_r_max += a_r_max

print(sum_r_max)