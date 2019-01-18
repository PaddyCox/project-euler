import re
from collections import Counter
from collections import defaultdict as ddict

with open('p098_words.txt', 'r') as words:
    word_list = re.sub('"', '', words.read()).split(',')

char_words = ddict(list)

word_chars = [''.join(sorted(list(s))) for s in word_list]

for word in word_list:
    char_words[''.join(sorted(list(word)))].append(word)

anagram_words = {k: v for k, v in char_words.items() if len(v) > 1}

print(len(anagram_words), anagram_words)

"""def match_squares(e):

    for"""