# -*- coding: utf-8 -*-
"""
  problem:
    https://projecteuler.net/problem=67

  preprocessing:
    Read 'p067_triangle.txt' and create the matrix a(m,n).
    a(0,0)
    a(1,0), a(1,1)
    a(2,0), a(2,1), a(2,2)
    ...

  main:
    Let sol(m,n) (0<=n<=m) be the "maximum path sum" in the small matrix

      a(0,0)
      a(1,0), a(1,1)
       ...
      a(m,0), a(m,1), ..., a(m,m)

      where m, n = 0, 1, 2, ... N.

    recursive expression:

      sol(m,n) = max{ sol(m-1,n-1), sol(m-1,n)} + a(m,n)
        m, n = 0, 1, 2, ..., N.

    with initial contitions:

      sol(0,0) = a(0,0),
      sol(m,-1) = sol(m,m+1) = 0.
"""

from __future__ import print_function


def solve(_input='p067_triangle.txt'):
    """
    main function.

    Arguments:
    _input: input file.
    """

    # input validation
    try:
        _input_file = open(_input, 'r')
    except IOError:
        print('[ERROR] failed to open file %s' % (_input))
        return -1

    # preprocessing
    # read file & prepare matrix
    _a = []
    for line in _input_file:
        line = line.rstrip('\n').split(' ')
        _line = []
        for _el in line:
            _line.append(int(_el))
        _a.append(_line)

    _max = len(_a)

    # initialize sol matrix
    sol = []
    for _m in xrange(0, _max, 1):
        _li = []
        for _n in xrange(0, _m + 1, 1):
            _li.append(0)
        sol.append(_li)

    # main
    # initial condition
    sol[0][0] = _a[0][0]

    # calculate sol[_m][_n] for fixed _m + _n = _npm
    for _m in xrange(1, _max, 1):

        # _n = 0
        sol[_m][0] = sol[_m - 1][0] + _a[_m][0]

        # 0 < _n < _m
        for _n in xrange(1, _m):
            sol[_m][_n] = max(sol[_m - 1][_n - 1],
                              sol[_m - 1][_n]) + _a[_m][_n]

        # _n = _m
        sol[_m][_m] = sol[_m - 1][_m - 1] + _a[_m][_m]

    return max(sol[_max - 1])


# call
print (solve())
