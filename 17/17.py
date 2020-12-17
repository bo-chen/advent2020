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

xbias = 15
ybias = 15
zbias = 8
wbias = 8
m = np.zeros((2*xbias+1, 2*ybias + 1, 2*zbias +1, 2*wbias +1), dtype = int)
def get(m, x, y, w, z):
    return m[x+xbias,y+ybias,z+zbias, w+wbias]
def set(m, x, y, z, w, v):
    m[x+xbias,y+ybias,z+zbias, w+wbias] = v

with open('./input.txt') as fp:
    z = 0
    w =0
    y = -1
    x = -1
    for line in fp:
        x = -1
        for c in line.strip():
            v = 0
            if c == "#":
                v = 1
            set(m, x, y, z, w, v)
            x += 1
        y += 1

def countn(m, x, y, z,w):
    t = 0
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                for l in range(-1,2):
                    if i == 0 and j ==0 and k == 0 and l == 0:
                        continue
                    if get(m, x+i, y+j, z+k, w+l) == 1:
                        t += 1
    return t

def step(m):
    nm = np.zeros((2*xbias+1, 2*ybias + 1, 2*zbias +1, 2*wbias +1), dtype = int)
    for x in range(-1 * xbias, xbias):
        for y in range(-1 * ybias, ybias):
            for z in range(-1 * zbias, zbias):
                for w in range(-1 * wbias, wbias):
                    v = get(m, x,y,z,w)
                    n = countn(m, x,y,z,w)
                    # print(x,y,z,n)
                    newv = 0
                    if v == 0 and (n == 3):
                        newv = 1
                    if v == 1 and (n == 2 or n == 3):
                        newv = 1
                    set(nm, x,y,z,w, newv)
    return nm

print(np.sum(m))
for i in range(6):
    m = step(m)

print(np.sum(m))







