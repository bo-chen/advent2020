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

ls = []
with open('./input.txt') as fp:
    for line in fp:
        ls.append(line.strip())


rules = {}
i = 0
while True:
    l = ls[i]
    if i >= len(ls) or l == "":
        break
    indstr, rstr = l.split(":")
    ind = int(indstr)

    m = re.search("\"(.+)\"",l)
    if m is not None:
        # match rule
        rules[ind] = {"type":"str", "v":m.group(1)}
    else:
        # concat rule
        ors = [] # [{:parts [1 2]}]
        rcstrs = rstr.split(" | ")
        for rcs in rcstrs:
            ns = rcs.strip().split(" ")
            ands = []
            for nstr in ns:
                ands.append(int(nstr))
            ors.append({"ands": ands})
        rules[ind] = {"type":"bool", "ors": ors}
    i+=1

def r2reg(rind):
    rstr = ""
    r = rules[rind]
    if r["type"] == "str":
        return r["v"]
    else:
        ostrs = []
        for o in r["ors"]:
            astrs = []
            for a in o["ands"]:
                astrs.append( "(" + r2reg(a) + ")" )
            ostrs.append("(" + "".join(astrs) + ")")
        return "|".join(ostrs)


reg =r2reg(0)

i2 = i
t = 0
while True:
    if i >= len(ls):
        break
    l = ls[i]
    m = re.match("^" + reg +  "$", l)
    if m is not None:
        t += 1
    i += 1

print(t)

def mands(ands, s):
    for r in mr(ands[0], s):
        #print(ands[0],s, "yielded", r)
        if r > 0:
            if len(ands) == 1:
                yield r
            else:
                for r2 in mands(ands[1:], s[r:]):
                    #print(ands[1:], s[r:], "yielded", r)
                    if r2 > 0:
                        yield r + r2

def mr(rind, s):
    if rind == 8:
        i = 0
        rs = []
        while True:
            matched = False
            for r in mr(42, s[i:]):
                if r > 0:
                    i += r
                    rs.append(i)
                    matched = True
            if not matched:
                break
        for r in rs:
            yield r
    elif rind == 11:
        i = 0
        rs = []
        while True:
            matched = False
            for r in mr(42, s[i:]):
                if r > 0:
                    i += r
                    rs.append(i)
                    matched = True
            if not matched:
                break
        paired = 0
        #print("11 first matched", rs)
        for c in range(len(rs)):
            if paired == len(rs):
                break
            matched = False
            for r in mr(31, s[i:]):
                if r > 0:
                    i += r
                    paired += 1
                    matched = True
            if not matched:
                break
        #print("11 then matched", paired)
        if paired > len(rs):
            print("bad1")
        if paired == len(rs):
            yield i
    else:
        rule = rules[rind]
        #print(rule, s)
        if rule["type"] == "str":
            if s[:len(rule["v"])] != rule["v"]:
                #print(s, "did not match", rule["v"])
                1 +1
            else:
                yield 1
        else:
            for o in rule["ors"]:
                for r in mands(o["ands"], s):
                    #print(o["ands"],s, "yielded", r)
                    if r > 0:
                        yield r

# print(rules)
t = 0
i2 = i2 + 1
while True:
    if i2 >= len(ls):
        break
    l = ls[i2]
    matched = False
    for r in mr(0, l):
        if r == len(l):
            matched = True
    if matched:
        # print(l, "matched")
        t += 1
    i2 += 1

print(t)
