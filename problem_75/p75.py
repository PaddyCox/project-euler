import useful_functions

print(useful_functions.is_prime(3))


def integer_right_triangle_finder(n):
    # n: an integer that represents the hypotenuse
    list_of_solutions = []

    a = int(n/(2**0.5))

    while a < n:
        b = (n**2 - a**2)**0.5
        if b == int(b):
            list_of_solutions.append((n, a, int(b)))
        a += 1

    return list_of_solutions

list_of_right_triangles = []

for n in range(3, 75, 2):
    temp_storage = integer_right_triangle_finder(n)
    if len(temp_storage) > 0:
        list_of_right_triangles.append(temp_storage)


print(list_of_right_triangles)