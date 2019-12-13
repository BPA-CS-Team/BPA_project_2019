class enemy:
	"""The base enemy class"""
	def __init__(self, x, y, movetime, hp):
		self.x = x
		self.y = y
		self.movetime = movetime
		self.hp = hp

	def act(self):
		#Override this function for different enemy behavior
		pass
