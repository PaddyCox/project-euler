import itertools

a_string = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeefffffffffffggggggggg"

b_string = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg"

print(len(a_string))

print("".join(set(b_string)))

result = (itertools.combinations(b_string, 20))

count = 0

total = 0

result_2 = itertools.islice(result, 0, None, 1000000000)


for a in result_2:
    total += len("".join(set(a)))
    count += 1
    if count > 100:
        break

print(total/count)