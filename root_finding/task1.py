import numpy as np
import math

##USER INPUT
##tol = float(input("Enter tolerance: "))
##maxiter = float(input("Enter maxiter: "))
##func = eval("lambda x:" + input("Enter g(x): "))
##table = input("Output table? (y or n): ")

##ITERATION FUNCTION g(x)
def fixed_point(g, x0, tol = 0.00001, maxiter = 25, table = '0'):

    x1 = 0
    iter = 0
    error = 10.0 * tol

    print("Output from fixed point:")
    if (table == '-v'):
        print("iter", end = "\t")
        print("root loc.", end = "\t")
        print("error")

    while error > tol and iter < maxiter:
        x = x0
        x1 = float(eval(g))
        error = np.abs(x1 - x0)
        if (table == '-v'):
            print(iter, end = "\t")
            print("%.10f" % x1, end = "\t")
            print("%.10f" % error)
        x0 = x1
        iter = iter + 1

    if (table != '-v'):
        print("%.10f" % x1)

def bisection(f, a, b, tol, table = '0'):
    x = a
    fa = float(eval(f))
    x = b
    fb = float(eval(f))
    n = int((np.log(tol) - np.log(b-a)) / np.log(0.5) + 1)

    print("Output from bisection: ")
    if (table == '-v'):
        print("iter", end = "\t")
        print("root loc.", end = "\t")
        print("error")

    for i in range(1,n):
        c = 0.5 * (a+b)
        x = c
        fc = float(eval(f))
        if (fa * fc < 0.0):
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        error = np.abs(b-a)
        if (table == '-v'):
            print(i, end = "\t")
            print("%.10f" % c, end = "\t")
            print("%.10f" % error)

    if (table != '-v'):
        print("%.10f" % c)

##TEST FUNCTIONS
fixed_point("x - (x * (math.e ** -x))", 1, 0.00001, 25, '-v')
##fixed_point("x + (10.14 * (math.e ** (x * x)) * math.cos(math.pi/x))", 0.1, 0.00001, 25, '-v')
bisection("x * (math.e ** -x)", -3, 7, 0.00001, '-v')
bisection("10.14 * (math.e ** (x * x)) * math.cos(math.pi/x)", -3, 7, 0.00001, '-v')

