import random, time
print "The speaking cave is asking -----"
print "What's your name traveller???"
name = raw_input()
print "Which cave do you wish to enter? cave1 or cave2"
print "But BEWARE!!!! one cave has treasure and other has dragon that will burn u alive and then eat u up"
choice = int(raw_input())
if choice == 1 or choice == 2:
	dragon = random.randint(1,2)
	if dragon == choice:
		print "You enter cave",choice
		time.sleep(2)
		print "You cannot see any thing"
		time.sleep(2)
		print "Suddenly the DRAGON approaches and ----"
		time.sleep(5)
		print "You are dead!!!"
	else:
		print "You enter cave",choice
		time.sleep(2)
		print "You cannot see any thing"
		time.sleep(2)
		print "Suddenly you see light"
		time.sleep(4)
		print "Holy fuck!!! you see a treasure"
		print "You are rich now"


