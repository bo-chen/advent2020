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

pubk1 = 10705932
pubk2 = 12301431


def t(sn, lsize):
    v = 1
    for i in range(lsize):
        v *= sn
        v = v % 20201227
    return v

def findlsize(pubk):
    i = 1
    v = 1
    while True:
        v *= 7
        v = v % 20201227
        if v == pubk:
            return i
        i += 1

lsize1 = findlsize(pubk1)
lsize2 = findlsize(pubk2)

print(t(pubk1, lsize2))
print(t(pubk2, lsize1))
