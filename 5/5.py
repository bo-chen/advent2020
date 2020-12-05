import sys
import os
import re

ma = 0
mi = 10000
nums = {}
with open("./input.txt") as fp:
    for line in fp:
        l = list(line.strip())
        rt = l[0:7]
        ct = l[7:10]

        row = 0
        for rl in rt:
            row = row << 1
            if rl == "F":
                row += 0
            elif rl == "B":
                row += 1
            else:
                print("BAD")

        col = 0
        for cl in ct:
            col = col << 1
            if cl == "L":
                col += 0
            elif cl == "R":
                col += 1
            else:
                print("BAD2")

        id = (row * 8 + col)
        if id > ma:
            ma = id
        if id < mi:
            mi = id

        nums[id] = 1

for id in range(mi, ma):
    if id not in nums.keys():
        print(id)


print(mi)
print(ma)

# print()
