# -*- coding: utf-8 -*-
"""
    problem:
        https://projecteuler.net/problem=35
"""

from __future__ import print_function


def solve():
    """
    main function.

    Arguments:
    """

    # preprocess
    ubound = 1000000  # integer upper bound

    # generate prime list
    is_prime = [True for _x in xrange(ubound)]
    is_prime[0] = False
    is_prime[1] = False

    cprimes = []
    primes = []
    for _i in xrange(2, ubound):
        if is_prime[_i]:
            primes.append(_i)

            for _j in xrange(2 * _i, ubound, _i):
                is_prime[_j] = False

    for _p in primes:
        if is_cprime(_p, is_prime):
            cprimes.append(_p)

    return len(cprimes)


def is_cprime(_p, is_prime):
    """
    check if _p is circular prime
    """
    _debug_str = str(_p)

    if not is_prime[_p]:
        return False

    _q = perm(_p)
#    _debug_str += ", " + str(_q)
    while _q != _p:
        if not is_prime[_q]:
            return False
        _q = perm(_q)
#        _debug_str += ", " + str(_q)

    print(_debug_str)
    return True


def perm(_n):
    """
    permulate integer
    """
    if _n < 10:
        return _n

    return int(str(_n % 10) + str(_n / 10))

    # call
print(solve())
