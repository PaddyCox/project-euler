from functools import reduce
from operator import mul
import timeit


class Problem110:
    def __init__(self, dict_pf):
        self.dict_pf = dict_pf
        self.unique_factors = list(set(sorted([pf for pf in dict_pf if dict_pf[pf] != 0])))
        self.num_unique_factors = len(self.unique_factors)
        self.dict_pf_2 = {pf: self.dict_pf[pf] * 2 for pf in self.unique_factors}
        self.diophantine_solutions = 0
        self.max_n = reduce(mul, [x ** dict_pf[x] for x in dict_pf])

    def diophantine_reciprocals(self, pf_i, total):
        if total <= self.max_n:
            self.diophantine_solutions += 1
            for i in range(pf_i, self.num_unique_factors):
                current_pf = self.unique_factors[i]
                count_pf = self.dict_pf_2[current_pf]
                for j in range(1, count_pf + 1):
                    self.diophantine_reciprocals(i + 1, total * (current_pf ** j))

    def answer(self):
        self.diophantine_reciprocals(0, 1)

        return self.diophantine_solutions, self.max_n


def di_sol(dict):
    n = 1
    initial_sol = 1
    sum_a = []
    for d in dict:
        if dict[d] > 0:
            initial_sol *= 3
            initial_sol -= 1
            sum_a.append(dict[d] - 1)
            n *= d ** dict[d]
    for j in sum_a:
        initial_sol += j * (initial_sol - (initial_sol + 1)//3)
    return initial_sol, n

def di_sol_class(dict):
    ans = Problem110(dict).answer()
    return ans

test_dict = {2:2, 3:2, 5:2, 7:1}

if __name__ == "__main__":
    print(timeit.timeit("di_sol_class(test_dict)", "from __main__ import di_sol_class, test_dict", number=100))

if __name__ == "__main__":
    print(timeit.timeit("di_sol(test_dict)", "from __main__ import di_sol, test_dict", number=100))


print(di_sol(test_dict))
print(di_sol_class(test_dict))
print(di_sol_class({2:1, 3:1, 5:1, 7:0}))
print(di_sol_class({2:1, 3:1, 5:1, 7:1}))