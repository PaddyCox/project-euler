from math import gcd, log
from functools import reduce
from collections import defaultdict
import time

class cuboid_i:
    """Class to find all cuboids (p86) with no dimension > vmax"""

    # vmax (integer): max edge size of cuboid
    def __init__(self, vmax=100):
        self.vmax = vmax
        self.d_dict = defaultdict(int)
        self.solution = 0

    # find primitive cuboids using pythagereon theor
    def solve(self):
        for v in range(2, self.vmax):
            for u in range(1 , v):
                if gcd(v, u) == 1:
                    B, A, C = sorted([v**2 - u**2, 2*v*u, v**2 + u**2])[0:3]
                    if reduce(gcd, (C, B, A)) == 1 and B <= self.vmax and A <= (self.vmax + B):
                        #print(self.solution, A, B)
                        self.non_prime_cuboids(A, B)
                        self.solutions()
                        #print(self.solution, sorted(self.d_dict.items()))
        return self.solutions()


    def non_prime_cuboids(self, A, B):
        i, j, k = 1, 1, 1
        while i*A <= self.vmax:
            self.d_dict[i*A] += i*(B) - (i*B + 1)//2
            i += 1
        if B > A//2:
            while j*B <= self.vmax:
                self.d_dict[j*B] += 1 + j*(B) - (j*A + 1)//2
                j += 1

        """while max(k*B, k*(A - B)) <= self.vmax:

            for x in range(max(k*B, k*(A - B)), min(self.vmax + 1, k*A)):
                #print('x_test', k, A, B, k*x)
                self.d_dict[k*x] += 1
            k += 1"""

    def solutions(self):
        self.solution = 0
        for x in sorted(self.d_dict):
            if x <= self.vmax:
                self.solution += self.d_dict[x]
            else:
                return self.solution
            if self.solution > 10**6:
                print('SUCCESS', self.solution, x)
                return self.solution
                break

        return self.solution

def big_O(w):
    t_0 = time.time()
    a = cuboid_i(vmax=w)
    a.solve()
    print("solution:", a.solution)
    print(a.d_dict)
    print("w = {} time: {}".format(w, time.time() - t_0))
    return time.time() - t_0


time_w = []

for W in range(1760, 2005):
    time_w.append(big_O(W))
print(time_w)
for i in range(1, len(time_w)):
    print('approx_O:', log(time_w[i]/time_w[i-1]), 2)




