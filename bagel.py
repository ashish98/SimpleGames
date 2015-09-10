import random,sys

num = str(random.randint(100,999))
print('I am thinking of a 3 digit number. Try to guess what it is.') 
print('Here are some clues:')
print('When I say: That means:')
print('Pico ---> One digit is correct but in the wrong position.')
print('Fermi ---> One digit is correct and in the right position.')
print('Bagels ---> No digit is correct.')
i = 1

while i<=10:
	count =0
	print "guess no. - " + str(i)
	guess = raw_input()

	if int(guess) > 999 or int(guess)<100:
		print "Wrong input"
		i -= 1
		continue
	if int(num) == int(guess):
		print "You guessed correctly"
		sys.exit()
	
	for j in [0,1,2]:
		for k in [0,1,2]:
			if guess[k] == num[j]:
				if j == k:
					count +=1
					print "Fermi\t",
				else:
					count +=1
					print "Pico\t",
	print
	if count == 0:
		print "Bagel"
	i += 1


