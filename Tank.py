class Tank(object):
	"""docstring for Tank"""
	def __init__(self, name):
		#super(Tank, self).__init__()
		self.name = name
		self.alive = True
		self.ammo = 5
		self.armour = 60

	def __str__(self):
		if self.alive:
			return "%s (%i armour,%i shells)" % (self.name,self.armour,self.ammo)
		else:
			return "%s (DEAD)" % self.name

	def fire_at(self,enemy):
		if self.ammo >=1:
			self.ammo -=1
			print self.name, "fires on", enemy.name
			enemy.hit()
		else:
			print self.name, "has no shells!"

	def hit(self):
		self.armour -=20
		print self.name, "is hit!"
		if self.armour <=0:
			self.explode()
	def explode(self):
		self.alive = False
		print self.name, "explodes!"


my_tank = Tank("Bob")
print my_tank
		
