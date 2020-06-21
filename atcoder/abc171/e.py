import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n = gete(int)
    a = list(geta(int))

    s = 0
    for ai in a:
        s ^= ai

    print(*[s ^ ai for ai in a], sep=" ")


if __name__ == "__main__":
    main()
