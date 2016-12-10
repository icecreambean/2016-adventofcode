#!/usr/bin/env python3.5

bot_holder = {} # hash(bot) of length 2 arrays
output_holder = {} # hash(num_id)
# required as 'value' instructs not at start of file
instructions = [] # holds strings broken up as words


# grab input
with open('input.txt') as in_f:
    for line in in_f:
        line = line.strip().split()
        # value line
        if line[0] == 'value':
            val = int(line[1])
            bot = int(line[5])
            if bot not in bot_holder:
                bot_holder[bot] = []
            bot_holder[bot].append(val)
            continue
        instructions.append(line)

bot_compare_61_17 = -1

# only contains 'bot' lines
# keep looping infinitely until all lines resolved
i = 0
while i < len(instructions):
    line = instructions[i]

    bot_from = int(line[1])
    low_type = line[5] # 'bot' or 'output'
    low_to = int(line[6])
    high_type = line[10] # 'bot' or 'output'
    high_to = int(line[11])

    # skip if the action cannot be performed yet
    if (bot_from not in bot_holder) or \
            (len(bot_holder[bot_from]) < 2):
        i += 1
        if i >= len(instructions):
            i = 0
        continue

    bot_holder[bot_from].sort() # array size 2, low = [0], hi = [1]
    # for answering part 1:
    if bot_holder[bot_from] == [17,61]:
        bot_compare_61_17 = bot_from

    low_val = bot_holder[bot_from].pop(0)
    high_val = bot_holder[bot_from].pop(0)

    # code duplication (could write a function?)
    if low_type == 'bot':
        if low_to not in bot_holder:
            bot_holder[low_to] = []
        bot_holder[low_to].append(low_val)
    else:
        output_holder[low_to] = low_val

    if high_type == 'bot':
        if high_to not in bot_holder:
            bot_holder[high_to] = []
        bot_holder[high_to].append(high_val)
    else:
        output_holder[high_to] = high_val

    # decrement array length (as opposed to incrementing i)
    instructions.pop(i)
    if i >= len(instructions):
        i = 0

# print out the ans for part 1
print("ans (part 1): bot", bot_compare_61_17)
ans2 = output_holder[0] * output_holder[1] * output_holder[2]
print("ans (part 2):    ", ans2)
# print out the output's contents
for i in sorted(output_holder.keys()):
    print("output bin {:2} holds: {:2}".format(i, output_holder[i]))
