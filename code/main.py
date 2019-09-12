import pygame, player, sys, keyboard as kb

class Main:
	"""The main class for the game"""
	def __init__(self):
		"""Initializes the game and begins the execution of the app"""
		pygame.init()
		self.screen = pygame.display.set_mode((720, 640))
		pygame.display.set_caption("Testing stuff")
		self.player = player.Player(0, 0) #The player handler
		self.mainloop() #This should be replaced with the main menu when we can get it working

	def mainloop(self):
		"""The main state of the game will be in this function"""
		while 1: #Same as while loop forever
			self.key_loop()
			pygame.time.wait(2)

	def key_loop(self):
		"""Handles events done by the user such as key and mouse presses"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT: #The user hit the close button
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == kb.K_q:
					pygame.quit()
					sys.exit()
		if self.player.movetimer.elapsed >= self.player.movetime:
			if kb.key_down(kb.K_UP): self.player.move(1)
			elif kb.key_down(kb.K_RIGHT): self.player.move(2)
			elif kb.key_down(kb.K_DOWN): self.player.move(3)
			elif kb.key_down(kb.K_LEFT): self.player.move(4)

test = Main()
