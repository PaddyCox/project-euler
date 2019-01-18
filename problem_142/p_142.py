import itertools
import collections
from useful_functions import find_p_factors_ii

d_s_ii = collections.defaultdict(list)
s_s = []


for s in range(1, 600):
    s_s.append(s**2)

d_s = [((x + y), (x, y)) for x, y in itertools.product(s_s, s_s) if (x + y) % 2 == 0 and x > y]

for k, v in d_s:
    d_s_ii[k].append(v)

for d in d_s_ii:
    values = d_s_ii[d]
    for i, j in itertools.combinations(values, 2):
        d_0 = d/2
        b = i[0] - d_0
        c = j[0] - d_0
        a_0 = (b**2 + c**2 - d_0**2)
        if a_0 > 0:
            a_check = a_0**0.5
            if a_check % 1 == 0:
                print('abcd', a_check, b, c, d_0)
                x = (a_check**2 + d_0**2)/2
                y = d_0**2 - x
                z = c**2 - x
                print(x+y+z, x, y, z)
                print(a_check**2 + d_0**2, b**2 + c**2)



"""count_sum = (collections.Counter(d_s))

set_ds = sorted(set(d_s))

for c in set_ds:
    count_c = d_s.count(c)//2
    if count_c > 1:
        print(c, count_c)"""

