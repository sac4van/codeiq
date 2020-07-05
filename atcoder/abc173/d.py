import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n = gete(int)
    a = list(geta(int))

    a.sort(reverse=True)

    ans = 2 * sum(a[:(n+1)//2]) - a[0]

    if n & 1 == 1:
        ans -= a[(n+1)//2-1]

    print(ans)


if __name__ == "__main__":
    main()
