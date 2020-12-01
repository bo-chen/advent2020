import sys
import os

ns = []
with open("./input.txt") as fp:
    for line in fp:
        i = int(line)
        ns.append(i)

for a in ns:
    if a > 2020:
        continue
    for b in ns:
        if a + b > 2020:
            continue
        for c in ns:
            if (a + b + c) == 2020:
                print(a * b * c)
                exit()
