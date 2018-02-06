#!/usr/bin/env python
import numpy as np

def numpy_integrate(f, a, b, N):
    """ Method to find the sum of integral by given function, start(a), end(b) and
    N points intervals by using numpy"""
    points = np.linspace(a, b, N+1)
    function = f(points)
    if (points.shape != np.asarray(function).shape):
        new_vfunc = np.vectorize(f)
        function = new_vfunc(points)

    result = np.sum(function)*((b-a)/N)
    return result

def midpoint_integrate(f, a, b, N):
    """ Method to find the sum/2 of integral by given function, start(a), end(b) and
    N points intervals by using numpy, but with midpoint value"""

    points = np.linspace(a, b, N+1)
    function = f(points + ((b-a)/N)/2)
    if (points.shape != np.asarray(function).shape):
        new_vfunc = np.vectorize(f)
        function = new_vfunc(points + ((b-a)/N)/2)

    result = np.sum(function) * ((b-a)/N)
    return result
