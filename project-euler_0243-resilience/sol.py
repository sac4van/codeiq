# -*- coding: utf-8 -*-
"""
    problem:
        https://projecteuler.net/problem=243
"""

from __future__ import print_function


def solve():
    """
    main function.

    Arguments:
    """

    # preprocess
    ubound = 50  # integer upper bound

    # generate prime list
    is_prime = [True for _x in xrange(ubound)]
    is_prime[0] = False
    is_prime[1] = False

    primes = []

    for _i in xrange(2, ubound):
        if is_prime[_i]:
            primes.append(_i)
            for _j in xrange(2 * _i, ubound, _i):
                is_prime[_j] = False
    print("preprocess finished.")

    # main
    _rm = float(15499) / 94744

    # candidates
    dlist = [
        2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23,
        2**2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23,
        2**3 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23,
        2 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19 * 23,
        2 * 3 * 5**2 * 7 * 11 * 13 * 17 * 19 * 23,
        2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29
    ]

    dlist.sort()
    for _d in dlist:
        _c = _r(_d, primes) - _rm
        print("--- (r(d) - r_given, d) =",_c, _d)
        if _c < 0:
            return _d

    return -1


def _r(_d, _primes):
    """
    Resilience R(d) of an integer d
    _d --- positive integer

    math formula:
        R(d) = d/(d-1) * (1-1/p[0]) * (1-1/p[1]) * ...
        where
        p[0], p[1], ... are distinct prime factors of d
    """

    _ret = _d

    # prime factorization
    for _p in _primes:
        if _d % _p == 0:
            _ret = _ret / _p * (_p - 1)

        if _p**2 > _d:
            break

    return float(_ret) / (_d - 1)


# call
print(solve())
