from math import factorial

def choose(a, b):

    return factorial(a)/(factorial(b) * factorial(a - b))

def choose_2(a, b):
    n = a - b
    total = 1
    for a in range(n + 1, a + 1):
        total *= a
    return total / factorial(b)



total = choose(70, 20)

six_c = 7 * choose(60, 20)

five_c = choose(7, 2) * choose(50, 20)

four_c = choose(7, 3) * choose(40, 20)

three_c = choose(7, 4) * choose(30, 20)

two_c = choose(7, 2) * choose(20, 20)

answer_1 = ((total - six_c - five_c - four_c - three_c - two_c) * 7 + six_c * 6 + five_c * 5 + four_c * 4 + three_c * 3 + two_c * 2)/total

print(answer_1)

total_2 = choose_2(70, 20)

six_c_2 = 7 * choose_2(60, 20)

five_c_2 = choose_2(7, 2) * choose_2(50, 20)

four_c_2 = choose_2(7, 3) * choose_2(40, 20)

three_c_2 = choose_2(7, 4) * choose_2(30, 20)

two_c_2 = choose_2(7, 2) * choose_2(20, 20)

answer_2 = ((total_2 - six_c_2 - five_c_2 - four_c_2 - three_c_2 - two_c_2) * 7 + six_c_2 * 6 + five_c_2 * 5 + four_c_2 * 4 + three_c_2 * 3 + two_c_2 * 2)/total_2

print(answer_2)

print(7 * (1 - (choose_2(60, 20)/choose_2(70, 20))))

print(choose_2(70, 20), choose(70, 20))