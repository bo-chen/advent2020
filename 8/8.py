import sys
import os
import re

def read_program(fname):
    prog = []
    with open(fname) as fp:
        for line in fp:
            line = line.strip()
            ins, v = line.split(" ")
            v = int(v)
            prog.append([ins, v])

    return prog

prog = read_program("./input.txt")
psize = len(prog)

def run(flip_ins):
    pc = 0
    acc = 0
    visited = set([])
    while True:
        if pc in visited:
            return False, acc
        visited.add(pc)

        ins, v = prog[pc]
        if (ins == "nop" and flip_ins != pc) or (flip_ins == pc and ins == "jmp"):
            pc += 1
        elif ins == "acc":
            acc += v
            pc += 1
        elif (ins == "jmp" and flip_ins != pc) or (flip_ins == pc and ins == "nop"):
            pc += v
        else:
            exit("BAD")

        if pc == psize:
            return True, acc

for i in range(psize):
    r, acc = run(i)
    if r == True:
        print(acc)
