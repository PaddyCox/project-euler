import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

d_mult = 1

d = (((100*d_mult)/2)**2 * 2)**0.5
n = 100*d_mult - d
d_i = d/5

def m_solve(a, v):
    """Determine time taken to cross marsh with vertical displacement a, speed dx"""
    a *= d_mult
    return (((d_i - a)**2 + a**2)**0.5)/v

def dm_solve(a, v):
    a *= d_mult
    return (2*a - d_i)/(v*((d_i - a)**2 + a**2)**0.5)

def dmc_solve(c, v):
    c *= d_mult
    return (2 * c + d_i) / (v * ((d_i + c) ** 2 + c ** 2) ** 0.5)

def a_solve(dm, v):
    return 1/(sqrt(1/2)*sqrt(d_i**2/(2*dm*v**2) - d_i**2/2) - d_i/(sqrt(2)))

def dn_solve(A, v):
    A *= d_mult
    return (2*A + n)/(v*((n + A)**2 + A**2)**0.5)

#def


m_array = np.arange(0, d/10, 0.1, dtype=float)
n_array = np.arange(0, d/2, 0.1, dtype=float)

plt.plot(n_array, dmc_solve(n_array, 9))
plt.plot(m_array, dm_solve(m_array, 5))
plt.plot(m_array, dm_solve(m_array, 6))
plt.plot(m_array, dm_solve(m_array, 7))
plt.plot(m_array, dm_solve(m_array, 8))
plt.plot(m_array, dm_solve(m_array, 9))


"""plt.plot(m_array, m_solve(m_array, 5))
plt.plot(m_array, m_solve(m_array, 6))
plt.plot(m_array, m_solve(m_array, 7))
plt.plot(m_array, m_solve(m_array, 8))
plt.plot(m_array, m_solve(m_array, 9))"""

plt.plot(n_array, dn_solve(n_array, 10))
plt.plot(m_array,  len(m_array)*[-0.1357196689091694], color='k')
plt.plot(m_array,  len(m_array)*[-0.11013390195151529], color='k')


plt.axis([-1, d/2, -2, 3])
plt.grid(True)
plt.show()

for i in range(5, 10):
    print(i, [dm_solve(x/100*d, i) for x in range(0, 11)])

for i in range(0, 11):
    print(i, dn_solve(d * i/20, 10))