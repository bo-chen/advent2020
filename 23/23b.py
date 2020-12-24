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

cs = [6,4,3,7,1,9,2,5,8] #input
#cs = [3,8,9,1,2,5,4,6,7] #sample
minc = 1
maxc = int(1e6)

ns = {}

for i in range(0,len(cs)):
    if i + 1 == len(cs):
        ns[cs[i]] = 10
    else:
        ns[cs[i]] = cs[i+1]

for i in range(10, 1000000):
    ns[i] = i + 1

ns[1e6] = cs[0]

print(ns[8])
print(ns[1e6])
print(ns[6])

def print1():
    s = ""
    c = ns[1]
    while c != 1:
        s += str(c)
        c = ns[c]
    print(s)

def rc(c):
    #print1()
    dest = c - 1
    picked = ns[c]

    ns[c] = ns[ns[ns[ns[c]]]]
    removed = set((picked, ns[picked], ns[ns[picked]]))
    if dest < minc:
        dest = maxc
    while dest in removed:
        dest -= 1
        if dest < minc:
            dest = maxc

    prevdest = ns[dest]
    ns[dest] = picked
    ns[ns[ns[picked]]] = prevdest
    return ns[c]

cur = cs[0]
for i in range(int(1e7)):
    cur = rc(cur)
    if i % 1e6 == 0:
        print("loop", i)

#print(cs)
#print1()

print(ns[1] * ns[ns[1]])
