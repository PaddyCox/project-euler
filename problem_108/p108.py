import time
import collections

start_time = time.time()

dict_1 = {x: 0 for x in range(1, 5001)}

for x in range(1, 10001):
    for y in range(1, x):
        a = x + y
        b = x * y
        if b % a == 0:
            c = b // a
            dict_1[c] += 1

c = collections.Counter(dict_1)

print(c)

print(time.time() - start_time)