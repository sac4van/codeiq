import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n, k = geta(int)
    p = list(geta(int))

    p.sort()

    print(sum(p[:k]))


if __name__ == "__main__":
    main()
