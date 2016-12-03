#!/usr/bin/env python3.5

n_valid = 0
finished = False
# read 3 rows at a time
with open('input.txt') as in_file:
    while True:
        # grab three lines at a time
        three_lines = [] # array of arrays
        for i in range(3):
            line = in_file.readline()
            if line == '':
                finished = True
                break
            line = line.split()
            line = list(map(int, line))
            three_lines.append(line)
        if finished == True:
            break
        # transpose the matrix
        three_lines = list(zip(*three_lines))
        # apply the formula
        for i in range(3):
            three_lines[i] = list(three_lines[i])
            three_lines[i].sort()
            if three_lines[i][0] + three_lines[i][1] > three_lines[i][2]:
                n_valid += 1




print(n_valid)


# http://stackoverflow.com/questions/4306574/python-method-function-arguments-starting-with-asterisk-and-dual-asterisk
