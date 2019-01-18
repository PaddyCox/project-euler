import time

time_0 = time.time()

T = 1000000

r_1 = T//4 + 1
r_2 = int(T**0.5)

c_1 = 0

for a in range(r_1, r_2, -1):
    a_u = a
    a_i = ((a_u**2 - T)**0.5)
    a_l = int(a_i) + (a_i % 1 > 0)

    sum_a = (a_u - a_l) // 2

    c_1 += sum_a

t_1 = time.time()

print(t_1 - time_0)

c_2 = 0

for b in range(r_2, 2, -1):
    sum_b = (b - 1) // 2
    print(b, sum_b)
    c_2 += sum_b

t_2 = time.time()

print(t_2 - t_1)

print(c_1, c_2, c_1 + c_2)

