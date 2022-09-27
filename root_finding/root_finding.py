import numpy as np
import math

##FUNCTIONAL ITERATION
def functional_iteration(g, x0, tol, maxiter, table = '0'):
    ##MAIN LOOP
    iter = 0
    error = 10.0 * tol

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
        else:
            print(x1)
        x0 = x1
        iter = iter + 1
               
    return x0

##BISECTION
def bisect(f, a, b, tol, maxiter, table = '0'):

    x = a
    fa = float(eval(f))
    x = b
    fb = float(eval(f))
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
    return c

##NEWTON'S METHOD
def newtons(f, fDeriv, x0, tol, maxiter, table = '0'):

    x = x0
    f0 = float(eval(f))
    fDeriv0 = float(eval(fDeriv))
    error = 10.0 * tol
    iter = 0
    skip = 0
    x1 = 0

    print("Output from Newton's Method:")
    if (table == '-v'):
        print("iter", end = "\t")
        print("root loc.", end = "\t")
        print("error")

    while error > tol and iter < maxiter:
        if (fDeriv0 != 0):
            x1 = x0 - f0/fDeriv0
        else:
            print("ERROR: f'(0) = 0, cannot divide by 0, select new x0")
            skip = 1
            break
        error = abs(x1 - x0)
        x0 = x1
        x = x1
        f0 = float(eval(f))
        fDeriv0 = float(eval(fDeriv))
        iter += 1
        if (table == '-v' and skip != 1):
            print(iter, end = "\t")
            print("%.10f" % x1, end = "\t")
            print("%.10f" % error)

    if (table != '-v' and skip != 1):
        print("%.10f" % x1)

    if x1:
        return x1

##SECANT METHOD
def secant(f, x0, x1, tol, maxiter, table = '0'):

    x = x0
    f0 = float(eval(f))
    x = x1
    f1 = float(eval(f))
    error = 10.0 * tol
    iter = 0

    print("Output from Secant Method:")
    if (table == '-v'):
        print("iter", end = "\t")
        print("root loc.", end = "\t")
        print("error")

    while error > tol and iter < maxiter:
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        error = abs(x2 - x1)
        x0 = x1
        x1 = x2
        f0 = f1
        x = x1
        f1 = float(eval(f))
        iter += 1
        if (table == '-v'):
            print(iter, end = "\t")
            print("%.10f" % x2, end = "\t")
            print("%.10f" % error)

    if (table != '-v'):
        print("%.10f" % x2)

    return x1

##HYBRID BISECTION/NEWTON'S METHOD
def bisect_newton(f, fDeriv, x0, a, b, tol, maxiter, table = '0'):

    x = x0
    f0 = float(eval(f))
    fDeriv0 = float(eval(fDeriv))
    error = 10.0 * tol
    iter = 0
    skip = 0
    x1 = 0

    print("Output from Bisect/Newton's Hybrid Method:")
    if (table == '-v'):
        print("iter", end = "\t")
        print("root loc.", end = "\t")
        print("error")

    while error > tol and iter < maxiter:
        if (fDeriv0 != 0):
            x1 = x0 - f0/fDeriv0
        else:
            print("ERROR: f'(0) = 0, cannot divide by 0, select new x0")
            skip = 1
            break
        newterror = abs(x1 - x0)
        if (newterror > error):
            x = a
            fa = float(eval(f))
            x = b
            fb = float(eval(f))
            for i in range(1,4):
                c = 0.5 * (b + a)
                x = c
                fc = float(eval(f))
                if (fa * fc < 0.0):
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc
            error = abs(b-a)
        else:
            x0 = x1
            error = newterror
        iter += 1
            
        if (table == '-v' and skip != 1):
            print(iter, end = "\t")
            print("%.10f" % x1, end = "\t")
            print("%.10f" % error)

    if (table != '-v' and skip != 1):
        print("%.10f" % x1)

    if x1:
        return x1

##HYBRID BISECTION/SECANT METHOD
def bisect_secant(f, x0, x1, a, b, tol, maxiter, table = '0'):

    x = x0
    f0 = float(eval(f))
    x = x1
    f1 = float(eval(f))
    error = 10.0 * tol
    iter = 0

    print("Output from Bisect/Secant Hybrid Method:")
    if (table == '-v'):
        print("iter", end = "\t")
        print("root loc.", end = "\t")
        print("error")

    while error > tol and iter < maxiter:
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        secanterror = abs(x2 - x1)
        if (secanterror > error):
            x = a
            fa = float(eval(f))
            x = b
            fb = float(eval(f))
            for i in range(1,4):
                c = 0.5 * (b + a)
                x = c
                fc = float(eval(f))
                if (fa * fc < 0.0):
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc
            error = abs(b-a)
        else:
            x0 = x1
            x1 = x2
            f0 = f1
            x = x1
            f1 = float(eval(f))
            error = secanterror
        iter += 1
            
        if (table == '-v'):
            print(iter, end = "\t")
            print("%.10f" % x1, end = "\t")
            print("%.10f" % error)

    if (table != '-v'):
        print("%.10f" % x1)

    return x1

##TEST ALGORITHMS
#fval = functional_iteration("x - x*x - 4.1", 1, 0.1, 25, '-v')
#fval = bisect("x*x - 4.1", 1.9, 4.2, 0.0001, 25, '-v')
fval = newtons("x * (math.e ** -x)", "(math.e ** -x) - x * (math.e ** -x)", -1, 0.00001, 25)
fval = secant("x * (math.e ** -x)", -1, 1, 0.0001, 25)
fval = bisect_newton("10.14 * math.e**(x * x) * math.cos(math.pi/x)", "10.14*(2 * x * math.e**(x * x) * math.cos(math.pi/x) + (math.pi * math.e**(x * x) * math.sin(math.pi/x))/(x * x))", -1, -3, 7, 0.0001, 25, '-v')
fval = bisect_secant("10.14 * math.e**(x * x) * math.cos(math.pi/x)", -2, 0.25, -3, 7, 0.00001, 25, '-v')
