#!/usr/bin/env python3.5
import re

nodes = [ [] ] # 2d array (x,y)
USED = 0; AVAIL = 1

line_regex = re.compile('.*x(\d*)-y(\d*)\s*(\d*)T\s*(\d*)T\s*(\d*)T\s*(\d*)%')
with open('in.txt') as in_f:
    cur_x = 0
    for line in in_f:
        m = line_regex.search(line)
        if m == None:
            continue
        # x, y, size, used, avail, use(%)
        x = int(m.group(1))
        y = int(m.group(2))
        used = int(m.group(4))
        avail = int(m.group(5))
        if x > cur_x:
            nodes.append([])
            cur_x += 1
        nodes[x].append( [used,avail] )

# from part 1, assume the following details:
# ** (17,22) is '_'
# ** nodes can only be moved into (17,22), mark as '.'
# ** if node's used > (17,22)'s avail, mark as '#'
# ** goal data at ( len(nodes)-1, 0 ), mark as 'G'
# ** goal position is (0,0)
def print_map(nodes):
    avail = nodes[17][22][AVAIL] # lazy implementation
    for y in range(len(nodes[0])):
        for x in range(len(nodes)):
            # print the node
            cur_node = nodes[x][y]
            if cur_node[USED] == 0: # empty node at (17,22)
                if x != 17 and y != 22: # debug only
                    print('Something went wrong!', end='')
                print('_', end='')
            elif x == len(nodes)-1 and y == 0:
                print('G', end='')
            elif cur_node[USED] > avail:
                print('#', end='')
            else:
                print('.', end='')
        print('')


print_map(nodes)

# not sure how to do this with an algorithm (such as A*)
# need to fix day 11's efficiency issue first before i do
# this problem (which seems a lot harder)
#https://www.reddit.com/r/adventofcode/comments/5jry0y/2016_day_22_part_2_any_general_solution/

# reddit recommends just solving it manually...
