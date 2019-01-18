

repunits = []
repunits_ii = []

def repunit_calc(repunit, base):
    # repunit: type string
    return(sum([base**n for n in range(0, len(repunit))]))


for b in range(2, 1000):
    r_i = 0
    starting_rep = '1'
    while r_i < 10**3:
        r_i = repunit_calc(starting_rep, b)
        repunits.append(r_i)
        starting_rep = starting_rep + '1'

set_r = set(repunits)

sum_strong = 0

for r in set_r:
    if repunits.count(r) > 1:
        sum_strong += r
        print(r)

print(sum_strong)


