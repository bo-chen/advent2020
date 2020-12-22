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

ls = []
p1s = []
p2s = []
with open('./input.txt') as fp:
    state = ""
    for line in fp:
        line = line.strip()
        if len(line) == 0:
            continue
        if state == "" and line == "Player 1:":
            state = "p1"
            continue
        if state == "p1" and line == "Player 2:":
            state = "p2"
            continue
        if state == "p1":
            p1s.append(int(line))
        else:
            p2s.append(int(line))


def score(l):
    t = 0
    x = 1
    for i in range(len(l)-1, -1, -1):
        t += x * l[i]
        x += 1
    return t

def playg(p1, p2):
    #print("start p1", p1)
    #print("start p2", p2)
    r = 1
    ds = set()
    while True:
        #print("p1", p1)
        #print("p2", p2)
        hs = tuple(p1)
        if hs in ds:
            #print("p1 dupe win")
            return "p1", score(p1)
        ds.add(hs)

        if len(p1) == 0:
            #print("p2 win")
            return "p2", score(p2)
        if len(p2) == 0:
            #print("p1 win")
            return "p1", score(p1)

        w = ""
        c1 = p1[0]
        p1 = p1[1:]
        c2 = p2[0]
        p2 = p2[1:]
        if (c1 <= len(p1)) and (c2 <= len(p2)):
            w, n = playg(p1[:c1], p2[:c2])
            #print(w, "wins recurse")
        elif c1 > c2:
            w = "p1"
        else:
            w = "p2"
        # print(w, r)

        if w == "p1":
            p1 = p1 + [c1, c2]
        elif w == "p2":
            p2 = p2 + [c2, c1]
        else:
            print("bad")
        r += 1

w, n = playg(p1s, p2s)
print(w, n)

