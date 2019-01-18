import time

start_time = time.time()

def digit_add(m, d):
    str_d = str(d)
    check_against = m
    len_m = len(str(m))
    for i in range(10):
        temp_d = int(str_d + str(i))
        check = int(str(temp_d ** 2)[0:len_m])
        print(m, i, check, check_against, temp_d)
        if check == check_against:
            #print("AAA")
            return int(str_d + str(i - 1))
    return int(str_d + str(9))

def a_finder():

    cumulative_total = 0

    for n in range(1, 44):
        if n**0.5 != int(n**0.5):

            seed_value = int(n ** 0.5)

            b = seed_value

            for c in range(100):
                temp_b = digit_add(n, b)
                b = temp_b

            b_string = str(b)

            b_s = b_string[1:len(b_string)-1]
            f_d = int(b_string[-1:-2:-1])

            answer = 0

            for c in b_s:
                answer += int(c)
            if f_d > 4:
                answer += 1

            cumulative_total += answer

            print(answer, f_d, b_s, n)

    return cumulative_total

print(a_finder())

print(time.time() - start_time)