import sys
import os
import re

t = 0
g = {}
ng = 0
with open("./input.txt") as fp:
    for line in fp:
        line = line.strip()

        if len(line) == 0:
            for c in g.values():
                if c == ng:
                    t += 1
            g = {}
            ng = 0
            continue

        ng += 1
        for c in list(line):
            if c in g.keys():
                g[c] = g[c] + 1
            else:
                g[c] = 1

for c in g.values():
    if c == ng:
        t += 1

print(t)
