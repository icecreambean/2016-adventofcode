#!/usr/bin/env python3.5

#start_row = '..^^.'
#n_rows = 3

#start_row = '.^^.^.^^^^'
#n_rows = 10

part1 = False
start_row = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'
if part1:
    n_rows = 40
else:
    n_rows = 400000

future_trap_condit = [ [True, True, False],
                       [False, True, True],
                       [True, False, False],
                       [False, False, True] ]

def main():
    trap_map = [list(start_row)]
    c = count_tile_type(trap_map, '.') # and keep counting in the loop
    for row_i in range(1, n_rows):
        # generate next row
        next_row = []
        for col_i in range(len(start_row)):
            # get neighbours (prior row)
            d_col = [-1,0,1]
            trap_status = [] # of the row above
            for d in d_col:
                status = is_trap(trap_map, row_i -1, col_i +d)
                trap_status.append(status)
            # determine status of next tile
            if trap_status in future_trap_condit:
                next_row.append('^')
            else:
                next_row.append('.')
                c += 1
        trap_map.append(next_row)
    #print_map(trap_map)
    #print("part 1:", count_tile_type(trap_map,'.'))
    print("no. safe:", c)

# checks if the given tile is a trap
# DOESN'T PREDICT if future tiles are traps or not
def is_trap(trap_map, row_i, col_i):
    # note: row = y, col = x
    # row col must be valid
    if not (0 <= col_i < len(trap_map[0])):
        return False
    if trap_map[row_i][col_i] == '^':
        return True
    return False

def print_map(trap_map):
    for l in trap_map:
        print(''.join(l))

def count_tile_type(trap_map, tile_type):
    c = 0
    for l in trap_map:
        for i in l:
            if i == tile_type:
                c += 1
    return c


if __name__ == '__main__':
    main()
