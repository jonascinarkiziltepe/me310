import math
import numpy as np

print(math.pi)

#Take necesarry input values
n = int(input("Enter the number of particles: "))
timeInstant = float(input("Enter the time instant: "))
tolerance = int(input("Enter the tolerance to terminate: "))
maxIteration = int(input("Enter the max number of iterations to terminate: "))

#For Gauss Elimination We will use Thomas Algorithm to solve this special matrix, which is a tridiagonal system
#Creating variable arrays for the Thomas Algorithm for ease of use
#Initialise Arrays
a = np.zeros(n)
b = np.zeros(n)
c = np.zeros(n)
d = np.zeros(n)

#Fill Them up
a.fill(1)
b.fill(-2)
c.fill(1)
a[0] = 0
c[0] = 0
b[0] = 1
b[n-1] = 1
a[n-1] = 0
c[n-1] = 0
d[0] = float(0.25 * math.sin(math.pi * timeInstant))
d[n-1] = 1

#Debug

print(" a values are: ")
print(a)
print(" b values are: ")
print(b)    
print(" c values are: ")
print(c)
print(" Position values are: ")
print(d)


def gaussEliminationMethod(ag, bg, cg, dg):
#Attention Points
# -Index of a array and c array values 
# Because a values start from i = 1 instead of i = 0

    #Loops for Forward Elimination
    for i in range(cg.size):
        print("cg iteration number: " + str(i))
        if i == 0:
            #print(cg[int(i)])
            cg[i] = cg[i]/bg[i]
            #print("cg " + str(i) + " is now: " + str(cg[i]))
            print(" CG ARRAY IS ")
            print(cg)  
        else:
            lam = bg[i] - (cg[i-1]*ag[i])
            cg[i] = cg[i] / lam
            #print("cg " + str(i) + " is now: " + str(cg[i]))
            print("ag value is " + str(ag[i]))
            print(" CG ARRAY IS ")
            print(cg)  
    cg[cg.size-1] = 1

    for i in range(dg.size):
        print("dg iteration number: " + str(i))
        if i == 0:
            dg[i] = dg[i]/bg[i]
            print("dg " + str(i) + " is now: " + str(dg[i]))
        else:
            dg[i] = (dg[i] - (dg[i - 1] * ag[i])) / (bg[i] - (cg[i - 1] * ag[i]) )
            print("dg " + str(i) + " is now: " + str(dg[i]))

    #Back Substitution
    #Check index of cg
    roots = np.zeros(n)
    for i in range(dg.size):
        print("root iteration number: " + str(i))
        if i == 0:
            roots[n-i-1] = dg[n-i-1]
        else:
            roots[n-i-1] = dg[n-i-1] - (cg[n-i-1]*roots[n-i])
        print("root " + str(n-1-i) + " is now: " + str(roots[n-i-1]))

    return roots

#print(gaussEliminationMethod(a,b,c,d))

def gaussSeidel (ags,bgs,cgs,dgs): 
    return 0




def gauss_seidel(A, b, x, max_iterations=100, tolerance=1e-5):
  """
  Solves the linear system Ax = b using the Gauss-Seidel method.

  Args:
    A: A square matrix of coefficients, as a 2D NumPy array.
    b: The right-hand side vector, as a 1D NumPy array.
    x: The initial guess for the solution, as a 1D NumPy array.
    max_iterations: The maximum number of iterations to perform (default: 100).
    tolerance: The convergence tolerance (default: 1e-5).

  Returns:
    The final solution, as a 1D NumPy array.
  """
  n = len(A)

  for i in range(max_iterations):
    x_prev = x.copy()

    for j in range(n):
      s1 = sum(A[j][k] * x[k] for k in range(j))
      s2 = sum(A[j][k] * x_prev[k] for k in range(j + 1, n))
      x[j] = (b[j] - s1 - s2) / A[j][j]

    if np.allclose(x, x_prev, rtol=tolerance):
      return x

  return x


A = np.array([[4, 1, 2], [3, 5, 6], [1, 3, 4]])
b = np.array([1, 2, 3])
x = np.array([0, 0, 0])

x_final = gauss_seidel(A, b, x)