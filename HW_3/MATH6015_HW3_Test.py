# Tests student's code for Assignment #3
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
#
#  How to run the test script:
#    1) Ensure that your source code and this test script are in the current
#           working directory
#
#    2) Run the python script MATH6015_HW3_Test.py in the conda prompt using the command:
#           python MATH6015_HW3_Test
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
import scipy.linalg as la

import zlib, base64
from time import time

def test_problem_1(solve_hilbert, N=5000, tol=1e-6):
    print('Solving Hilbert system...')
    
    b = np.random.rand(N)  # Compute a random RHS 

    print('\nComputing your solution...')
    start_time = time()
    
    z = solve_hilbert(b)
    
    print('Computed solution in {:3.2f} seconds.'.format(time() - start_time))

    print('\nSolving benchmark solution...')
    start_time = time()
    
    local_vars = {'N': N, 'b': b}
    exec(zlib.decompress(base64.b64decode('eJxFjLEOwiAURXe+4o1gEVNHE/ZO/IBxaBtq7ksLBIyJ/XpbTON67jl3ynGhMiJ9TEl+RD8TlhTziwaEuAhnB1OwetHZkMzqcyxSOu2UElPMBBAC5T48vXTqJqi7Axp42PYirycJNK06t4oE7TrzX98nXZtfxFyjDTM3tdg483F2cLF6O/emxPntZacHJb6McTpa')), globals(), local_vars)
    ze = local_vars['ze']
    print('Computed benchmark solution in {:3.2f} seconds.'.format(time() - start_time))
    
    err = la.norm(z-ze, np.inf)
    
    if err > tol:
        print(f"*** Error in Problem #1! (Difference = {err:.3e})\n")
        return False
    else: 
        print(f'Test passed. (Difference = {err:.3e})\n')
        return True

def test_problem_2(solve_fdm, N=500000, tol=1e-6):
    print('Solving FDM system...')

    print('\nComputing your solution...')
    start_time = time()
    
    z = solve_fdm(N)

    print('Computed solution in {:3.2f} seconds.'.format(time() - start_time))

    print('\nSolving benchmark solution...')
    start_time = time()

    local_vars = {'N': N}
    exec(zlib.decompress(base64.b64decode('eJxztM0r0KtKLcov1tAw1vHT1ORyjDbQsYq11TUEsgxBLAUjIMsIKpZkq2ukBdSSn5darOGnqa/hp22oqaVlxFWVapuTqFecn1OWGp+UmJeSmqKhYahjqKnjqJOkyQUAduYbHg==')), globals(), local_vars)
    ze = local_vars['ze']
    print('Computed benchmark solution in {:3.2f} seconds.'.format(time() - start_time))
    
    err = la.norm(z-ze, np.inf)
    
    if err > tol:
        print(f"*** Error in Problem #2! (Difference = {err:.3e})")
        return False
    else:
        print(f'Test passed. (Difference = {err:.3e})\n')
        return True

def HW3_Test(filename):
    # Dynamically load the module to test        
    mod = importlib.import_module(filename)    
    solve_hilbert = getattr(mod, "solve_hilbert")
    solve_fdm = getattr(mod, "solve_fdm")
    
    passed = test_problem_1(solve_hilbert) and test_problem_2(solve_fdm)
    
    print("Tests {}!".format("passed" if passed else "failed" ))
        
    return passed

if __name__ == "__main__":
    filename = input("Enter Filename of the Source Code to Test without the Extension: ")

    passed = HW3_Test(filename)
