import collections

a_hand = [1, 2, 3, 3, 3, 3]

print(collections.Counter(a_hand).most_common(1)[0][0])
