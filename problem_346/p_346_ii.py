repunits_ii = []

def repunit_calc(repunit, base):
    # repunit: type string
    return(sum([base**n for n in range(0, len(repunit))]))

def sum_geometric_series(a, r, n):
    # a is first term of series
    # r is common ratio
    # n is total number of terms
    sum_g_series = a*((1 - r**n)/(1 - r))
    return sum_g_series

max_val = 1000

max_b = int((max_val - 0.75)**0.5 - 0.5)


for l in
    for b in range(2, max_b + 1):
        repunits_ii.append(repunit_calc('111', b))


print(repunits_ii, sum(repunits_ii))

