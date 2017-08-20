# -*- coding: utf-8 -*-
"""
  problem:
    https://projecteuler.net/problem=81

  preprocessing:
    Read 'p081_matrix.txt' and create the matrix a(m,n).

  main:
    Let sol(m,n) be the "minimal path sum" in the small matrix

      a(0,0), a(0,1), ..., a(0,n)
      a(1,0), a(1,1), ..., a(1,n)
       ...
      a(m,0), a(m,1), ..., a(m,n)

      where m, n = 0, 1, 2, ... N.

    recursive expression:

      sol(m,n) = min{ sol(m-1,n), sol(m,n-1)} + a(m,n)
        m, n = 0, 1, 2, ..., N.

    with initial contitions:

      sol(0,0) = a(0,0),
      sol(m,-1) = sol(-1,n) = 0.
"""

from __future__ import print_function

def solve(_input='p081_matrix.txt'):
    """
    main function.

    Arguments:
    _input: input file.
    """

    ## input validation
    try:
        _input_file = open(_input, 'r')
    except IOError:
        print('[ERROR] failed to open file %s' % (_input))
        return -1

    ## preprocessing
    # read file & prepare matrix
    _a = []
    for line in _input_file:
        line = line.rstrip('\n').split(',')
        _line = []
        for _el in line:
            _line.append(int(_el))
        _a.append(_line)

    _max = len(_a) - 1

    # initialize sol matrix
    sol = []
    _m = 0
    while _m <= _max:
        _n = 0
        _li = []
        while _n <= _max:
            _li.append(0)
            _n += 1
        sol.append(_li)
        _m += 1
    

    ## main
    # initial condition
    sol[0][0] = _a[0][0]

    # calculate sol[_m][_n] for fixed _m + _n = _npm
    _mpn = 1 
    while _mpn <= _max:

        # _m = 0
        sol[0][_mpn] = sol[0][_mpn-1] + _a[0][_mpn]

        # 0 < _m < _npm
        _m = 1
        while _m < _mpn:
            _n = _mpn - _m
            sol[_m][_n] = min(sol[_m-1][_n], sol[_m][_n-1]) + _a[_m][_n]
            _m += 1

        # _m = _mpn
        sol[_mpn][0] = sol[_mpn-1][0] + _a[_mpn][0]

        _mpn += 1

    while _mpn <= 2 * _max:

        # _npm - _max <= _m <= _max
        _m = _mpn - _max
        while _m <= _max:
            _n = _mpn - _m
            sol[_m][_n] = min(sol[_m-1][_n], sol[_m][_n-1]) + _a[_m][_n]
            _m += 1

        _mpn += 1

    return sol[_max][_max]

# call
print (solve())
