import math
import numpy as np
import os
import re
import sys

ls = []
with open('./input.txt') as fp:
    for line in fp:
        ls.append(line.strip())

def eval(l):
    #print("eval", l)
    depth = 0
    parens = False
    begin = 0
    end = 0
    # find the first outer set of parens first
    for i in range(len(l)):
        c = l[i]
        if c == "(":
            depth += 1
            parens = True
            if depth == 1:
                begin = i+1
        elif c == ")":
            depth -= 1
            if depth == 0:
                end = i
                break
            if depth < 0:
                print("bad3")

    if parens:
        # eval the outer parens and redo
        n = eval(l[begin:end])
        s = l[0:begin-1] + str(n) + l[end+1:]
        return eval(s)
    else:
        # no parens
        ms = l.split("*")
        macc = 1
        for m in ms:
            ps = m.split("+")
            pacc = 0
            for p in ps:
                n = int(p.strip())
                pacc += n
            macc *= pacc
        return macc

t = 0
for l in ls:
    n = eval(l)
    t += n

print(t)
