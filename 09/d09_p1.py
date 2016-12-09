#!/usr/bin/env python3.5
# (can't be bothered doing it in perl, debugging is a nightmare,
#  and so are the random variables for the index of a regex match)
#
# could probably also do the entire logic in one line of regex???
# no? python typing won't allow for it in regex

import re
pattern = re.compile(r'\((\d+)x(\d+)\)')

with open('input.txt') as in_f:
    #in_contents = in_f.read().strip();
    for in_contents in in_f:
        # note that some test files are multi-line
        in_contents = in_contents.strip()
        i = 0
        res = ''
        # NOTE: ignore markers if they are consumed as part of data
        # do while loop
        m = pattern.search(in_contents)
        while m:
            length = int(m.group(1))
            n_repeat = int(m.group(2))
            after_sequence = in_contents[m.end() : m.end() + length]
            # splice to remove the matched bracket formatter
            in_contents = in_contents[:m.start()] + \
                          after_sequence * (n_repeat -1) + \
                          in_contents[m.end():]
            # compute new substring of in_contents to regex over
            i = m.start() + length * n_repeat
            # find next match in remaining in_contents string
            res += in_contents[:i]
            in_contents = in_contents[i:]
            m = pattern.search(in_contents)

        # add whatever is remaining to res
        res += in_contents

        print(res)
        print('  length:', len(res))
