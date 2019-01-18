import time

start_time = time.time()

from math import log, ceil, sqrt
N = 10**12
print ("Result:", 1 - (31 + 8191 if N > 8191 else 31 if N > 31 else 0) + sum((b**n - 1) // (b - 1) for b in range(2, int(sqrt(N - 0.75) + 0.5)) for n in range(3, int(ceil(log(N * (b - 1) + 1) / log(b))))))

print(time.time() - start_time)