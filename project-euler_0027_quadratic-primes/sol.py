# -*- coding: utf-8 -*-
"""
  problem:
    https://projecteuler.net/problem=27
"""

from __future__ import print_function
import sys

def solve(_input):
    """main function.

    Arguments:
    _input -- maximum value of |a| and |b|
    """

    ## input validation
    try:
        _max = int(_input)
    except ValueError as _ex:
        print ('error: %s' % (_ex) )
        return -1

    ## preprocessing
    # generate prime table
    _max_prime = 2 * _max * _max + _max
    is_prime = [False, False]
    _i = 2
    while _i < _max_prime:
        is_prime.append(True)
        _i += 1

    _i, _j = 2, 1
    while _i < _max_prime:
        if is_prime[_i]:
            _j = 2 * _i
            while _j < _max_prime:
                is_prime[_j] = False
                _j += _i
        _i += 1

    ## main
    _ans = 0
    _n_max = 0

    _a = - _max + 1
    while _a < _max:
        _b = 2
        while _b < _max:
            if is_prime[_b]:
                _n = 1
                while _n < _b:
                    _fn = _n * _n + _a * _n + _b
                    if _fn >= _max_prime or _fn < 1 or not is_prime[_fn]:
                        break
                    _n += 1
                if _n > _n_max:
                    _n_max = _n
                    _ans = _a * _b
                    # print (_a, _b, _n)
            _b +=1
        _a += 1

    return _ans

# call
print (solve(sys.stdin.readline()))
