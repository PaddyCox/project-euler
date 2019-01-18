primes_under_10 = [7, 5, 3, 2]


def regress_solve(n, nums, i_s):
    total = 0
    if n == 0:
        print(nums)
        return 1

    elif n == 1:
        return 0

    else:
        for i in range(i_s, 4):
            p_sub = primes_under_10[i]
            if p_sub <= n:
                total += regress_solve(n - p_sub, nums + [p_sub], i)

    return total


print(regress_solve(10, [], 0))


def coin_partition_regress(n, max):
    running_total = 0

    if n == 0:
        return 1
    else:
        max_i = min(n, max)
        for i in range(max_i, 0, -1):
            running_total += coin_partition_regress(n - i, i)
    return running_total


print(coin_partition_regress(5, 5))


for j in range(1, 11):
    print(j, coin_partition_regress(j,j))

# Dictionary of results, combine

dict_coin_partitions = {0: 1, 1: 1, 2: 2, 3: 3}

def foo_boy(n, m):
    if n >= m:
        return dict_coin_partitions[m]
    else:
        subtract_amount = 0
        for x in range(1, m - n):
            subtract_amount += dict_coin_partitions[x]
        return dict_coin_partitions[m] - subtract_amount


for j in range(4, 100):
    temp_coin_partitions = 1
    for a in range(j, 0, -1):
        temp_coin_partitions += foo_boy(a, j - a)
    dict_coin_partitions[j] = temp_coin_partitions

print(dict_coin_partitions)

