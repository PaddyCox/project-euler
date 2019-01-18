# 86_ii: Determine distinct primitive integer cuboids that satisfy solution. Additional cuboids can be found by multiplying by scalar

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

# ii - X**2 + (Y + Z)**2 is a square

import time
import itertools
from math import sqrt
from math import gcd
from functools import reduce

t_0 = time.time()




def int_sides_1(Z, Y, X):
    # arguments in ascending order to match gen output
    d1 = (sqrt((X*Y)**2 + (Y+Z)**2 * Y**2) + sqrt((X*Z)**2 + (Y+Z)**2 * Z**2))/(Y+Z)
    # print(X, Y, Z, d1)
    if d1 % 1 == 0:
        return True
    else:
        if d1 % 1 < 0.00:
            print("CHECK", X, Y, Z, d1 % 1)
        return False


XYZ = (itertools.combinations_with_replacement(range(1, 11), 3))

total = 0
negative = 0
primitive_cuboids = []

"""for C in XYZ:
    if int_sides_1(*C) != int_sides_0(*C):
        print('FAIL', *C)
        total += 1
    else:
        negative += 1"""

for C in XYZ:
    print(C)
    if int_sides_1(*C):
        total += 1
        s = reduce(gcd, C)
        if s == 1:
            print("Primitive:", *C)
            primitive_cuboids.append(C)
        else:
            C_check = tuple([q//s for q in C])
            print("Scalar:", *C)
            if C_check not in primitive_cuboids:
                print(s, 'STOP STOP STOP')
                break
    else:
        negative += 1




print(total, negative)
print(len(primitive_cuboids))

print(time.time() - t_0)