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


def main():
	# variables (center from (0,0))
	cur_dir = NORTH
	cur_x = 0
	cur_y = 0
	all_visited_ords = [] # array of tuples
	all_visited_ords.append((cur_x, cur_y))
	part2_solved = False

	path_list = path.split(', ')
	for i in path_list:
		turn_dir = i[0] # either L or R
		length = int(i[1:]) # numeric (can be more than one digit)
		cur_dir = updateDir(cur_dir, turn_dir)

		# replaces: cur_x, cur_y = updateOrds(cur_x, cur_y, cur_dir, length)
		# (north, east, south, west): (x,y)
		inc = [	[0, 1],
			   	[1, 0],
				[0, -1],
				[-1, 0] ]
		x_inc, y_inc = inc[cur_dir]
		for j in range(length):
			cur_x += x_inc
			cur_y += y_inc
			if (cur_x, cur_y) in all_visited_ords:
				if part2_solved == False:
					part2_solved = True
					print("#### PART 2 ANSWER: ####")
					print('ords from origin are: {},{}'.format(cur_x, cur_y))
					print('blocks away: ' + str(abs(cur_x) + abs(cur_y)))
			else:
				all_visited_ords.append((cur_x, cur_y))
			# NOTE: works, but is this the most efficient method?? :/

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


if __name__ == '__main__':
	main()
