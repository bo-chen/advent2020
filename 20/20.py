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

tiles = {}
with open('./input.txt') as fp:
    tile = np.zeros((10,10), dtype = int)
    id = None
    lind = 0
    for line in fp:
        line = line.strip()
        if len(line.strip()) == 0:
            continue
        if id is None:
            #print(line.strip()[5:-1])
            id = int(line.strip()[5:-1])
            continue
        j = 0
        for c in line.strip():
            if c == "#":
                tile[lind, j] = 1
            else:
                tile[lind, j] = 0
            j += 1

        if lind == 9:
            tiles[id] = tile
            tile = np.zeros((10,10), dtype = int)
            id = None
            lind = 0
        else:
            lind += 1

fid = list(tiles.keys())[0]
mesh = {(0,0) : {"v" : tiles[fid], "id" : fid} }

def checku(t1, t2):
    return np.array_equal(t1[0,:], t2[9,:])
def checkd(t1, t2):
    return checku(t2, t1)
def checkl(t1, t2):
    return np.array_equal(t1[:,0], t2[:,9])
def checkr(t1, t2):
    return checkl(t2, t1)

def addtilestatic(id, t):
    # top
    for x,y in mesh.keys():
        m = mesh[(x,y)]
        if (x, y+1) in mesh.keys():
            continue
        if checku(m["v"], t):
            '''
            if (x-1, y+1) in mesh.keys()
                if checkl mesh[x-1,y+1]
            '''
            mesh[(x,y+1)]= {"v": t, "id": id}
            return True
    # bottom
    for x,y in mesh.keys():
        m = mesh[(x,y)]
        if (x, y-1) in mesh.keys():
            continue
        if checkd(m["v"], t):
            mesh[(x,y-1)]= {"v": t, "id": id}
            return True
    # left
    for x,y in mesh.keys():
        m = mesh[(x,y)]
        if (x -1, y) in mesh.keys():
            continue
        if checkl(m["v"], t):
            mesh[(x-1,y)]= {"v": t, "id": id}
            return True
    # right
    for x,y in mesh.keys():
        m = mesh[(x,y)]
        if (x +1, y) in mesh.keys():
            continue
        if checkr(m["v"], t):
            mesh[(x+1,y)]= {"v": t, "id": id}
            return True
    return False


def addtile(id, t):
    nt = t
    for i in range(4):
        r = addtilestatic(id, nt)
        if r:
            return r
        nt = np.rot90(nt)
    nt = np.fliplr(nt)
    for i in range(4):
        r = addtilestatic(id, nt)
        if r:
            return r
        nt = np.rot90(nt)
    return False

# keep adding tiles to the existing map
nextl = list(tiles.keys())
while True:
    unadded = []
    for id in nextl:
        if id == fid:
            continue
        r = addtile(id, tiles[id])
        if not r:
            unadded.append(id)
    if len(unadded) == 0:
        break
    nextl = unadded
    print(len(nextl), "to go")

minx, maxx = 10000, -10000
miny, maxy = 10000, -10000
for x,y in mesh.keys():
    if x < minx:
        minx = x
    if x > maxx:
        maxx = x
    if y < miny:
        miny = y
    if y > maxy:
        maxy = y
        #print((x,y), mesh[(x,y)]["id"])

print("part1:", mesh[(minx, miny)]["id"] *mesh[(minx, maxy)]["id"] *mesh[(maxx, miny)]["id"] *mesh[(maxx, maxy)]["id"])

dragon = np.zeros((3, 20), dtype = int)
with open('./dragon.txt') as fp:
    for line in fp:
        if len(line) == 0:
            continue
        j = 0
        for c in line:
            if j == 20:
                continue
            if c == "#":
                dragon[lind, j] = 1
            else:
                dragon[lind, j] = 0
            j += 1
        lind += 1

dragonsum = np.sum(dragon)
#print("dragon sum", dragonsum)
#print(dragon)

maxfinalx =(maxx - minx + 1) * 8
maxfinaly =(maxy - miny + 1) * 8
final = np.zeros((maxfinalx, maxfinaly), dtype = int)
#print(minx,maxx,miny,maxy)
# assemble final
for x in range(minx, maxx + 1):
    for y in range(miny, maxy +1):
        xs =(x - minx) * 8
        xe =(x - minx + 1) * 8
        ys =(y - miny) * 8
        ye =(y - miny + 1) * 8
        final[ys:ye,xs:xe] = mesh[(x,maxy - y + miny)]['v'][1:-1, 1:-1]

def countdsstatic(t):
    d = 0
    for x in range(maxfinalx - 3):
        for y in range(maxfinaly - 20):
            if np.sum(t[x:x+3,y:y+20] * dragon) == dragonsum:
                d += 1
    return d

def countds():
    nt = final
    for i in range(4):
        r = countdsstatic(nt)
        if r > 0:
            return r
        nt = np.rot90(nt)
    nt = np.fliplr(nt)
    for i in range(4):
        r = countdsstatic(nt)
        if r > 0:
            return r
        nt = np.rot90(nt)
    return None

ds = countds()
print("num dragons:", ds)
print("part2:", np.sum(final) - ds * dragonsum)
