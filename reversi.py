# NOT finished ...

board = [[0, 1,  2,  3,  4,  5,  6,  7,  8 ],
		 [1,' ',' ',' ',' ',' ',' ',' ',' '],
		 [2,' ',' ',' ',' ',' ',' ',' ',' '],
		 [3,' ',' ',' ',' ',' ',' ',' ',' '],
		 [4,' ',' ',' ',' ',' ',' ',' ',' '],
		 [5,' ',' ',' ',' ',' ',' ',' ',' '],
		 [6,' ',' ',' ',' ',' ',' ',' ',' '],
		 [7,' ',' ',' ',' ',' ',' ',' ',' '],
		 [8,' ',' ',' ',' ',' ',' ',' ',' ']]

def showBoard():
	for i in board:
		for j in i:
			print j,
			print "|",
		print 
		print "-"*35

print "Enter your choice 'X' or 'O' "
choice = raw_input()
choice = choice.upper()

import sys

if choice == 'X':
	choice2 ='O'
elif choice == 'O':
	choice2 = 'X'
else:
	print "Invalid choice"
	sys.exit()

import time,random

def AI():
	lst = []
	flag = True
	for xi in xrange(1,7):
		for yj in xrange(1,9):
			if board[xi][yj] == choice2 and board[xi+1][yj] == choice and board[xi+2][yj] == ' ':
				if [xi+2,yj] not in lst:
					lst.append([xi+2,yj])

	for yj in xrange(1,9):
		xi = 2
		if board[10-xi][yj] == choice2 and board[9-xi][yj] == choice and board[8-xi][yj] == ' ':
			if [8-xi,yj] not in lst:
				lst.append([8-xi,yj])

	for xi in xrange(1,9):
		for yj in xrange(1,7):
			if board[xi][yj] == choice2 and board[xi][yj+1] == choice and board[xi][yj+2] == ' ':
				if [xi,yj+2] not in lst:
					lst.append([xi,yj+2])

	for xi in xrange(1,9):
		yj = 2		
		if board[xi][10-yj] == choice2 and board[xi][9-yj] == choice and board[xi][8-yj] == ' ':
			if [xi,8-yj] not in lst:
				lst.append([xi,8-yj])

	if lst == []:
		while flag == True:
			X = random.randint(1,8)
			Y = random.randint(1,8)
			if board[X][Y] != ' ':
				continue
			else:
				board[X][Y] = choice2
				flag = False

	else:
		print lst
		len_list = len(lst)
		pos = random.randint(0,len_list-1)
		temp = lst[pos]
		X = temp[0]
		Y = temp[1]
		board[X][Y] = choice2

def points():
	userPoint = 0
	compPoint = 0
	for i in board:
		for j in i:
			if j == choice:
				userPoint += 1
			if j == choice2:
				compPoint += 1
	return [userPoint,compPoint]

def findWinner():
	point = points()
	if point[0] > point[1]:
		print "You Won!!!"
	elif point[0] < point[1]:
		print "Computer Won!!!"
	else:
		print "Its a draw!!!"

	sys.exit()

def check():
	count = 0
	for i in board:
		for j in i:
			if j == ' ':
				count += 1
	if count == 0:
		Winner = findWinner()

while True:

	showBoard()

	print "Enter your position 'x y'"
	print "For eg, to enter (3,4) type 3 4"
	pos = raw_input()

	try:
		x,y = pos.split(" ")
		x = int(x)
		y = int(y)
	except:
		print "Please enter a valid coordinate"
		continue

	if x > 8 or x < 1 or y > 8 or y < 1:
		print "Please Enter a valid coordinate"

	board[x][y] = choice
	#time.sleep(2)
	AI()
	point = points()
	print "Your score is - " + str(point[0])
	print "Computer score is - " + str(point[1])
	check()

