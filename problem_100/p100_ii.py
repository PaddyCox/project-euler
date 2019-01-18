import numpy as np
import math


frmt = "{:>25}"*6
frmt_1="{}"*6

for a in range (1, 10):
    # a; offset from perfect square
    a /= 100
    # P(b); no balls removed odds
    s_0 = 2**0.5 - (1 * a)
    # A; scalar factor
    A = s_0/(2**0.5)
    # P(b); one ball (b) removed
    s_1 = 2 / s_0
    # b; sqrt offset
    b = s_1 - (2)**0.5
    # B; scalar offest
    B = s_1/(2**0.5)

    to_print = (a, b, A * B, a - b, s_0, s_1)
    #print("a b A B s_0 s_1:", a, b*1000, A * B, a - b, s_0, s_1)
    print(('{:>25{type}}' * 6).format(*to_print, type='e'))


for A in range(2, 10000):
    B = int(A * (2**0.5))

    B_1 = B - 1
    A_1 = A - 1
    error_f = 2 - (B*B_1)/(A*A_1)
    if abs(error_f) < 10**-8:
        print('{}, {}, {:{type}}, {:{type}}, {}'.format(A, B, B/A, B_1/A_1, error_f, type='e'))

        for frac in ((A, B), (A_1, B_1)):
            num = frac[0]
            denom = frac[1]
            gcd_f = []
            gcd_i = math.gcd(num, denom)
            while gcd_i > 1:
                gcd_f.append(gcd_i)
                num //= gcd_i
                denom //= gcd_i
                gcd_i = math.gcd(num, denom)
            print(num, denom, gcd_f)

def hund_solve_gen(max_n):
    A_P = (3, 4)
    B_P = (2, 3)
    A_R = A_P

    while A_R[1] < max_n:

        A_N = (B_P[0] + B_P[1], 2*B_P[0] + B_P[1])
        A_R = (A_N[0] * A_P[0], A_N[1] * A_P[0])
        B_N = (A_P[0] + A_P[1], 2*A_P[0] + A_P[1])
        B_R = (B_N[0] * B_P[0], B_N[1] * B_P[0])

        print('{}/{}  -->  {}/{}'.format(*A_R, *B_R))
        A_P, B_P = A_N, B_N

    if A_R[1] > max_n:
        return

hund_solve_gen(10**13)
