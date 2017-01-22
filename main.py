#!/usr/bin/env python
import argparse
import math

#parsing option from users
parser = argparse.ArgumentParser(description='Please give mr.robot a terrain information')
parser.add_argument('filename', help='the name of the file for terrain info')
parser.add_argument('method', type=int, choices=range(1, 7), help='choice for heuristic method')
args = parser.parse_args()


#read the file and turn into array
f = open(args.filename)
l = [] #all the information about the terrain
r = 0 #row of the terrain
c = 0 #column of the terrain
for line in f.readlines():
	cols = line.split()
	l.append(cols)
	r += 1
	c = len(cols)
f.close()

#helper function
#these two should not be needed anymore
def array_pos(row, col):
	if row >= r or col >= c:
		return -1
	return row*c + col

def rowcol_from(arraypos):
	if arraypos >= len(l):
		return (-1,-1)

	row = arraypos // c
	col = arraypos % c
	return (row, col)

#robot information


#node for a star
class Robot:
	valid_dir = ["n", "s", "e", "w"]
	def __init__(self):
		self.robot_pos = [[0 for i in range(c)] for j in range(r)]
		for i in l:
			if 'S' in i:
				self.pos_r = l.index(i)
				self.pos_c = i.index('S')
				self.robot_pos[pos_r][pos_c] = 1
		self.direction = 'n'

	def getcost(self, dis):
		new_rc = (-1,-1)
		f = math.inf
		
		#direction of the step
		if self.direction == "n":
			new_r = self.pos_r - dis
			if new_r < 0:
				return math.inf
			f = l[new_r][self.pos_c]
		elif self.direction == "s":
			new_r = self.pos_r + dis
			if new_r >= r:
				return math.inf
			f = l[new_r][self.pos_c]
		elif self.direction == "e":
			new_c = self.pos_c + dis
			if new_c >= c:
				return math.inf
			f = l[self.pos_r][new_c]
		elif self.direction == "w":
			new_c = self.pos_c - dis
			if new_c < 0:
				return math.inf
			f = l[self.pos_r][new_c]

		return f

class Step:
	valid = ["fw", "leap", "left", "right"]
	def __init__(self,type):
		if type in valid:
			self.type = type

	def cost(robot):
		if self.type == "leap":
			if robot.getcost(3) == math.inf:
				return math.inf
			return 20
		elif self.type == "fw":
			return robot.getcost(1)
		elif self.type == "left" or self.type == "right":
			cost = math.ceil(robot.getcost(0) * 1/3)
			return cost
		else:
			return math.inf









#main a star function


#test
#print (array_pos(1,2))
#print (rowcol_from(5))

# vim: set noexpandtab ts=4 sw=4 :
