import copy

f = open('p081_matrix.txt', 'r')

string_1 = f.read()

matrix_text = string_1.splitlines()

matrix_1 = []

for l in matrix_text:
    row = l.split(',')
    matrix_1.append(row)

def matrix_solver(a_matrix):

    copy_matrix = copy.deepcopy(a_matrix)
    size_matrix = len(a_matrix)

    for a in range(1, size_matrix):
        for j in range(a + 1):
            i = a - j
            if i == 0:
                previous_left = 99999999
            else:
                previous_left = int(copy_matrix[j][i-1])
            if j == 0:
                previous_up = 99999999
            else:
                previous_up = int(copy_matrix[j-1][i])

            max_previous_cell = min(previous_left, previous_up)

            new_cell_value = str(int(max_previous_cell) + int(copy_matrix[j][i]))

            copy_matrix[j][i] = new_cell_value

    for b in range(1, size_matrix):
        for x in range(b, 80):
            y = 79 + b - x
            max_previous_path = min(int(copy_matrix[y][x-1]), int(copy_matrix[y-1][x]))

            new_cell_value_2 = str(int(max_previous_path) + int(copy_matrix[y][x]))

            copy_matrix[y][x] = new_cell_value_2

    return copy_matrix


print(len(matrix_1))

half_there = matrix_solver(matrix_1)

check_sum = 0

for i in matrix_1:
    check_sum += int(i[0])

print(check_sum)

sum_matrix_values = 0

for i in matrix_1:
    for j in i:
        sum_matrix_values += int(j)

print(sum_matrix_values/6400)


print((float(half_there[79][79]))/160)

print(half_there[0][79])

print(half_there[79][0])

check_1 = 0

check_2 = 0

for i in matrix_1[0]:
    check_1 += int(i)

for j in matrix_1:
    check_2 += int(j[0])

print(check_1, check_2)

for n in half_there:
    print(n)

print(half_there[79][79])