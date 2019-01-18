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
combos = []
def die_generator(d_1, d_2):
    n_0 = [2, 5]
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    c_1 = (d_1 + list(i) for i in itertools.combinations_with_replacement(nums, 5 - len(d_1)))
    c_2 = (d_2 + list(i) for i in itertools.combinations_with_replacement(nums, 5 - len(d_2)))
    print(c_1, '\n', c_2)
    c_12 = list(sorted([i[0] + [n_0[j]], i[1] + [n_0[1 - j]]]) for i in itertools.product(c_1, c_2) for j in range(2))
    print(c_12)
    return c_12

combos += die_generator([6, 0, 8], [0, 1, 4, 3])
combos += die_generator([6, 0, 8], [6, 1, 4, 3])
combos += die_generator([6, 0, 3, 8], [0, 1, 4])
combos += die_generator([6, 0, 1], [6, 0, 4, 3, 1])
combos += die_generator([6, 0, 1, 3], [6, 0, 4, 8])
combos += die_generator([6, 1, 4, 3], [6, 1, 4, 8])
combos += die_generator([6, 1, 4], [6, 1, 4, 3, 8])



print(len(combos))
print(combos)
sorted_comb = [(tuple(sorted(x[0])), tuple(sorted(x[1]))) for x in combos]
sorted_comb_2 = [(tuple(sorted(x[1])), tuple(sorted(x[0]))) for x in combos]
print(sorted_comb)
s_comb = set(sorted_comb)
s_comb_ii = set(sorted_comb_2)

print(len(s_comb), len(s_comb_ii))

print(sorted_comb)

l = 2676
s_3 = s_comb - s_comb_ii

for i in s_comb:
    if i in s_comb_ii:
        print(i)
        l -= 1

print(l)
print(len(s_3))
answer = len(s_3)
for s in s_3:
    num_six = s[0].count(6) + s[1].count(6)
    answer += (2**num_six - 1)

print(answer)






