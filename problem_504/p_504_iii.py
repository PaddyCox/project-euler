import math
import itertools
import time


def points_in_quadrant(A, B):
    sum_points = 0
    for x in range(1, A):
        sum_points += math.ceil(-B/A*x + B) - 1
    return sum_points

def axis_points(A, C):
    return (A + C - 1)



def smart_504(max_n):
    answer_504 = 0
    for a in range(1, max_n + 1):
        for b in range(1, a + 1):
            for c in range(1, b + 1):
                for d in range(1, c + 1):
                    quadrants = ((a, b), (b, c), (c, d), (d, a))
                    i_points = sum([points_in_quadrant(q[0], q[1]) for q in quadrants])
                    i_points += (axis_points(a, c) + axis_points(b, d) - 1)
                    #print(a, b, c, d, i_points)
                    if math.sqrt(i_points) % 1 == 0:
                        bool_check = sum((a == c, b == d, min(a == b, c == d)))
                        #print(a, b, c, d, bool_check, i_points)
                        if bool_check == 3:
                            answer_504 += 1
                        elif bool_check == 1:
                            answer_504 += 4
                        else:
                            answer_504 += 8
                    if b == d:
                        for c_2 in range(c + 1, a):
                            i_points = sum([points_in_quadrant(q[0], q[1]) for q in quadrants])
                            i_points += (axis_points(a, c) + axis_points(b, d) - 1)
                            if math.sqrt(i_points) % 1 == 0:
                                answer_504 += 4
    return answer_504

def dumb_504(max_n):
    answer_dumb_504 = 0
    for p in itertools.product(range(1, max_n + 1), repeat=4):
        a, b, c, d = p[0], p[1], p[2], p[3]
        quadrants = ((a, b), (b, c), (c, d), (d, a))
        i_points = sum([points_in_quadrant(q[0], q[1]) for q in quadrants])
        i_points += (axis_points(a, c) + axis_points(b, d) - 1)
        if math.sqrt(i_points) % 1 == 0:
            #print(a, b, c, d)
            answer_dumb_504 += 1
    return answer_dumb_504


t_0 = time.time()

print(dumb_504(10))

t_1 = time.time()

print(smart_504(10))

t_2 = time.time()

print(t_2 - t_1, t_1 - t_0)