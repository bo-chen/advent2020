import sys
import os
import re

c_rules = {}
c_inverse = {}
with open("./input.txt") as fp:
    for line in fp:
        line = line.strip()
        parent, cs = line.split(" bags contain ")
        if cs != "no other bags.":
            cs = re.split(" bags*, ", re.sub(" bags*.$", "", cs))
            c_rules[parent] = []
            for c in cs:
                n = int(c[0])
                k = c[2:]
                if k in c_inverse.keys():
                    c_inverse[k].append(parent)
                else:
                    c_inverse[k] = [parent]
                c_rules[parent].append([k, n])

def inverse_count(parent, ted):
    if parent in c_inverse.keys():
        t = 0
        for c in c_inverse[parent]:
            if c in ted:
               continue
            ted.append(c)
            t += 1 + inverse_count(c, ted)
        return t
    else:
        return 0

def b_count(parent):
    if parent in c_rules.keys():
        t = 1
        for r in c_rules[parent]:
            c, n = r
            t += n * b_count(c)
        return t
    else:
        return 1

print(inverse_count("shiny gold", []))
print(b_count("shiny gold") - 1)
