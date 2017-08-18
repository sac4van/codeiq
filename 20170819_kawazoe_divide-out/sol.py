# -*- coding: utf-8 -*-
"""
  preprocessing:
    for r = 1, 2, ..., p-1,
    a[r] = F(r,p) = r!  mod p
    a[p-1] = -1

  main:
    F(n, p)
    = F(n[1], p) * a[r[1]] * a[-1]^n[1]
        where n[1], r[1] are quotient and reminder of n divided by p

"""

from __future__ import print_function
import sys

def solve(_input):
    """
    main function.
    """

    # input validation
    _l = _input.split(" ")
    _n, _p = int(_l[0]), int(_l[1])

    # if _p = 2 return 1
    if _p == 2:
        return 1

    # preprocessing
    _a = [1, 1]
    for _i in range(2, _p):
        _a.append((_a[_i - 1] * _i) % _p)

    # find F(n, p)
    _f = recurse(_n, _p, _a)

    return _f

def recurse(_f, _p, _a):
    """
    recursive calculation.
    """
    if _f < _p:
        return _a[_f]
    else:
        _q, _r = _f / _p, _f % _p
        return recurse(_q, _p, _a) * _a[_r] * (1 if _q % 2 == 0 else -1) % _p

# call
print (solve(sys.stdin.readline()))
