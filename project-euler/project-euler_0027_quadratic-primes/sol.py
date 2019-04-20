# -*- coding: utf-8 -*-
"""
  problem:
    https://projecteuler.net/problem=27
"""

from __future__ import print_function


def solve():
    """
    main function.

    Arguments:
    None
    """

    # input validation
    _max = 1000

    # preprocessing
    # generate prime table
    _max_prime = 2 * _max * _max + _max

    is_prime = [True for _x in xrange(_max_prime)]
    is_prime[0] = False
    is_prime[1] = False

    primes = []

    for _i in xrange(2, _max_prime):
        if is_prime[_i]:
            primes.append(_i)
            for _j in xrange(2 * _i, _max_prime, _i):
                is_prime[_j] = False

    # main
    _ans = 0
    _n_max = 0

    _a = - _max + 1
    for _a in xrange(-_max + 1, _max, 1):
        for _b in xrange(2, _max, 1):
            if is_prime[_b]:
                for _n in xrange(1, _b, 1):
                    _fn = _n * _n + _a * _n + _b
                    if _fn >= _max_prime or _fn < 1 or not is_prime[_fn]:
                        if _n > _n_max:
                            _n_max = _n
                            _ans = _a * _b
                        break

    return _ans


# call
print (solve())
