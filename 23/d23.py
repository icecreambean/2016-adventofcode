#!/usr/bin/env python3.5
# taken from day 12 and modified

# part 2: too slow - needs recursion

import time

PART_1 = False
PART_2 = False

if PART_1:
    IN_FILE = 'in.txt'
    regs = {'a':7,'b':0,'c':0,'d':0}
elif PART_2:
    # reddit: need to consider while loop structures in the code
    # (should be less lazy and analyse the input myself...)
    IN_FILE = 'in.txt'
    regs = {'a':12,'b':0,'c':0,'d':0}
else:
    IN_FILE = 'in_ts.txt'
    regs = {'a':0,'b':0,'c':0,'d':0}

# inc is diff in value, set is special case cpy
VAL_IND = 0; STATUS_IND = 1
INC = 0; SET = 1 # for the status
# ((cpy - sets the counter))
# various inc / dec commands <- what to multiply
#    (ignore inc / dec of counter)
# ((jnz back to some instruction after cpy))
# -> needs recursion to handle nested loops
# RETURN: dict of reg_increments, new_cursor
def mul(regs, code, cursor):
    # TODO: handle cpy instructions to check recursively
    #       for while loops
    reg_inc = {'a':[0,INC],'b':[0,INC],'c':[0,INC],'d':[0,INC]}
    instruction = code[cursor]
    if instruction[0] != 'cpy':
        return reg_inc, cursor # not a loop structure, no changes
    # get instruction info
    n_loops = instruction[1] # (SHOULD MAKE A FUNCTION)
    if n_loops in regs:
        n_loops = regs[n_loops]
    else:
        n_loops = int(n_loops)
    if n_loops == 0: # no potential to be a loop on this step
        return reg_inc, cursor
    reg_counter = instruction[2] # a b c d (str)
    # check valid cpy instruction
    if reg_counter not in regs:
        return reg_inc, cursor
    # setup to go to next instruction after cpy if possible
    cur_cursor = cursor +1
    if cur_cursor >= len(code):
        return reg_inc, cursor
    new_cursor = cur_cursor # cursor pos on return
    found = False
    while new_cursor < len(code):
        cur_instruction = code[new_cursor]
        if cur_instruction[0] == 'tgl':
            return reg_inc, cursor # TODO: too lazy to handle
        if cur_instruction[0] == 'jnz':
            if cur_instruction[1] == reg_counter and \
                    new_cursor - cur_cursor == n_loops:
                # set cursor to instruction after jump
                new_cursor += 1
                found = True
                break
            # (potentially unknown behaviour) TODO
            # too lazy to handle nested looping right now...
            # (or i.e., need to learn to write code step by step)
            return reg_inc, cursor
        new_cursor += 1
    if not found: # no loop found
        return reg_inc, cursor
    # established how many lines the loop is contained over
    # (( note this could be merged with the first loop... ))
    while cur_cursor < new_cursor -1: # go up to jnz
        cur_instruction = code[cur_cursor]
        # disgusting code duplication due to spec change
        # and lazy design??
        if cur_instruction[0] == 'inc':
            if instruction[1] in regs: # only run if valid
                reg_inc[instruction[1]][VAL_IND] += 1
        elif cur_instruction[0] == 'dec':
            if instruction[1] in regs: # only run if valid
                reg_inc[instruction[1]][VAL_IND] -= 1
        elif cur_instruction[0] == 'cpy':
            val1 = instruction[1]
            val2 = instruction[2]
            if val2 in regs: # only run if valid
                if val1 in regs: # 1st val is a reg
                    # move contents in val1(reg) into val2(reg)
                    # copied value is 'set' every loop cycle
                    reg_inc[val2] = [regs[val1] + reg_inc[val1], SET]
                else: # 1st val is numeric
                    reg_inc[val2] = [int(val1), SET]
        else:
            print('unhandled instruction in mul:', cur_instruction)
        cur_cursor += 1
    # mul by n_loops
    for r in reg_inc:
        if reg_inc[r][STATUS_IND] == INC:
            reg_inc[r][VAL_IND] *= n_loops
    return reg_inc, new_cursor


def mul_update(regs, reg_inc):
    for r in regs:
        if reg_inc[r][STATUS_IND] == INC:
            regs[r] += reg_inc[r][VAL_IND]
        else:
            regs[r] = reg_inc[r][VAL_IND]
    #return regs (regs is a reference)


code = []
with open(IN_FILE) as in_f:
    # or use readlines
    for line in in_f:
        code.append(line.strip().split())

# run the assembly
start_time = time.time()
cursor = 0 # 1st instruction of code
while cursor < len(code):
    to_inc = True                   # IMPORTANT!!
    # part 2: analyse for 'loop' structures (mul optimisation)
    #reg_inc, cursor = mul(regs, code, cursor)
    #mul_update(regs, reg_inc)

    instruction = code[cursor]
    #print(regs)                     # DEBUG
    #print("   ", instruction)
    if instruction[0] == 'cpy':
        val1 = instruction[1]
        val2 = instruction[2]
        if val2 in regs: # only run if valid
            if val1 in regs: # 1st val is a reg
                # move contents in val1(reg) into val2(reg)
                regs[val2] = regs[val1]
            else: # 1st val is numeric
                regs[val2] = int(val1)

    elif instruction[0] == 'inc':
        if instruction[1] in regs: # only run if valid
            regs[instruction[1]] += 1

    elif instruction[0] == 'dec':
        if instruction[1] in regs: # only run if valid
            regs[instruction[1]] -= 1

    elif instruction[0] == 'jnz':
        # instruction always valid
        val1 = instruction[1] # reg or int
        jump_dist = instruction[2] # reg or int
        if jump_dist in regs:
            jump_dist = regs[jump_dist]
        else:
            jump_dist = int(jump_dist)
        if val1 in regs:
            if regs[val1] != 0:       # unnecessary code dup
                cursor += jump_dist
                to_inc = False
        else:
            if int(val1) != 0:
                cursor += jump_dist
                to_inc = False

    elif instruction[0] == 'tgl':
        val1 = instruction[1]
        if val1 in regs:
            tgl_cursor = cursor + regs[val1]
        else:
            tgl_cursor = cursor + val1
        if 0 <= tgl_cursor < len(code): # only if valid
            tgl_instruction = code[tgl_cursor]
            if len(tgl_instruction) == 2: # one arg
                if tgl_instruction[0] == 'inc':
                    tgl_instruction[0] = 'dec'
                else:
                    tgl_instruction[0] = 'inc'
            else: # 2 args
                if tgl_instruction[0] == 'jnz':
                    tgl_instruction[0] = 'cpy'
                else:
                    tgl_instruction[0] = 'jnz'

    # increment the cursor in normal operation
    if to_inc:
        cursor += 1

# result
print("******* Results:")
print(regs)
print("time taken:", time.time() - start_time)
