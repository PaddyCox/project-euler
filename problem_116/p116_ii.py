import time

t_0 = time.time()


def rgb_tiles(x, i, len_colour):
    sub_total = 0

    if i > x:
        return 0

    if i == x:
        return 1
    sub_total += rgb_tiles(x, i + len_colour, len_colour)
    sub_total += rgb_tiles(x, i + 1, len_colour)

    return sub_total


print(rgb_tiles(40, 0, 2) - 1)

print(rgb_tiles(40, 0, 3) - 1)

print(rgb_tiles(40, 0, 4) - 1)


print(time.time() - t_0)