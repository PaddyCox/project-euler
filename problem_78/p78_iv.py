import time


t_0 = time.time()

sums_nk = [0, 1, 2, 3]
n_k = [(0), (0, 1), (0, 1, 1), (0, 1, 1, 1)]

for n in range(4, 500):
    list_n_k = [0]
    for k in range(1, n//2 + 1):
        list_n_k.append(int(str(n_k[n-1][k-1] + n_k[n-k][k])[-6::]))
    for k in range(n//2 + 1, n + 1):
        #print(n, k, n_k)
        #print(n_k[n-1][k-1])
        list_n_k.append(int(str(n_k[n-1][k-1])[-6::]))
    n_k.append(tuple(list_n_k))
    sum_nk = sum(list_n_k)
    sums_nk.append(sum_nk)
    # print(n, sum_nk)
    if sum_nk % 10**6 == 0:
        print("Answer is:", sums_nk)
        break
    # print(n_k)

print(sums_nk[-1:-5:-1])
print(time.time() - t_0)