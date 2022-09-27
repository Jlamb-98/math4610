# Newton's Method for Root Finding
**Routine Name:** secant          

**Author:** Joseph Lamb

**Language:** Python

**Description/Purpose:** This routine estimates the root values of a given function f using the Secant Method of approximation. 

**Input:** The function (f), two initial guesses for the root (x0 and x1), tolerance for the error (tol), maximum number of iterations for the loop to perform (maxiter), and a request for the iterations to be displayed in a table (table).

**Output:** The approximate root of the function given. A table of each iteration leading to the final result can be requested.

**Usage/Example:** For the function $x * e^(-x)$, the routine can be called like so:

 `fval = secant("x * (math.e ** -x)", -1, 1, 0.00001, 25, '-v')`

This would result in the output:

```
Output from Secant Method:
iter	root loc.	error
1	0.7615941560	0.2384058440
2	-6.1451151921	6.9067093480
3	0.7607373842	6.9058525763
4	0.7598809491	0.0008564352
5	-2.4117305198	3.1716114688
6	0.7185207502	3.1302512700
7	0.6782842465	0.0402365037
8	-1.6152103159	2.2934945624
9	0.5850439821	2.2002542980
10	0.5001671785	0.0848768036
11	-0.6389152674	1.1390824459
12	0.2719161660	0.9108314334
13	0.1387967231	0.1331194429
14	-0.0474062702	0.1862029934
15	0.0068740986	0.0542803688
16	0.0003193255	0.0065547731
17	-0.0000022030	0.0003215285
18	0.0000000007	0.0000022037
```

The final approximate root location is saved into `fval`. Removing the final parameter `'-v'` would output only the final root location approximate:

```
Output from Secant Method:
0.0000000007
```

**Implementation/Code:** The following is the code for newton()

```
import numpy as np
import math

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

```

**Last Modified:** September/2022
