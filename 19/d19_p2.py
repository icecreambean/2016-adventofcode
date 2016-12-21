#!/usr/bin/env python3.5
# disclaimer: attempts to replicate a solution on reddit
# *** very cool and fast way to code up a solution
# *** (otherwise, would code it in same manner to cs1927 course)
# still makes use of brute force - research up on the maths
# practises python oop syntax??

# initialisation is O(2n) - should make O(n) :/
# computation per loop is now O(1) instead of O(n) - but can you only
# do this with a custom data structure? :(

import sys

#n_elves = 5
n_elves = 3012210

# for a custom deque (more control)
class Node:
    # (static variables here)
    def __init__(self, val, prev_node, next_node):
        # (instance variables)
        self.val = val
        self.prev_node = prev_node
        self.next_node = next_node
    # (getters and setters to avoid encapsulation breaking...)

def print_list(head):
    cur = head
    print(str(cur.val) + '->',end='')
    cur = cur.next_node
    while cur != head:
        print(str(cur.val) + '->',end='')
        cur = cur.next_node
    print('END')


elves = [Node(i+1,None,None) for i in range(n_elves)]
# for next_node: (more efficient to use one loop :/)
for i in range(n_elves -1):
    elves[i].next_node = elves[i+1]
# ** link last elf back to first elf
elves[n_elves -1].next_node = elves[0]
# for prev_node:
for i in range(1, n_elves):
    elves[i].prev_node = elves[i-1]
# ** link first elf back to last elf
elves[0].prev_node = elves[n_elves -1]
# elf sitting opposite 1 & left; result is 'floored'
opp_elf = elves[int(n_elves/2)]
cur_elf = elves[0]

# no need to use the array again - the array sets up the linked list
n_loops = 0 # debug
while cur_elf.next_node != cur_elf:
    #prev_of_opp = opp_elf.prev_node
    #next_of_opp = opp_elf.next_node
    opp_elf.prev_node.next_node = opp_elf.next_node
    opp_elf.next_node.prev_node = opp_elf.prev_node
    # (can't 'free' opp_elf under this array implementation?)
    # update cursors, deque length
    n_elves -= 1
    cur_elf = cur_elf.next_node # next elf's turn
    opp_elf = opp_elf.next_node # recalc new 'opp' position
    if not (n_elves % 2): # shift one more, if even
        opp_elf = opp_elf.next_node # adjust such that it is 'left'
    n_loops += 1

print(cur_elf.val)
