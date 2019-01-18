from itertools import product
from math import gcd


def problem504a(m=30):
    """Return the number of quadrilaterals with vertices lying at lattice
    points on the coordinate axes, no more than m units from the
    origin, whose interior contains a square number of lattice points.

    """
    square_plus_three = [False] * (4 * m * m + 3)
    for i in range(2 * m):
        square_plus_three[i * i + 3] = True
    R = range(m + 1)
    U = [[((a - 1) * (b - 1) - gcd(a, b) + 1) // 2 + a for a in R] for b in R]
    count = 0
    for a, b, c, d in product(range(1, m + 1), repeat=4):
        if square_plus_three[U[a][b] + U[b][c] + U[c][d] + U[d][a]]:
            count += 1
    return count

print(problem504a(m=30))