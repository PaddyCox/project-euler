import time

start_time = time.time()

p_k_n_d = {"0_0": 0, "1_0": 0, "1_1": 1}

for n in range(2, 101):
    current_n_partitions = {str(n) + "_0": 0}
    for k in range(1, n + 1):
        try:
            pkn_a = p_k_n_d[str(n - k) + "_" + str(k)]
        except KeyError:
            pkn_a = 0
        try:
            pkn_b = p_k_n_d[str(n - 1) + "_" + str(k - 1)]
        except KeyError:
            pkn_b = 0

        current_n_partitions[str(n) + "_" + str(k)] = (pkn_a + pkn_b)
    partitions_n = sum(current_n_partitions.values())
    if partitions_n % 100000 == 0:
        print(n, partitions_n)
        break
    p_k_n_d.update(current_n_partitions)

"""for j in range(1, len(p_k_n)):
    partitions_j = sum(p_k_n[j])
    print(j, partitions_j)
    if partitions_j % 100000 == 0:
        break"""

print(p_k_n_d)

print(time.time() - start_time)
