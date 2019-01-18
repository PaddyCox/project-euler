import collections

lower_case_letters = 'abcdefghijklmnopqrstuvwxyz'

import helper_functions

valid_words = helper_functions.load_words('words.txt')

text_to_chars = helper_functions.text_to_string('p059_cipher.txt')

copy_text_to_chars = text_to_chars[:]

for i in range(len(text_to_chars)):
    copy_text_to_chars[i] = chr(int(text_to_chars[i]))

list_of_lists = helper_functions.n_splitter(copy_text_to_chars, 3)

print(collections.Counter(list_of_lists[2]).most_common(3))