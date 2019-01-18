import copy

m_text = open('p082_matrix.txt', 'r')

string_1 = m_text.read()

matrix_text = string_1.splitlines()

matrix_1 = []

for l in matrix_text:
    row = l.split(',')
    matrix_1.append(row)

matrix_1_copy = copy.deepcopy(matrix_1)

og_matrix = copy.deepcopy(matrix_1)

for x in range(1, 80):
    for y in range(0, 80):
        if y == 0:
            option_1 = 999999
        else:
            option_1 = (int(matrix_1[y-1][x]) + int(matrix_1[y-1][x-1]))
        option_2 = (int(matrix_1[y][x-1]))
        if y == 79:
            option_3 = 999999
        else:
            option_3 = (int(matrix_1[y+1][x])) + int(matrix_1[y+1][x-1])

        min_route = min(option_1, option_2, option_3)
        matrix_1_copy[y][x] = (min_route + int(matrix_1_copy[y][x]))
    matrix_1 = matrix_1_copy

for row in matrix_1:
    print(row)

final_values = []

for j in range(80):
    final_values.append(matrix_1[j][79])
    temp_sum = 0
    for i in og_matrix[j]:
        temp_sum += int(i)
    print(temp_sum)

print(min(final_values))