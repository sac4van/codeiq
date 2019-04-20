# -*- coding: utf-8 -*-
a, b, c = map(int, raw_input().split())

ans="No"
if a < c and c < b:
    ans="Yes"
elif b < c and c < a:
    ans="Yes"

# 出力
print("{}".format(ans))