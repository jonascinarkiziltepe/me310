
#import functions
from hashlib import new
from tkinter.filedialog import Open
import f as f
import fp as fp
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

def new_bisection(xl, xu, it_Max, error_Goal, xprev = 500, i = 0, bisectionOutput = 0 ):

  #Initialization, open output file
  if i == 0: 
    bisectionOutput = open("output_bisection.txt", "w")

  #Termination, close output file
  if it_Max == i or it_Max < i :
    print("Bisection Method, Max iteration reached")
    print("Last estimate= " + str(xprev) + "Apprx. % Relative Err: " + str(bisection_Errors[-1]) + "# of iterations: " + str(i) + "f(xr) = " + str(f.f(xprev)))
    bisectionOutput.close() #Close output file
    return 0 #Terminate function

  #Advance iteration
  i = i+1

  #Store function values to decrease function evaluations
  fxl = f.f(xl)
  fxu = f.f(xu)
  
  #Check if the bounding input values give different sign
  if sign(fxl) == sign(fxu):
    print("xl is " + str(xl))
    print("fxl is " + str(fxl))
    print("xu is " + str(xu))
    print("fxu is " + str(fxu))
    bisectionOutput.write(" No sign change between point, program terminated")
    raise Exception(" No sign change between the points ")
  
  #Calculate mid value
  xi = (xl + xu)/2
  fxi = f.f(xi)


  #Error not calculated for the first iteration
  if i == 1:
    approxError = "---"
  else:#Calculate error
    approxError = calculate_error(xi,xprev)
    bisection_Errors.append(approxError)
    if approxError < error_Goal: #Stop process if error goal is reached
      print("Bisection Method, Error tolerance goal reached")
      print("Last estimate= " + str(xprev) + "Apprx. % Relative Err: " + str(bisection_Errors[-1]) + "# of iterations: " + str(i) + "f(xr) = " + str(f.f(xprev)))
      bisectionOutput.write(str(i) + " " + str(xi) + " " + str(fxi) + " " + str(approxError) + "\n")
      return 0 

  #Record mid value for error calculation in the next iteration
  xprev = xi
  #debug
  #print("xi is " + str(xi))
  #print("xl was " + str(xl))
  #print("xu was " + str(xu))

  #Replace xi with whichever bound that gives the same sign
  if sign(fxi) == sign(fxl):
    xl = xi
  elif sign(fxi) == sign(fxu):
    xu = xi

  #Debug
  #print("xl is " + str(xl))
  #print("xu is " + str(xu))

  #Write to output file
  bisectionOutput.write(str(i) + " " + str(xi) + " " + str(fxi) + " " + str(approxError) + "\n")

  #Perform Recursive function call 
  new_bisection(xl,xu,it_Max,error_Goal,xprev,i,bisectionOutput)

########
# 
# 
# False Position

def falsePosition(xl, xu, it_Max, error_Goal, xprev = 500, i = 0, falsePositionOutput = 0 ):

  #Initialization, open output file
  if i == 0: 
    falsePositionOutput = open("output_falseposition.txt", "w")

  #Termination, close output file
  if it_Max == i or it_Max < i :
    print("False Position Method, Max iteration reached")
    print("Last estimate= " + str(xprev) + "Apprx. % Relative Err: " + str(falsepos_Errors[-1]) + "# of iterations: " + str(i) + "f(xr) = " + str(f.f(xprev)))
    falsePositionOutput.close() #Close output file
    return 0 #Terminate function

  #Advance iteration
  i = i+1

  #Store values to decrease the number of function calls
  fxl = f.f(xl)
  fxu = f.f(xu)
  
  #Check if the bounding input values give different sign
  if sign(fxl) == sign(fxu):
    print("xl is " + str(xl))
    print("fxl is " + str(fxl))
    print("xu is " + str(xu))
    print("fxu is " + str(fxu))
    falsePositionOutput.write(" No sign change between point, program terminated")
    raise Exception(" No sign change between the points ")
  
  #Calculate xr
  xr = xu - ((fxu*(xl-xu))/(fxl - fxu))
  fxr = f.f(xr)

  #Error not calculated for the first iteration
  if i == 1:
    approxError = "---"
  else:#Calculate error
    approxError = calculate_error(xr,xprev)
    #Add error to the list 
    falsepos_Errors.append(approxError)
    if approxError < error_Goal: #Stop process if error goal is reached
      print("False Position Method, Error tolerance goal reached")
      print("Last estimate= " + str(xprev) + "Apprx. % Relative Err: " + str(falsepos_Errors[-1]) + "# of iterations: " + str(i) + "f(xr) = " + str(f.f(xprev)))
      falsePositionOutput.write(str(i) + " " + str(xr) + " " + str(f.f(xr)) + " " + str(approxError) + "\n")
      return 0 

  #Record mid value for error calculation in the next iteration
  xprev = xr
  #debug
  #print("xr is " + str(xr))
  #print("xl was " + str(xl))
  #print("xu was " + str(xu))

  #Replace xr with whichever bound that gives the same sign
  if sign(fxr) == sign(fxl):
    xl = xr
  elif sign(fxr) == sign(fxu):
    xu = xr

  #Debug
  #print("xl is " + str(xl))
  #print("xu is " + str(xu))

  #Write to output file
  falsePositionOutput.write(str(i) + " " + str(xr) + " " + str(fxr) + " " + str(approxError) + "\n")

  #Perform Recursive function call 
  falsePosition(xl,xu,it_Max,error_Goal,xprev,i,falsePositionOutput)


#----------------------------

#Newton-Rhapson Method

def newton(xl, xu, it_Max, error_Goal, xprev = 500, i = 0, newtonOutput = 0 ):

  #Initialization, open output file
  if i == 0: 
    newtonOutput = open("output_newton.txt", "w")
    #Calculate the mean of the bounds for the single guess
    xprev = (xl + xu)/2

  #Termination, close output file
  if it_Max == i or it_Max < i :
    print("Newton Method, Max iteration reached")
    print("Last estimate= " + str(xprev) + "Apprx. % Relative Err: " + str(newton_Errors[-1]) + "# of iterations: " + str(i) + "f(xr) = " + str(f.f(xprev)))
    newtonOutput.close() #Close output file
    return 0 #Terminate function

  #Advance iteration
  i = i+1

  fxprev = f.f(xprev)
  fpxprev = fp.fp(xprev)
  if fpxprev == 0:
    newtonOutput.write(" The derivative equals zero, program terminated")
    raise Exception("The derivative of f equals zero")
  #Calculate the next x
  xnext = xprev - ((fxprev)/(fpxprev))
  #print(xnext)
  fxnext = f.f(xnext)


  #Error not calculated for the first iteration
  if i == 1:
    approxError = "---"
  else:#Calculate error
    approxError = calculate_error(xnext,xprev)
    newton_Errors.append(approxError)
    if approxError < error_Goal: #Stop process if error goal is reached
      print("Error tolerance goal reached")
      print("Last estimate= " + str(xprev) + "Apprx. % Relative Err: " + str(newton_Errors[-1]) + "# of iterations: " + str(i) + "f(xr) = " + str(f.f(xprev)))
      newtonOutput.write(str(i) + " " + str(xnext) + " " + str(fxnext) + " " + str(approxError) + "\n")
      return 0 

  #Record x with the next value
  xprev = xnext

  #Write to output file
  newtonOutput.write(str(i) + " " + str(xnext) + " " + str(fxnext) + " " + str(approxError) + "\n")

  #Perform Recursive function call 
  newton(xl,xu,it_Max,error_Goal,xprev,i,newtonOutput)


#---------------------------
#Secant Method


def secant(xold, xolder, it_Max, error_Goal, i = 0, secantOutput = 0 ):

  #Initialization, open output file
  if i == 0: 
    secantOutput = open("output_secant.txt", "w")

  #Termination, close output file
  if it_Max == i or it_Max < i :
    print("Secant Method, Max iteration reached")
    print("Last estimate= " + str(xold) + "Apprx. % Relative Err: " + str(secant_Errors[-1]) + "# of iterations: " + str(i) + "f(xr) = " + str(f.f(xold)))
    secantOutput.close() #Close output file
    return 0 #Terminate function

  #Advance iteration
  i = i+1

  fxold = f.f(xold)
  fxolder = fp.fp(xolder)
  if fxold == fxolder:
    secantOutput.write(" Zero in the denominator, program terminated")
    raise Exception("Zero in the denominator")
  #Calculate the next x
  xnew = xold - (((fxold)*(xolder - xold))/(fxolder - fxold))
  #print(xnext)
  fxnew = f.f(xnew)


  #Error not calculated for the first iteration
  if i == 1:
    approxError = "---"
  else:#Calculate error
    approxError = calculate_error(xnew,xold)
    secant_Errors.append(approxError)
    if approxError < error_Goal: #Stop process if error goal is reached
      print("Secant Method, error tolerance goal reached")
      print("Last estimate= " + str(xold) + "Apprx. % Relative Err: " + str(secant_Errors[-1]) + "# of iterations: " + str(i) + "f(xr) = " + str(f.f(xold)))
      secantOutput.write(str(i) + " " + str(xnew) + " " + str(fxnew) + " " + str(approxError) + "\n")
      return 0 

  #Record x with the next value
  xolder = xold
  xold = xnew

  #Write to output file
  secantOutput.write(str(i) + " " + str(xnew) + " " + str(fxnew) + " " + str(approxError) + "\n")

  #Perform Recursive function call 
  secant(xold,xolder,it_Max,error_Goal,i,secantOutput)

#-----------------------------------
#New Poly Method

def polynomial(xl, xu, it_Max, error_Goal, xprev = 500, i = 0, polynomialOutput = 0 ):

  #Initialization, open output file
  if i == 0: 
    polynomialOutput = open("output_polynomial.txt", "w")

  #Termination, close output file
  if it_Max == i or it_Max < i :
    print("Polynomial Method, Max iteration reached")
    print("Last estimate= " + str(xprev) + "Apprx. % Relative Err: " + str(polynomial_Errors[-1]) + "# of iterations: " + str(i) + "f(xr) = " + str(f.f(xprev)))
    polynomialOutput.close() #Close output file
    return 0 #Terminate function

  #Advance iteration
  i = i+1
  #calculate middle value
  xi = (xu + xl)/2

  #Store values to decrease the number of function calls
  fxl = f.f(xl)
  fxu = f.f(xu)
  fxi = f.f(xi)

  #Check if the bounding input values give different sign
  if sign(fxl) == sign(fxu):
    print("xl is " + str(xl))
    print("fxl is " + str(fxl))
    print("xu is " + str(xu))
    print("fxu is " + str(fxu))
    polynomialOutput.write(" No sign change between point, program terminated")
    polynomialOutput.close()
    raise Exception(" No sign change between the points ")
  
  #Calculate polynomial coefficients
  poly_a = ((fxl - fxi)/((xl - xi)*(xl - xu))) + ((fxi - fxu)/((xu - xi)*(xl-xu)))
  poly_b = (((fxl-fxi)*(xi-xu))/((xl-xi)*(xl-xu)))-(((fxi-fxu)*(xl-xi))/((xu-xi)*(xl-xu))) 
  poly_c = fxi

  #Using the coefficients, calculate the root of the polynomial
  
  xr = xi - ((2*poly_c)/(poly_b + sign(poly_b)*(math.sqrt(poly_b*poly_b - 4*poly_a*poly_c))))
  fxr = f.f(xr)

  #Error not calculated for the first iteration
  if i == 1:
    approxError = "---"
  else:#Calculate error
    approxError = calculate_error(xr,xprev)
    polynomial_Errors.append(approxError)
    if approxError < error_Goal: #Stop process if error goal is reached
      print("Polynomial Method, Error tolerance goal reached")
      print("Last estimate= " + str(xprev) + "Apprx. % Relative Err: " + str(polynomial_Errors[-1]) + "# of iterations: " + str(i) + "f(xr) = " + str(f.f(xprev)))
      polynomialOutput.write(str(i) + " " + str(xr) + " " + str(f.f(xr)) + " " + str(approxError) + "\n")
      return 0 

  #Record mid value for error calculation in the next iteration
  xprev = xr

  #Replace xr with whichever bound that gives the same sign
  if sign(fxr) == sign(fxl):
    xl = xr
  elif sign(fxr) == sign(fxu):
    xu = xr

  #Write to output file
  polynomialOutput.write(str(i) + " " + str(xr) + " " + str(fxr) + " " + str(approxError) + "\n")

  #Perform Recursive function call 
  polynomial(xl,xu,it_Max,error_Goal,xprev,i,polynomialOutput)









new_bisection(x_low,x_up, iteration_max, error_set)
falsePosition(x_low,x_up, iteration_max, error_set)
newton(x_low,x_up, iteration_max, error_set)
secant(x_low,x_up, iteration_max, error_set)
polynomial(x_low,x_up, iteration_max, error_set)
