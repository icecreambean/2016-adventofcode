#!/usr/bin/env python3.5

import re

hypernet_pattern = re.compile(r'\[.*?\]')
# use of negative lookahead to implement 'and not'
abba_pattern = re.compile(r'([a-z])(?!\1)([a-z])\2\1')
# test:
#re.findall(r'(([a-z])(?!\2)([a-z])\3\2)','abbaccccdeed')

counter = 0
with open('input.txt') as in_f:
    for line in in_f:
        line = line.strip()
        # note: there can be multiple hypernets
        hypernet_list = hypernet_pattern.findall(line)
        remains_list = hypernet_pattern.split(line)

        # ignore if abba in hypernet
        to_ignore = False
        for hn in hypernet_list:
            if abba_pattern.search(hn):
                to_ignore = True
                break
        if to_ignore:
            continue
        # ignore if NO abba in remaining line
        for r in remains_list:
            if abba_pattern.search(r):
                # not ignored
                counter += 1
                break
        # ignored ('continue', but end of loop)
print(counter)
