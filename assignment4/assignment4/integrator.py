#!/usr/bin/env python

def integrate(f, a, b, N):
    """ Method to find the sum of integral by given function, start(a), end(b) and
    N points intervals"""
    result = 0
    dx = (b-a)/N
    temp = a
    for i in range(N+1):
        result += f(temp) * dx
        temp += dx
    return result

def midpoint_integrate(f, a, b, N):
    """ Method to find the sum of integral by given function, start(a), end(b) and
    N points intervals, but with midpoint value"""
    result = 0
    dx = (b-a)/N
    temp = a + (dx/2)
    for i in range(N+1):
        result += f(temp) * dx
        temp += dx
    return result
