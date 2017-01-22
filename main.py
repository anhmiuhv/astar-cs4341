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
    cols = line.split('\t')
    l.extend(cols)
    r += 1
    c = len(cols)
l = [a.strip('\n') for a in l]
f.close()

#helper function
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
		self.robot_pos = [0 for _ in range(c * r)]
		self.robot_pos[l.index('S')] = 1
		self.pos = l.index('S')
		self.direction = 'n'

	def getcost(self, dis):
		rowcol = rowcol_from(self.pos)
		new_rc = (-1,-1)
		f = math.inf
		if self.direction == "n":
			new_rc = (rowcol[0] - dis, rowcol[1])
			if new_rc[0] < 0:
				return math.inf
			f = l[arraypos(new_rc)]
		elif self.direction == "s":
			new_rc = (rowcol[0] + dis, rowcol[1])
			if new_rc[0] >= r:
				return math.inf
		elif self.direction == "e":
			new_rc = (rowcol[0], rowcol[1] + 1)
			if new_rc[1] >= c:
				return math.inf


class Step:
	valid = ["fw", "leap", "left", "right"]
	def __init__(self,type):
		if type in valid:
			self.type = type

	def cost(robot):
		rowcol = rowcol_from(robot_pos)
		if self.type == "leap":
			#TODO: detect unleapable terrain
			return 20
		if robot.direction == "n":
			new_rc = (rowcol[0] + 1, rowcol[1])









#main a star function


#test
print (array_pos(1,2))
print (rowcol_from(5))


