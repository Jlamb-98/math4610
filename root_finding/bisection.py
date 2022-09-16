import numpy as np

##CONSTANTS
e = 2.718281828459045
pi = 3.141592653589793

##DEFAULT VALUES
tol = 0.000001
error = 10.0 * tol
maxiter = 25
func = 0
table = user = 'y'

##USER INPUT
##tol = float(input("Enter tolerance: "))
##maxiter = float(input("Enter maxiter: "))
##func = eval("lambda x:" + input("Enter f(x): "))
##table = input("Output table? (y or n): ")
##a = float(input("Enter a: "))
##b = float(input("Enter b: "))
a = -3
b = 7
##FUNCTION f(x)
def f(x):
    if (func):
        fval = func(x)
    else:
        fval = x * (e ** -x)
    return fval

fa = f(a)
fb = f(b)
n = int((np.log(tol) - np.log(b-a)) / np.log(0.5) + 1)

for i in range(1,n):
    c = 0.5 * (a+b)
    print("%.10f" % c)
    fc = f(c)
    if (fa * fc < 0.0):
        b = c
        fb = fc
    else:
        a = c
        fa = fc

print(c)

