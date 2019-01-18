

def hundred_digit_irrational_root(n):

    count = 0

    seed_int = int(n**0.5)
    a = seed_int
    check = 0

    i = 0
    while len(str(a)) < 101:
        while check < n:
            temp_a = int(str(a) + str(i))
            num_digits = len(str(temp_a))
            check_1 = int(temp_a**2)
            added_digit = (len(str(check)) > 2 * num_digits)
            if added_digit:
                check = int(str(check_1)[0:2])
            else:
                check = int(str(check_1)[0:1])

            i += 1
        if i < 10:
            a = int(str(a) + str(i-1))
        else:
            a = int(str(a) + str(9))
            count += 1
    return a

print(hundred_digit_irrational_root(2))