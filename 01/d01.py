#!/usr/bin/env python3.5
# read up on: taxicab geometry problem

# test data
#path = 'R2, L3'
#path = 'R2, R2, R2'
#path = 'R5, L5, R5, R3'
#path = 'R8, R4, R4, R8'

path = 'R3, L5, R2, L2, R1, L3, R1, R3, L4, R3, L1, L1, R1, L3, R2, L3, L2, R1, R1, L1, R4, L1, L4, R3, L2, L2, R1, L1, R5, R4, R2, L5, L2, R5, R5, L2, R3, R1, R1, L3, R1, L4, L4, L190, L5, L2, R4, L5, R4, R5, L4, R1, R2, L5, R50, L2, R1, R73, R1, L2, R191, R2, L4, R1, L5, L5, R5, L3, L5, L4, R4, R5, L4, R4, R4, R5, L2, L5, R3, L4, L4, L5, R2, R2, R2, R4, L3, R4, R5, L3, R5, L2, R3, L1, R2, R2, L3, L1, R5, L3, L5, R2, R4, R1, L1, L5, R3, R2, L3, L4, L5, L1, R3, L5, L2, R2, L3, L4, L1, R1, R4, R2, R2, R4, R2, R2, L3, L3, L4, R4, L4, L4, R1, L4, L4, R1, L2, R5, R2, R3, R3, L2, L5, R3, L3, R5, L2, R3, R2, L4, L3, L1, R2, L2, L3, L5, R3, L1, L3, L4, L3'

# directions (could enum this)
NORTH = 0; EAST = 1; SOUTH = 2; WEST = 3

all_visited_ords = []	# quick hack
def main():
	# variables (center from (0,0))
	cur_dir = NORTH
	cur_x = 0
	cur_y = 0
	all_visited_ords.append((cur_x, cur_y))

	path_list = path.split(', ')
	for i in path_list:
		turn_dir = i[0] # either L or R
		length = int(i[1:]) # numeric (can be more than one digit)
		cur_dir = updateDir(cur_dir, turn_dir)
		cur_x, cur_y = updateOrds(cur_x, cur_y, cur_dir, length)




		# part 2:
		#print("#### PART 2 ANSWER: ####")
		#print('ords from origin are: {},{}'.format(cur_x, cur_y))
		#print('blocks away: ' + str(abs(cur_x) + abs(cur_y)))
	
	# part 1:
	print("\n#### PART 1 ANSWER: ####")
	print('ords from origin are: {},{}'.format(cur_x, cur_y))
	print('blocks away: ' + str(abs(cur_x) + abs(cur_y)))


# turn_dir: string('L' or 'R')
def updateDir(cur_dir, turn_dir):
	# could use a dictionary
	# (north, east, south, west)
	left = [WEST, NORTH, EAST, SOUTH]
	right = [EAST, SOUTH, WEST, NORTH]

	if turn_dir == 'L':
		return left[cur_dir]
	return right[cur_dir]


def updateOrds(cur_x, cur_y, cur_dir, length):
	# (north, east, south, west): (x,y)
	inc = [[0, length], 
			 [length, 0],
			 [0, -length],
			 [-length, 0]]
	
	x_inc, y_inc = inc[cur_dir]
	return (cur_x + x_inc, cur_y + y_inc)



# direction (from c to p via length) and...
# cur ords, prev ords = line 1; 2 other sets of ords = line 2
#		line1: c,p     line2: 1,2
def checkIntersection(cur_dir, c_x, c_y, p_x, p_y, x1, y1, x2, y2):
	HORIZONTAL = 0
	VERTICAL = 1
	line1_dir = HORIZONTAL
	line2_dir = HORIZONTAL
	# determine line orientation
	if c_x == p_x:
		line1_dir = VERTICAL
	if x1 == x2:
		line2_dir = VERTICAL
	# determine intervals (min, max) for each line
	line1_min_x = c_x
	line1_max_x = p_x
	if p_x < c_x:
		line1_min_x = p_x
		line1_max_x = c_x
	
	line1_min_y = c_y
	line1_max_y = p_y
	if p_y < c_y:
		line1_min_y = p_y
		line1_max_y = c_y

	line2_min_x = x1
	line2_max_x = x2
	if x2 < x1:
		line2_min_x = x2
		line2_max_x = x1
	
	line2_min_y = y1
	line2_max_y = y2
	if y2 < y1:
		line2_min_y = y2
		line2_max_y = y1

	# case: one line horizontal, one line vertical
	if line1_dir == HORIZONTAL and line2_dir == VERTICAL:
		# check line2_x bounded between line1_x's, and...
		# check line1_y bounded between line2_y's
		if line1_min_x <= line2_min_x <= line1_max_x:
			if line2_min_y <= line1_min_y <= line2_max_y:
				return (line2_min_x, line1_min_y)
		return False # no intersect

	if line1_dir == VERTICAL and line2_dir == HORIZONTAL:
		# check line2_y bounded between line1_y's, and...
		# check line1_x bounded between line2_x's
		if line1_min_y <= line2_min_y <= line1_max_y:
			if line2_min_x <= line1_min_x <= line2_max_x:
				return (line1_min_x, line2_min_y)
		return False # no intersect

	# case: both lines horizontal
	if line1_dir == HORIZONTAL and line2_dir == HORIZONTAL:
		# check line1 and line2 same x value, and y-intervals overlap
		# TODO (check east west direction, determine which line in front, etc)
		a = 1

	# case: both lines vertical	
	if line1_dir == VERTICAL and line2_dir == VERTICAL:
		# check line1 and line2 same y value, and x-intervals overlap
		a = 1

	return False	# no intersection exists / (no cases match)


if __name__ == '__main__':
	main()
