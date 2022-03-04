# Tests student's code for Assignment #2
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
#
#  How to run the test script:
#    1) Ensure that your source code and this test script are in the current
#           working directory
#
#    2) Run the python script MATH6015_HW2_Test.py in the conda prompt using the command:
#           python MATH6015_HW2_Test
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
#    5) Depending on how fast your computer is, Test #3 might take a few
#           seconds to a minute to finish
#   
#    6) If the test script hangs, then you probably have an error in the 
#           find_narcissistic function and the script cannot find the required 
#           twenty numbers

import sys
import math
import importlib

def test_problem_1(factorial):
    if factorial is math.factorial:
        print('You are using the factorial function from the math module!')
        return False
        
    n_lst = list(range(11)) + [20, 30, 40]
    for n in n_lst:
        f1 = math.factorial(n)
        f2 = factorial(n)
        if (f1 - f2) != 0:
            print(f"*** Error in Problem #1: n = {n}, Factorial(n) = {f2}, factorial(n) = {f1}.")
            return False
    print("Problem #1 Test Finished.")
    
    return True

def test_problem_2(is_narcissistic):    
    true_lst = list(range(1,10)) + [153, 9474, 93084, 32164049651]
    false_lst = [17, 186, 1395, 65479, 984315, 6527416, 23486475]
    for n in true_lst:
        if (not is_narcissistic(n)):
            print(f"*** Error in Problem #2: n = {n} is narcissitic but function returned false.")
            return False
    for n in false_lst:
        if (is_narcissistic(n)):
            print(f"*** Error in Problem #2: n = {n} is not narcissitic but function returned true.")
            return False
    print("Problem #2 Test Finished.")
    
    return True

def test_problem_3(find_narcissistic):    
    narc_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834]
    test_lst = find_narcissistic(20)
    if (narc_lst != test_lst):
        print("*** Error in Problem #3: Compute list of narcissistic numbers is not correct")
        print("***    ", narc_lst)
        print("***    ", test_lst)
        return False
    print("Problem #3 Test Finished.")
    
    return True

def test_problem_4(compute_pi):
    cPi = compute_pi()
    
    delta = abs(math.pi - cPi)
    
    if (delta > 1e-12):
        print("*** Error in Problem #4: Estimate of pi is not within 1e-12.")
        print(f"***     Computed pi = {cPi} \t delta = {delta:3.2e}")
        return False
    
    print("Problem #4 Test Finished.")
    
    return True

def HW2_Test(filename):            
    mod = importlib.import_module(filename)    
    factorial = getattr(mod, "factorial")
    is_narcissistic = getattr(mod, "is_narcissistic")
    find_narcissistic = getattr(mod, "find_narcissistic")
    compute_pi = getattr(mod, "compute_pi")
            
    passed = test_problem_1(factorial) and test_problem_2(is_narcissistic) and test_problem_3(find_narcissistic) and test_problem_4(compute_pi)
        
    print("Tests {}!".format("passed" if passed else "failed" ))
        
    return passed
        

if __name__ == "__main__":    
    filename = input("Enter Filename of the Source Code to Test without the Extension: ")

    passed = HW2_Test(filename)
