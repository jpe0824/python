
import numpy as np
def GaussSeidel(A,b,x0,es=1.e-7,maxit=50):
    """
    Implements the Gauss-Seidel method
    to solve a set of linear algebraic equations
    without relaxation
    Input:
    A = coefficient matris
    b = constant vector
    x0 = Initial guess
    es = stopping criterion (default = 1.e-7)
    maxit = maximum number of iterations (default=50)
    Output:
    x = solution vector
    """
    n,m = np.shape(A)
    if n != m :
        return 'Coefficient matrix must be square'
    C = np.zeros((n,n))
    #x = np.zeros((n,1))
    for i in range(n): # set up C matrix with zeros on the diagonal
        for j in range(n):
            if i != j:
                C[i,j] = A[i,j]
    d = np.zeros((n,1))
    for i in range(n): # divide C elements by A pivots
        C[i,0:n] = C[i,0:n]/A[i,i]
        d[i] = b[i]/A[i,i]
    ea = np.zeros((n,1))
    x = np.copy(x0)
    for it in range(maxit): # Gauss-Seidel method
        xold = np.copy(x)
        for i in range(n):
            x[i] = d[i] - C[i,:].dot(x) # update the x's 1-by-1
            if x[i] != 0:
                ea[i] = abs((x[i]-xold[i])/x[i]) # compute change error
        if np.max(ea) < es: # exit for loop if stopping criterion met
            break
    if it == (maxit-1): # check for maximum iteration exit
        print(it)
        return 'maximum iterations reached'
    else:
        print("Number of iteration: ",it)
        return x
A = np.matrix(' 3. -0.1 -0.2 ; 0.1 7. -0.3 ; 0.3 -0.2 10. ')
b = np.matrix(' 7.85 ; -19.3 ; 71.4 ')
x0 = np.zeros((0,0))
x = GaussSeidel(A,b,x0)
print('Gauss Seidel Solution is\n',x)
x2 = np.linalg.solve(A,b)
print('Analytical solution is\n',x2)
