import string

lower_case_letters = "abcdefghijklmnopqrstuvwxyz"

import helper_functions

valid_words = helper_functions.load_words('words.txt')

text_to_chars = helper_functions.text_to_string('p059_cipher.txt')

copy_text_to_chars = text_to_chars[:]

for i in range(len(text_to_chars)):
    copy_text_to_chars[i] = chr(int(text_to_chars[i]))

list_of_lists = helper_functions.n_splitter(copy_text_to_chars, 3)

string1 = ''.join(list_of_lists[0][:])
string2 = ''.join(list_of_lists[1][:])
string3 = ''.join(list_of_lists[2][:])

print(len(string1), len(string2), len(string3))

xors_1 = [helper_functions.XOR_encrypt(string1, x) for x in lower_case_letters]

xors_2 = [helper_functions.XOR_encrypt(string2, x) for x in lower_case_letters]

xors_3 = [helper_functions.XOR_encrypt(string3, x) for x in lower_case_letters]

best = 0

print(xors_1)

print(len(xors_1))

all_xors = [xors_1, xors_2, xors_3]

for xor in all_xors:
    xor_copy = xor[:]
    for string1 in xor_copy:
        for char in string1:
            ascii_char = ord(char)
            if ascii_char < 32 or ascii_char > 122:
                xor.remove(string1)
                break

print(len(xors_1), len(xors_2), len(xors_3))

for a in range(len(xors_1)):
    for b in range(len(xors_2)):
        for c in range(len(xors_3)):
            current_score = 0
            compiled_string = ''
            for i in range(len(xors_3[c])):
                add_string = xors_1[a][i] + xors_2[b][i] + xors_3[c][i]
                compiled_string += add_string
            compiled_string += xors_1[a][400]
            list_of_words = compiled_string.split(' ')
            for word in list_of_words:
                if helper_functions.is_word(valid_words, word):
                    current_score += 1
            if current_score > best:
                print(current_score, a, b, c)
                best = current_score
                result = compiled_string


total = 0

print("Length of result:", len(result))

for i in result:
    total += ord(i)

print(total)