#!/usr/bin/env python3.5

import re

sum_id = 0
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
			sum_id += sector_id

print(sum_id)
