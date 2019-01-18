from math import gcd
from functools import reduce
from collections import defaultdict
import time

class cuboid_i:
    def __init__(self, vmax=100):
        self.vmax = vmax
        self.d_dict = defaultdict(int)
        self.solution = 0

    def solve(self):
        for v in range(2, self.vmax):
            for u in range(1 , v):
                if gcd(v, u) == 1:
                    C, B, A = sorted([v**2 - u**2, 2*v*u, v**2 + u**2])[0:3]
                    if reduce(gcd, (C, B, A)) == 1 and B <= self.vmax and A <= 2*B:
                        print(A, B, C, self.solution)
                        self.non_prime_cuboids(B, C)
                        self.solutions()
                        print(A, B, C, self.solution)
        return self.solutions()


    def non_prime_cuboids(self, A, B):
        i, j, k = 1, 1, 1
        while i*A <= self.vmax:
            self.d_dict[i*A] += i*(B) - (i*B - 1)//2
            i += 1
        if B > A//2:
            while j*B <= self.vmax:
                self.d_dict[j*B] += j*(B) - (j*A + 1)//2
                j += 1

        while max(k*B, k*(A - B)) <= self.vmax:

            for x in range(max(k*B, k*(A - B)), min(self.vmax + 1, k*A)):
                #print('x_test', k, A, B, k*x)
                self.d_dict[k*x] += 1
            k += 1

    def solutions(self):
        self.solution = 0
        for x, v in self.d_dict.items():
            if x <= self.vmax:
                self.solution += v
        return self.solution

def big_O(w):
    t_0 = time.time()
    a = cuboid_i(vmax=w)
    a.solve()
    print("solution:", a.solution)
    print(a.d_dict)
    print("w = {} time: {}".format(w, time.time() - t_0))


for W in range(1, 3):
    big_O(10**W)

#big_O(99)

