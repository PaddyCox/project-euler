import operator
import functools
import math
import time

# Approach: For each set of size k, determine upper bound and lower bound of possible
#           product-sum numbers. Then iterate over different factor combinations within
#           this range to find minimum product-sum N.



class min_product_sum:
    """ Determines minimum set(s) of size k that satisfies: product(s) == sum(s). """
    def __init__(self, k):
        self.k = k
        self.max_n = 2 * k
        self.min_n = k + math.ceil(math.log(k, 2))
        self.max_j = int(math.log(self.max_n, 2))

    def solve(self):
        """ Initiate recurse() function for j number of factors """
        for j in range(2, self.max_j + 1):
            self.recurs(j, [2], self.max_n)
        return self.max_n

    def recurs(self, j, x_l, n_0):
        """ Recursively builds size j factor combinations with product between min_n and max_n """
        if j > 1:
            x_min = x_l[-1]
            x_max = int(n_0**(1/j))
            for x in range(x_min, x_max + 1):
                self.recurs(j - 1, x_l + [x], n_0/x)
        # When only one factor (z) remains, determine algebraically
        if j == 1:
            try:
                sum_i = sum(x_l[1:]) + (self.k - len(x_l))
            except TypeError:
                print(j, x_l)
                return
            prod_i = functools.reduce(operator.mul, x_l[1:])
            z = sum_i/(prod_i - 1)
            # Check if z is int, is so list of factors is a valid product sum number
            if z % 1 == 0 and z < self.max_n:
                temp_n = sum_i + int(z)
                # If smallest product sum number found set as new upper limit
                if temp_n < self.max_n:
                    self.max_n = temp_n
                    # print([1] * (self.k - len(x_l)) + x_l[1:] + [int(z)])


set_n = set()
t_0 = time.time()

for k in range(2, 1200):
    set_n.add(min_product_sum(k).solve())

print(sum(set_n))
print(time.time() - t_0)