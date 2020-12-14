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

amask = 0 # for 0s
omask = 0 # for 1s
mem = {}
with open('./input.txt') as fp:
    for line in fp:
        ins, v = line.strip().split(" = ")
        if ins == "mask":
            amask = 0
            omask = 0
            for c in v:
                ov = 0
                av = 0
                if c == "X":
                    ov = 0
                    av = 1
                elif c == "1":
                    ov = 1
                elif c == "0":
                    av = 0
                amask = amask << 1
                omask = omask << 1
                omask += ov
                amask += av
        else:
            addr = int(ins[4:-1])
            print(addr)
            v = int(v)
            mem[addr] = (v & amask) | omask

t = 0
for k in mem.keys():
    t += mem[k]

print(t)















