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

a = [13,0,10,12,1,5,8]
ns = {}

for i in range(len(a) - 1):
    n = a[i]
    ns[n] = i # last index

lastN = a[-1]

for i in range(len(a), 30000000):
    if lastN in ns.keys():
        li = ns[lastN]
        newN = i - 1 - li
    else:
        newN = 0
    ns[lastN] = i - 1
    lastN = newN

print(lastN)

