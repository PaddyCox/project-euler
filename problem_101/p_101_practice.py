from numpy import polyfit, polyval

x = [1, 2, 3, 4, 5]
y = [i**3 for i in x]

class Generator:
    def __init__(self, n):
        self.n = n
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def func_n(self, x):
        return x**3

    def next(self):
        if self.num <= self.n:
            x, self.num = self.num, self.num + 1
            return self.func_n(x)
        else:
            raise StopIteration

print(list(Generator(5)))

print(x, y)

second_order = (polyfit(x, y, 1))

print(second_order)

sum_fit = 0

for i in range(1, 4):
    x_samples = x[0:i]
    y_samples = y[0:i]
    op_func = polyfit(x_samples, y_samples, i-1)
    fit_i = int(polyval(op_func, i+1)+0.5)
    sum_fit += fit_i
    print(fit_i, sum_fit)
