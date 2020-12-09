import sys
import os
import re

a = []
with open('./input.txt') as fp:
    for line in fp:
        a.append(int(line.strip()))

t = 0
for i in range(25,len(a)):
    t = a[i]
    is_s = False
    for n in range(i-25, i):
        for m in range(i-25,i):
            if m == n:
                continue
            if t == (a[m] + a[n]):
                is_s = True
                break
        if is_s:
            break
    if not is_s:
        print(t)
        break

target = t

cumm = a[0] + a[1]
i = 0
j = 1
while True:
    if cumm == target:
        ma = 0
        mi = target
        for k in range(i, j+1):
            if a[k] < mi:
                mi = a[k]
            if a[k] > ma:
                ma = a[k]
        print(mi + ma)
        break
    if cumm > target:
        cumm -= a[i]
        i += 1
    if cumm < target:
        j += 1
        cumm += a[j]

print("Over")

