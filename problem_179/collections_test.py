import collections

l_1 = [2,2,3,3,7,7,7,9]

l_2 = [2,2,11,11,7,7,7,13]

c_1 = collections.Counter(l_1)

c_2 = collections.Counter(l_2)

def num_p_factors(list_p):
    """
    Returns frequency of unique integers in list_p
    :param list_p:
    :return: sorted list of occurrences
    """
    d_1 = {}

    for p in list_p:
        if p in d_1:
            d_1[p] += 1
        else:
            d_1[p] = 1

    l_r = sorted(d_1.values())

    return l_r

c_1_v = c_1.values()
c_2_v = c_2.values()

if c_1_v == c_2_v:
    print('Yay')

else:
    print('Boo')

print(len(c_1_v))

print(len(c_2_v))

print(num_p_factors(l_2) == num_p_factors(l_2))