#!/usr/bin/env python3.5
# (written in Python IDLE this time)


# md5 hash the door id (id is given, 8-char password = ?)
# integer index (starting with 0)
# (required to hash at least 8 times)

# hash "id"+"integer" for each integer index value (0 ascending)
# if hexadecimal of hash starts with 5 0's => 6th char of hash

# NOTE: could import hashlib; call: hashlib.md5('string'.encode()).hexdigest()
# or write your own?? http://www.iusmentis.com/technology/hashfunctions/md5/

import hashlib, time


def main():
    start = time.time()
    n_successes = 0
    index = 0
    #door_id = 'abc' # debug
    door_id = 'ojvtpuvg'
    password = ''

    # md5 hashing (each successful hash produces one char of password)
    while n_successes < 8:
        to_hash = door_id + str(index)
        # ** (md5 hash a byte representation of to_hash, and convert to hex)
        hash_hex = str(hashlib.md5(to_hash.encode()).hexdigest())
        if hash_hex[:5] == '00000':
            password += hash_hex[5] # 6th char
            print(to_hash + ' -> ' + password)
            n_successes += 1
        index += 1
        
    end = time.time()
    print('Time taken (seconds): {:.2f}'.format(end-start))



if __name__ == '__main__':
    main()


# links of interest:
# http://security.stackexchange.com/questions/33531/why-improvising-your-own-hash-function-out-of-existing-hash-functions-is-so-bad
