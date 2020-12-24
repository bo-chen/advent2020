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

def d2c(str, x, y):
    if str == "e":
        return x+1, y
    elif str == "w":
        return x - 1, y
    elif str == "nw":
        return x - (y % 2), y + 1
    elif str == "ne":
        return x + (y + 1) % 2, y + 1
    elif str == "sw":
        return x - (y % 2), y - 1
    elif str == "se":
        return x + (y + 1) % 2, y - 1

ts = set()
with open('./input.txt') as fp:
    for line in fp:
        x, y = 0,0
        line = line.strip()

        i = 0
        while i < len(line):
            s = line[i]
            if s != "e" and s != "w":
                i += 1
                s = s + line[i]
            x, y = d2c(s, x, y)
            i += 1

        if (x,y) in ts:
            ts.remove((x,y))
        else:
            ts.add((x,y))

print(len(ts))

def ca(x,y):
    t = 0
    for d in ["e", "se", "sw", "w", "nw", "ne"]:
        nx, ny = d2c(d, x, y)
        if (nx,ny) in ts:
            t += 1
    return t

def n(ts):
    minx, miny, maxx, maxy = 1000, 1000, -1000, -1000
    for x,y in ts:
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y

    newts = set()
    for x in range(minx -1 , maxx + 2):
        for y in range(miny -1, maxy + 2):
            t = ca(x,y)
            #print(x,y,t,(x,y) in ts)
            if (x,y) in ts:
                # black
                if t > 0 and t <= 2:
                    newts.add((x,y))
                    #print("removed")
            else:
                if t == 2:
                    newts.add((x,y))
                    #print("added")
    return newts

#print(ts)
for i in range(100):
    ts = n(ts)

#print(ts)

print(len(ts))




