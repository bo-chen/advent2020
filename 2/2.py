import sys
import os
from functools import reduce

def count_ls(s, l):
    chars = list(s)
    chars.insert(0,0)
    repeats = reduce(lambda a,b: a+1 if b == l else a, chars)
    return repeats

def is_positioned(s, min, max, l):
    chars = list(s)
    return ((chars[min] == l) and (chars[max] != l)) or ((chars[min] != l) and (chars[max] == l))


ns = []
t = 0
with open("./input.txt") as fp:
    for line in fp:
        f,pas = line.split(":")
        nums, letter = f.split(" ")
        min, max = map(lambda x : int(x),nums.split("-"))

        repeats = count_ls(pas, letter)
        if is_positioned(pas, min, max, letter):
            t += 1

print(t)
