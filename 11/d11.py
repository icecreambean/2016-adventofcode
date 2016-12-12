#!/usr/bin/env python3.5

# brute force method: move combinations of things to adjacent floors (bfs)
# could add a heuristic:
#    1/2 the no. of remaining items (round up) to move to the 4th level
#    * max distances moving these item (pairs) to the 4th floor
#    (should always be an underestimate, but how to prove?)

import re, copy, sys
# heapq for priority queues

# array(floor id (floor level -1)) of arrays(string id of items)
INPUT = 'input_test.txt'

# TODO: BFS is WAY TOO slow (too many combinations)
# implement A* search using the above heuristic
# other interesting optimisations to read up on here:
#https://www.reddit.com/r/adventofcode/comments/5hoia9/2016_day_11_solutions/
#https://www.reddit.com/r/adventofcode/comments/5htco3/help_day_11_trying_to_figure_out_exponential/
# essentially: grasping the tricks of the logic problem will lead
# to smarter ways of doing things. (especially pruning)

def main():
    floors = read_file(INPUT)
    # bfs: set up 'queues' for the 'state'
    elevator_q = [0] # starts on the 1st floor
    floors_q = [floors] # queue of floors(2d array)
    floors_visited = [(0,floors)]
    # constants for floors_visited
    FLOORS_VISITED_ELEVATOR = 0
    FLOORS_VISITED_FLOORS = 1

    moves_q = [0] # moves made
    while len(elevator_q) > 0:              # BFS
        cur_elevator = elevator_q.pop(0)
        cur_floors = floors_q.pop(0)
        cur_moves = moves_q.pop(0)
        ######################
        print_debug(cur_moves, cur_elevator, cur_floors)
        # debug stuff
        debug = False
        a = [['lithium microchip'], [], ['lithium generator', 'hydrogen generator', 'hydrogen microchip'], []]
        #a.sort()
        #if cur_floors == a:
        #    debug = True
        ######################
        # possible neighbour actions
        level_inc = [-1,1]
        if cur_elevator <= 0: # correct level_inc, depending on index
            level_inc.remove(-1)
        if cur_elevator >= len(cur_floors) -1:
            level_inc.remove(1)
        # get neighbours (tuples of len 1 and 2)
        neighbours = make_pairs(cur_floors[cur_elevator])
        for item in cur_floors[cur_elevator]:
            neighbours.append( (item,) ) # one ele tuple
        # ugly?
        found = False
        for n_group in neighbours:
            for inc in level_inc:
                # update the floors state
                next_elevator = cur_elevator + inc
                next_floors = copy.deepcopy(cur_floors)
                next_moves = cur_moves + 1
                #print("n group:", n_group)
                for n in n_group:
                    #print_floors(next_floors)
                    #print("n: '{}'".format(n))
                    next_floors[cur_elevator].remove(n)
                    next_floors[next_elevator].append(n)
                # sort elements on each floor level for equality chk
                next_floors = sort_floors(next_floors)
                # check not a state we have already visited
                if in_floors_visited(floors_visited, next_moves, next_floors):
                    if debug:
                        print("**** Neighbour ALREADY VISITED; valid:", valid)
                        print_debug(next_moves, next_elevator, next_floors)
                        print("**************************")
                    continue
                # check valid
                valid = True
                for f in next_floors:
                    f_valid = check_valid(f)
                    if not f_valid:
                        valid = False
                        break
                # intermediate debug stuff
                if debug:
                    print("**** Neighbour valid:", valid)
                    print_debug(next_moves, next_elevator, next_floors)
                    print("**************************")
                if not valid:
                    continue
                # check if goal state
                if check_goal(next_floors):
                    found = True
                    print_floors(next_floors)
                    print("No. moves:", next_moves)
                    break
                # otherwise add to queue (3 queues), visited
                elevator_q.append(next_elevator)
                floors_q.append(next_floors)
                moves_q.append(next_moves)
                floors_visited.append((next_elevator, next_floors))
            if found == True:
                break
        if found == True:
            break
        if debug:
            break

    # end of main

# IMPORTANT FOR EQUALITY TESTS!!!
def sort_floors(all_floors):
    for i in all_floors:
        i.sort()
    return all_floors

def in_floors_visited(floors_visited, next_moves, next_floors):
    for t in floors_visited:
        if (next_moves,next_floors) == t:
            return True
    return False

def print_debug(moves, elevator, all_floors):
    print("M:", moves, "   E:", elevator)
    print_floors(all_floors)
    print("--- array:", all_floors)

def print_floors(all_floors):
    i = len(all_floors) -1
    while i >= 0:
        print(all_floors[i])
        i -= 1

def check_goal(all_floors):
    for i in range(len(all_floors) -1):
        # number of items on that floor
        if len(all_floors[i]) > 0:
            return False
    if len(all_floors[-1]) > 0:
        return True
    return False

# checks if layout of a floor fries a chip or not
# UPDATE: "Generators will only protect their element's microchip."
def check_valid(floor_level):
    # get chips and generators
    floor_items = copy.deepcopy(floor_level) # overkill
    chips = []
    gens = []
    for i in floor_items:
        i = i.split()
        if i[1] == 'microchip':
            chips.append(i[0])
        else:
            gens.append(i[0])
    if len(gens) > 0:
        for c in chips: # unpaired chips on the same floor get fried
            if c not in gens:
                return False
    return True

# pairs of elements in a list
def make_pairs(l):
    pairs = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            pairs.append( (l[i], l[j]) )
    return pairs

def read_file(in_f_name):
    floors = []
    with open(in_f_name) as in_f:
        # each line lists the floors in order from 1 .. n
        for line in in_f:
            microchip_list = re.findall(r'[a-z\-]+ microchip', line)
            for i,m in enumerate(microchip_list):
                microchip_list[i] = re.sub('-compatible', '', m)
            generator_list = re.findall(r'[a-z\-]+ generator', line)
            # side effect
            floors.append(microchip_list + generator_list)
    floors = sort_floors(floors)
    return floors

if __name__ == "__main__":
    main()

# move everything to the 4th floor (unshielded) for assembly

# microchip powered by corresponding RTG,
# chip fried if not powered by correct RTG, in same area as another RTG

# elevator: powered by at least one component,
# can move at most 2 components at a time
# always stops on each floor (can causes items to irradiate one another)
#    (ie. can't "skip" floors)


# game state search algorithms: bfs, dfs, A*
# https://en.wikipedia.org/wiki/Zobrist_hashing
