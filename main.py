#!/usr/bin/env python
import argparse
import math
import heapq
import time
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
def construct_path(came_from, start, goal):
	current = goal
	path = [current]
	while current != start:
		current = came_from[current]
		path.append(current)	
	path.reverse() 
	return path

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
valid_dir = ["n", "s", "e", "w"]
valid = ["fw", "leap", "left", "right"]
inf = 1000000000

#node for a-star
class PriorityQueue:
	def __init__(self):
		self.elements = []
	
	def empty(self):
		return len(self.elements) == 0
	
	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))
	
	def get(self):
		return heapq.heappop(self.elements)[1]

class Robot:
	def __init__(self, pos_r = None, pos_c = None):
		if pos_r == None:
			for i in l:
				if 'S' in i:
					self.pos_r = l.index(i)
					self.pos_c = i.index('S')
					self.prevstep = "start"
		else:
			self.pos_c = pos_c
			self.pos_r = pos_r
		self.direction = 'n'
		
	
	def isGoal(self):
		return l[self.pos_r][self.pos_c] == "G"
	
	def __eq__(self, other): 
		return self.__dict__ == other.__dict__
	
	def __lt__(self, other):
		return True
	
	def __str__(self):
		return str(self.__dict__)
	
	def __hash__(self):
		return hash((self.pos_r, self.pos_c, self.direction))

	def getcost(self, dis):
		f = inf
		
		#direction of the step
		if self.direction == "n":
			new_r = self.pos_r - dis
			if new_r < 0:
				return inf
			f = l[new_r][self.pos_c]
		elif self.direction == "s":
			new_r = self.pos_r + dis
			if new_r >= r:
				return inf
			f = l[new_r][self.pos_c]
		elif self.direction == "e":
			new_c = self.pos_c + dis
			if new_c >= c:
				return inf
			f = l[self.pos_r][new_c]
		elif self.direction == "w":
			new_c = self.pos_c - dis
			if new_c < 0:
				return inf
			f = l[self.pos_r][new_c]

		if f == "#":
			return inf
		if f == "S" or f == "G":
			return 1
		return int(f)

	def cost(self,step):
		if step.type == "leap":
			if self.getcost(3) == inf:
				return inf
			return 20
		elif step.type == "fw":
			return self.getcost(1)
		elif step.type == "left" or step.type == "right":
			co = math.ceil(self.getcost(0) * 1/3)
			return co
		else:
			return inf

	#make sure that the step cost is not infinity before running this function
	def execute(self, step):
		dis = 0
		
		new_robot = Robot(self.pos_r, self.pos_c)
		new_robot.direction = self.direction
		
		if step.type == "leap":
			new_robot.prevstep = "leap"
			dis = 3
		elif step.type == "fw":
			new_robot.prevstep = "Forward"
			dis = 1
		elif step.type == "left":
			new_robot.prevstep = "Turn left"
			if self.direction == "n":
				new_robot.direction = "w"
			elif self.direction == "s":
				new_robot.direction = "e"
			elif self.direction == "e":
				new_robot.direction = "n"
			elif self.direction == "w":
				new_robot.direction = "s"
			return new_robot
		elif step.type == "right":
			new_robot.prevstep = "Turn right"
			if self.direction == "n":
				new_robot.direction = "e"
			elif self.direction == "s":
				new_robot.direction = "w"
			elif self.direction == "e":
				new_robot.direction = "s"
			elif self.direction == "w":
				new_robot.direction = "n"
			return new_robot

		if self.direction == "n":
			new_robot.pos_r -= dis
		elif self.direction == "s":
			new_robot.pos_r += dis
		elif self.direction == "w":
			new_robot.pos_c -= dis
		elif self.direction == "e":
			new_robot.pos_c += dis
		return new_robot
			
	def neighbors(self):
		steps = []
		step = Step("fw")
		if self.cost(step) != inf:
			steps.append(step)
		step = Step("left")
		steps.append(step)
		step = Step("right")
		steps.append(step)
		step = Step("leap")
		if self.cost(step) != inf:
			steps.append(step)
		return steps

class Step:
	def __init__(self, t):
		if t in valid:
			self.type = t
		else:
			self.type = "fw"

score = 0
#a star function
def astar(heuristic):
	global score
	r = Robot()
	opqueue = PriorityQueue()
	opqueue.put(r, 0)
	cameFrom = {}
	cost_so_far = {}
	cameFrom[r] = None
	cost_so_far[r] = 0
	
	while not opqueue.empty():
		current = opqueue.get()
		
		if current.isGoal():
			score += 500
			break
		
		for n in current.neighbors():
			new_node = current.execute(n)
			new_cost = cost_so_far[current] + current.cost(n) + heuristic(new_node)
			if new_node not in cost_so_far or new_cost < cost_so_far[new_node]:
				cost_so_far[new_node] = new_cost
				priority = new_cost
				opqueue.put(new_node, priority)
				cameFrom[new_node] = current
	return cameFrom, cost_so_far
		
#heuristic function

#handling the input and main function
exetime = time.time()
if args.method == 1:
	cameFrom = astar(lambda x: 0)[0]

exetime = time.time() - exetime
score -= int(exetime / 0.02) 
goal = next(filter(lambda x: x.isGoal(), cameFrom.keys()))
path = construct_path(cameFrom, Robot(), goal)
print("Score: " + str(score))
print("Number of steps: " + str(len(path) - 1))
for a in path:
	print(a.prevstep)
#test
#print (array_pos(1,2))
#print (rowcol_from(5))

# vim: set noexpandtab ts=4 sw=4 :
