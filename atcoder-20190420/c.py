# -*- coding: utf-8 -*-
n = int(raw_input())
s = str(raw_input())

ans=[]
bk=[]
for i in range(0,n):
    ans.append(-1)
    bk.append(-1)

ans[0]=0
if s[0]==".":
    bk[0]=0
else:
    bk[0]=1

for i in range(1,n):
    if s[i] == ".":
        bk[i] = bk[i-1]
        ans[i] = min(bk[i-1], ans[i-1]+1)
    else:
        bk[i] = bk[i-1] + 1
        ans[i] = min(ans[i-1], bk[i-1]+1)

print ans[n-1]
