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

ls=  []
with open('./input.txt') as fp:
    for line in fp:
        ls.append(line.strip())

def eval(l):
    #print(l)
    acc = 0
    op = ""
    i = 0
    while True:
        if i >= len(l):
            break
        c = l[i]
        if c == " ":
            i += 1
            continue
        elif c == ")":
            return acc, i +1
        elif c == "+":
            op = "+"
            i += 1
            continue
        elif c == "*":
            op = "*"
            i += 1
            continue
        elif c == "(":
            n, skip = eval(l[i+1:])
            i += skip + 1
        else:
            m = re.search("^\d+", l[i:])
            n = int(m.group(0))
            i += len(m.group(0))

        if op == "":
            acc = n
        elif op == "+":
            acc = acc + n
            op = ""
        elif op == "*":
            acc = acc * n
            op = ""
        else:
            print("bad")

    return acc, i

t = 0
for l in ls:
    n,i = eval(l)
    t += n

print(t)




