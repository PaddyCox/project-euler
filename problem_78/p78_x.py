import time
t_0 = time.time()

coin_partitions_previous = [[1]]

for c in range(2, 500):
    coin_partitions_current = [[1] * c]
    for p in coin_partitions_previous:
        s_p = set(p)
        for n in s_p:
            p_copy = p[:]
            p_copy.remove(n)
            p_copy.append(n + 1)
            coin_partitions_current.append(p_copy)
    print(c, len(coin_partitions_current))
    coin_partitions_previous = coin_partitions_current

print(coin_partitions_current)

print(time.time() - t_0)