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


def check_combos(c):
    c_l = ([6 if d == 9 else d for d in c[0]], [6 if d == 9 else d for d in c[1]])
    pairs = ((0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (6, 4), (8, 1))
    for p in pairs:
        if p[0] in c_l[0] and p[1] in c_l[1]:
            continue
        elif p[0] in c_l[1] and p[1] in c_l[0]:
            continue
        else:
            return False
    return True

def dice_pairs():
    choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
            true_val += 1


print(dice_pairs())







