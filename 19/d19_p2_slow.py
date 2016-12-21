#!/usr/bin/env python3.5

# brute force strategy for part 2 :/
# see if shift and rotate is more efficient :/
# *** doesn't matter if it's more efficient, O(n) is too slow
# *** HENCE -> need a make a custom data struct that saves the position
# *** of being 'opposite' the table, in order to get O(1) access.

import sys
from collections import deque
#from math import floor

#n_elves = 5 # test
#n_elves = 9
#n_elves = 3012210

n_elves = int(sys.argv[1])

elves = deque([i+1 for i in range(n_elves)])
while len(elves) > 1:
    #print(elves)
    #print('   removing:',elves[ int(len(elves) / 2) ])
    del elves[ int(len(elves) / 2) ]
    elves.rotate(-1)

print(elves[0])


#https://www.reddit.com/r/adventofcode/comments/5j4lp1/2016_day_19_solutions/ ~ >:(
# 1. write a simulator to look for patterns
# alternatively,
# 1. learn about data structures better
# 2. for efficiency, keep track of the 'middle'. It should move at
#    nearly the same pace the cur_elf moves.
# alternatively,
# 1. study a math degree:
#    https://en.wikipedia.org/wiki/Josephus_problem
