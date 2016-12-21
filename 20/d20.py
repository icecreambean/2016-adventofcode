#!/usr/bin/env python3.5
from collections import deque
# O(n^2)?? at least the list decreases in size over time
# in O(1) fashion...

# inclusive, range of tuples
ranges = deque()
START = 0
END = 1

PART1 = False
all_allowed = []
MAX_VAL = 4294967295

with open('in.txt') as in_f:
    for line in in_f:
        start,end = line.strip().split('-')
        ranges.append( (int(start),int(end)) )

lowest = 0
while True:
    i = 0 # deque index
    lowest_updated = False
    while i < len(ranges):
        if ranges[0][END] < lowest:
            ranges.popleft()
            # no need to increment i
            continue
        if ranges[0][START] <= lowest <= ranges[0][END]:
            lowest = ranges[0][END] +1
            ranges.popleft()
            # no need to increment i
            lowest_updated = True
            continue
        # nothing interesting yet with this range
        i += 1
        ranges.rotate(-1)
    if not lowest_updated:
        if PART1:
            break
        # (note: test for len(ranges) == 0; efficiency)
        if lowest > MAX_VAL: # edge case: '4294967296'
            break
        all_allowed.append(lowest)
        lowest += 1 # test next number up
        if lowest > MAX_VAL: # another edge case test :/
            break

if PART1:
    print(lowest)
else:
    #print(all_allowed)
    print(len(all_allowed))
