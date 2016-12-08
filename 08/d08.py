#!/usr/bin/env python3.5

TEST_FILE = 'input.txt'
# y,x (row,col) format
if TEST_FILE == 'input_test.txt': # part 1 example test
    Y_MAX = 3
    X_MAX = 7
else:
    Y_MAX = 6 # the actual question
    X_MAX = 50
PIXEL_OFF = '.'
PIXEL_ON = '#'
screen = [[PIXEL_OFF for i in range(X_MAX)] for j in range(Y_MAX)]

def main():
    with open(TEST_FILE) as in_f:
        for line in in_f:
            line = line.strip().split()
            # new rect (X by Y format)
            if line[0] == 'rect':
                rx, ry = line[1].split('x')
                screen_add_rect(int(ry),int(rx))
                continue
            # rotate row / col
            if line[1] == 'row':
                # row (y)
                y_ind = int(line[2].split('=')[1])
                rot_amount = int(line[4])
                screen_rotate_row(y_ind, rot_amount)
                continue
            # col (x)
            x_ind = int(line[2].split('=')[1])
            rot_amount = int(line[4])
            screen_rotate_col(x_ind, rot_amount)

    print_screen()
    print(count_pixels())

############## 'ADT' for the 'screen' ##############
def screen_add_rect(ry,rx):
    for y in range(len(screen)):
        if y >= ry: # control no. rows to write to
            break
        for x in range(len(screen[y])):
            if x >= rx: # control no. cols to write to
                break
            screen[y][x] = PIXEL_ON

def screen_rotate_row(y_ind, rot_amount):
    # rotate (RIGHT) by slicing
    rot_amount %= len(screen[0]) # note len -> row length
    row = screen[y_ind] # for readability purposes
    screen[y_ind] = row[-rot_amount:] + row[:len(row)-rot_amount]

def screen_rotate_col(x_ind, rot_amount):
    # rotate (DOWN) by slicing, but have to read-write ele by ele
    # (alt: transpose the grid, call the row function)
    rot_amount %= len(screen) # col length based off range(y)
    # ** grab the slice
    col = [screen[y][x_ind] for y in range(len(screen))]
    col = col[-rot_amount:] + col[:len(col)-rot_amount]
    for y in range(len(screen)): # same as length(col)
        screen[y][x_ind] = col[y]

def print_screen():
    for l in screen:
        print(''.join(l))

def count_pixels():
    count = 0
    for y_row in screen:
        for pixel in y_row:
            if pixel == PIXEL_ON:
                count += 1
    return count
####################################################

if __name__ == '__main__':
    main()
