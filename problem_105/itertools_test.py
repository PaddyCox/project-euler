import itertools

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
            print(sum_c)
            if sum_c in subset_sum:
                return False
            subset_sum.add(sum_c)
    return True

def recursive_sum_finder(a, b, running_total):
    sums = []
    if (a + 1) < b:
        for i in range(a + 1, b):
            sums.append(running_total + false_positive[i])
            sums = sums + recursive_sum_finder(i, b, running_total + false_positive[i])

    return sums

def total_sum_finder():
    subset_sums = []
    for l in range(0, 5):
        subset_sums += recursive_sum_finder(l, 7, false_positive[l])
    return subset_sums

def check_set(list_1):
    set_1 = set(list_1)
    if len(set_1) == len(list_1):
        return True
    else:
        list_2 = list(set_1)
        for a in list_2:
            list_1.remove(a)
        print(list_1)
        return False


test_list = [1, 2, 3, 4, 5]

predicted_set_o = (22, 33, 40, 41, 42, 44, 47)

false_positive = [19, 33, 40, 41, 42, 44, 47]

print(list(itertools.combinations(test_list, 2)))

len_1 = len(predicted_set_o)//2


print(itertools_sum_check(false_positive))

if check_set(total_sum_finder()):
    print(false_positive)
    print(sum(false_positive))