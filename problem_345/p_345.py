import itertools


matrix = \
" 7  53 183 439 863 497 383 563  79 973 287  63 343 169 583 " \
"627 343 773 959 943 767 473 103 699 303 957 703 583 639 913 "\
"447 283 463  29  23 487 463 993 119 883 327 493 423 159 743 "\
"217 623   3 399 853 407 103 983  89 463 290 516 212 462 350 "\
"960 376 682 962 300 780 486 502 912 800 250 346 172 812 350 "\
"870 456 192 162 593 473 915  45 989 873 823 965 425 329 803 "\
"973 965 905 919 133 673 665 235 509 613 673 815 165 992 326 "\
"322 148 972 962 286 255 941 541 265 323 925 281 601  95 973 "\
"445 721  11 525 473  65 511 164 138 672  18 428 154 448 848 "\
"414 456 310 312 798 104 566 520 302 248 694 976 430 392 198 "\
"184 829 373 181 631 101 969 613 840 740 778 458 284 760 390 "\
"821 461 843 513  17 901 711 993 293 157 274  94 192 156 574 "\
" 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699 "\
"815 559 813 459 522 788 168 586 966 232 308 833 251 631 107 "\
"813 883 451 509 615  77 281 613 459 205 380 274 302  35 805"

# print(matrix)

matrix_list = [int(s) for s in matrix.split()]

print('matrix_list', matrix_list)

matrix_list_ii = []

row_list = []

for i, s in enumerate(matrix_list):
    row_list.append(s)
    if (i + 1) % 15 == 0:
        matrix_list_ii.append(row_list)
        row_list = []


#initial_solution = [matrix_list_ii[i][i] for i in range(15)]

#print(initial_solution)

def matrix_sum_calc(indices):
    return sum([matrix_list_ii[i][j] for i, j in enumerate(indices)])


def max_matrix_sum(indices, size=15):
    """ Iterate over each element in matrix and swap if new result is greater than current
        Parameters:
            indices: list with index representing i and value representing j
    """

    changes_made = 0
    current_indices = indices
    max_sum = matrix_sum_calc(current_indices)
    current_max_indices = current_indices
    for i in range(0, size):
        for j in range(0, size):
            indices_copy = current_indices[:]
            c_i = current_indices[i]
            c_j = current_indices.index(j)
            indices_copy[i] = j
            indices_copy[c_j] = c_i
            check_sum = matrix_sum_calc(indices_copy)
            # print('c_s', check_sum)
            if check_sum > max_sum:
                current_max_indices = indices_copy
                max_sum = check_sum
                changes_made += 1

    return(max_sum, current_max_indices, changes_made)

def matrix_shift(i, j, indices, size=15):
    indices_copy = indices[:]
    indices_copy[i] = j
    indices_copy[indices.index(j)] = indices[i]

    return indices_copy


zero_changes = 0
index = [i for i in range(0, 15)]
max_matrix_sum_i = 0

while zero_changes < 4:
    og_max_sum = max_matrix_sum_i
    for p in itertools.product(range(0, 15), repeat=2):
        temp_matrix = matrix_shift(p[0], p[1], index)
        sum_iteration = max_matrix_sum(temp_matrix)
        index = sum_iteration[1]
        max_matrix_sum_i = sum_iteration[0]
    if max_matrix_sum_i == og_max_sum:
            zero_changes += 1
    print(sum_iteration, zero_changes)





