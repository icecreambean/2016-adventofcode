#!/usr/bin/env python3.5
# (written in Python IDLE this time)

import hashlib, time

def main():
    start = time.time()
    n_successes = 0
    index = 0
    #door_id = 'abc' # debug
    door_id = 'ojvtpuvg'
    password = list('#' * 8) # placeholder

    # md5 hashing (each successful hash produces one char of password)
    while n_successes < len(password):
        to_hash = door_id + str(index)
        # ** (md5 hash a byte representation of to_hash, and convert to hex)
        hash_hex = str(hashlib.md5(to_hash.encode()).hexdigest())
        if hash_hex[:5] == '00000':
            # part 2
            pos = int(hash_hex[5],16)
            val = hash_hex[6]
            if 0 <= pos < len(password) and password[pos] == '#':
                password[pos] = val
                print(to_hash + ' -> ' + ''.join(password))
                n_successes += 1
        index += 1
        
    end = time.time()
    print('Time taken (seconds): {:.2f}'.format(end-start))

# cinematic encryption: gui + change and re-render a label, or
# some kind of console hacks (backspace ascii character?)

if __name__ == '__main__':
    main()

