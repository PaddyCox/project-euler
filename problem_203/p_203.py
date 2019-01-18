
pascals_triangle = [(0,)]

for row in range(1, 51):
    row_list = [1]
    for j in range(1, row):
        row_list.append(pascals_triangle[row - 1][j - 1] + pascals_triangle[row - 1][j])
    pascals_triangle.append(tuple(row_list + [1]))

set_numbers = set()

for r in pascals_triangle:
    set_numbers = set_numbers | set(r)

print(set_numbers)

total = 0

for n in set_numbers:

    i_max = int(n**0.5)

    for i in range(2, i_max + 1):
        if n % (i * i) == 0:
            set_numbers = set_numbers ^ set([n])
            break

print(set_numbers)

for x in set_numbers:
    total += x

print(total)