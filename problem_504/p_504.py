
def sq_sum(n, max_p):
    sols = 0
    perms = [1, 4, 12, 24]
    for a in range(min(n-3, max_p), (n - 1)//4, -1):
        for b in range(min(n - a - 2, a), (n - a -1)//3, -1):
            for c in range(min(n - a - b - 1, b), (n - a - b - 1)//2, -1):
                d = n - a - b - c
                sol = [a, b, c, d]
                perm_i = len(set(sol))
                if perm_i == 2 and sol.count(sol[0]) == 2:
                    sols += 6
                    print(a, b, c, d, sum([a, b, c, d]), perms[len(set(sol)) - 1])
                else:
                    sols += perms[len(set(sol)) - 1]
    return sols


print(sq_sum(9, 4))

total = 0

for x in range(2, 21):
    x_i = sq_sum(x**2, 100)
    print(x, x_i)
    total += x_i

print(total)