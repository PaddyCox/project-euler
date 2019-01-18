

def sign(m):
    if m < 0:
        return -1
    elif m > 0:
        return 1
    else:
        return 0

def is_bounce(n):
    n_s = str(n)
    n_len = len(n_s)

    test_against = 0

    if n_len <= 2:
        return False

    for j in range(1, n_len):
        current_case = sign(int(n_s[j]) - int(n_s[j - 1]))
        if current_case == 0:
            pass
        elif test_against == 0:
            test_against = current_case
        else:
            if test_against != current_case:
                return True


    return False

total_bouncy = 0

for i in range(1, 3000000):
    if is_bounce(i):
        total_bouncy += 1

    if i % 100 == 0:
        if (total_bouncy) * 100 == i * 99:
            print ("YAYAYA")
            print(i)
            break

print(total_bouncy, i)