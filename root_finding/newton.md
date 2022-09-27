# Newton's Method for Root Finding
**Routine Name:** newtons          

**Author:** Joseph Lamb

**Language:** Python

**Description/Purpose:** This routine estimates the root values of a given function f using Newton's Method of approximation. 

**Input:** The function (f) and its derivative (fDeriv), an initial guess for the root (x0), tolerance for the error (tol), maximum number of iterations for the loop to perform (maxiter), and a request for the iterations to be displayed in a table (table).

**Output:** The approximate root of the function given. A table of each iteration leading to the final result can be requested.

**Usage/Example:** For the function $x * e^-x$, the routine can be called like so:

 `fval = newtons("x * (math.e ** -x)", "(math.e ** -x) - x * (math.e ** -x)", -1, 0.00001, 25, '-v')`



**Implementation/Code:** 

**Last Modified:** September/2022
