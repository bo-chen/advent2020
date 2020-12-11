import sys
import os
import re

def p(m):
    for r in m:
        s = ""
        for c in r:
            print(c, end="")
        print("")

a = []
with open('./input.txt') as fp:
    for line in fp:
        a.append(line.strip())

l = len(a)
w = len(a[0])

def check_seat(m, i, j, x, y):
    i = i + x
    j = j + y
    while True:
        if i < 0 or i >= l:
            return "."
        if j < 0 or j >= w:
            return "."
        if m[i][j] == ".":
            i += x
            j += y
        else:
            return m[i][j]

def step(m):
    next = []
    changed = False
    for i in range(l):
        row = ''
        for j in range(w):
            adj = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if x == 0 and y == 0:
                        continue
                    if check_seat(m, i, j, x, y) == "#":
                        adj += 1
            if m[i][j] == "L" and adj == 0:
                row += "#"
                changed = True
            elif m[i][j] == "#" and adj >= 5:
                row += "L"
                changed = True
            else:
                row += m[i][j]
        next.append(row)

    return changed, next

changed = True
a
while changed:
    changed, a = step(a)

t = 0
for l in a:
    for c in l:
        if c == "#":
            t +=1

print(t)

