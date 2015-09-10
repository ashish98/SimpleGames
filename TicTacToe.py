import sys, time, random
print "Enter your name"
name = raw_input()
print "Hello, " + name +". Do you want X or O?"
choices = ['X','O']
choice = raw_input()
choice = choice.upper()

if not (choice == 'X' or choice == 'O'):
		print "Wrong Input." 
		sys.exit()
count = 0
if choice == 'X':
	print name + ", you will start"
	count = 1
	choice2 = choices[1]
else:
	print "Computer starts"
	choice2 = choices[0]
	time.sleep(1)
put = ['0','1','2','3','4','5','6','7', '8','9']

flag = 0
def board(pos,val):
	flag = 1
	print
	put[pos] = val
	print " " + put[7] + " | " + put[8] + " | " + put[9] 
	print "-----------"
	print " " + put[4] + " | " + put[5] + " | " + put[6] 
	print "-----------"
	print " " + put[1] + " | " + put[2] + " | " + put[3]
	print
	return flag

def side():
	flag = 0
 	free = []
 	for i in [2,4,6,8]:
 		if put[i] == str(i):
 			free.append(put[i])
 	len_free = len(free)
 	rand = int(random.choice(free))
 	board(rand,choice2)

def centre():
	flag = 0
	if put[5] == '5':
		flag = board(5,choice2)
	if flag == 0:
		side()


def corner():
	flag = 0
 	free = []
 	for i in [1,3,7,9]:
 		if put[i] == str(i):
 			free.append(put[i])
 	len_free = len(free)
 	rand = int(random.choice(free))
 	flag = board(rand,choice2)
 	if flag == 0:
		centre()


def counterwin():
	flag = 0
	if put[1] == choice and put[2] == choice and put[3] != choice2:
		flag = board(3,choice2)
	elif put[1] == choice and put[3] == choice and put[2] != choice2:
		flag = board(2,choice2)
	elif put[2] == choice and put[3] == choice and put[1] != choice2:
		flag = board(1,choice2) 

	elif put[4] == choice and put[5] == choice and put[6] != choice2:
		flag = board(6,choice2)
	elif put[4] == choice and put[6] == choice and put[5] != choice2:
		flag = board(5,choice2)
	elif put[5] == choice and put[6] == choice and put[4] != choice2:
		flag = board(4,choice2)

	elif put[7] == choice and put[8] == choice and put[9] != choice2:
		flag = board(9,choice2)
	elif put[7] == choice and put[9] == choice and put[8] != choice2:
		flag = board(8,choice2)
	elif put[8] == choice and put[9] == choice and put[7] != choice2:
		flag = board(7,choice2)

	elif put[1] == choice and put[4] == choice and put[7] != choice2:
		flag = board(7,choice2)
	elif put[1] == choice and put[7] == choice and put[4] != choice2:
		flag = board(4,choice2)
	elif put[4] == choice and put[7] == choice and put[1] != choice2:
		flag = board(1,choice2)

	elif put[2] == choice and put[5] == choice and put[8] != choice2:
		flag = board(8,choice2)
	elif put[2] == choice and put[8] == choice and put[5] != choice2:
		flag = board(5,choice2)
	elif put[5] == choice and put[8] == choice and put[2] != choice2:
		flag = board(2,choice2)

	elif put[3] == choice and put[6] == choice and put[9] != choice2:
		flag = board(9,choice2)
	elif put[3] == choice and put[9] == choice and put[6] != choice2:
		flag = board(6,choice2)
	elif put[6] == choice and put[9] == choice and put[3] != choice2:
		flag = board(3,choice2)

	elif put[1] == choice and put[5] == choice and put[9] != choice2:
		flag = board(9,choice2)
	elif put[1] == choice and put[9] == choice and put[5] != choice2:
		flag = board(5,choice2)
	elif put[5] == choice and put[9] == choice and put[1] != choice2:
		flag = board(1,choice2)
 	
 	elif put[3] == choice and put[5] == choice and put[7] != choice2:
 		flag = board(7,choice2)
 	elif put[3] == choice and put[7] == choice and put[5] != choice2:
 		flag = board(5,choice2)
 	elif put[5] == choice and put[7] == choice and put[3] != choice2:
 		flag = board(3,choice2)

 	if flag == 0:
 		corner()


def checkwin():
	flag = 0
	if put[1] == choice2 and put[2] == choice2 and put[3] != choice:
		flag = board(3,choice2)
	elif put[1] == choice2 and put[3] == choice2 and put[2] != choice:
		flag = board(2,choice2)
	elif put[2] == choice2 and put[3] == choice2 and put[1] != choice:
		flag = board(1,choice2) 
	elif put[4] == choice2 and put[5] == choice2 and put[6] != choice:
		flag = board(6,choice2)
	elif put[4] == choice2 and put[6] == choice2 and put[5] != choice:
		flag = board(5,choice2)
	elif put[5] == choice2 and put[6] == choice2 and put[4] != choice:
		flag = board(4,choice2)
	elif put[7] == choice2 and put[8] == choice2 and put[9] != choice:
		flag = board(9,choice2)
	elif put[7] == choice2 and put[9] == choice2 and put[8] != choice:
		flag = board(8,choice2)
	elif put[8] == choice2 and put[9] == choice2 and put[7] != choice:
		flag = board(7,choice2)
	elif put[1] == choice2 and put[4] == choice2 and put[7] != choice:
		flag = board(7,choice2)
	elif put[1] == choice2 and put[7] == choice2 and put[4] != choice:
		flag = board(4,choice2)
	elif put[4] == choice2 and put[7] == choice2 and put[1] != choice:
		flag = board(1,choice2)	
	elif put[2] == choice2 and put[5] == choice2 and put[8] != choice:
		flag = board(8,choice2)
	elif put[2] == choice2 and put[8] == choice2 and put[5] != choice:
		flag = board(5,choice2)
	elif put[5] == choice2 and put[8] == choice2 and put[2] != choice:
		flag = board(2,choice2)
	elif put[3] == choice2 and put[6] == choice2 and put[9] != choice:
		flag = board(9,choice2)
	elif put[3] == choice2 and put[9] == choice2 and put[6] != choice:
		flag = board(6,choice2)
	elif put[6] == choice2 and put[9] == choice2 and put[3] != choice:
		flag = board(3,choice2)
	elif put[1] == choice2 and put[5] == choice2 and put[9] != choice:
		flag = board(9,choice2)
	elif put[1] == choice2 and put[9] == choice2 and put[5] != choice:
		flag = board(5,choice2)
	elif put[5] == choice2 and put[9] == choice2 and put[1] != choice:
		flag = board(1,choice2)	
 	elif put[3] == choice2 and put[5] == choice2 and put[7] != choice:
 		flag = board(7,choice2)
 	elif put[3] == choice2 and put[7] == choice2 and put[5] != choice:
 		flag = board(5,choice2)
 	elif put[5] == choice2 and put[7] == choice2 and put[3] != choice:
 		flag = board(3,choice2)

 	if flag == 1:
 		print "Computer Won !!!!"
 		sys.exit()
 	elif flag == 0 :
 		counterwin()

def AI():
	checkwin()

def checkuserwin():
	if put[1] == choice and put[2] == choice and put[3] == choice:
		print name + ", You Have Won!!!"
		sys.exit()
	elif put[4] == choice and put[5] == choice and put[6] == choice:
		print name + ", You Have Won!!!"
		sys.exit()
	elif put[7] == choice and put[8] == choice and put[9] == choice:
		print name + ", You Have Won!!!"
		sys.exit()
	elif put[1] == choice and put[5] == choice and put[9] == choice:
		print name + ", You Have Won!!!"
		sys.exit()
	elif put[3] == choice and put[5] == choice and put[7] == choice:
		print name + ", You Have Won!!!"
		sys.exit()
	elif put[1] == choice and put[4] == choice and put[7] == choice:
		print name + ", You Have Won!!!"
		sys.exit()
	elif put[2] == choice and put[5] == choice and put[8] == choice:
		print name + ", You Have Won!!!"
		sys.exit()
	elif put[3] == choice and put[6] == choice and put[9] == choice:
		print name + ", You Have Won!!!"
		sys.exit()

def draw():
	flag = 0
	for x in xrange(1,10):
		if put[x] == str(x):
			flag += 1

	if flag == 1:
		print "It's a draw!!!"
		sys.exit()			

i = 1
board(0,'X')
while i<=9:
	draw()
	if count%2 != 0:
		print "Enter your position"
		pos = raw_input()
		pos = int(pos)
		board(pos,choice)
		checkuserwin()
		time.sleep(2)
		AI()
		

	else:
		AI()
		print "Enter your position"
		pos = raw_input()
		pos = int(pos)
		board(pos,choice)
		checkuserwin()
		time.sleep(2)
	i += 2 

