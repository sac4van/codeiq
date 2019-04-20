# -*- coding: utf-8 -*-
"""
  problem:
    https://agc021.contest.atcoder.jp/tasks/agc021_a
"""

from __future__ import print_function
import sys

def solve(_input):
    """
    main function.

    Arguments:
    _input -- string of the format "n p", where n and p are positive integer, separated by space " ".
    """

    # input validation
    _li = list(_input.strip())
    try:
        _digits = map(int,_li)
    except (ValueError, IndexError) as ex:
        print ('[ERROR] Please input a whole number', ex)
        return -1

    # preprocessing
    _ans = sum(_digits)

    for _i in range(0,len(_digits)-1):

        if ( _digits[_i] == 0 ):
            continue

        _r = 0
        
        for _j in range(0,_i - 1):
            _r += _digits[_j]
        
        _r += _digits[_i] - 1

        _r += (len(_digits) - _i - 1) * 9

        _ans = max(_ans, _r)

    return _ans

# call
print (solve(sys.stdin.readline()))
