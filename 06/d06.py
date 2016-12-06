#!/usr/bin/env python3.5

char_dicts = [] # array of dicts
with open('input.txt') as in_f:
	line = in_f.readline().strip()
	for c in line:
	   char_dicts.append({})
	
	while line != '':
		for index, letter in enumerate(line):
			if letter not in char_dicts[index]:
				char_dicts[index][letter] = 0
			char_dicts[index][letter] += 1
		line = in_f.readline().strip()

message = ''
message2 = ''
for index, d in enumerate(char_dicts):
	message += max(char_dicts[index], key=lambda x: char_dicts[index][x])
	message2 += min(char_dicts[index], key=lambda x: char_dicts[index][x])
print('part1:',message)
print('part2:',message2)
