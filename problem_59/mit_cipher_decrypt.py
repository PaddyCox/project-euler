# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
import time
from ps4a import get_permutations


### HELPER CODE ###
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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'


class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text

        self.valid_words = load_words('words.txt')

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''

        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        copy_valid_words = self.valid_words[:]

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled
        according to vowels_permutation. The first letter in vowels_permutation
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''

        ordered_vowels = 'aeiou'

        all_letters = string.ascii_letters

        transpose_dict = {all_letters[i]: all_letters[i] for i in range(len(all_letters))}

        for i in range(5):
            transpose_dict[ordered_vowels[i]] = vowels_permutation[i]
            transpose_dict[str.upper(ordered_vowels[i])] = str.upper(vowels_permutation[i])

        return transpose_dict

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary

        Returns: an encrypted version of the message text, based
        on the dictionary
        '''

        original_message_list = list(self.get_message_text())

        all_letters = string.ascii_letters

        for i in range(len(original_message_list)):
            if original_message_list[i] in all_letters:
                copy_of_char = original_message_list[i]
                original_message_list[i] = transpose_dict[copy_of_char]

        encrypted_text = ''.join(original_message_list)

        return encrypted_text


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words('words.txt')

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message

        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.

        If no good permutations are found (i.e. no permutations result in
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message

        Hint: use your function from Part 4A
        '''
        vowels = 'aeiou'

        vowels_permutations = get_permutations(vowels)

        max_words = 0

        best_decrypt_perm = ''

        list_message_words = self.message_text.split(' ')

        for p in vowels_permutations:

            valid_word_count = 0

            test_transpose_dict = self.build_transpose_dict(p)
            transposed_text = self.apply_transpose(test_transpose_dict)
            transposed_word_list = transposed_text.split(' ')

            for word in transposed_word_list:
                if is_word(self.valid_words, word):
                    valid_word_count += 1

            if valid_word_count > max_words:
                max_words = valid_word_count
                best_decrypt_perm = p

        decryption_dict = self.build_transpose_dict(best_decrypt_perm)

        decrypted_text = self.apply_transpose(decryption_dict)

        return decrypted_text


if __name__ == '__main__':
    start_time = time.time()
    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

    message1 = SubMessage("Hi my name is a strange dog from the planet far beyond the known universe.")
    permutation = "ouiea"
    enc_dict1 = message1.build_transpose_dict(permutation)
    print("Original message:", message1.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "###!")
    print("Actual encryption:", message1.apply_transpose(enc_dict1))
    enc_message1 = EncryptedSubMessage(message1.apply_transpose(enc_dict1))
    print("Decrypted message:", enc_message1.decrypt_message())

    time_taken = time.time() - start_time

    print('Time taken is:', str(time_taken) + 's')
    # TODO: WRITE YOUR TEST CASES HERE
