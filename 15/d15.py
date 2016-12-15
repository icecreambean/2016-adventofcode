#!/usr/bin/env python3.5

# array of tuples (what is equivalent to a struct in py?)
discs = []
START_POS_IND = 0 # position at t = 0
NUM_POS_IND = 1 # no. of positions (for modulus)

def passes_disc(disc_id, t): # refers to discs[], time t
    # compute position of the disc (0 == passes through)
    disc_info = discs[disc_id]
    disc_pos = (disc_info[START_POS_IND] + t) % \
        disc_info[NUM_POS_IND]
    return not disc_pos

with open('in_p2.txt') as in_f:
    for line in in_f:
        # discs in file are in chronological order
        line = line.strip().split()
        n_pos = int(line[3])
        start_pos = int(line[-1][:-1])
        discs.append( (start_pos, n_pos) )

t = 0 # time
while True:
    # success(t) = f1(t+1) and f2(t+2) and f3...
    successes = []
    for i in range(len(discs)):
        successes.append( passes_disc(i, t +i +1) )
    if False not in successes: # AND operation
        print('part 1: earliest t at:', t)
        break
    t += 1
