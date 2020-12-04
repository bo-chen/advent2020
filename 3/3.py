import sys
import os

a = []
with open("./input.txt") as fp:
    i = 0
    for line in fp:
        a.append([])
        for c in list(line.strip()):
            a[i].append(c)
        i += 1

w = len(a[0])
h = len(a)

def trees(ws, hs):
    t = 0
    c = 0

    for hi in range(0, h, hs):
        if a[hi][c] == "#":
            t += 1
        c = (c + ws) % w
    return t

r = trees(3, 1) * trees(1,1) * trees(5,1) * trees(7,1) * trees(1,2)
print(r)

exit()

for l in a:
    for i in l:
        print(i, end="")
    print("")
