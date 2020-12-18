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
    while True:
        ins, v = prog[pc]
        if ins == "nop":
            pc += 1
        elif ins == "acc":
            acc += v
            pc += 1
        elif ins == "jmp":
            pc += v
        else:
            exit("BAD")

        if pc == psize:
            return True, acc

