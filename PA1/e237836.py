
#import functions
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
  # loop start
  while i <3 or current_error > error_set :
    x_i = (x_u + x_l)/2
    print("xi is " + str(x_i))

    fxl=f.f(x_l)
    fxu=f.f(x_u)
    fxi=f.f(x_i)

    #poly_a = ((fxl-fxi)/((x_l-x_i)*(x_l-x_u)))+((fxi-fxu)/((x_u-x_i)*(x_l-x_u)))
    print("fxl is " + str(fxl))
    print(fxu)
    print(fxi)
    
    poly_a = ((fxl - fxi)/((x_l - x_i)*(x_l - x_u))) + ((fxi - fxu)/((x_u - x_i)*(x_l-x_u)))
    poly_b = (((fxl-fxi)*(x_i-x_u))/((x_l-x_i)*(x_l-x_u)))-(((fxi-fxu)*(x_l-x_i))/((x_u-x_i)*(x_l-x_u))) 
    #poly_b = ()
    print("xi is " + str(x_i))
    poly_c = fxi

    print("Polyvars")
    print("a = " + str(poly_a))
    print("b = " + str(poly_b))
    print("c = " + str(poly_c))

    print("yrk " + str(poly_b*poly_b - 3*poly_a*poly_c))
    

    x_r = x_i - ((2*poly_c)/(poly_b + sign(poly_b)*(math.sqrt(poly_b*poly_b - 4*poly_a*poly_c))))

    fxr = f.f(x_r)

    if fxl*fxr < 0 :
      x_u = x_r
    elif fxl*fxr > 0 :
      x_l =x_r
    else:
      #x_r is the root
      print(x_r + " is the root")
    
    #to calculate error after the first iteration
    if i > 1:
      current_error = calculate_error(x_r,x_prev)
    x_prev = x_r
    print( "Current iteration " + str(i) )
    print("Current Error " + str(current_error))
    print( "Current x_r is " + str(x_r))
    i = i+1
    if i >= 30:
      break

  print("Total iteration " + str(i))
  print("The root is " + str(x_r))


poly(x_low,x_up)
print(os.getcwd())