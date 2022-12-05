import math
import numpy as np

#Take necesarry input values
n = int(input("Enter the number of particles: "))
timeInstant = input("Enter the time instant: ")
tolerance = input("Enter the tolerance to terminate: ")
maxIteration = input("Enter the max number of iterations to terminate: ")

#We will use Thomas Algorithm to solve this special matrix, which is a tridiagonal system
#Creating variable arrays for the Thomas Algorithm for ease of use
#Initialise Arrays
e = np.zeros(n)
f = np.zeros(n)
g = np.zeros(n)

#Fill Them up
e.fill(1)
f.fill(-2)
g.fill(1)
e[0] = 0
f[0] = 1
f[n-1] = 1
g[n-1] = 0

print(" e values are: ")
print(e)
print(" f values are: ")
print(f)    
print(" g values are: ")
print(g)