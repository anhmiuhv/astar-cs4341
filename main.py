import argparse

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

#helper function
def array_pos(row, col):
	if row >= r or col >= c:
		return -1

	return row*count + col

#robot information
robot_pos = [0 for _ in range(c * r)]
robot_pos[l.index('S')] = 1
print robot_pos
#main a star function




f.close()