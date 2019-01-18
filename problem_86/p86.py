"""A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million."""

# Let X, Y, Z be 3 sides of cuboid: X >= Y >= Z

# Shortest path will cross 2 faces from cuboid: XY, XZ

# Let X = x0 + x1
# Path distance = A + B = (x0**2 + Y**2)**0.5 + (x1**2 + Z**2)**0.5

# dD/dA = x0/((x0**2 + Y**2)**0.5), dD/dB = x1/((x1**2 + Z**2)**0.5)
# For minimum distance dD/dA == dD/dB
# Therefore x0/x1 = Y/Z

import time
import itertools
from math import sqrt, gcd
from functools import reduce

t_0 = time.time()

def int_sides_0(Z, Y, X):
    # arguments in ascending order to match gen output
    d1 = sqrt((X*Y/(Y+Z))**2 + Y**2) + sqrt((X*Z/(Y+Z))**2 + Z**2)
    #print(X, Y, Z, p1 + p2)
    if d1 % 1 == 0:
        return True
    else:
        if d1 % 1 < 0.00:
            print("CHECK", X, Y, Z, d1 % 1)
        return False

def int_sides_1(Z, Y, X):
    # arguments in ascending order to match gen output
    d1 = (sqrt((X*Y)**2 + (Y+Z)**2 * Y**2) + sqrt((X*Z)**2 + (Y+Z)**2 * Z**2))/(Y+Z)
    # print(X, Y, Z, d1)
    if d1 % 1 == 0:
        # print(X, Y, Z, d1)
        return True
    return False


XYZ = itertools.combinations_with_replacement(range(1, 12), 3)

total = 0
negative = 0
prim_souls = []

"""for C in XYZ:
    if int_sides_1(*C) != int_sides_0(*C):
        print('FAIL', *C)
        total += 1
    else:
        negative += 1"""

for C in XYZ:
    if int_sides_1(*C):
        total += 1
        if reduce(gcd, C) == 1:
            prim_souls.append(C)
            print("prim_soul", C)
    else:
        negative += 1

def m_gen(M):
    return itertools.combinations_with_replacement(range(1, M + 1), 2)

print(time.time() - t_0)
t_1 = time.time()

sol_count = 0
M = 1

"""while M < 101:
    x = M
    YZ = m_gen(M)
    for yz in YZ:
        #if reduce(gcd, (*yz, x)) == 1:
        if int_sides_1(*yz, x):
                #print("prim cube:", *C, M)
            sol_count += 1
    M += 1

print(M, sol_count)"""


print(total, negative)


print(time.time() - t_1)