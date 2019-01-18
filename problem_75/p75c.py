import collections

from math import gcd

a = 0
b = 0
c = 0

list_prim_pythag_triples = []

dict_lengths = {x: 0 for x in range(1500000)}

for n in range(1, 867):
    for m in range(1, min(n, int((750000 - n ** 2)**0.5))):
        a = n ** 2 - m ** 2
        b = 2 * n * m
        c = n ** 2 + m ** 2
        if gcd(a, b) == 1:
            list_prim_pythag_triples.append((a, b, c, a + b + c))



print(len(list_prim_pythag_triples))

for i in range(10):
    print(list_prim_pythag_triples[i])


totals = []

for case in list_prim_pythag_triples:

    i_length = case[3]
    n = 1
    c_length = i_length * n

    while c_length < 1500001:
        totals.append(c_length)
        n += 1
        c_length = n * i_length

coll = collections.Counter(totals)

a_1 = sorted(list(set(totals)))

print(a_1)

print(len(a_1))

total_2 = 0

for j in coll:
    if coll[j] == 1:
        total_2 += 1

print(total_2)


"""use dictionary, if dict[n] == 1, total += 1, if dict[n] == 2, total -= 1"""


