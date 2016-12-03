#!/usr/bin/env python3.5

# test data
#instructions = ['ULL','RRDDD','LURDL','UUUUD']

# keypad[y][x]
keypad = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# increments, also in (y,x) format
# ** first index => direction you moved in
# ** (be careful! (0,0) starts at top left!)
inc = { 'U':[-1,0], 'L':[0,-1], 'D':[1,0], 'R':[0,1] }
Y_KEY = 0; X_KEY = 1

def main():
    password = ''
    # start at keypad number: 5
    y = 1; x = 1
    instructions = open('input.txt')
    for line in instructions:
        line = line.strip()
        for c in line:
            y,x = move(y,x,c)
        password += str(keypad[y][x])
    instructions.close()
    print(password)

# y,x are numeric, dir is a char
def move(y,x, dir):
    new_y = y + inc[dir][Y_KEY]
    if new_y < 0 or new_y >= len(keypad):
        new_y = y
    new_x = x + inc[dir][X_KEY]
    if new_x < 0 or new_x >= len(keypad[0]):
        new_x = x
    return (new_y,new_x)


if __name__ == '__main__':
    main()
