import itertools

total = 0

for v in range(2, int(10**(9/2))):
    even_v = v % 2
    for u in range(1 + even_v, v, 2):
        pythag_triple = (v ** 2 - u ** 2, 2 * v * u, v ** 2 + u ** 2)
        if 3 * pythag_triple[2] > 10**9:
            break
        """j = v - u
        two_v_three_j = ((3 * (j ** 2) - 2) ** 0.5, (3 * (j ** 2) + 2) ** 0.5)
        for n, i in enumerate(two_v_three_j):
            if i % 1 == 0:
                s = pythag_triple[0] * 2
                h = pythag_triple[1]
                b = s + (-1 + (2 * n))
                #print('b_compare', b, pythag_triple[2])
                #print(v, u, pythag_triple)"""
        for p in range(2):
            b_check = pythag_triple[2] - 2 * pythag_triple[p]
            if b_check == -1:
                total += 3 * pythag_triple[2] + 1
                print('BB_1', b_check, pythag_triple[2], pythag_triple[2] + 1, 2*pythag_triple[p], v, p)
            elif b_check == 1:
                total += 3 * pythag_triple[2] - 1
                print('BB_2', b_check, pythag_triple[2], pythag_triple[2] - 1, 2 * pythag_triple[p])

print(total)