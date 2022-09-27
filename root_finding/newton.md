# Newton's Method for Root Finding
**Routine Name:** newtons          

**Author:** Joseph Lamb

**Language:** Python

**Description/Purpose:** This routine estimates the root values of a given function f using Newton's Method of approximation. 

**Input:** The function (f) and its derivative (fDeriv), an initial guess for the root (x0), tolerance for the error (tol), maximum number of iterations for the loop to perform (maxiter), and a request for the iterations to be displayed in a table (table).

**Output:** The approximate root of the function given. A table of each iteration leading to the final result can be requested.

**Usage/Example:** For the function $x * e^(-x)$, the routine can be called like so:

 `fval = newtons("x * (math.e ** -x)", "(math.e ** -x) - x * (math.e ** -x)", -1, 0.00001, 25, '-v')`

This would result in the output:

```
Output from Newton's Method:
iter	root loc.	error
1	-0.5000000000	0.5000000000
2	-0.1666666667	0.3333333333
3	-0.0238095238	0.1428571429
4	-0.0005537099	0.0232558140
5	-0.0000003064	0.0005534034
6	-0.0000000000	0.0000003064
```

The final approximate root location is saved into `fval`. Removing the final parameter `'-v'` would output only the final root location approximate:

```
Output from Newton's Method:
-0.0000000000
```

**Implementation/Code:** The following is the code for newton()

```
import numpy as np
import math

def newtons(f, fDeriv, x0, tol, maxiter, table = '0'):

    x = x0
    f0 = float(eval(f))
    fDeriv0 = float(eval(fDeriv))
    error = 10.0 * tol
    iter = 0

    print("Output from Newton's Method:")
    if (table == '-v'):
        print("iter", end = "\t")
        print("root loc.", end = "\t")
        print("error")

    while error > tol and iter < maxiter:
        x1 = x0 - f0/fDeriv0
        error = abs(x1 - x0)
        x0 = x1
        x = x1
        f0 = float(eval(f))
        fDeriv0 = float(eval(fDeriv))
        iter += 1
        if (table == '-v'):
            print(iter, end = "\t")
            print("%.10f" % x1, end = "\t")
            print("%.10f" % error)

    if (table != '-v'):
        print("%.10f" % x1)
```

**Last Modified:** September/2022
