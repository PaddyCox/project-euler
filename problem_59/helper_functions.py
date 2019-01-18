def text_to_string(file_name):
    """Takes input text file from directory and returns list of chars separated at ',' """
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    char_list = []
    for line in inFile:
        char_list.extend([word.lower() for word in line.split(',')])
    return char_list

list_of_chars = text_to_string('p059_cipher.txt')

test_list_char = [1,2,3,4,5,6,7,8,9]

def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    #>>> is_word(word_list, 'bat') returns
        True
    #>>> is_word(word_list, 'asdf') returns
        False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def n_splitter(list1, n):
    """splits input lists into n lists with every nth char"""

    list_to_split = list1

    length1 = len(list_to_split)

    return_list = []

    for m in range(n):
        sub_list = []
        count = m
        while count < length1:
            sub_list.append(list_to_split[count])
            count += n
        return_list.append(sub_list)

    print(len(return_list))
    return return_list


print(n_splitter(test_list_char, 3))

def XOR_encrypt(input_string, a):
    # input_string: string of ascii chars to be XOR'd
    # a: value to +XOR by
    number_of_ascii_chars = 128
    ascii_a = ord(a)

    translated_string = ''

    for c in input_string:
        ascii_c = ord(c)
        translated_char = chr((ascii_c ^ ascii_a))
        translated_string += translated_char

    return translated_string

print (XOR_encrypt('abcde', 'b'))

def XOR_decrypt(input_string, a):
    # input_string: string of ascii chars to be XOR'd
    # a: value to be -XOR by
    number_of_ascii_chars = 128
    ascii_a = ord(a)

    translated_string = ''

    for c in input_string:
        ascii_c = ord(c)
        translated_char = chr((ascii_c - ascii_a) % number_of_ascii_chars)
        translated_string += translated_char

    return translated_string

def how_many_chars_are_letters(string):
    total = 0
    all_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in string:
        if char in all_letters:
            total += 1

    return total

print(XOR_encrypt("&'$%*", "b"))

print(XOR_encrypt('DEFGH', 'b'))

print(how_many_chars_are_letters('abc2321%$&$'))