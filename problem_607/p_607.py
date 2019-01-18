import numpy
import math
import matplotlib.pyplot as plt



x = 3.4738/(1/5*(sum([1/i for i in range(5, 10)])) - 1/10)
print(x)
alpha = 180*math.asin(50/x)/math.pi
print(alpha)

length_multipler = 10**0
d_length = length_multipler * 100*(0.5**0.5)
n_length = (100 * length_multipler - d_length)
print('d_length', d_length)

m_values = numpy.arange(0, d_length/10, 0.1 * length_multipler, dtype=float)

n_values = numpy.arange(0, d_length/(2)*(3/5), 0.5 * length_multipler, dtype=float)

def func_dm(x, i):
    output = (2*x - d_length)/(i*((d_length - x)**2 + x**2)**0.5)
    #print(i, output)
    return output

def func_dn(x, i):
    output = i*(2*x + n_length)/(10*((n_length + x)**2 + x**2)**0.5)
    #print(i, output)
    return output

def func_n(x):
    return (((n_length + x)**2 + x**2)**0.5)/10

def func_m(x, i):
    return (((d_length/5 - x)**2 + x**2)**0.5)/i

plt.plot(m_values, func_dm(m_values, 5))
plt.plot(m_values, func_dm(m_values, 6))
plt.plot(m_values, func_dm(m_values, 7))
plt.plot(m_values, func_dm(m_values, 8))
plt.plot(m_values, func_dm(m_values, 9))

plt.plot(n_values, func_dn(n_values, 1))
plt.plot(n_values, func_n(n_values))

plt.axis([0, d_length, -0.5, 0.75])
plt.grid(True)
plt.show()

def sol_finder(guess, i, scalar):
    n_cont = d_length/5
    d_sol = func_dn(guess + n_cont, 1) + func_dm(guess, i)
    guess_i = guess
    while abs(d_sol) > 10**-12:
        dn_i, dm_i = func_dn(guess_i + n_cont, 1), func_dm(guess_i, i)
        #print('stage_check', guess_i, dn_i, dm_i, sol)
        d_sol = dn_i + dm_i
        sol = func_m(guess_i, i) + func_n(guess_i + n_cont)
        #print(guess_i, guess_i - (d_sol * scalar * sol))
        guess_i = guess_i - (d_sol * scalar * sol)
        print("iteration", guess_i, dn_i, dm_i, sol, d_sol)
    return sol, guess_i, dn_i, dm_i

check = sol_finder(d_length/20, 7, 2/3)

print('check', check)

print('solution check', func_dm(check[1], 7 * length_multipler), func_dn(d_length/5 + check[1], 1), func_dm(check[1], 7 * length_multipler) + func_dn(d_length/5 + check[1], 1))

m_d_i = [10 * length_multipler, 10 * length_multipler, ((d_length/5 * length_multipler - check[1])**2 + check[1]**2)**(0.5), d_length/5, d_length/5]
n_d = ((n_length + d_length/5 + check[1])**2 + (d_length/5 + check[1])**2)**(0.5)

m_d_i_default = [10*length_multipler] * 5
n_d_default = ((n_length + d_length/2)**2 + (d_length/2)**2)**0.5

time_m = [m_d_i[i]/(5 + i) for i in range(5)]
time_n = n_d/10
time_m_default = [m_d_i_default[i]/(5 + i) for i in range(5)]
time_n_default = n_d_default/10

time_total = time_n + sum(time_m)
print(time_total, time_m, time_n)
print(sum(time_m_default) + time_n_default, time_m_default, time_n_default)

print(sum(m_d_i), n_d)
print(m_d_i[2])