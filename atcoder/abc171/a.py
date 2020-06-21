import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    a = gete()

    if ord('a') <= ord(a) <= ord("z"):
        print("a")
    else:
        print("A")


if __name__ == "__main__":
    main()
