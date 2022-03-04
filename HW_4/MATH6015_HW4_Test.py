# Test script for student's code for Assignment #4
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
#
#  How to run the test script:
#    1) Ensure that your source code and this test script are in the current
#           working directory
#
#    2) Run the python script MATH6015_HW4_Test.py in the conda prompt using the command:
#           python MATH6015_HW4_Test
#
#    3) At the prompt, enter the FILENAME with the actual filename of the code you want to
#           test using quotes and without the py extension. 
#			Example: 
# 
#           Enter Filename of the Source Code to Test without the Extension: fileTestCode 
#                   
#           will test the code in the fileTestCode.py
#    
#    4) The test script will output "Tests Passed" if the code passes all the 
#           tests otherwise it will output which tests have failed
#

import importlib
import numpy as np
import matplotlib.pyplot as plt
from time import time

def print_convergence_table(M, err):
    header1 = "Convergence Table:\n"
    header2 = "      M     Error     Ratio"
    hbar = "-"*(len(header2)+2)
    first_row = " {:>6}   {:7.3e}"
    row = first_row + "  {:6.2f}"
    
    ratio = err[:-1]/err[1:]
    
    print(header1)
    print(header2)
    print(hbar)    
    print(first_row.format(M[0], err[0]))
    for kk, E, R in zip(M[1:], err[1:], ratio):
        print(row.format(kk, E, R))
    
    return

def plot_parametric_fit(x, xx, XX):
    M = x.shape[0]
    
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    
    plt.plot( x[:,0],  x[:, 1], 'o')
    plt.plot(xx[:,0], xx[:, 1], 'r')
    plt.plot(XX[:,0], XX[:, 1], 'g')
    
    ax.set_aspect('equal')
    ax.set_axis_off()
    
    plt.legend(['Nodes', 'Interpolant', 'Exact'])
    plt.title(f'{M} nodes')
    plt.show()
    
    return
    
def print_integral_table(vI, vIe, vE, tol):
    header1 = "\nIntegral Table:\n"
    header2 = "Problem #    Approximation    Exact       Error"
    hline = "-"*(len(header2)+6)
    row     = "{:^9}      {:>9.3e}   {:10.3e}   {:9.3e} {}"

    print(header1)
    print(header2)
    print(hline)
    
    for kk, (I, I_exact, err) in enumerate(zip(vI, vIe, vE)):
        print(row.format(kk, I, I_exact, err, '*' if err > tol else ''))
            
    return

def test_problem_1(exp_quad, tol=1e-8):      
    
    benchmark_problems = [((lambda x: x          ), 1.0             ),
                          ((lambda x: x**2       ), 2.0             ),
                          ((lambda x: np.cos(x)  ), 1/2             ),
                          ((lambda x: -np.log(x) ), np.euler_gamma  ), 
                          ((lambda x: x*np.log(x)), 1-np.euler_gamma), 
                         ]
        
    start_time = time()
    
    vI  = np.zeros(len(benchmark_problems))
    vIe = np.zeros(len(benchmark_problems))
    vE  = np.zeros(len(benchmark_problems))
    
    failed = False
    for kk, (f, I_exact) in enumerate(benchmark_problems):
            
        I = exp_quad(f, tol)
        err = abs(I-I_exact)
        
        vI[kk] = I; vIe[kk] = I_exact; vE[kk] = err
                
        failed = failed or (err > tol)
    
    print_integral_table(vI, vIe, vE, tol)
    print('\nComputed solutions in {:3.2f} seconds.'.format(time() - start_time))
    print('\n{} the integral tests!\n'.format('Failed' if failed else 'Passed'))

    
    return not failed

def test_problem_2(parametric_interp, n_pts=5000, tol=1e-6, N=15):
    A = 1; B = 1
    a = 6; b = 5; delta = np.pi/4

    T = 2*np.pi*np.gcd(a, b)
    
    F = lambda s: np.c_[A*np.sin(a*s + delta), B*np.sin(b*s)]
    
    vM = 10*(2**np.arange(N))
    
    err = np.zeros((N,))
    passed = False
            
    for kk, M in enumerate(vM):
        s = np.linspace(0, T, M)
    
        x = F(s)
    
        f = parametric_interp(s, x[:,0], x[:,1])
        
        ss = np.linspace(0, T, n_pts)
        xx = f(ss)
        XX = F(ss)
        err[kk] = np.linalg.norm(xx-XX, np.inf)   
        
        if (kk == 0):
            plot_parametric_fit(x, xx, XX)
          
        
        if err[kk] < tol:
            vM = vM[:kk+1]
            err = err[:kk+1]
            passed = True
            break
            
    plot_parametric_fit(x, xx, XX)                    
    print_convergence_table(vM, err)        
        
    print('\n{} the parametric interepolation test!\n'.format('Passed' if passed else 'Failed'))
    
    return passed

def HW4_Test(filename):
    mod = importlib.import_module(filename)    
    exp_quad = getattr(mod, "exp_quad")
    parametric_interp = getattr(mod, "parametric_interp")

    passed = test_problem_1(exp_quad) and test_problem_2(parametric_interp)
    
    print("\n\nTests {}!".format("passed" if passed else "failed"))
        
    return passed

if __name__ == "__main__":
    filename = input("Enter Filename of the Source Code to Test without the Extension: ")

    passed = HW4_Test(filename)
