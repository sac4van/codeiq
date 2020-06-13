import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n, k = geta(int)
    ans = 0
    for i in range(1, n+1):
        l = i
        while l < k:
            l *= 2
        ans += i/l/n

    print(ans)


if __name__ == "__main__":
    main()
