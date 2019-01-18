import helper_functions
import string

list_of_all_chars = helper_functions.text_to_string('p059_cipher.txt')

lower_case_chars = 'abcdefghijklmnopqrstuvwxyz'

all_letters = string.ascii_letters

split_lists = helper_functions.n_splitter(list_of_all_chars, 3)

for i in range(len(split_lists)):
    string_from_chars = ''.join(split_lists[i])

    current_decryption_guess = [0]

    max_letters = 0

    for a in lower_case_chars:
        decrypted_string = helper_functions.XOR_encrypt(string_from_chars, a)
        number_letters = helper_functions.how_many_chars_are_letters(decrypted_string)
        print(a, number_letters)
        if number_letters > max_letters:
            current_decryption_guess[0] = a
            max_letters = number_letters

    print(i, max_letters, current_decryption_guess)


