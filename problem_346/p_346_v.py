import time

t_0 = time.time()

repunits_iii = 1 - 8222

def geometric_power_summation_ii(a, n):
    global repunits_count
    repunits_base_a = 0
    initial = a + 1
    previous_i = initial * a + 1
    while previous_i < n:
        """if previous_i == 8191:
            print(a, n)"""
        repunits_base_a += (previous_i)
        previous_i *= a
        previous_i += 1
    return repunits_base_a

for b in range(2, int((10**12 - 1)**0.5) + 1):
    repunits_iii += geometric_power_summation_ii(b, 10**12)
    #print(b)


print(repunits_iii)

print("Time taken is {}".format(time.time() - t_0))