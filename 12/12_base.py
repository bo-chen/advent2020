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

a = []
with open('./input.txt') as fp:
    for line in fp:
        a.append(line.strip())


