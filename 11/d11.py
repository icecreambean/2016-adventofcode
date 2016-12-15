#!/usr/bin/env python3.5
# as of 23:19, 14/12/16:
#   incomplete: code is too slow; might need major restructuring.
#   logic seems correct though (too many mallocs, etc.?)

# brute force method: move combinations of things to adjacent floors (bfs)
# could add a heuristic:
#    1/2 the no. of remaining items (round up) to move to the 4th level
#    * max distances moving these item (pairs) to the 4th floor
#    (should always be an underestimate, but how to prove?)

# RESULTS:
# part 1:
#    No. moves: 47 - correct
#    time taken: 367.99784111976624
#    (probably due to all the mallocs?)

import re, copy, sys, heapq, math, time
# heapq for priority queues

# array(floor id (floor level -1)) of arrays(string id of items)
INPUT = 'input_p2.txt'

# optimisations to consider
#   don't go down if no other items are below you - done
#   look for equivalent states, not just identical states - done
#   A* cost function - done

# needs further pruning??
# https://andars.github.io/aoc_day11.html ~  to compare ideas
#    my performance is probably slow as due to infinite mallocs

UNIT_TEST = False
def main():
    # place test code here (for unit testing)
    if UNIT_TEST:
        test_equivalent_states() # correct
        return

    start = time.time()

    floors = read_file(INPUT)
    # bfs: set up 'PRIORITY queues' for the 'state'
    # heapq: each element is a tuple, 1st element is compare val
    # (= f-cost)
    initial_fcost = calc_h_cost(floors) # note moves = 0
    initial_elevator = 0
    # ** initial_floors = floors
    initial_moves = 0
    q = [ (initial_fcost, initial_elevator, \
            floors, initial_moves) ]
    #Q_FCOST = 0; Q_ELEVATOR = 1; Q_FLOORS = 2; Q_MOVES = 3
    #elevator_q = [0] # starts on the 1st floor
    #floors_q = [floors] # queue of floors(2d array)
    #moves_q = [0] # moves made
    floors_visited = [(0,floors)] # (also chk equivalent states)
    # constants for floors_visited
    FLOORS_VISITED_ELEVATOR = 0
    FLOORS_VISITED_FLOORS = 1

    while len(q) > 0:
        # note cur_fcost is useless
        cur_fcost, cur_elevator, cur_floors, cur_moves = \
            heapq.heappop(q)
        #cur_elevator = elevator_q.pop(0)
        #cur_floors = floors_q.pop(0)
        #cur_moves = moves_q.pop(0)
        ######################
        #print_debug(cur_moves, cur_elevator, cur_floors)
        # debug stuff
        debug = False
        ######################
        # possible neighbour actions
        level_inc = [-1,1]
        if cur_elevator >= len(cur_floors) -1:
            level_inc.remove(1)
        if cur_elevator <= 0:
            level_inc.remove(-1)
        elif not are_items_below(cur_floors, cur_elevator):
            # note: optimisation
            level_inc.remove(-1)
        # get neighbours (tuples of len 1 and 2)
        neighbours = make_pairs(cur_floors[cur_elevator])
        for item in cur_floors[cur_elevator]:
            neighbours.append( (item,) ) # one ele tuple
        # ugly?
        found = False
        for n_group in neighbours:
            for inc in level_inc:
                # optimisation: (2 up, 1 down)
                if inc == 1: # up
                    if len(n_group) == 1 and \
                            len(cur_floors[cur_elevator]) % 2 == 1:
                        continue
                else: # down
                    if len(n_group) == 2:
                        continue
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
                #next_floors = sort_floors(next_floors)
                # check not a state we have already visited
                if is_equivalent_state(floors_visited, \
                        next_elevator, next_floors):
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
                next_fcost = calc_h_cost(next_floors) + next_moves
                heapq.heappush(q, (next_fcost, next_elevator, \
                                   next_floors, next_moves) )
                #elevator_q.append(next_elevator)
                #floors_q.append(next_floors)
                #moves_q.append(next_moves)
                floors_visited.append((next_elevator, next_floors))
            if found == True:
                break
        if found == True:
            break
        if debug:
            break
    print('time taken:', time.time() - start)
    # end of main

# reddit alternative: take the average distance from the top floor.
# is this a good option? :o

# why is my code so long??

# heuristic cost: REMEMBER to add in g-cost to get total f-cost
def calc_h_cost(all_floors):
    all_dist = []
    for index, item_list in enumerate(all_floors):
        distance = len(all_floors) - index -1
        all_dist += [distance] * len(item_list)
    all_dist.sort(reverse=True)
    return sum(all_dist[: math.ceil( len(all_dist)/2 ) ])

# used to be important for equality checking
# most likely don't require this anymore
def sort_floors(all_floors):
    for i in all_floors:
        i.sort()
    return all_floors

def are_items_below(all_floors, elevator):
    for i in range(elevator):
        if len(all_floors[i]) > 0:
            return True
    return False

def test_equivalent_states():       # it is correct
    #FLOORS_VISITED_ELEVATOR = 0
    #FLOORS_VISITED_FLOORS = 1
    # (test using a custom floors_visited[])
    f1 = read_file('ut1_1.txt')
    f2 = read_file('ut1_2.txt')
    f2_elevator = 1
    floors_visited = [(0,f1)]
    if not is_equivalent_state(floors_visited, f2_elevator, f2):
        print("Test 1 correct.")
    else:
        print("Test 1 NOT CORRECT <-----")
    floors_visited = [(1,f1)]
    if is_equivalent_state(floors_visited, f2_elevator, f2):
        print("Test 2 correct.")
    else:
        print("Test 2 NOT CORRECT <-----")


def is_equivalent_state(floors_visited, next_elevator, \
                            next_floors):
    next_positions = get_positions(next_floors)
    for elevator_state, floor_state in floors_visited:
        if elevator_state != next_elevator:
            continue
        state_positions = get_positions(floor_state)
        # state_positions[material] = {chip, gen}
        # iterate through next pos, if the two lists match, remove and continue TODO TODO TODO TODO
        next_positions_copy = copy.deepcopy(next_positions)
        for state_material in list(state_positions.keys()):
            for next_material in list(next_positions_copy.keys()):
                # comparing equality of arrays, ignoring
                # name of the material
                if state_positions[state_material] == \
                        next_positions_copy[next_material]:
                    del state_positions[state_material]
                    del next_positions_copy[next_material]
                    break
        if not state_positions and not next_positions_copy:
            # equivalent state
            return True
    # no equivalent state found
    return False



def get_positions(all_floors):
    positions = {}
    for level_no, level in enumerate(all_floors):
        for item in level:
            item = item.split()
            material = item[0]
            machine_type = item[1]
            if material not in positions:
                positions[material] = {'microchip':[],'generator':[]}
            positions[material][machine_type].append(level_no)
    for k in positions: # note: keys not in sorted order
        for kk in positions[k]: # chip / gen
            positions[k][kk].sort()
    return positions


# decrepated - not 'GOOD' enough; see is_equivalent_state()
def in_floors_visited(floors_visited, next_elevator, next_floors):
    for t in floors_visited:
        if (next_elevator,next_floors) == t:
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
    #floors = sort_floors(floors)
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

###############################################################

# game state search algorithms: bfs, dfs, A*
# https://en.wikipedia.org/wiki/Zobrist_hashing


# links to learn off:
#https://www.reddit.com/r/adventofcode/comments/5hoia9/2016_day_11_solutions/
#https://www.reddit.com/r/adventofcode/comments/5htco3/help_day_11_trying_to_figure_out_exponential/
# essentially: grasping the tricks of the logic problem will lead
# to smarter ways of doing things. (especially pruning)
