import sys
import os
import re

a = []
with open('./input.txt') as fp:
    for line in fp:
        a.append(int(line.strip()))

a.append(0)
a.sort()
a.append(a[len(a) -1] + 3)

freq = {0 : 0, 1:0, 2:0, 3:0}
prev = a[0]
for i in a[1:]:
    if i - prev == 0:
        print("BAD2")
    if i - prev > 3:
        print("BAD")
    freq[i - prev] += 1
    prev = i

print(freq[1] * freq[3])

l = len(a)
cached = {l-1 : 1}

def dfs(s):
    if s in cached.keys():
        return cached[s]
    t = dfs(s+1)
    if s + 2 < l and (a[s+2] - a[s]) <= 3:
        t += dfs(s+2)
    if s + 3 < l and (a[s+3] - a[s]) <= 3:
        t += dfs(s+3)

    cached[s] = t
    return t

print(dfs(0))



