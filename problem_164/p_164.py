import time

t_0 = time.time()

sum_total = []

def consecutive_digit_sum(n_1, n_2, n_i, n_max):
    total = 0
    if n_i == n_max:
        return 1
    for d in range(0, 10 - n_1 - n_2):
        total += consecutive_digit_sum(n_2, d, n_i + 1, n_max)
    return total

for num_d in range(1, 13):
    sum_d = 0
    for n_0 in range(1, 10):
        sum_d += consecutive_digit_sum(0, n_0, 1, num_d)
    sum_total.append(sum_d)

for s in range(1, len(sum_total)):
    print(s, sum_total[s], sum_total[s]/sum_total[s - 1])

print(time.time() - t_0)

print(sum_total)