#!/usr/bin/env python3.5

# SUPER INEFFICIENT - brute force

n_elves = 20 # test input
#n_elves = 3012210

circle = [i+1 for i in range(n_elves)]

i = 0
while len(circle) > 1:
    print(circle)
    next_i = i +1
    if next_i >= len(circle):
        next_i = 0
    circle.pop(next_i)  # use deque instead: doubly linked list
    i += 1 # interesting logic...
    if i >= len(circle):
        i = 0

print(circle)
