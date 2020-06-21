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
    ans = ""

    while n > 0:
        n -= 1
        ans += chr(n % 26 + ord('a'))
        n //= 26

    print(ans[::-1])


if __name__ == "__main__":
    main()
