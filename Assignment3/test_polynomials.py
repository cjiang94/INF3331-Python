#!/usr/bin/env python
import sys
from polynomials import Polynomial

a = Polynomial([3, 4])          # 4x + 3
b = Polynomial([2, 3])          # 3x + 2
c = Polynomial([5])             # 5
d = Polynomial([3, 6, 2, 0])    # 0x**3 + 2x**2 + 6x + 3
e = Polynomial([2, 3, 4, 5])    # 5x**3 + 4x**2 + 3x + 2
f = Polynomial([0])             # 0

def test_call():
    print("\n====== Testing call ======")
    assert a(2) == 11
    assert c(1) == 5
    assert d(2) == 23
    assert f(3) == 0
    print(" - Success - ")

def test_add_two_poly():
    print("\n====== Testing adding ======")
    assert (a + b) == Polynomial([5, 7])
    assert (e + c) == Polynomial([7, 3, 4, 5])
    assert (d + f) == Polynomial([3, 6, 2, 0])
    print(" - Success - ")

def test_sub_two_poly():
    print("\n====== Testing subtract ======")
    assert (a - b) == Polynomial([1, 1])
    assert (e - c) == Polynomial([-3, 3, 4, 5])
    assert (d - f) == Polynomial([3, 6, 2, 0])
    assert (e - d) == Polynomial([-1, -3, 2, 5])
    print(" - Success - ")

def test_mul_poly():
    print("\n====== Testing multiply ======")
    assert (a * 2) == Polynomial([6, 8])
    assert (2 * a) == Polynomial([6, 8])
    assert (f * 5) == Polynomial([0])
    assert (d * 0) == Polynomial([0, 0, 0, 0])
    print(" - Success - ")


def test_degree():
    print("\n====== Testing degree ======")
    assert c.degree() == 0
    assert d.degree() == 2
    assert e.degree() == 3
    assert f.degree() == -1
    print(" - Success - ")

def test_repr():
    print("\n====== Testing repr ======")
    assert str(b) == "3x + 2"
    assert str(c) == "5"
    assert str(d) == "2x^2 + 6x + 3"
    assert str(e) == "5x^3 + 4x^2 + 3x + 2"
    assert str(f) == "0"
    print(" - Success - ")

test_degree()
test_call()
test_add_two_poly()
test_mul_poly()
test_sub_two_poly()
test_repr()
