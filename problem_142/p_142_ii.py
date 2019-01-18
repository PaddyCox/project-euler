import itertools
import collections

square_difference = collections.defaultdict(list)
x_values = collections.defaultdict(list)


squares = [i**2 for i in range(1, 3000)]

for pair in itertools.combinations(squares, 2):
    sqr_1 = pair[0]
    sqr_2 = pair[1]
    difference = sqr_2 - sqr_1
    if not difference % 2:
        x_i = (sqr_2 + sqr_1)/2
        square_difference[difference].append(pair)
        x_values[x_i].append(pair)


for x_i in x_values:
    x_v = x_values[x_i]
    if len(x_v) > 1:
        for c in itertools.combinations(x_v, 2):
            squares_abcd = sorted([val for t in c for val in t])
            y = squares_abcd[3] - x_i
            z = squares_abcd[2] - x_i
            if (y - z)**0.5 % 1 == 0  and (y + z)**0.5 % 1 == 0:
                print('sum(x, y, z), x, y, z:', x_i + y + z, x_i, y, z)