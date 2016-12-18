#!/usr/bin/env python3.5

import hashlib, collections
# to learn: itertools (compress), yield

# PART 1
#passcode = 'ihgpwlah' # test
#passcode = 'kglvqrro'
#passcode = 'hijkl' # no soln
#passcode = 'ulqzkmiv'

# PART 2
#passcode = 'ihgpwlah'
#passcode = 'kglvqrro'
#passcode = 'ulqzkmiv'

passcode = 'qljzarfv' # part 1, 2

start = (0,0)
end = (3,3) # goal ords

# room state constants (collections.namedtuple would be easier?)
UP = 0; DOWN = 1; LEFT = 2; RIGHT = 3
# for bfs (first index is same as room state constants)
navigate = [ ((0,-1),'U'), ((0,1),'D'),
				 ((-1,0),'L'), ((1,0),'R') ] # (x,y)
NAVIGATE_ORDS = 0; NAVIGATE_CHAR = 1
X_IND = 0; Y_IND = 1

def main():
	# (current implementation of visited states isn't correct) :oo
	#visited_states = [] # requires: ( (x,y), [room_state] )
	q = collections.deque([ (start,[]) ]) # requires: ( (x,y), [path] )
	# bfs
	part1 = False
	found = False
	found_path_list = None
	all_found_path_strings = [] # assume all paths are finite :oo (part 2)

	while len(q) > 0 and not found:
		cur_ords, cur_path_list = q.popleft()
		#print(cur_ords, cur_path_list)
		# get room state
		cur_room = room_state(''.join(cur_path_list))
		# check in visited
		#if ( cur_ords, cur_room ) in visited_states:
		#	continue
		# add to visited
		#visited_states.append( (cur_ords, cur_room) )
		# get neighbours
		for i in range(4):
			if cur_room[i] == False:
				 continue
			d_ords, d_char = navigate[i]
			next_ords = ( cur_ords[X_IND] + d_ords[X_IND],
			 			  cur_ords[Y_IND] + d_ords[Y_IND] )
			# check next neighbour is valid
			if not in_map_bounds(next_ords):
				continue
			# generate info (next_ords, [next_path_list])
			next_path_list = cur_path_list + [d_char]
			# check goal ords
			if next_ords == end:
				if part1:
					found = True
					found_path_list = next_path_list
					break
				else:
					all_found_path_strings.append(''.join(next_path_list))
					continue
			# add to queue
			q.append( (next_ords,next_path_list) )
	# results
	if part1 and found:
		found_path = ''.join(found_path_list)
		print("PART 1: found:", found_path)
		#for i in range(len(found_path)):
		#	print(hash_string(found_path[:i]))
	if not part1:
		print(len(max(all_found_path_strings,key=lambda x:len(x))))
		#for p in all_found_path_strings:
		#	print(len(p),":",p)

def in_map_bounds(ords):
	for i in ords:
		if not (0 <= i < 4):
			return False
	return True

def hash_string(path_string):
	return hashlib.md5((passcode + path_string).encode()).hexdigest()

def room_state(path_string):
	room = hashlib.md5((passcode + path_string).encode()).hexdigest()[:4]
	v = ['b','c','d','e','f']
	res = [True if door in v else False for door in room]
	return res

if __name__ == '__main__':
	main()
