#!/usr/bin/env python
import numba
from numpy_integrator import numpy_integrate
import numpy as np

def numba_integrate(f, a, b, N):
    """ Method to find the sum of integral by given function, start(a), end(b) and
    N points intervals by using numba"""

    jit_func = numba.jit("f8(f8)", nopython=True)(f)

    result = 0
    dx = (b-a)/N
    temp = a

    @numba.jit("f8(f8, f8, f8, i8)", nopython=True)
    def call(result, dx, temp, N):
        for i in range(N+1):
            result += jit_func(temp) * dx
            temp += dx
        return result
    return call(result, dx, temp, N)

def midpoint_integrate(f, a, b, N):
    """ Method to find the sum of integral by given function, start(a), end(b) and
    N points intervals by using numba"""

    jit_func = numba.jit("f8(f8)", nopython=True)(f)

    result = 0
    dx = (b-a)/N
    temp = a

    @numba.jit("f8(f8, f8, f8, i8)", nopython=True)
    def call(result, dx, temp, N):
        for i in range(N+1):
            result += jit_func(temp + dx/2) * dx
            temp += dx
        return result
    return call(result, dx, temp, N)
