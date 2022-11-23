
#import functions
from tkinter.filedialog import Open
from types import NoneType
import f as f
import math
import os

# Structure for input.txt
# x_low
# x_up
# error_set
# iteration_max

# Reading input

 #Open the input file
input_file = open("input.txt", "r")

#read line by line
x_low = float(input_file.readline())
x_up = float(input_file.readline())
error_set = float(input_file.readline())
iteration_max = float(input_file.readline()) 

#debug
print(x_low, x_up, error_set, iteration_max)

#The arrays here will be used for easy and automatic plotting.
newton_Errors = []
secant_Errors = []
polynomial_Errors = []
bisection_Errors = []
falsepos_Errors = []
newton_Roots = []
secant_Roots = []
polynomial_Roots = []
bisection_Roots = []
falsepos_Roots = []

# Define the sign function to get sign of b
def sign(b):
  if b >= 0:
    return 1
  else: 
    return -1

# Error Calculation
def calculate_error (x_current, x_previous):
  E_a = (x_current - x_previous)/(x_current)
  E_a = E_a * 100
  return abs(E_a)


# The Methods


# The new polynomial method

def poly(x_l,x_u):
  x_r = 0
  i = 0
  current_error = 1000
  x_prev = 0
  # loop start
  while i <3 or current_error > error_set :
    x_i = (x_u + x_l)/2
 

    fxl=f.f(x_l)
    fxu=f.f(x_u)
    fxi=f.f(x_i)


    poly_a = ((fxl - fxi)/((x_l - x_i)*(x_l - x_u))) + ((fxi - fxu)/((x_u - x_i)*(x_l-x_u)))
    poly_b = (((fxl-fxi)*(x_i-x_u))/((x_l-x_i)*(x_l-x_u)))-(((fxi-fxu)*(x_l-x_i))/((x_u-x_i)*(x_l-x_u))) 

    poly_c = fxi

    x_r = x_i - ((2*poly_c)/(poly_b + sign(poly_b)*(math.sqrt(poly_b*poly_b - 4*poly_a*poly_c))))

    fxr = f.f(x_r)

    if fxl*fxr < 0 :
      x_u = x_r
    elif fxl*fxr > 0 :
      x_l =x_r
    else:
      #x_r is the root
      print(str(x_r) + " is the root")
      break
    
    #to calculate error after the first iteration
    if i > 1:
      current_error = calculate_error(x_r,x_prev)
    x_prev = x_r
    print( "Current iteration " + str(i) )
    print("Current Error " + str(current_error))
    print( "Current x_r is " + str(x_r))
    i = i+1
    if i >= iteration_max:
      break

  print("Total iteration " + str(i))
  print("The root is " + str(x_r))
  print(" Last Error is " + str(current_error))


#poly(x_low,x_up)

#bisection method
def bisection(x_l,x_u):
  x_prev = 0
  i= 1
  current_error = 1000

  #ensure that there is a sign change between guesses
  if x_l*x_u >= 0:
    print("Invalid initial guess")
    return 0

  while i<30 :
    x_r = (x_l + x_u)/2
    fxl = f.f(x_l)
    fxu = f.f(x_u)
    fxr = f.f(x_r)
    print(fxl)
    print(fxu)
    print(fxr)
    print(x_r)


    if fxl*fxr < 0:
      x_u = x_r
    elif fxu*fxr < 0:
      x_l = x_r
    elif fxr == 0:
      print("The root is " + str(x_r))
      break
    else:
      print(fxu*fxr)
      print(fxl*fxr)
      print("There are no single roots in the interval") 
      break

    if i > 1:
      current_error = calculate_error(x_r,x_prev)
    if current_error < error_set:
      break

  print("The root is " + str(x_r))
  print("Last Error is "+ str(current_error))
  return x_r
  

#bisection(x_low,x_up)

def new_bisection(xl, xu, it_Max, error_Goal, xprev = 500, i = 0, bisectionOutput = None ):

  if i == 0: #Initialization
    bisectionOutput = open("output_bisection.txt", "w")

  if it_Max == i or it_Max < i :
    print("Max iteration reached")
    bisectionOutput.close() #Close output file
    return 0 #Terminate function

  i = i+1
  
  if sign(f.f(xl)) == sign(f.f(xu)):
    raise Exception(" No sign change between the points ")
  
  xi = (xl + xu)/2

  if i == 1:
    approxError = "---"
  else:
    approxError = calculate_error(xi,xprev)
    if approxError < error_Goal:
      print("Error tolerance goal reached")
      print("Last approx error is " + str(approxError))
      return 0 

  xprev = xi
  #debug
  print("xi is " + xi)

  if sign(xi) == sign(xl):
    xl = xi
  elif sign(xi) == sign(xu):
    xu = xi

  bisectionOutput.write(str(i) + " " + str(xi) + " " + str(f.f(xi)) + " " + str(approxError))
  new_bisection(xl,xu,it_Max,error_Goal,xprev,i,bisectionOutput)
