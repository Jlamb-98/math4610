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
##func = eval("lambda x:" + input("Enter g(x): "))
##table = input("Output table? (y or n): ")

##ITERATION FUNCTION g(x)
def g(x):
    if (func):
        gval = x - func(x)
    else:
        gval = x - (0.1)*(x * (e ** -x))
    return gval

x0 = float(input("Enter x0: "))
##MAIN LOOP
while (user == 'y'):
    x1 = 0
    iter = 0
    error = 10.0 * tol

    print("iter", end = "\t")
    print("root loc.", end = "\t")
    print("error")

    while error > tol and iter < maxiter:
        x1 = g(x0)
        error = np.abs(x1 - x0)
        if (table == 'y'):
            print(iter, end = "\t")
            print("%.10f" % x1, end = "\t")
            print("%.10f" % error)
        elif (table == 'n'):
            print(x1)
        x0 = x1
        iter = iter + 1

    x0 = float(input("Enter x0 (n to exit): "))
               
##  user = input("Try another x0? (y or n): ")
    
