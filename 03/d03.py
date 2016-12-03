#!/usr/bin/env python3.5

in_file = open('input.txt') # use sys.stdin if you want
n_valid = 0
for line in in_file:
    line = line.split()
    line = list(map(int, line))
    line.sort()
    if line[0] + line[1] > line[2]:
        n_valid += 1

in_file.close()
print(n_valid)
