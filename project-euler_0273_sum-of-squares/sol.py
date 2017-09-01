# -*- coding: utf-8 -*-
"""
    problem:
        https://projecteuler.net/problem=273

    how to solve:
        1) Every prime of the form 4k+1 is the square sum of two integers.
        2) If A = a^2 + b^2 and B = c^2 + d^2 then
            AB = |ad-bc|^2 + (ac+bd)^2
               = (ad+bc)^2 + |ac-bd|^2 

"""

from __future__ import print_function
import math


def primes(_n):
    """
    generate prime list.
    _n --- upper bound of prime
    """

    _plist = []
    _is_prime = [False, False]

    _i = 2
    while _i <= _n:
        _is_prime.append(True)
        _i += 1

    _i = 0
    while _i <= _n:
        if _is_prime[_i]:
            _plist.append(_i)
            _j = 2
            while _j * _i <= _n:
                _is_prime[_j * _i] = False
                _j += 1
        _i += 1

    return _plist


_p = []
for a in primes(150):
    if a % 4 == 1:
        for x in range(1, 150):
            y = round(math.sqrt(a - x * x))
            if x * x + y * y == a:
                _p += [[x, y]]
                break


_ans = 0L

def dfs(a, b, dep):
    global _ans
    if a > b:
        a, b = b, a
    if dep < 0:
        _ans += long(a)
        return
    c, d = _p[dep]
    dfs(a, b, dep - 1)
    dfs(abs(a * c - b * d), a * d + b * c, dep - 1)
    dfs(abs(a * d - b * c), a * c + b * d, dep - 1)


dfs(0, 1, 16 - 1)
print (long(_ans / 2))
