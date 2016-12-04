#!/usr/bin/env python3.5

import re

# shift c by n places (if alphabetical), otherwise, convert '-' to ' '
def shift_cipher(c, n):
	if c == '-':
		return ' '
	c_num = ord(c) + (n % 26)
	if c_num > ord('z'): # guaranteed lowercase
		c_num -= 26
	return chr(c_num)



rooms = [] # array of tuples
with open('input.txt') as f_in:
	for line in f_in:
		r = re.search(r'([a-z\-]*)(\d*)\[([a-z]*)\]', line)
		if r == None: # debug only
			line = line.strip()
			print(line)
		
		letter_count = {}
		e_name = r.group(1)
		sector_id = int(r.group(2))
		checksum = r.group(3)

		for c in e_name:
			if c == '-':
				continue
			if c not in letter_count:
				letter_count[c] = 0
			letter_count[c] += 1

		# (sort by frequency, then alphabetically)
		# ** (tuple sorting trick not necessary bc python sort is stable)
		letters = letter_count.keys()
		letters = sorted(letters, key=lambda x: (-letter_count[x], x))

		if checksum == ''.join(letters[:5]):
			# part 2: translate e_name
			converted_name = ''
			for c in e_name:
				converted_name += shift_cipher(c, sector_id)
			#print(e_name,converted_name)
			rooms.append((converted_name, sector_id))
			if re.search('north|pole',converted_name):
				print(converted_name, 'with room id', sector_id)

# do something with rooms[] if you want
#for line in rooms:
#	print(line)
