import time

start_time = time.time()

p_k_n = [[0, 0], [0, 1]]

for n in range(2, 101):
    current_n_partitions = [0]
    for k in range(1, n + 1):
        try:
            pkn_a = p_k_n[n - k][k]
        except IndexError:
            pkn_a = 0
        try:
            pkn_b = p_k_n[n-1][k-1]
        except IndexError:
            pkn_b = 0

        current_n_partitions.append(pkn_a + pkn_b)
    partitions_n = sum(current_n_partitions)
    if partitions_n % 100000 == 0:
        print(n, partitions_n)
        break
    p_k_n.append(current_n_partitions)

"""for j in range(1, len(p_k_n)):
    partitions_j = sum(p_k_n[j])
    print(j, partitions_j)
    if partitions_j % 100000 == 0:
        break"""

print(p_k_n)

print(time.time() - start_time)
