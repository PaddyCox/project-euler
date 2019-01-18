import itertools

non_repeated_digits = [0,1,2,3]

insert_digits = itertools.combinations_with_replacement(non_repeated_digits, 2)

insert_digits_1 = itertools.product(non_repeated_digits, repeat=3)

for x, i in enumerate(insert_digits):
    print(x, i)

print('break')

for y, j in enumerate(insert_digits_1):
    print(y, j)

num_create = [1]*10

num_create_2 = 10*[2]

print(num_create)

print(num_create_2)

zipped_nums = zip(num_create, num_create_2)

print(list(zipped_nums))

num_test = int(''.join(map(str, num_create_2)))

print(num_test * 2)

print(num_test)

print(set([2]))