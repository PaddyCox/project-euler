import time


t_0 = time.time()

print('a')


def rgb_tiles_ii(x, len_colour):
    f_in = [0] * len_colour + [1] + [2]
    for n in range(len_colour + 2, x + 1):
        #print('n', n)
        f_n = f_in[n - 1] + f_in[n - len_colour] + 1
        #print('n, f_in:', n, f_in)
        f_in.append(f_n)
    print('f_in', f_in)
    return f_in[-1::]

def rgb_tiles(x, i, len_colour):
    sub_total = 0

    if i > x:
        return 0

    if i == x:
        return 1
    sub_total += rgb_tiles(x, i + len_colour, len_colour)
    sub_total += rgb_tiles(x, i + 1, len_colour)

    return sub_total


test_n = 5

sum_ii = 0

sum_i = 0

print(rgb_tiles_ii(test_n, 2))

print(rgb_tiles_ii(test_n, 3))

print(rgb_tiles_ii(test_n, 4))

"""print(rgb_tiles(test_n, 0, 2) - 1)

print(rgb_tiles(test_n, 0, 3) - 1)

print(rgb_tiles(test_n, 0, 4) - 1)"""


print(time.time() - t_0)

# a generator that yields items instead of returning a list
"""def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))"""