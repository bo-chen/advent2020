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
minc = min(cs)
maxc = max(cs)

#cs += list(range(10,33))
#print(len(cs))

def wrapr(start, end, l):
    while start > l:
        start -= l
        end -= l

    if end <= l:
        return start, end, 0, 0
    else:
        return start, l, 0, end - l

def rc(curi, cs):
    #print(cs, "curi", curi, "label", cs[curi])
    c = cs[curi]
    dest = cs[curi] - 1
    s1,e1,s2,e2 = wrapr(curi+1, curi+4, len(cs))
    removed = cs[s1:e1] + cs[s2:e2]
    if e2 == 0:
        cs = cs[:s1] + cs[e1:]
    else:
        cs = cs[e2:s1]
        #print("picked", removed)
        #print("left", cs)
    if dest < minc:
        dest = maxc

    while dest in set(removed):
        dest -= 1
        if dest < minc:
            dest = maxc

    place = cs.index(dest)
    #print("place", place, cs[:place+1])
    cs = cs[:place + 1] + removed + cs[place+1:]

    #print("")
    return (cs.index(c) + 1) % len(cs) , cs

cur = 0
for i in range(100):
    cur, cs = rc(cur, cs)
    if i % 100 == 0:
        print(i)

#print(cs)
cut =(cs.index(1)+1) % len(cs)
cs = cs[cut:] +cs[:cut]

s = ""
for c in cs:
    s += str(c)
print(s[:-1])
