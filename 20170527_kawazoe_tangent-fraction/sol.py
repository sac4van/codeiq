# -*- coding: utf-8 -*-
"""
Let
 tan(¥alpha) = 1/a,
 tan(¥beta) = 1/b,
 tan(¥alpha + ¥beta) = 1/c
where a, b and c are positive integer.
Using the additive formula for tangent function, we have
 1/c = ((1/a) + (1/b))/(1-(1/a)(1/b))
which is equivalent to
 (a-c)(b-c) = c^2+1.

since tan(¥alpha + ¥beta) > 0 and ¥alpha + ¥beta > m, we have
 c < 1/tan(m).

Thus, to find F(m), we count pisitive integer factors of (c^2+1), say f(c),
and sum f(c) for all 1 <= c <= 1/m.
"""

from __future__ import print_function
from math import tan


def solve(_m):
    """
    function docstring:
    """

    # input validation
    try:
        _n = float(_m)
    except ValueError as ex:
        print('"%s" cannot be converted to an int: %s' % (_m, ex))
        return
    if _n <= 0.001 or _n >= 1:
        print('input value m should satisfy 0.001 < m < 1')
        return

    # find F(m)
    _fm = 0
    _t = tan(_n)
    for _c in range(1, int(1 / _t)+1):
        if _c > 1 / _t:
            break

        _cc = _c * _c + 1

        for _a in range(1, _cc):
            if _a * _a > _cc:
                break
            if _cc % _a == 0:
                _fm += 1
                continue

    return _fm

# call
print (solve(input()))
