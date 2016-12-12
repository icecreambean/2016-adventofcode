#!/usr/bin/env python3.5

import time

code = []
with open('input.txt') as in_f:
    # or use readlines
    for line in in_f:
        code.append(line.strip().split())

# run the assembly
#regs = {'a':0,'b':0,'c':0,'d':0} # part 1
regs = {'a':0,'b':0,'c':1,'d':0} # part 2

start_time = time.time()
cursor = 0 # 1st instruction of code
while cursor < len(code):
    to_inc = True                   # IMPORTANT!!
    instruction = code[cursor]
    #print(regs)                     # DEBUG
    #print("   ", instruction)
    if instruction[0] == 'cpy':
        val1 = instruction[1]
        val2 = instruction[2]
        if val1 in regs: # 1st val is a reg
            # move contents in val1(reg) into val2(reg)
            regs[val2] = regs[val1]
        else: # 1st val is numeric
            regs[val2] = int(val1)

    elif instruction[0] == 'inc':
        regs[instruction[1]] += 1

    elif instruction[0] == 'dec':
        regs[instruction[1]] -= 1

    elif instruction[0] == 'jnz':
        val1 = instruction[1] # reg or int
        jump_dist = int(instruction[2])
        if val1 in regs:
            if regs[val1] != 0:
                cursor += jump_dist
                to_inc = False
        else:
            if int(val1) != 0:
                cursor += jump_dist
                to_inc = False
    # increment the cursor in normal operation
    if to_inc:
        cursor += 1

# result
print("******* Results:")
print(regs)
print("time taken:", time.time() - start_time)
