#!/usr/bin/env python
from integrator import integrate
from numpy_integrator import numpy_integrate
from numba_integrator import numba_integrate
import time

def integral_of_constant_function(x):
    return 2

def integral_of_linear_function(x):
    return 2*x

# Made my own function for 4.2
def integral_of_exponential_function(x):
    return x**2

# Made my own test for 4.2
def test_integral_of_exponential_function():
    print("\n====== Testing test_integral_of_exponential_function ======")
    assert abs(integrate(integral_of_exponential_function, 0, 1, 500000) - 1/3) < 1E-5
    print(" - Success - ")

def test_integral_of_constact_function():
    print("\n====== Testing test_integral_of_constact_function ======")
    assert abs(integrate(integral_of_constant_function, 0, 1, 1000000) - 2) < 1E-5
    assert abs(integrate(integral_of_constant_function, 0, 1, 5000000) - 2) < 1E-5
    assert abs(integrate(integral_of_constant_function, 0, 1, 8000000) - 2) < 1E-5
    assert abs(integrate(integral_of_constant_function, 0, 1, 1100000) - 2) < 1E-5
    print(" - Success - ")

def test_integral_of_linear_function():
    print("\n====== Testing test_integral_of_linear_function ======")
    assert abs(integrate(integral_of_linear_function, 0, 1, 1000000) - 1) < 1E-5
    assert abs(integrate(integral_of_linear_function, 0, 1, 5000000) - 1) < 1E-5
    assert abs(integrate(integral_of_linear_function, 0, 1, 1000000) - 1) < 1E-5
    assert abs(integrate(integral_of_linear_function, 0, 1, 1500000) - 1) < 1E-5
    print(" - Success - ")

def test_integral_of_numpy_function():
    print("\n====== Testing test_integral_of_numpy_function ======")
    assert abs(numpy_integrate(integral_of_constant_function, 0, 1, 10000000) - 2) < 1E-5
    assert abs(numpy_integrate(integral_of_linear_function, 0, 1, 10000000) - 1) < 1E-5
    assert abs(numpy_integrate(integral_of_exponential_function, 0, 1, 10000000) - 1/3) < 1E-5
    print(" - Success - ")

def test_integral_of_numba_function():
    print("\n====== Testing test_integral_of_numba_function ======")
    assert abs(numba_integrate(integral_of_constant_function, 0, 1, 10000000) - 2) < 1E-5
    assert abs(numba_integrate(integral_of_linear_function, 0, 1, 10000000) - 1) < 1E-5
    assert abs(numba_integrate(integral_of_exponential_function, 0, 1, 10000000) - 1/3) < 1E-5
    print(" - Success - ")

#----------------------------------------------------------------------------
# Just remove the # to test the different cases. Beneath you'll also find the test
# cases for time, but you can also read the times in the reports

test_integral_of_constact_function()
test_integral_of_linear_function()
test_integral_of_exponential_function()
test_integral_of_numpy_function()
test_integral_of_numba_function()

#print("======================")
#print("Test for NORMAL python")
#t0 = time.time()
#s1 = integrate(integral_of_exponential_function, 0, 1, 100)
#t1 = time.time()
#print('{:.6f} sec'.format(t1-t0))
#print("Value: {0}".format(s1))
#print("======================\n")

#print("======================")
#print("Test for NUMPY python")
#t2 = time.time()
#s2 = numpy_integrate(integral_of_exponential_function, 0, 1, 10000000)
#t3 = time.time()
#print('{:.6f} sec'.format(t3-t2))
#"print("Value: {0}".format(s2))
#print("======================\n")

#print("======================")
#print("Test for NUMBA python")
#t4 = time.time()
#numba_integrate(integral_of_exponential_function, 0, 1, 10000000)
#t5 = time.time()
#print('{:.6f} sec'.format(t5-t4))
#print("======================\n")
