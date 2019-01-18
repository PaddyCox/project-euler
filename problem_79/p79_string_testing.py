string1 = 'abcde'

string2 = 'ae'

f = open('p079_keylog.txt')

import collections

print(string1[1])
partial_passcodes = f.read()

list_p_p = partial_passcodes.replace('\n', ' ').split(' ')

#def string_in_string(s1, s2):





first_digit = [x[0] for x in list_p_p]

second_digit = [x[1] for x in list_p_p]

third_digit = [x[2] for x in list_p_p]


frequency_first = collections.Counter(first_digit)
frequency_second = collections.Counter(second_digit)
frequency_third = collections.Counter(third_digit)

print(frequency_first)
print(frequency_second)
print(frequency_third)

#print(list_first_digits)