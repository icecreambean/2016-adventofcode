#!/usr/bin/env python3.5
import re, sys

# reuse of part 1 code + small modifications
# various strategies:
# ** reverse start/end variables
# ** no change required for the 'reverse' option
# ** rotating by pos of char requires O(n) brute force,
#    working backwards

TEST = False
if TEST:
    pw = 'decab'
    f = 'in_t.txt'
else:
    pw = 'fbgdceah'
    f = 'in.txt'

lines = None
with open(f) as in_f:
    lines = in_f.readlines()

for line in lines[::-1]:
    line = line.strip()
    print(line,':len:', len(pw), pw) # debug
    line = line.split()

    # ((reverse all operations in part 1))
    if line[0] == 'swap': # PART 2 DONE (swap start/end)
        end = line[2]
        start = line[-1]
        if line[1] == 'position':
            start = int(start) # one char
            end = int(end)
            pw_temp = list(pw)
            temp = pw_temp[start]
            pw_temp[start] = pw_temp[end]
            pw_temp[end] = temp
            pw = ''.join(pw_temp)
        else:
            pw_temp = list(pw)
            all_start = re.finditer(start, pw)
            all_end = re.finditer(end, pw)
            for g in all_start:
                pw_temp[g.start(0)] = end
            for g in all_end:
                pw_temp[g.start(0)] = start
            pw = ''.join(pw_temp)
    elif line[0] == 'rotate': # PART 2 DONE (swap left/right)
        if line[1] == 'right':
            amt = int(line[2]) % len(pw)
            pw = pw[amt:] + pw[:amt]
        elif line[1] == 'left':
            amt = int(line[2]) % len(pw)
            amt = len(pw) - amt
            pw = pw[amt:] + pw[:amt]
        else: # based on position of letter
            # test all rotation configs to find correct one
            pw_cur = pw
            c = line[-1]
            for i in range(len(pw)):
                # run part 1 test, see if pw_cur gives pw
                amt = re.search(c, pw_cur).start(0)
                if amt >= 4:
                    amt += 2 # special + regular
                else:
                    amt += 1 # just the regular
                amt = amt % len(pw_cur)
                # rotate right (same code)
                amt = len(pw_cur) - amt
                pw_temp = pw_cur[amt:] + pw_cur[:amt]
                if pw_temp == pw: # found
                    pw = pw_cur
                    break
                # otherwise, update pw_cur (rotate right)
                amt = 1
                pw_cur = pw_cur[amt:] + pw_cur[:amt]
    elif line[0] == 'reverse': # PART 2 DONE (no change required)
        start = int(line[2]) # range
        end = int(line[-1])
        if start != 0:
            pw = pw[:start] + pw[end:start-1:-1] + \
                 pw[end+1:]
        else:
            # special syntax required (gross)
            pw = pw[end::-1] + pw[end+1:]
    elif line[0] == 'move': # PART 2 DONE (swap start/end)
        end = int(line[2]) # one char
        start = int(line[-1])
        if start < end:
            pw = pw[:start] + pw[start+1 : end+1] + \
                 pw[start] + pw[end+1:]
        elif start > end:
            pw_temp = pw[:end] + pw[start]
            pw_temp += pw[end:start] + pw[start+1:]
            pw = pw_temp
        # do nothing if start == end
    else:
        print("unhandled instruction:",line)



print(''.join(pw))
