
total_a = 0

def recursive_1D_blocks(i, x, r):
    sub_total = 0
    if i == x - 1:
        sub_total += 1
    if i >= x:
        return 0
    if r == 0:
        sub_total += recursive_1D_blocks(i + 1, x - 2, r)
        print('b_0', i, x)
    else:
        sub_total += recursive_1D_blocks(i + 1, x, r)
        print('b_n', i, x)
    for r in range(i + 3, x):
        sub_total += recursive_1D_blocks(i + r, x, r=1)
        print('r', i, x)
    return sub_total

print(recursive_1D_blocks(0, 7, 0))
