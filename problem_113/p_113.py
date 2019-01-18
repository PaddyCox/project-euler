def check_non_bounce(x):

    list_digits = [int(d) for d in str(x)]
    length_1 = len(list_digits)
    if length_1 < 3:
        return True
    positive_difference = False
    negative_difference = False
    for i in range(1, length_1):
        diff = list_digits[i - 1] - list_digits[i]
        if diff > 0:
            positive_difference = True
        elif diff < 0:
            negative_difference = True
        if negative_difference and positive_difference:
            return False

    if negative_difference:
        return -1
    else:
        return 1

total = 99
pos_num = 0
neg_num = 0
for x in range(100, 1000):
    if check_non_bounce(x) == 1:
        pos_num += 1
    if check_non_bounce(x) == -1:
        neg_num += 1


print(neg_num, pos_num, total + neg_num + pos_num)


def recursive_descending(seed, num_digits, num):
    total = 0
    if num_digits == 0:
        return 1
    if seed == 0:
        return 1
    for i in range(0, seed + 1):
        num_i = int(str(num) + str(i))
        total += recursive_descending(i, num_digits - 1, num_i)
    return total

def recursive_ascending(seed, num_digits, num):
    total = 0
    if num_digits == 0:
        return 1
    if seed == 9:
        return 1
    for i in range(seed, 10):
        num_i = int(str(num) + str(i))
        total += recursive_ascending(i, num_digits - 1, num_i)
    return total

non_bounce = 99

asc_num_t = 0

des_num_t = 0

total = 99
for y in range(2, 20):
    asc_num = 0
    des_num = 0
    for z in range(1, 10):
        asc_num += recursive_ascending(z, y, z)
        des_num += recursive_descending(z, y, z)
        asc_num -= 1
    asc_num_t += asc_num
    des_num_t += des_num
    total += asc_num + des_num
    print(asc_num, des_num, asc_num + des_num, total)