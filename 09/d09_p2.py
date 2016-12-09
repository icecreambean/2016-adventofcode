#!/usr/bin/env python3.5
import re, time

# note: '(5x5)(5x5)A' is infinite...
# require only the length of what is being decrypted, not the decrypted file

pattern = re.compile(r'\((\d+)x(\d+)\)')

# the input is small enough that caching sub-results are not required?
#    question: how would you cache it anyway? (since we are not decrypting
#              the file as we go...)

def main():
    # note: better to buffer it all in first...
    with open('input.txt') as in_f:
        #in_contents = in_f.read().strip();
        for in_contents in in_f:
            in_contents = in_contents.strip()
            start = time.time()

            d_length = process_line_length(in_contents)
            #print(in_contents)
            print('  length:', d_length)
            end = time.time()
            print('Time taken: {:.2f}'.format(end-start))


# note: only works because we assume the bracket formatters operate on
#       separable, partitioned substrings
# hence: e.g. won't work on '(5x5)(5x5)A' or on '(6x6)(6x6)AB'
def process_line_length(in_contents):
    # base case
    if '(' not in in_contents:
        return len(in_contents) # numeric result

    m = pattern.search(in_contents)
    length = int(m.group(1))
    n_repeat = int(m.group(2))
    after_sequence = in_contents[m.end() : m.end() + length]

    # require the following lengths:
    #   length up to regex match: m.start()
    #   length of the after sequence: compute via recursion
    #   length of what is after that sequence: via recursion

    l1 = m.start() # numeric result
    l2 = process_line_length(after_sequence) * n_repeat
    #total = l1 + l2 + process_line_length(in_contents[m.end() + length :])
    #print(in_contents, total)
    #return total
    return l1 + l2 + process_line_length(in_contents[m.end() + length :])

if __name__ == '__main__':
    main()
