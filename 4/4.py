import sys
import os
import re

a = []
c = {}
with open("./input.txt") as fp:
    for line in fp:
        for kv in line.strip().split(" "):
            if len(kv) == 0:
                next = True
                continue
            k,v = kv.split(":")
            c[k] = v

        if next == True:
            a.append(c)
            c = {}
            next = False
a.append(c)

t = 0
for p in a:
    good = True
    for k in ["byr","iyr","eyr","hgt","hcl","ecl","pid"]:
        if k not in p.keys():
            good = False

    if (good != True):
        continue

    byr = p["byr"]
    if re.search("^\d\d\d\d$", byr) is None:
        continue
    if (int(byr) < 1920 or int(byr) > 2002):
        continue

    iyr = p["iyr"]
    if re.search("^\d\d\d\d$", iyr) is None:
        continue
    if (int(iyr) < 2010 or int(iyr) > 2020):
        continue

    eyr = p["eyr"]
    if re.search("^\d\d\d\d$", eyr) is None:
        continue
    if (int(eyr) < 2020 or int(eyr) > 2030):
        continue

    hgt = p["hgt"]
    m = re.search("^(\d+)(cm|in)$", hgt)
    if m is None:
        continue
    if m[2] == "cm" and (int(m[1]) < 150 or int(m[1]) > 193):
        continue
    if m[2] == "in" and (int(m[1]) < 59 or int(m[1]) > 76):
        continue

    hcl = p["hcl"]
    m = re.search("^#([0-9a-f]{6})$", hcl)
    if m is None:
        continue

    ecl = p["ecl"]
    m = re.search("^amb|blu|brn|gry|grn|hzl|oth$", ecl)
    if m is None:
        continue


    pid = p["pid"]
    m = re.search("^\d{9}$", pid)
    if m is None:
        continue

    t += 1

print(t)
