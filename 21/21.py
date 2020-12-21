import math
import numpy as np
import os
import re
import sys
from collections import OrderedDict

def pm(m):
    for r in m:
        s = ""
        for c in r:
            print(c, end="")
        print("")

ls = []
a2is = {}
i2a = {} # confirmed ingredients
tings = set()

def unique_ing(ing, al):
    for a in a2is.keys():
        if a == al:
            continue
        if ing in a2is[a]:
            a2is[a].remove(ing)
            if len(a2is[a]) == 1:
                u = list(a2is[a])[0]
                unique_ing(u, a)



with open('./input.txt') as fp:
    for line in fp:
        l = line.strip()
        m = re.search("^(.+) \(contains (.+)\)$", l)
        ings = []
        for ing in m.group(1).split(" "):
            ings.append(ing)
            tings.add(ing)
        als = []
        for al in m.group(2).split(", "):
            als.append(al)
        ls.append({"ings": set(ings), "als": set(als)})

        for al in als:
            av_ings = []
            for ing in ings:
                if ing not in i2a.keys():
                    av_ings.append(ing)
            if al not in a2is.keys():
                a2is[al] = set(av_ings)
            else:
                a2is[al] = a2is[al].intersection(av_ings)
                if len(a2is[al]) == 0:
                    print("Bad")
                if len(a2is[al]) == 1:
                    uing =list(a2is[al])[0]
                    i2a[uing] = al
                    unique_ing(uing, al)

safes = []
for ting in tings:
    safe = True
    for a in a2is.keys():
        if ting in a2is[a]:
            safe = False
            break
    if safe:
        safes.append(ting)

t = 0
for s in safes:
    for l in ls:
        if s in l["ings"]:
            t += 1

print(t)

a2i = {}
for a in a2is:
    if len(a2is[a]) == 0:
        print("Bad")
    if len(a2is[a]) == 1:
        a2i[a]= list(a2is[a])[0]

print(",".join(OrderedDict(sorted(a2i.items())).values()))
