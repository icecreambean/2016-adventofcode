#!/usr/bin/env python3.5

import re

hypernet_pattern = re.compile(r'\[.*?\]')
# use of negative lookahead to implement 'and not'
# use of positive lookahead to implement OVERLAPPING
# ** (not sure if this should have been required for part 1
# **  as well?)
# ** also: could use finditer, then ele.group(int)
ssl_pattern = re.compile(r'(?=(([a-z])(?!\2)([a-z])\2))')


counter = 0
with open('input.txt') as in_f:
    for line in in_f:
        line = line.strip()
        # note: there can be multiple hypernets
        hypernet_list = hypernet_pattern.findall(line)
        remains_list = hypernet_pattern.split(line)

        # grab ssl-support criteria
        h_matches = []
        r_matches = []
        for hn in hypernet_list:
            h_iters = ssl_pattern.finditer(hn)
            for i in h_iters:
                h_matches.append(i.group(1))
        for r in remains_list:
            r_iters = ssl_pattern.finditer(r)
            for i in r_iters:
                r_matches.append(i.group(1))
        # check if ssl supported
        for m in h_matches:
            required = m[1] + m[0] + m[1]
            if required in r_matches:
                #print(line)
                counter += 1
                break

print('SSL supported by:',counter)


# overlapping regexes:
#http://stackoverflow.com/questions/5616822/python-regex-find-all-overlapping-matches
