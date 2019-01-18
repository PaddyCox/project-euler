import matplotlib.pyplot as plt
import scipy.integrate as s_integrate
from math import pi
from numpy import arctan2

def p_integrate(f, a, b, dx=1.0):
    i = a
    s = 0
    while i < b:
        s+= f(i) * dx
        i += dx
    return s


def x_squared(x):
    return x**2

def p_dbl_integrate(f, x_a, x_b, dx=1.0):
    i = x_a
    count = 0
    s = 0
    while i < x_b:
        j = 0.0
        while j < (3 - (3 * i / 4.0)):
            s += f(i, j)
            count += 1
            j += dx
        i += dx
    return (s/count)


def x_squared(x):
    return x**2

print(p_integrate(x_squared, 0, 10, dx=0.01))

dx_samples = [1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001]

integral_result = [p_integrate(x_squared, 0, 10, dx=i) for i in dx_samples]

plt.plot(dx_samples, integral_result, 'ro')
plt.axis([0, 1, 280, 350])
# plt.show()

s_test = s_integrate.quad(lambda x: x_squared(x), 0, 10)

print(s_test)

# Solution beneath this point

s_test = s_integrate.dblquad(lambda y, x: 5 * x * y, 0, 4, lambda x: 0, lambda x: 3 - 3 * x / 4)

s_answer = s_integrate.dblquad(lambda y, x: 3/4 - 1/(2 * pi) * (arctan2(3 - y, x) + arctan2(4 - x, y)), 0, 4, lambda x: 0, lambda x: 3 - 3 * x / 4)

s_answer_2 = s_integrate.dblquad(lambda y, x: 1/4 + 1/(2 * pi) * (arctan2(y, 4 - x) + arctan2(x, 3-y)), 0, 4, lambda x: 0, lambda x: 3 - 3 * x / 4)

s_answer_4i = s_integrate.dblquad(lambda y, x: 1/(2 * pi) * (arctan2(y, 4 - x)), 0, 4, lambda x: 0, lambda x: 3 - 3 * x / 4)

s_answer_4ii = s_integrate.dblquad(lambda y, x: 1/(2 * pi) * (arctan2(x, 3 - y)), 0, 4, lambda x: 0, lambda x: 3 - 3 * x / 4)

s_answer_4iii = s_integrate.dblquad(lambda y, x: 1/4, 0, 4, lambda x: 0, lambda x: 3 - 3 * x / 4)

def f(x, y):
    return 1/4 + 1/(2 * pi) * (arctan2(y, 4 - x) + arctan2(x, 3-y))

def f1(x, y):
    return 1/(2 * pi) * (arctan2(y, 4 - x))

def f2(x, y):
    return 1/(2 * pi) * (arctan2(x, 3-y))

def bounds_x():
    return [2, 4]

def bounds_y(x):
    return [0, 3 - (3 * x)/4]

s_answer_3 = s_integrate.nquad(f, [bounds_y, bounds_x])

print(s_test)
x_1 = 3.9
y_1 = 0
print('ANGLES', arctan2(y_1, 4 - x_1)*(180/pi), arctan2(x_1, 3-y_1)*(180/pi))
print(s_answer, s_answer[0]/6.0)
print('a2', s_answer_2, s_answer_2[0]/6.0)
print('a3', s_answer_3, s_answer_3[0]/(6/16))

print(f(3, 3-(9/4)))

print(s_answer_4i)
print(s_answer_4ii)
print(s_answer_4iii)
print('c_a', s_answer_4i[0]/6.0, s_answer_4ii[0]/6.0, s_answer_4iii[0]/6.0, (s_answer_4i[0] + s_answer_4ii[0] + s_answer_4iii[0])/6.0)

print(p_dbl_integrate(f, 0, 4, dx=0.01))
print(p_dbl_integrate(f1, 0, 4, dx=0.01))
print(p_dbl_integrate(f2, 0, 4, dx=0.01))