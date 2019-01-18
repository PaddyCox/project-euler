import math
import itertools

def points_in_quadrant(A, B):
    sum_points = 0
    for x in range(1, A):
        sum_points += math.ceil(-B/A*x + B) - 1
    return sum_points

def axis_points(A, C):
    return (A + C - 1)



def smart_504(max_n):
    answer_504 = 0
    for a in range(1, max_n):
        for c in range(1, a + 1):
            for b in range(1, a + 1):
                for d in range(1, b + 1):
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
                    """if b == d:
                        for c_2 in range(c + 1, a):
                            i_points = sum([points_in_quadrant(q[0], q[1]) for q in quadrants])
                            i_points += (axis_points(a, c) + axis_points(b, d) - 1)
                            if math.sqrt(i_points) % 1 == 0:
                                answer_504 += 4"""
    return answer_504

def dumb_504_ii(max_n):
    answer_dumb_504 = 0
    for p_0 in itertools.product(range(1, max_n), repeat=2):
        sol_ii = 0
        a, c = p_0[0], p_0[1]
        for p_1 in itertools.product(range(1, max_n), repeat=2):
            b, d = p_1[0], p_1[1]
            quadrants = ((a, b), (b, c), (c, d), (d, a))
            i_points = sum([points_in_quadrant(q[0], q[1]) for q in quadrants])
            i_points += (axis_points(a, c) + axis_points(b, d) - 1)
            if math.sqrt(i_points) % 1 == 0:
                #print(a, b, c, d)
                answer_dumb_504 += 1
                sol_ii += 1
        #print("a, c, sol_ii:", a, c, sol_ii)
    return answer_dumb_504

def count_points_quad(a, c, max_val):
    square_quads = 0
    b_points = []
    x_axis_points = a + c - 1

    for b in range(1, max_val + 1):
        points = b - 1
        points += (((a - 1)*(b - 1) - math.gcd(a, b) + 1)/2)
        points += (((c - 1)*(b - 1) - math.gcd(c, b) + 1)/2)
        b_points.append(points)

    for b, p in enumerate(b_points):
        #print(b, p, 2 * p + x_axis_points, p + x_axis_points)
        max_square = int(math.sqrt((2 * p) + x_axis_points))
        min_square = int((math.sqrt((p) + x_axis_points)))

        for sq in range(min_square, max_square + 1):
            d_check = sq**2 - p - x_axis_points
            if d_check in b_points:
                d = b_points.index(d_check)
                if d == b:
                    square_quads += 1
                else:
                    square_quads += 2
    if a != c:
        square_quads *= 2
    #print("a, c, b_points, x_axis_points, min, max:", a, c, b_points, x_axis_points, min_square, max_square)
    return square_quads

max_n = 100

sol_504 = 0

for a_i in range(1, max_n + 1):
    for c_i in range(1, a_i + 1):
        sol_i = count_points_quad(a_i, c_i, max_n)
        #print("a_i, c_i, sol_i:", a_i, c_i, sol_i)
        sol_504 += sol_i

print("Solution:", sol_504)

#print(dumb_504_ii(max_n + 1))