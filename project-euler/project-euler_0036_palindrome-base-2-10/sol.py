# -*- coding: utf-8 -*-
"""
    problem:
        https://projecteuler.net/problem=36
"""

from __future__ import print_function


def solve():
    """
    main function.

    Arguments:
    """

    # preprocess
    ubound = 1000000  # integer upper bound

    _ans = 0

    for _i in xrange(1, ubound):
        if is_parindrome_10(_i) and is_parindrome_2(_i):
            _ans += _i

    return _ans


def is_parindrome_2(_n):
    """
    check if _n is palindrome with base 2
    """

    if _n%2==0:
        return False

    _original = "{0:b}".format(_n)

    return _original == _original[::-1]  

def is_parindrome_10(_n):
    """
    check if _n is palindrome with base 10
    """

    if _n%10==0:
        return False

    _original = str(_n)

    return _original == _original[::-1]

    # call
print(solve())
