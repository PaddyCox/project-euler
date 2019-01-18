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




def single_cell_return(y_s, y_e, x_e, updated_matrix, og_matrix):

    route_totals = []

    if y_s == y_e:
        route_value = int(matrix_1_copy[y_e][x_e - 1]) + int(og_matrix[y_e][x_e])
        route_totals.append(route_value)
    else:
        number_routes = abs(y_s - y_e) + 1

        direction_travel = -int((y_s - y_e)/abs(y_s - y_e))

        for x in range(number_routes):
            i = x_e - 1
            j = y_s
            print(i,j)
            route_total = int(updated_matrix[j][i])
            count = 0
            while count < number_routes:
                if x == count:
                    i += 1
                    count += 1
                else:
                    j += direction_travel
                    count += 1
                route_total += int(og_matrix[j][i])
            route_totals.append(route_total)

    return route_totals

for x in range(1, 80):
    for y in range(0, 80):
        path_options = []
        for z in range(y - 7, min(y + 7, 80)):
            path_options += single_cell_return(z, y, x, matrix_1_copy, og_matrix)

        matrix_1_copy[y][x] = min(path_options)


print(single_cell_return(0, 2, 1, og_matrix, og_matrix))

print(single_cell_return(4, 2, 1, og_matrix, og_matrix))

list_final_path_values = [x[79] for x in matrix_1_copy]

for value in list_final_path_values:
    print(value)

print(single_cell_return(2, 2, 1, og_matrix, og_matrix))

print(min(list_final_path_values))