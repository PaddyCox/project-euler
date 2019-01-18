import time

t_0 = time.time()

def recursive_1D_blocks(row_blocks, x):
    sub_total = 0
    l_0 = len(row_blocks)

    if l_0 == x - 1:
        sub_total += 1
        #print(row_blocks)
        return sub_total
    if l_0 >= x:
        return 0

    sub_total += recursive_1D_blocks(row_blocks + [0], x)

    spaces_left = x - 1 - l_0

    if spaces_left > 2:
        sub_total += recursive_1D_blocks(row_blocks + spaces_left * [1], x)

    for r in range(3, x - l_0):
        sub_total += recursive_1D_blocks(row_blocks + r*[1] + [0], x)


    return sub_total


for z in range(4, 21):
    print(z -1, recursive_1D_blocks([], z))

print(time.time() - t_0)

