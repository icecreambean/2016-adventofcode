#!/usr/bin/env python3.5
# (a more standard bfs)

#FAV_NUM = 10 # test input
#GOAL_ORDS = (7,4) # test output

# fortunately this doesn't interfere with part 2
FAV_NUM = 1364
GOAL_ORDS = (31,39)

X_IND = 0
Y_IND = 1

PART_2 = True

def main():
    # queue
    ords_q = [(1,1)]
    moves_q = [0]
    # visited ords (prevent going backwards / loops)
    ords_visited = [(1,1)]
    # bfs
    found = False
    n_moves = 0
    while len(ords_q) > 0 and found == False:
        # pop off queue
        cur_ords = ords_q.pop(0)
        next_moves = moves_q.pop(0) + 1 # assumes start ords not goal
        # part 2
        if PART_2:
            if next_moves > 50:
                continue
        # get neighbours (left up right down)
        ords_incs = [(-1,0),(0,-1),(1,0),(0,1)]
        for do in ords_incs:
            next_ords = (cur_ords[X_IND]+do[X_IND], \
                            cur_ords[Y_IND]+do[Y_IND])
            # ignore if out of bounds
            if is_out_of_bounds(next_ords):
                continue
            # ignore if wall
            if is_wall(next_ords):
                continue
            # check if goal ords
            if next_ords == GOAL_ORDS:
                found = True
                n_moves = next_moves
                break
            # check if already visited
            if next_ords in ords_visited:
                continue
            # add to queue, visited list
            ords_q.append(next_ords)
            moves_q.append(next_moves)
            ords_visited.append(next_ords)
    # result
    if found and not PART_2:
        print("No. moves:", n_moves)
    if PART_2:
        #print_map(15,15,ords_visited)
        #print(ords_visited)
        print("No. distinct locations:", len(ords_visited))


# n_cols, n_rows, is better
def print_map(x_max, y_max, visited_list = []):
    for y in range(y_max):
        for x in range(x_max):
            if is_wall((x,y)):
                print("#",end='')
            elif (x,y) in visited_list:
                print('o',end='')
            else:
                print('.',end='')
        print('') # newline

def is_out_of_bounds(ords):
    x = ords[X_IND]; y = ords[Y_IND]
    if x < 0 or y < 0:
        return True
    return False

def is_wall(ords):
    x = ords[X_IND]; y = ords[Y_IND]
    res = x*x + 3*x + 2*x*y + y + y*y + FAV_NUM
    res_bin = str(bin(res))
    return res_bin[2:].count('1') % 2

if __name__ == '__main__':
    main()
