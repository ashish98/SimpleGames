import random,sys
def blank(i):
	while i>0:
		print "_",
		i -=1

words = ['tree','bear','elephant','ant','ship','sheep','sand','nest','sea','see',
			'aeroplane','pneumonia','aerodrum','airport','vulture','telephone',
			'ventilator','house''helicopter','window','loafor','suitcase','eagle',
			'tablet','computer','laptop','mobile','parachute','tiger','giraffe','zebra'
			'oil','umbrella','glass','cool','bulb','train','hippopotamus',
		]
num = len(words)
board = [	"""
			----------------\n\n\n\n\n\n\t\t\t================""",

			"""
			----------------\n\t\t\t\t|\n\n\n\n\t\t\t================""",
			"""
			----------------\n\t\t\t\t|\n\t\t\t\tO\n\n\n\n\t\t\t================""",
			"""
			----------------\n\t\t\t\t|\n\t\t\t\tO\n\t\t\t\t|\n\n\n\t\t\t================""",
			"""
			----------------\n\t\t\t\t|\n\t\t\t\tO\n\t\t\t       /|\n\n\n\t\t\t================""",
			"""
			----------------\n\t\t\t\t|\n\t\t\t\tO\n\t\t\t       /|\\\n\n\n\t\t\t================""",
			"""
			----------------\n\t\t\t\t|\n\t\t\t\tO\n\t\t\t       /|\\\n\t\t\t\t|\n\n\t\t\t================""",
			"""
			----------------\n\t\t\t\t|\n\t\t\t\tO\n\t\t\t       /|\\\n\t\t\t       /|\n\n\t\t\t================""",
			"""
			----------------\n\t\t\t\t|\n\t\t\t\tO\n\t\t\t       /|\\\n\t\t\t       /|\\\n\n\t\t\t================"""]

temp = words[random.randint(1,num)-1]
word = []
already = []
for wordi in xrange(0,len(temp)):
	word.append('_')	
blank(len(temp))
count = 0 

while count<9:

	print board[count]
	print
	for wordi in xrange(0,len(word)):
		print word[wordi],
	print
	print "Guess a letter"
	x = raw_input()

	if x in already:
		print "You already selected this letter"
		continue
	else:
		already.append(x)
		check = 0
		for j in xrange(0,len(temp)):
			if x == temp[j]:
				word[j] = temp[j]
				check += 1
		if check == 0:
			count += 1
			

		new = ''
		for asd in xrange(0,len(word)):
			new = new + word[asd]
		if temp in new:
			print temp
			print "You Won!!!"
			sys.exit()

print "You Lose"




	
