import timeit

dict_a = {'a': 0}
dict_b = {'b': 1}
dict_a.update(dict_b)

print(dict_a)

print(sum(dict_a.values()))