# Source code for Assignment #4
# Name: YOUR NAME HERE!!!!
#
# Required function definitions:
#
# Problem #1: 
#   Function: exp_quad(f, tol)
#       Input: a callable object (f) and a positive float (tol)
#       Output: float
#
# Problem #2: 
#   Function: parametric_interp(s, x, y)
#       Input: two arrays of length N
#       Output: callable object that takes an array of length M and returns an array of size (M, 2)

import numpy as np

# Problem 1
def exp_quad(f, tol):           
    return np.inf

# Problem #2
def parametric_interp(s, x, y):
    return lambda s: np.zeros((s.size,2))
