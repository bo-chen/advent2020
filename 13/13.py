import sys
import os
import re
import math
import numpy as np

def pm(m):
    for r in m:
        s = ""
        for c in r:
            print(c, end="")
        print("")

with open('./input.txt') as fp:
    lines = fp.readlines()

bs = []
t = 0
t = int(lines[0])
for i in lines[1].strip().split(","):
    if i == "x":
        bs.append("x")
    else:
        bs.append(int(i))

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

incr = bs[0]
lt = 0
for i in range(len(bs)):
    # Add in 1 number at a time
    if bs[i] == "x":
        continue
    while True:
        if (lt + i) % bs[i] == 0:
            incr = lcm(incr, bs[i])
            break
        lt += incr

print(lt)

