from collections import Counter
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
    s = []
    for _ in range(n):
        s.append(gete())

    c = Counter(s)

    for v in ['AC', 'WA', 'TLE', 'RE']:
        print(v, "x", c[v])


if __name__ == "__main__":
    main()
