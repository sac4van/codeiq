# -*- coding: utf-8 -*-
"""
    problem:
        https://codeiq.jp/challenge/3397
    
    functions:
        g(n) = n * 10^(n-1)
        (total number of the char '3' in the set of n-digit numbers)

    main:
        F(m) = d_n ... d_2 d_1 in 10-adic form.

        0) g(n) <= m < g(n+1)
           r_1 = m - g(n)

           n3 = 0 : number of 3 found.

        1) find d_n:
         switch r_1 / (g(n-1) + n3*10^(n-1)):
          case 0:  d_n = 0
          case 1:  d_n = 1
          case 2:  d_n = 2
          case >2:
            switch (r_1 - 10^(n-1)) / (g(n-1) + n3*10^(n-1)):
                case < 4: d_n = 3 and n3 += 1
                case 4: d_n = 4
                ...
                case 9: d_n = 9

         

"""

from __future__ import print_function
import sys

def solve(_input):
    """
    main function.
    
    Arguments:
    _input -- string of the format "m", where m is positive integer.
    """

    # input validation
    _l = _input.split(" ")
    try:
        _m= int(_l[0])
    except (ValueError) as ex:
        print ('[ERROR] Please input a string of the format "m" where m is positive integer.')
        return -1

    ## preprocessing
    # find digit length
    _n = 1
    for _i in xrange(1,20):
        if _m <= _g(_i):
            _n = _i
            break

    _n3 = 0
    _ans = ''
    for _i in xrange(_n, 1, -1):
        for _q in xrange(0, 3, 1):
            if _m <= (_q + 1) * ( _g(_i-1) + _n3 * 10**(_i - 1)):
                _ans += str(_q)
                _m -=  _q * ( _g(_i-1) + _n3 * 10**(_i - 1))
                break
        _q = 3
        if _m <= (_q + 1) * ( _g(_i - 1) + _n3 * 10**(_i - 1)) + 10**(_i - 1):
            _ans += '3'
            _n3 += 1
            _m -= _q * _g(_i - 1) + _n3 * 10**(_i - 1)
            continue
        for _q in xrange(4, 10, 1):
            if _m <= (_q + 1) * ( _g(_i-1) + _n3 * 10**(_i - 1)) + 10**(_i - 1):
                _ans += str(_q)
                _m -= _q * ( _g(_i-1) + _n3 * 10**(_i - 1)) + 10**(_i - 1)
                break

#    print('debug: _n3, _m', _n3, _m)

    if _n3 == 0:
        _ans += '3'
        return _ans
    else:
        for _q in xrange(0,3,1):
            if _m <= _n3 * (_q+1):
                _ans += str(_q)
                return _ans
        for _q in xrange(3,10,1):
            if _m - 1 <= _n3 * (_q + 1):
                _ans += str(_q)
                return _ans
            


def _g(_n):
    """
    total number of the char '3' in the set of n-digit numbers
    """
    return _n * 10**(_n-1)

# call
print (solve(sys.stdin.readline()))
