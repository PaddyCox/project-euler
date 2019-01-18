"""Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?"""

# Determine pairs required. 6 == 9, with arrangements +1 for each instance of 6
# 2, 5 are isolated. Problem becomes choose 5 side of each die
# 0, 1, 4, 6 are linked subgroup > determine combinations that satisfy these pairs
# 0 pairs 1, 4, 6; 6 pairs 0, 1, 4
# 3, 8 are isolated nodes; linked to 6 and 1 respectively

# let a be 0 or 6, requiring connection to all within subgroup
# let b be 1 or 4, requiring connection to all a's
# let c be 3 or 8, requiring connection to one number only

# Scenario 1: find all possible combinations that satisfy a_0 on one die only

# {a_0}, {} > {a_0}, {a_1, b_0, b_1} > {a_0, a_1}, {a_1, b_0, b_1}
# S1 == ({a_0, a_1} & {a_1, b_0, b_1},
#        {a_0, a_1} & {a_0, b_0, b_1})

# Scenario 2: then find combinations with a_0 AND a_1 on both die

# 1: {a_0, a_1}, {a_0, a_1} > {a_0, a_1, b_0, b_1}, {a_0, a_1} OR {a_0, a_1, b_0}, {a_0, a_1, b_1}
# S2 == ({a_0, a_1, b_0, b_1} & {a_0, a_1}, THIS COMBINATION IS REDUNDANT AS a_0 or a_1 not required in first group
#        {a_0, a_1, b_0} & {a_0, a_1, b_1})

# Scenario 3: a_0 and a_1 on opposite die

# S3 == ({a_0, b_0, b_1} & {a_1, b_0, b_1})

# c_0 linked to a_0, c_1 linked to b_0. (3 -> 6, 8 -> 1)

# S1 == ({a_0, a_1, c_1} & {a_1, b_0, b_1, c_0}, (C2, C1)      * 2 for (6, 9)           * 2 for (25, 52)
#        {a_0, a_1, c_1} & {a_0, b_0, b_1, c_0}, (C2, C1)      * 4 for (66, 69, 96, 99) * 2 for (25, 52)
#        {a_0, a_1, c_0, c_1} & {a_0, b_0, b_1}) (C1, C2)      * 4 for (66, 69, 96, 99) * 2 for (25, 52)

# S2 == ({a_0, a_1, b_0} & {a_0, a_1, b_1, c_0, c_1}) (C2, C0) * 4 for (66, 69, 96, 99) * 2 for (25, 52)
#        {a_0, a_1, b_0, c_0} & {a_0, a_1, b_1, c_1}) (C1, C1) * 4 for (66, 69, 96, 99) * 2 for (25, 52)

# S3 == ({a_0, b_0, b_1, c_1} & {a_1, b_0, b_1, c_0})
#        {a_0, b_0, b_1} & {a_1, b_0, b_1, c_0, c_1})

# Final solution; brute force to add combinations and ensure no duplicate sets

import itertools
combos = set()

def die_generator(d_1, d_2):
    global combos
    N = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    l_1 = len(d_1)
    l_2 = len(d_2)
    gen_1 = (c for c in itertools.combinations_with_replacement(N, 5 - l_1))
    gen_2 = (c for c in itertools.combinations_with_replacement(N, 5 - l_2))
    com = (c for c in itertools.product(gen_1, gen_2))
    for g in com:
        c_0 = tuple(sorted(list(g[0]) + [2] + d_1))
        c_1 = tuple(sorted(list(g[1]) + [5] + d_2))
        Combo_1 = tuple(sorted([c_0, c_1]))
        c_0 = tuple(sorted(list(g[0]) + [5] + d_1))
        c_1 = tuple(sorted(list(g[1]) + [2] + d_2))
        Combo_2 = tuple(sorted([c_0, c_1]))
        combos = combos | set([Combo_1, Combo_2])





die_generator([6, 0, 8], [0, 1, 4, 3])
die_generator([6, 0, 8], [6, 1, 4, 3])
die_generator([6, 0, 8, 3], [6, 1, 4])

die_generator([6, 0, 1], [6, 0, 4, 3, 8])
die_generator([6, 0, 1], [0, 1, 3, 4, 8])
die_generator([6, 0, 1], [1, 3, 4, 6, 8])

die_generator([6, 0, 1, 3], [6, 0, 4, 8])
die_generator([6, 0, 1, 3], [6, 1, 4, 8])

die_generator([6, 1, 4], [0, 1, 4, 3, 8])
die_generator([6, 1, 4, 8], [0, 1, 4, 3])

ans_0 = len(combos)

combos_reversed = [(a[1], a[0]) for a in combos]

count = 0

for b in combos_reversed:
    if b[0] == b[1]:
        print('Same', b)
    if b in combos:
        print(b)
        count += 1
print(count)

def check_combos(c):
    pairs = ((0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (6, 4), (8, 1))
    for p in pairs:
        if p[0] in c[0] and p[1] in c[1]:
            continue
        elif p[0] in c[1] and p[1] in c[0]:
            continue
        else:
            return False
    return True

for x in combos:
    check_combos(x)

for z in combos_reversed:
    check_combos(z)

for a in combos:
    num_six = (a[0].count(6) + 1, a[1].count(6) + 1)
    prod = num_six[0] * num_six[1]
    ans_0 += (prod - 1)

def six_nine(dice_pair):
    num_six = (dice_pair[0].count(6) + 1, dice_pair[1].count(6) + 1)
    prod = num_six[0] * num_six[1]
    return prod

print(ans_0)

def combo_creator():
    choice = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    found = False
    count = 0
    true_val = 0
    d_1 = itertools.combinations_with_replacement(choice, 6)
    die_c = itertools.combinations(d_1, 2)
    while not found:
        count += 1
        try:
            D = next(die_c)
        except StopIteration:
            print(count, true_val)
            return
        a = tuple(sorted(D[0]))
        b = tuple(sorted(D[1]))
        pair_die = tuple(sorted([a, b]))
        if check_combos(pair_die):
            tup_die = tuple(pair_die)
            true_val += six_nine(tup_die)
            if tup_die not in combos:
                print(tup_die)
                found = True

    return tup_die, count


print(combo_creator())







