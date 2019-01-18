import math

sol_504 = 0

def count_points_quad(a, c, max_val):
    square_quads = 0
    b_points = []
    x_axis_points = a + c - 1

    for b in range(1, max_val + 1):
        points = 0
        for x in range(-c + 1, 0):
            points += math.ceil((b/c)*x + b) - 1
        for x in range(0, a):
            points += math.ceil((-b/a)*x + b) - 1
        b_points.append(points)

    for b, p in enumerate(b_points):
        #print(b, p, 2 * p + x_axis_points, p + x_axis_points)
        max_square = (math.sqrt((2 * p) + x_axis_points))
        if max_square % 1 == 0:
            square_quads += 1
            #print("(a, c) (b, d):({}, {}) ({}, {})".format(a, c, b + 1, b + 1))
            max_square = int(max_square)
            min_square = int(math.sqrt(p + x_axis_points))
            # print("p, min_square, max_square:", p, min_square, max_square)
            for i in range(min_square, max_square):
                lower_half_points = i ** 2 - p - x_axis_points
                # print("i, b, p, lhp:", i, b, p, lower_half_points)
                if lower_half_points in b_points:
                    square_quads += 2
                    d = b_points.index(lower_half_points) + 1
                    #print("(a, c) (b, d):({}, {}) ({}, {})".format(a, c, b + 1, d))
        else:
            max_square = int(max_square)
            min_square = int(math.sqrt(p + x_axis_points))
            #print("p, min_square, max_square:", p, min_square, max_square)
            for i in range(min_square, max_square + 1):
                lower_half_points = i**2 - p - x_axis_points
                #print("i, b, p, lhp:", i, b, p, lower_half_points)
                if lower_half_points in b_points:
                    square_quads += 2
                    d = b_points.index(lower_half_points) + 1
                    print("(a, c) (b, d):({}, {}) ({}, {})".format(a, c, b+1, d))
    if a != c:
        square_quads *= 2
    #print("a, c, b_points, x_axis_points, min, max:", a, c, b_points, x_axis_points, min_square, max_square)
    return square_quads

max_n = 30

for a_i in range(1, max_n + 1):
    for c_i in range(1, a_i + 1):
        sol_i = count_points_quad(a_i, c_i, max_n)
        print("a_i, c_i, sol_i:", a_i, c_i, sol_i)
        sol_504 += sol_i

print("Solution:", sol_504)