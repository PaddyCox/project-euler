import math
import operator


list_points = []

for y in range(0, 51):
    temp_row = []
    for x in range(0, 51):
        if x == 0 and y == 0:
            pass
        try:
            theta = math.atan(y/x)
        except ZeroDivisionError:
            theta = (math.pi/2)
        r = math.sqrt(x**2 + y**2)
        list_points.append((x, y, theta, r))

del list_points[0]

sort_by_theta = sorted(list_points, key=operator.itemgetter(2), reverse=True)

def dot_product(v_1, v_2):
    return v_1[0]*v_2[0] + v_1[1]*v_2[1]



def angle_checker(coord_1, coord_2):
    """Takes two xy coordinates and origin, checks three vector dot products for perpendicular result"""
    v_1 = coord_1
    v_2 = coord_2
    v_3 = (coord_1[0] - coord_2[0], coord_1[1] - coord_2[1])
    if dot_product(v_1, v_2) == 0:
        return True
    elif dot_product(v_1, v_3) == 0:
        return True
    elif dot_product(v_2, v_3) == 0:
        return True
    return False

number_triangles = 0

for P in range(0, len(sort_by_theta)):
    for Q in range(P, len(sort_by_theta)):
        t_P = sort_by_theta[P]
        t_Q = sort_by_theta[Q]
        theta_P = t_P[2]
        theta_Q = t_Q[2]
        if theta_Q < theta_P:
            xy_P = (t_P[0], t_P[1])
            xy_Q = (t_Q[0], t_Q[1])
            if angle_checker(xy_P, xy_Q):
                #print(xy_P, xy_Q)
                number_triangles += 1

print(number_triangles)

