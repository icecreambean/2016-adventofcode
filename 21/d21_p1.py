#!/usr/bin/env python3.5
import re

# disgusting code? splicing is very finnicky, and some
# strange syntax for edge cases? (PART 1)
# ((don't like this code - written all at once without
#   any vigourous testing...))
# ** though since part 2 works, part 1 probably mostly correct

TEST = True

if TEST:
    pw = 'abcde'
    f = 'in_t.txt'
else:
    pw = 'abcdefgh'
    f = 'in.txt'

with open(f) as in_f:
    for line in in_f:
        line = line.strip()
        print(line,':todo:', pw) # debug
        line = line.split()
        if line[0] == 'swap':
            start = line[2]
            end = line[-1]
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
        elif line[0] == 'rotate':
            if line[1] == 'left':
                amt = int(line[2]) % len(pw)
                pw = pw[amt:] + pw[:amt]
            elif line[1] == 'right':
                amt = int(line[2]) % len(pw)
                amt = len(pw) - amt
                pw = pw[amt:] + pw[:amt]
            else: # based on position of letter
                c = line[-1]
                amt = re.search(c, pw).start(0)
                if amt >= 4:
                    amt += 2 # special + regular
                else:
                    amt += 1 # just the regular
                amt = amt % len(pw)
                # rotate right (same code)
                amt = len(pw) - amt
                pw = pw[amt:] + pw[:amt]
        elif line[0] == 'reverse':
            start = int(line[2]) # range
            end = int(line[-1])
            if start != 0:
                pw = pw[:start] + pw[end:start-1:-1] + \
                     pw[end+1:]
            else:
                # special syntax required (gross)
                pw = pw[end::-1] + pw[end+1:]
        elif line[0] == 'move':
            start = int(line[2]) # one char
            end = int(line[-1])
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
