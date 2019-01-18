from numpy import polyfit, polyval

x = [i for i in range(1, 12)]
y = [1 - j + j ** 2 - j ** 3 + j ** 4 - j ** 5 + j ** 6 - j ** 7 + j ** 8 - j ** 9 + j ** 10 for j in x]


print(x, y)

sum_fit = 0

for i in range(1, 11):
    x_samples = x[0:i]
    y_samples = y[0:i]
    op_func = polyfit(x_samples, y_samples, i-1)
    fit_i = int(polyval(op_func, i + 1) + 0.5)
    sum_fit += fit_i
    print(fit_i, sum_fit)