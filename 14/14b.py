import math
import numpy as np
import os
import re
import sys

masks = [[0,0]]# amask at 0 for setting to 0. Or mask at 1 for setting to 1
mem = {}

with open('./input.txt') as fp:
    for line in fp:
        ins, v = line.strip().split(" = ")
        if ins == "mask":
            masks = [[0,0]] # amask 0 for setting to 0. Or mask 1 for setting to 1
            for c in v:
                newmasks = []
                for i in range(len(masks)):
                    if c == "X":
                        # first force 1 on new mask
                        # amask
                        newm = []
                        newm.append(masks[i][0] << 1)
                        newm[0] += 1
                        # omask
                        newm.append(masks[i][1] << 1)
                        newm[1] += 1

                        newmasks.append(newm)
                        # now force 0 on old mask
                        masks[i][0] = masks[i][0] << 1
                        masks[i][1] = masks[i][1] << 1
                    elif c == "1":
                        masks[i][0] = masks[i][0] << 1
                        masks[i][0] += 1
                        masks[i][1] = masks[i][1] << 1
                        masks[i][1] += 1
                    elif c == "0":
                        masks[i][0] = masks[i][0] << 1
                        masks[i][0] += 1
                        masks[i][1] = masks[i][1] << 1

                masks = masks + newmasks
        else:
            addr = int(ins[4:-1])
            v = int(v)
            for amask, omask in masks:
                mem[(addr & amask) | omask] = v

t = 0
for k in mem.keys():
    #print("{0:b}".format(mem[k]), v)
    t += mem[k]

print(t)















