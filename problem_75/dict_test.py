
from math import gcd

dict_1 = {x: 0 for x in range(1, 151)}

print(dict_1)

print(gcd(24,430))

for m in range(20):
    for n in range(m):
        if gcd(m, n) == 1:
            print(m,n,gcd(m,n))