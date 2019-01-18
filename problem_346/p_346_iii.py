import time


t_0 = time.time()

repunits_iii = set([1])


def geometric_power_summation_ii(a, n):
    global repunits_count
    set_repunits_base_a = set()
    initial = a + 1
    previous_i = initial * a + 1
    while previous_i < n:
        set_repunits_base_a.add(previous_i)
        previous_i *= a
        previous_i += 1
    return set_repunits_base_a

for b in range(2, int((10**7 - 1)**0.5) + 1):
    repunits_iii = repunits_iii | geometric_power_summation_ii(b, 10**7)
    #print(b)


# print(sorted(list_rep))

print(sum(repunits_iii))

print("Time taken is {}".format(time.time() - t_0))