import timer

class Player:
	"""The player class that is going to be used inside the game"""
	def __init__(self, x, y):
		"""Creates a player.
		Parameters:
			x (int): The starting x of the player
			y (int): The starting y of the player
		Return Value:
			None"""
		self.x = x
		self.y = y
		self.movetimer = timer.Timer()
		self.movetime = 150

	def move(self, val):
		"""Moves the player.
		Parameters:
			val (int, 1 <= 4): The value determining the direction the player should move
		Return Value:
			None"""
		self.movetimer.restart()
		if val == 1: self.y += 1
		elif val == 2: self.x += 1
		elif val == 3: self.y -= 1
		else: self.x -= 1
		print(self.x, self.y)