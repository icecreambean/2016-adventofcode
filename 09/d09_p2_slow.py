#!/usr/bin/env python3.5
import re, time

# '(5x5)(5x5)A' is infinite...
# require only the length of what is being decrypted, not the decrypted file

# note part 2: could also be done by reusing part 1 code multiple times

pattern = re.compile(r'\((\d+)x(\d+)\)')
with open('input_test_p2.txt') as in_f:
    #in_contents = in_f.read().strip();
    for in_contents in in_f:
        start = time.time()

        in_contents = in_contents.strip()
        loop_count = 0
        m = pattern.search(in_contents)
        while m:
            length = int(m.group(1))
            n_repeat = int(m.group(2))
            after_sequence = in_contents[m.end() : m.end() + length]
            # splice to remove the matched bracket formatter
            in_contents = in_contents[:m.start()] + \
                          after_sequence * (n_repeat -1) + \
                          in_contents[m.end():]
            m = pattern.search(in_contents)
            loop_count += 1
            #print(loop_count) # debug purposes only
        #print(in_contents)
        print('  length:', len(in_contents))

        end = time.time()
        #print('Time taken: {:.2f}'.format(end-start))
