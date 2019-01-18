"""Using numpy and scipy.optimize did not produce required significant figure accuracy. Unable to use larger
floating point decimals..."""

import numpy as np
from scipy.optimize import minimize
from scipy.optimize import LinearConstraint
length_multi = 10**3


def rosen(x):
    print(100.0*(x[1:]-x[:-1]**2.0)**2 + (1-x[:-1])**2.0)
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2 + (1-x[:-1])**2.0)

def path_problem(y):
    l_total = 100 * length_multi
    d = ((l_total/2.0)**2 * 2)**0.5
    n = l_total - d
    # print(y)
    return (((n + sum(y))**2 + sum(y)**2)**0.5)/10 + (((d/5.0 - y[0])**2 + y[0]**2)**0.5)/5 +\
           (((d/5.0 - y[1])**2 + y[1]**2)**0.5)/6 + (((d/5.0 - y[2])**2 + y[2]**2)**0.5)/7 + \
           (((d/5.0 - y[3])**2 + y[3]**2)**0.5)/8 + (((d/5.0 - y[4])**2 + y[4]**2)**0.5)/9


x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
#res = minimize(rosen, x0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True})


y0 = length_multi * np.array([6.0, 6.0, 4.0, 1.0, 0.0])
print(y0)
bnds = [(0, None) for i in range(y0.shape[0])]
print(bnds)
res_1 = minimize(path_problem, y0, method='L-BFGS-B', bounds=bnds, tol=10**-16,
               options={'disp': True, 'maxiter': 10**5})

res_2 = minimize(path_problem, y0, method='TNC', bounds=bnds, tol=10**-16,
               options={'disp': True, 'maxiter': 10**5})

res_3 = minimize(path_problem, y0, method='SLSQP', bounds=bnds, tol=10**-16,
               options={'disp': True, 'maxiter': 10**5})

#res_4 = minimize(path_problem, y0, method='trust-constr', bounds=bnds, tol=10**-16,
#               options={'disp': True, 'maxiter': 10**5})

print(y0)