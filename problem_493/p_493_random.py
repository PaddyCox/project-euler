import random

list_options = [i for i in range(1, 8)]

list_options *= 10

print(list_options)


def ball_selection():

    urn = list_options[:]
    selection = []
    for j in range(70, 50, - 1):
        r = random.randrange(0, j)
        selection.append(urn[r])
        del urn[r]

    return len(set(selection))

total = 0

for i in range(1, 10000001):
    total += ball_selection()

print(total/10000000)