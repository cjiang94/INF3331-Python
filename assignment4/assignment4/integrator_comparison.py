#!/usr/bin/env python
import numpy as np
import time
from integrator import midpoint_integrate as mid_intgrt
from numpy_integrator import midpoint_integrate as numpy_mid
from numba_integrator import midpoint_integrate as numba_mid

def find_sin(x):
    return np.sin(x)

def test_integral_of_all_functions():
    print("\n====== Testing midpoint for NORMAL ======")
    print("N = 200000")
    t0 = time.time()
    assert abs(mid_intgrt(find_sin, 0, np.pi, 200000) - 2) < 1E-10
    t1 = time.time()
    print("Time: {:.6f} sec".format(t1-t0))
    print("\n====== Testing midpoint for NUMPY ======")
    print("N = 202790")
    t2 = time.time()
    assert abs(numpy_mid(find_sin, 0, np.pi, 202790) - 2) < 1E-10
    t3 = time.time()
    print("Time: {:.6f} sec".format(t3-t2))
    print("\n====== Testing midpoint for NUMBA ======")
    print("N = 200000")
    t4 = time.time()
    assert abs(numba_mid(find_sin, 0, np.pi, 200000) - 2) < 1E-10
    t5 = time.time()
    print("Time: {:.6f} sec".format(t5-t4))

    print("- All Success - ")

test_integral_of_all_functions()