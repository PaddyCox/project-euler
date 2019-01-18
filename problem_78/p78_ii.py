# Partition number theory
# Elliptic modular functions
# Euler pentagonal number theorem
# Generator function
import time


t_0 = time.time()

def partitions_n(n):

    sum_partitions = 0
    k_max = ((20*n + 1)**0.5 + 1)//6
    k_min = -k_max

    for k in range(k_min, k_max + 1):
        n_k_partitions = (-1)**k * (x**(k * (3*k - 1)/2))


# Make as a generator function

partition_dict = {'1_0': 0, '1, 1': 1, '2, 0': 0, '2, 1': 1, '2, 2': 1}

def recurrence_partition(n, k):
    if k > n:
        print('k must be less than n')
        return False
    if n < 3:
        print('n must be greater than 3')
        return False
    n_k_string = str(n) + ', ' + str(k)
    if k == n:
        n_k_val = 1
    elif k == 0:
        n_k_val = 0
    else:
        n_k_val = 0
        if (k - 1) > 0:
            n_k_val += partition_dict[(str(n - 1) + ', ' + str(k - 1))]
        if (n - k) >= k:
            n_k_val += partition_dict[(str(n - k) + ', ' + str(k))]
    partition_dict.update({n_k_string: n_k_val})
    return n_k_val


max_n = 500

n_totals = [0, 1, 1]

for n_i in range(3, max_n + 1):
    n_total = 0
    for k in range(1, n_i + 1):
        p_nk = recurrence_partition(n_i, k)
        n_total += p_nk
    n_totals.append(n_total)
    check_p = int(str(n_total)[-6::])
    # print(n_i, n_totals[n_i], check_p)
    if n_total % 10**2 == 0:
        print(n_i, n_total)
    if check_p == 0:
        print('Winner:', n_i, n_total, check_p)
        break

print(n_totals[-1:-5:-1])

print(time.time() - t_0)




