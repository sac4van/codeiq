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

    d = defaultdict(int)
    s = sum(a)
    for i in a:
        d[i] += 1

    for _ in range(gete(int)):
        b, c = geta(int)

        if b in d:
            s += (c-b) * d[b]
            d[c] += d[b]
            d[b] = 0

        print(s)


if __name__ == "__main__":
    main()
