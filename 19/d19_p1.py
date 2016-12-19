#!/usr/bin/env python3.5

# part 1 solved mathematically! :o

#n_elves = 5 # test input
#n_elves = 9
n_elves = 3012210

cur_elf = 1
best_elf = 1
best_depth = 0
first_depth_add = n_elves

while cur_elf < n_elves:
    # guaranteed cur_elf is odd
    cur_depth = 0
    rank_add = first_depth_add # to divide by 2 each time (until odd)
    first_depth_add -= 1
    elf_rank = cur_elf # current and future ranks
    while elf_rank % 2: # while ranking is odd
        # works correctly: guaranteed rank_add terminates before or at
        # first instance of it becoming odd
        elf_rank += rank_add
        rank_add /= 2 # note this is a float
        cur_depth += 1
    if cur_depth > best_depth:
        best_elf = cur_elf
        best_depth = cur_depth

    #print(cur_elf, "depth:", cur_depth) # debug
    cur_elf += 2 # can skip even elf indexes, guaranteed depth 0

print(best_elf)
