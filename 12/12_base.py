import math
import numpy as np
import os
import re
import sys

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

