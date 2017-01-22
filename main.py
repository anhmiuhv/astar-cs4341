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
		for i in l:
			if 'S' in i:
				self.pos_r = l.index(i)
				self.pos_c = i.index('S')
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

		if f == "#":
			return math.inf
		if f == "S" or f == "G":
			return 1
		return f

	def cost(self,step):
		if step.type == "leap":
			if self.getcost(3) == math.inf:
				return math.inf
			return 20
		elif step.type == "fw":
			return self.getcost(1)
		elif step.type == "left" or step.type == "right":
			co = math.ceil(self.getcost(0) * 1/3)
			return co
		else:
			return math.inf

	#make sure that the step cost is not infinity before running this function
	def execute(self, step):
		dis = 0
		if step.type == "leap":
			dis = 3
		elif step.type == "fw":
			dis = 1
		elif step.type == "left":
			if self.direction == "n":
				self.direction = "w"
			elif self.direction == "s":
				self.direction = "e"
			elif self.direction == "e":
				self.direction = "n"
			elif self.direction == "w":
				self.direction = "s"
			return
		elif step.type == "right":
			if self.direction == "n":
				self.direction = "e"
			elif self.direction == "s":
				self.direction = "w"
			elif self.direction == "e":
				self.direction = "s"
			elif self.direction == "w":
				self.direction = "n"
			return

		if self.direction == "n":
			self.pos_r -= dis
		elif self.direction == "s":
			self.pos_r += dis
		elif self.direction == "w":
			self.pos_c -= dis
		elif self.direction == "e":
			self.pos_c += dis

class Step:
	valid = ["fw", "leap", "left", "right"]
	def __init__(self,type):
		if type in valid:
			self.type = type








#main a star function


#test
#print (array_pos(1,2))
#print (rowcol_from(5))


