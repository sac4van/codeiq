# -*- coding: utf-8 -*-
"""
  problem:
    https://projecteuler.net/problem=19
"""

from __future__ import print_function
import sys


def solve():
    """
    main function.

    Arguments:
    None
    """

    # days in each month
    dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    ans = 0
    days = 1

    for _y in xrange(1900, 2001, 1):

        # leap year
        if _y % 4 == 0 and (_y % 100 != 0 or _y % 400 == 0):
            dim[1] = 29
        else:
            dim[1] = 28

        for _m in dim:
            if days % 7 == 0:
                if _y > 1900:
                    ans += 1
            days += _m

    return ans


# call
print (solve())
