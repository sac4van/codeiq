import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    h, w, k = geta(int)
    c = []
    for _ in range(h):
        c.append(gete())

    ans = 0
    for b in range(2**(h+w)):
        ih = []
        iw = []
        for i in range(h):
            ih.append(b & 1 == 1)
            b >>= 1
        for i in range(w):
            iw.append(b & 1 == 1)
            b >>= 1

        rem = 0
        for i in range(h):
            if ih[i]:
                continue
            for j in range(w):
                if iw[j]:
                    continue
                if c[i][j] == "#":
                    rem += 1

        if rem == k:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
