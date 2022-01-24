# Source code for Assignment #2
# Name: ***--> YOUR NAME HERE!!!! <--**
# Required function definitions:
#
#    Problem #1: 
#        Function: factorial(n)
#        Input: n (integer)
#        Output: n! (integer)       
#
#    Problem #2: 
#        Function: is_narcissistic(n)
#        Input: n (integer)
#        Output: True/False (boolean)
#  
#    Problem #3:
#        Function: find_narcissistic(N)
#        Input: N (integer) # of narcissistic numbers to find
#        Output: List of the first N narcissistic numbers
#
#    Problem #4:
#        Function: compute_pi()
#        Input: None
#        Output: Value of pi to at least 12 digits of accuracy
#

import math


# Problem #1
# Handles non-integer and negative values by returning 0
def factorial(n):
    if not isinstance(n, int):
        return 0
    elif n < 0:
        return 0

    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


# Problem #2
def is_narcissistic(n):
    if not isinstance(n, int):
        return 0
    elif n < 0:
        return 0

    n_str = f"{n}"
    left = 0
    right = 0
    for i, char in enumerate(n_str[::-1]): # reverse string
        left += int(char) * pow(10, i)
        right += pow(int(char), len(n_str))

    return left == right


# Problem #3
def find_narcissistic(N):
    solutions = []
    i = 1

    while len(solutions) < N:
        if is_narcissistic(i):
            solutions.append(i)

        i += 1

    return solutions


# Problem #4
# Compute the value of pi using the iteration x = x + sin(x)    
def compute_pi():
    x = 3
    while abs(math.pi - x) > 1e-12:
        x += math.sin(x)

    return x
