

def num_finder(i):

    if i < 2:
        return 2
    elif i == 2:
        return 3
    else:
        j = 2
        n_1, n_2 = 2, 3

        while j < i:
            j += 1
            if j % 3 == 0:
                a = (2 * j) // 3
            else:
                a = 1
            n_n = (a * n_2) + n_1
            n_2, n_1 = int(n_n), int(n_2)


    return int(n_2)

num_100 = str(num_finder(100))

answer = 0
print(num_100)

for l in num_100:
    answer += int(l)

print(answer)

print(num_finder(100))
print(num_finder(10))

for i in range(100):
    print(num_finder(i))