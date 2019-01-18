import time

t_0 = time.time()

repunits_iii = [1]

def geometric_power_summation_ii(a, n):
    global repunits_count
    repunits_base_a = []
    initial = a + 1
    previous_i = initial * a + 1
    while previous_i < n:
        """if previous_i == 8191:
            print(a, n)"""
        repunits_base_a.append(previous_i)
        previous_i *= a
        previous_i += 1
    return repunits_base_a

for b in range(2, int((10**9 - 1)**0.5) + 1):
    repunits_iii = repunits_iii + geometric_power_summation_ii(b, 10**9)
    #print(b)

# print(repunits_iii, sum(repunits_iii))

set_rep = set(repunits_iii)

# print(sorted(list_rep))

list_sum = sum(repunits_iii)
set_sum = sum(set_rep)

#print([r for r in set_rep if repunits_iii.count(r) > 1])

print(set_sum, list_sum, list_sum - set_sum)

print("Time taken is {}".format(time.time() - t_0))