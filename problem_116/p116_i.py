import time

t_0 = time.time()

def number_blocks(results, i, m):

    results += [(1, 0)] * (m - 1)
    results += [(1, 1)]
    print(results)
    for x in range(m + 1, i+1):
        b = sum(results[x - 1])
        r = results[x - 1][1] + results[max(x - m, 0)][0]
        results.append((b, r))
        print(x, b + r, b, r)
        if (b + r) > 10**6:
            print('Success!', x, b+r)
            return True


results_initial = [(0, 0)]

number_blocks(results_initial, 300, 50)

print(time.time() - t_0)