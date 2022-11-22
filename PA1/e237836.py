
#import functions
import f as f
import math
import os



# Structure for input.txt
# x_lower
# x_upper
# error_set
# iteration_max

# Reading input

 #Open the input file
input_file = open("input.txt", "r")

#read line by line
x_lower = float(input_file.readline())
x_upper = float(input_file.readline())
error_set = float(input_file.readline())
iteration_max = float(input_file.readline()) 

#debug
print(x_lower, x_upper, error_set, iteration_max)

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


# Error Calculation
def calculate_error (x_current, x_previous):
  E_a = (x_current - x_previous)/(x_current)
  E_a = E_a * 100
  return abs(E_a)



# The Methods


# The new polynomial method

def poly(x_lower,x_upper):
    x_i = (x_upper + x_lower)/2
    #debug
    print(x_i)
   





poly(10,30)


print(os.getcwd())