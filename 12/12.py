import sys
import os
import re
import numpy as np

def pm(m):
    for r in m:
        s = ""
        for c in r:
            print(c, end="")
        print("")

def rotate(i, degrees):
    times = int(degrees / 90)

    if i == "L":
        times *= 3
    times = times % 4

    next = w
    rm = [[0, 1],
          [-1, 0]]
    for z in range(times):
        next = np.matmul(rm, next)

    return next

a = []
with open('./input.txt') as fp:
    for line in fp:
        ins = [line[0], int(line[1:])]
        a.append(ins)

w = np.array([10,1])
loc = np.array([0,0])

for [i, n] in a:
    if i == "L" or i == "R":
        w = rotate(i, n)
    elif i == "N":
        w[1] += n
    elif i == "S":
        w[1] -= n
    elif i == "W":
        w[0] -= n
    elif i == "E":
        w[0] += n
    elif i == "F":
        loc = (n * w) + loc
    else:
        exit("No good")

print(loc)
print(abs(loc[0]) + abs(loc[1]))
