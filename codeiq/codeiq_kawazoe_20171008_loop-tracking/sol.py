# -*- coding: utf-8 -*-
"""
    problem:
        https://codeiq.jp/challenge/3285
    
    functions:
        f(n,x) = floor( 4*n*(n-x)/n )

    main:
"""

from __future__ import print_function
import sys
import math

def solve(_input):
    """
    main function.
    
    Arguments:
    _input -- string of the format "m", where m is positive integer.
    """

    # input validation
    try:
        _n = int(_input)
    except ValueError:
        print ('[ERROR] Please input a positive integer.')
        return -1

    ## preprocessing
    for _i in xrange(1, _n/2, 1):
        _f(_n, _i)


def _f(_n, _x):
    """
    function docstring
    """
    return math.floor(4*_x*(_n-_x)/_n)

# call
print (solve(sys.stdin.readline()))
