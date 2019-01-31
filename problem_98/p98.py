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

def sub_check(n, w1, w2):
    str_n = str(n)
    inv_n = ''
    for l in w2:
        inv_n += str_n[w1.index(l)]

    return int(inv_n)

def same_check(n, s):
    sn = str(n)
    if len(sn) != len(s):
        return False
    for i in range(len(sn)):
        if sn.count(sn[i]) != s.count(s[i]):
            return False
    return True

print(same_check(21174, 'apple'))




print(sub_check(126356, "apples", "lappes"))

print(sub_check(1296, "care", "race"))

for s in range (int(10 ** (9/2)), 1, -1):
    sq = s ** 2
    for d in anagram_words:
        for w in anagram_words[d]:
            if same_check(sq, w):
                for w_2 in anagram_words[d]:
                    if w_2 != w:
                        sq_2 = sub_check(sq, w, w_2)
                        if sq_2 ** 0.5 % 1 == 0:
                            print(sq, sq_2, w, w_2)



print('abababab'.index('a'))