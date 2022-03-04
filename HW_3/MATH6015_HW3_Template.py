# Source code for Assignment #3
# Name: Marshal Stewart
# stewa2m3 M12811716
#
# Required function definitions:
#
#    Problem #1: 
#        Function: solve_hilbert(b)
#        Input: RHS vector in Hx = b
#        Output: 1D numpy.array of the same length as b
#
#    Problem #2: 
#        Function: solve_fdm(N)
#        Input: Size of the linear system N (integer)
#        Output: 1D numpy.array of length N
#

import numpy as np
import scipy.linalg as la

def solve_hilbert(b):
    N = len(b)
    H = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            H[j,i] = 1/(i+j+1)
#     H = la.hilbert(N)
    return la.solve(H, b)

# Problem #2
def solve_fdm(N): 
    
    # Create bounded storage matrix A
    A = np.zeros((3, N))
    A[0, :] = -1
    A[1, :] = 2
    A[2, :] = -1
    
    # Create RHS
    b = np.zeros(N)
    for i in range(1, N+1):
        b[(i-1)] = -2/(N+1)**2
    
    return la.solve_banded((1,1), A, b)
