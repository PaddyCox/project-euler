import operator
import functools
import math

def product_sum(k, j=2):
    # k: size of set
    # j: number of elements k that != 1
    x = k - j
    y = int((x + 1)**0.5 + 1)
    z = (x + y)/(y - 1)
    for y in range(int((x + 1)**0.5 + 1), 0, -1):
        z = (x + y) / (y - 1)
        if z % 1 == 0:
            return(x, y, int(z))
    return False

def product_sum3(k, j=3):
    # k: size of set
    # j: number of elements k that != 1
    max_j = int(math.log(k, 2))
    for j in range(max_j, 1, -1):
        x = k - j
        js = [math.ceil(k**(1/j))] * (j - 1)





    x = k - j
    y = int((x + 1)**0.5 + 1)
    z = (x + y)/(y - 1)
    for y in range(int((x + 1)**0.5 + 1), 0, -1):
        z = (x + y) / (y - 1)
        if z % 1 == 0:
            return(x, y, int(z))
    return False


for k in range(2, 20):
    print(k, sum(product_sum(k)), functools.reduce(operator.mul, product_sum(k)[1:]), product_sum(k))

k = 100
print(k, sum(product_sum(k)), functools.reduce(operator.mul, product_sum(k)[1:]), product_sum(k))


