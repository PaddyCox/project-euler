import math

f = open('p099_base_exp.txt')

bases = []
exponents = []

for line in f:
    base_and_exponent = line.split(',')
    bases.append(int(base_and_exponent[0]))
    exponents.append(int(base_and_exponent[1]))


def approx_how_many_digits(base, exponent):
    number_digits_approx = math.log10(base) * exponent
    return number_digits_approx

how_long_so_far = 0

for i in range(len(bases)):
    iterated_base = bases[i]
    iterated_exponent = exponents[i]
    length_product = approx_how_many_digits(iterated_base, iterated_exponent)
    if length_product > how_long_so_far:
        print(i, length_product, iterated_base, iterated_exponent)
        how_long_so_far = length_product
