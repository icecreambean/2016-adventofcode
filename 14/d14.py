#!/usr/bin/env python3.5

# 64 new keys for a one-time pad
# salt -> md5() + integer index (in hex)

# key if:
#   contains 3 of same char in a row
#   1 in 1000 next hashes contains same char 5 times in a row

# 1. integer = ? s.t. salt (input) hashes out a a triple
#       hash 1000 times (array), then process the first hash
#       for each result in your array identify all 3's and 5's
#       to avoid running regex multiple times
# 2. repeat 1. until 64 hashes generated

# why part 1 took so long:
#    regex patterns misinterpreted wrongly
#    triples = triples_pattern.findall(string); only needed .search()
# part 2:
#    not sure how caching helps? chance of md5 collision = ...?

import re, hashlib, sys

#salt = 'abc' # test input
salt = 'qzyelonm'
PART_2 = True

# r'(?=((.)\2{2}))' is better but completely unnecessary
#    store res as a single char
#triples_pattern = re.compile(r'(.)(?<=^.|(?<!\1).)\1{2}(?!\1)')
#fifths_pattern = re.compile(r'(.)(?<=^.|(?<!\1).)\1{4}(?!\1)')
triples_pattern = re.compile(r'(.)\1{2}') # above is wrong
fifths_pattern = re.compile(r'(.)\1{4}')

# hash_entries constants
STRING = 0      # hash_entires is an array of tuples
TRIPLES = 1     # stored as a single char
FIFTHS = 2

hash_cache = {} # only needed for part 2

def main():
    keys = [] # needs 64 elements
    index = 0 # for hash_entries[]
    hash_entries = [] # could be optimised as a linked list of 10001 ele

    # fill in the first 1000 entries (first cmp val, 999 others)
    for i in range(1000):
        index, hash_entries = add_hash_entry(salt, index, hash_entries)
    while len(keys) < 64:
        index, hash_entries = add_hash_entry(salt, index, hash_entries)
        cur_hash_index = index - 1001
        found = False
        found_index = 0
        found_char = ''
        for char_triple in hash_entries[cur_hash_index][TRIPLES]:
            for i,next_entry in enumerate(hash_entries[cur_hash_index+1 :]):
                if char_triple in next_entry[FIFTHS]:
                    found = True
                    found_index = i + cur_hash_index +1 # debug
                    found_char = char_triple # debug
                    break
            if found == True:
                break
        if found:
            print('key at index:', cur_hash_index, '& repeat at:', found_index, 'with char:', char_triple)
            print('   cur:', hash_entries[cur_hash_index][STRING])
            print('   rep:', hash_entries[found_index][STRING])
            keys.append(hash_entries[cur_hash_index][STRING])
            # otherwise: index will increment next turn, compare new hash
        # part 1:
        if len(keys) == 64:
            print('64th key at index:', cur_hash_index)


def print_keys(keys):
    for h in keys:
        print(h)

# string, integer, list of tuples
def add_hash_entry(salt,index, hash_entries):
    if PART_2:
        string = hash_part_2(salt,index)
    else:
        string = hash(salt,index)
    #triples = set([ i.group(0) for i in triples_pattern.finditer(string)])
    #fifths = set([ i.group(0) for i in fifths_pattern.finditer(string) ])
    # NOTE: Only consider the first such triplet in a hash (oops...)
    triples = triples_pattern.findall(string)
    if len(triples) > 0:
        triples = [triples[0]]
    fifths = list(set(fifths_pattern.findall(string)))
    hash_entries.append((string,triples,fifths))
    index += 1
    return index, hash_entries

def hash_part_2(salt,index):
    hash_line = salt + str(index)
    for i in range(2017):
        if hash_line in hash_cache:
            hash_line = hash_cache[hash_line]
        else:
            res = hashlib.md5((hash_line).encode()).hexdigest()
            hash_cache[hash_line] = res
            hash_line = res

    return hash_line

def hash(salt, index):
    return hashlib.md5( (salt + str(index) ).encode() ).hexdigest()

if __name__ == '__main__':
    main()
