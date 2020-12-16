import math
import numpy as np
import os
import re
import sys

def pm(m):
    for r in m:
        s = ""
        for c in r:
            print(c, end=",")
        print("")

rules = []
pstate = "rules"
mine = []
nearby = []
with open('./input.txt') as fp:
    for line in fp:
        line = line.strip()
        if line == "":
            continue
        if pstate == "rules":
            if line == "your ticket:":
                pstate = "mine"
                continue
            n, r = line.split(": ")
            r1, r2 = r.split(" or ")
            r1min, r1max = r1.split("-")
            r1min = int(r1min)
            r1max = int(r1max)
            r2min, r2max = r2.split("-")
            r2min = int(r2min)
            r2max = int(r2max)
            rules.append( {"r1min":r1min, "r1max": r1max, "r2min":r2min, "r2max": r2max, "name": n })
        elif pstate == "mine":
            if line == "nearby tickets:":
                pstate = "nearby"
                continue
            t = []
            for i in line.split(","):
                t.append(int(i))
            mine = t
        elif pstate == "nearby":
            t = []
            for i in line.split(","):
                t.append(int(i))
            nearby.append(t)
        else:
            print("B")

nr = [mine]
for nt in nearby:
    keep = True
    for i in range(len(nt)):
        correct = False
        for r in rules:
            if (r["r1min"] <= nt[i] and nt[i] <= r["r1max"]) or (r["r2min"] <= nt[i] and nt[i] <= r["r2max"]):
                correct = True
        if not correct:
            keep = False
    if keep:
        nr.append(nt)

c_cache = {}
for r in rules:
    for i in range(len(mine)):
        c_cache[r["name"] + str(i)] = True

for r in rules:
    for i in range(len(nt)):
        match = True
        for nt in nr:
            if (r["r1min"] <= nt[i] and nt[i] <= r["r1max"]) or (r["r2min"] <= nt[i] and nt[i] <= r["r2max"]):
                1 + 1
            else:
                match = False
                break
        c_cache[r["name"] + str(i)] = match

b_cache = set()
def check_rule(rind, ts, matched_rules, inds):
    if frozenset(inds) in b_cache:
        return None
    if rind >= len(rules):
        return matched_rules
    crule = rules[rind]
    for i in inds:
        match = c_cache[(crule["name"] +  str(i))]
        if match:
            nm = matched_rules.copy()
            nm[crule["name"]] = i
            new_inds = inds.copy()
            new_inds.remove(i)
            r = check_rule(rind + 1, ts, nm, new_inds)
            if r is not None:
                return r

    b_cache.add(frozenset(inds))
    return None

ainds = []
for i in range(len(mine)):
    ainds.append(i)

r = check_rule(0, nr, {}, ainds)

print(r)
print(mine[r["departure location"]] * mine[r["departure station"]] * mine[r["departure platform"]] * mine[r["departure track"]] * mine[r["departure date"]] * mine[r["departure time"]])






