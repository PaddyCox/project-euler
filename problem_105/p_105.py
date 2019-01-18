import itertools

import csv

def itertools_sum_check(list_1):
    list_1.sort()
    number_items = len(list_1)
    set_list = set(list_1)

    if len(set_list) != number_items:
        return False

    check_up_to = number_items // 2
    lower_half = (number_items + 1) // 2
    large_sum = sum(list_1[0:lower_half])
    small_sum = sum(list_1[:(-lower_half):-1])

    if large_sum <= small_sum:
        return False

    subset_sum = set()

    for i in range(1, check_up_to + 1):
        i_combos = itertools.combinations(list_1, i)
        for c_i in i_combos:
            sum_c = sum(c_i)
            if sum_c in subset_sum:
                return False
            subset_sum.add(sum_c)
    return True

total_sum = 0

with open('p105_sets.csv') as csvfile:
    all_sums = csv.reader(csvfile)
    for line in all_sums:
        int_line = list(map(int, line))
        if itertools_sum_check(int_line):
            total_sum += sum(int_line)
            print(int_line)

print(total_sum)