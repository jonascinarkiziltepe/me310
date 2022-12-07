import math
import numpy as np
import matplotlib.pyplot as plt


#Take necesarry input values
n = int(input("Enter the number of particles: "))
timeInstant = float(input("Enter the time instant: "))
tolerance = float(input("Enter the tolerance to terminate: "))
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


def gaussEliminationMethod(ag, bg, cg, dg):
#Attention Points
# -Index of a array and c array values 
# Because a values start from i = 1 instead of i = 0

    #Loops for Forward Elimination
    for i in range(cg.size):
        #print("cg iteration number: " + str(i))
        if i == 0:
            #print(cg[int(i)])
            cg[i] = cg[i]/bg[i]
            #print("cg " + str(i) + " is now: " + str(cg[i]))
            #print(" CG ARRAY IS ")
            #print(cg)  
        else:
            lam = bg[i] - (cg[i-1]*ag[i])
            cg[i] = cg[i] / lam
            #print("cg " + str(i) + " is now: " + str(cg[i]))
            #print("ag value is " + str(ag[i]))
            #print(" CG ARRAY IS ")
            #print(cg)  
    cg[cg.size-1] = 1

    for i in range(dg.size):
        #print("dg iteration number: " + str(i))
        if i == 0:
            dg[i] = dg[i]/bg[i]
            #print("dg " + str(i) + " is now: " + str(dg[i]))
        else:
            dg[i] = (dg[i] - (dg[i - 1] * ag[i])) / (bg[i] - (cg[i - 1] * ag[i]) )
            #print("dg " + str(i) + " is now: " + str(dg[i]))

    #Back Substitution
    #Check index of cg
    roots = np.zeros(n)
    for i in range(dg.size):
        #print("root iteration number: " + str(i))
        if i == 0:
            roots[n-i-1] = dg[n-i-1]
        else:
            roots[n-i-1] = dg[n-i-1] - (cg[n-i-1]*roots[n-i])
        #print("root " + str(n-1-i) + " is now: " + str(roots[n-i-1]))

    
    return roots

#print(gaussEliminationMethod(a,b,c,d))

def gaussSeidel (dgs, tolerance_goal, iteration_max):

  x = np.copy(dgs)
  xprev = np.copy(x)
  errors = np.zeros(x.size)
  error_check = np.zeros(x.size)
  error_check[0] = 1
  error_check[x.size - 1] = 1
  

  for i in range(iteration_max):
    error_sum = 0
    #print("Xprev = " + str(xprev))
    for j in range(1,dgs.size-1):
      xprev[j] = x[j]  
      x[j] = (dgs[j] - x[j-1] - x[j+1])/(-2)
      errors[j] = 100*(x[j] - xprev[j])/x[j]
    for j in range(errors.size):
        if errors[j] < tolerance_goal:
            error_check[j] = 1
        else:
            error_check[j] = 0
    error_sum = np.sum(error_check)
    
    if error_sum >= x.size:
        print("Reached goal")
        print("iteration number: " + str(i))
        print(errors)
        return x
          
  print("errors is")
  print(errors)


  return x



gauss_seidel_roots = gaussSeidel(d,tolerance,maxIteration)
print("Result from gauss seidel is: ")
print(gauss_seidel_roots)
plt.plot(gauss_seidel_roots, 'ro')
plt.ylabel("Position")
plt.xlabel("Particle Number")
plt.title("Gauss-Seidel Plot N=5, t=1.5 ")
plt.show()


gauss_elim_roots = gaussEliminationMethod(a,b,c,d)
print("Result from gauss Elimination is: ")
print(gauss_elim_roots)

plt.plot(gauss_elim_roots, 'ro')
plt.ylabel("Position")
plt.xlabel("Particle Number")
plt.title("Gauss Elimination Plot N=5, t=1.5 ")
plt.show()