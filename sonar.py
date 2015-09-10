lst = [	[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],
		[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],
		[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],
		[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],
		[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9], ] 
count = 0
for i in lst:
	for j in i:
		if j == 0:
			lst[count][0] = count
			count += 1 

for x in xrange(1,23):
	for y in xrange(1,10):
		lst[x][y] = '.'

def show():
	for i in lst:
		for j in i:
			print j, "\t",
		print

import random, math,sys
X = random.randint(1,9)
Y = random.randint(1,22)
for x in xrange(0,10):
	print "guess no - " + str(x)
	print "Enter position 'x y' to find treasure"
	pos = raw_input()
	x,y = pos.split(' ')
	x = int(x)
	y = int(y)
	dis = math.sqrt(pow((X-x),2)+pow((Y-y),2))
	if dis == 0:
		print "You found the treasure!!!"
		sys.exit()
	else:
		lst[x][y] = int(dis)
	show()




