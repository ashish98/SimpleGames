import random
print "Hie, What's your name??? :)"
name = raw_input();
print "Ok "+ name + " I am guessing a number from 1 to 20."
print "Can you guess? I will give you 6 tries....."

num = random.randint(1,20)

for tries in range(7):
	print "try - ", tries
	try:
		x = int(raw_input())
		if x == num:
			print "Well " + name + " You guessed it right"
			break
		elif x>num and x<=20:
			print "No dude, The number I am thinking of is less than ",x 
		elif x<num and x>0:
			print "No dude, The number I am thinking of is more than ",x
		else:
			print "I am thinking of a number between 1 and 20, both inclusive"
	except:
		print "Wrong input.... Enter a number"

	if tries == 6:
		print "Sry, But You are a loser"
		print "I was thinking of",num



