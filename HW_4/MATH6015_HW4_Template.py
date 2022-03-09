# Source code for Assignment #4
# Name: Marshal Stewart M12811716
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
import matplotlib.pyplot as plt
from math import gcd
from time import time
import scipy.integrate as intg
import scipy.interpolate as interp


# Problem 1
def exp_quad(f, tol):
    """

    To solve the problem, created a lambda function that includes the e^-x multiplication
    approx the integral by using intg.quad, this method uses quadpack, which is form of adaptive
    integration. The function takes an epsabs argument that is absolute error tolerance satisfying
    requirement d.

    :param f:
    :param tol:
    :return:
    """

    y = lambda x: f(x) * np.exp(-x)
    sol = intg.quad(y, 0, np.inf, epsabs=tol)
    #     if err > tol:
    #         print(f"error: {err} is greater than tolerance {tol}")
    return sol


# Problem #2
def parametric_interp(s, x, y):
    """

    To solve interpolate the vectors x and y individually with s, however then
    create a lambda function that groups the results into a matrix. This function
    is returned to the user. The dimensions are flipped if the output vectors are grouped in
    a tuple. They are grouped using vstack and T (transpose) to create a 2D matrix.


    :param s:
    :param x:
    :param y:
    :return:
    """
    # Generate interpolation data
    #     x = np.linspace(-5, 5, 11, endpoint=True)
    #     y = f(x)
    # Piecewise Linear Interpolation
    #     f1 = interp.interp1d(x, y, kind="linear")
    # Cubic spline Interpolation
    #     f3 = interp.interp1d(x, y, kind="cubic")
    f1 = interp.interp1d(s, x, kind="cubic")
    f2 = interp.interp1d(s, y, kind="cubic")
    #     f2 = interp.interp1d(s, y, kind="cubic")
    #     plt.plot(s, x, 'o', s, y, 'o', s, f1(s))
    #     plt.show()
    return lambda s: np.vstack((f1(s), f2(s))).T
