import pygame,timer, GameObject, Box2D

class Player(GameObject.GameObject) :
	"""The player class that is going to be used inside the game"""
	def __init__(self, x, y, image_path):
		"""Creates a player.
		Parameters:
			x (int): The starting x of the player
			y (int): The starting y of the player
			image_path (string): Player image path
		Return Value:
			None"""
		# Call the parent class (Sprite) constructor
		GameObject.GameObject.__init__(self)

	   	# Create an image of the block, and fill it with a color.
       	# This could also be an image loaded from the disk.
		self.image = pygame.image.load(image_path)

       	# Fetch the rectangle object that has the dimensions of the image
       	# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.movetimer = timer.Timer()
		self.movetime = 150
		#Jumping variables
		self.jumptimer = timer.Timer()
		self.jumptime = 100 #How fast we rise and fall
		self.min_h = self.rect.y #The height to which the player will descend back to before falling
		self.max_h = self.min_h
		self.jump_h = 5 #Change this for the player to be able to jump higher
		self.jumping = False
		self.falling = False
		self.jump_direction = 0 #Direction determining if a player rises or falls in the jump
		self.hp = 100
		self.physics = True
		self.dynamic = True

	@property
	def can_move(self):
		"""Determines whether the player is allowed to move
		Return value:
			True on success, False on failure"""
		return self.movetimer.elapsed >= self.movetime

	@property
	def can_jump(self):
		"""Determines whether a player can jump.
		Return Value:
			True on success, False on failure"""
		return not self.jumping and not self.falling

	@property
	def is_jumping(self):
		"""Determines whether the player is jumping"""
		return self.jumping

	@property
	def is_falling(self):
		"""Determines whether the player is falling
		Return Value:
			True on success, False on failure"""
		return self.falling

	def move(self, val):
		"""Moves the player.
		Parameters:
			val (int, 1 <= 4): The value determining the direction the player should move
		Return Value:
			None"""
		self.movetimer.restart()
		self.update_movement(val)
		#Wall detection and platform checking should go here
		#We should only trigger my sudo code if a wall was encountered
		#if self.rect.x and self.rect.y == wall
			#if val <= 2: val += 2
			#else: val -= 2
			#self.update_coordinates(val)
		print(self.rect.x, self.rect.y)

	def update_movement(self, val):
		"""Updates the player's movement
		Parameters:
			val (int, 1 <= 4): Forces will be applied to the player
		Return Value:
			None"""
		#Applies force to the players physical body
		dx, dy = 0, 0
		if val == 1 and not self.is_falling:
			 dy += 1
			 self.jumping = True
		elif val == 2: dx += 1
		elif val == 4: dx -= 1

		self.body.ApplyLinearImpulse(impulse=(dx*self.body.mass*2, dy*self.body.mass*6), point=(self.body.position.x, self.body.position.y), wake=True)

	def update(self):
		"""Calls the player internal functions
		Return Value:
			None"""
		#Uncomment this only when you replaced all of my sudo code with the actual deal and only want to test if you did it properly
		#self.jumploop()
		#self.fallingloop()

		if self.body.linearVelocity.y != 0:
			self.falling = True
		else:
			self.falling = False
			self.jumping = False

		if self.is_falling: print("Falling")
		if self.is_jumping: print("Jumping")

	def collisionBegin(self, gameObject):
		print("Started Touching: "+type(gameObject).__name__)

	def collisionEnd(self, gameObject):
		print("Stopped Touching: "+type(gameObject).__name__)

	def hit(self, value):
		"""Hits, or heals, the player, depending on the value
		Parameters:
			Value (int): How much damage we should hit the player for, can be positive or negative, negative will hurt and positive will heal
		Return Value:
			None"""
		self.hp += value

	def jump(self):
		"""Initiates the jumping sequence for the player
		Return Value:
			None"""
		self.jumptimer.restart()
		self.min_h = self.rect.y
		self.max_h = self.min_h + self.jump_h

	def land(self):
		"""Lands the player
		Return Value:
			None"""
		#If we wish for the player to take damage, this is the place to do so.
		#I know you mentioned using the real physics engine, but I don't think we will need such a level of complexity
		#I do think it will be cool, though.
		#I can always be persuaded to change my mind, too.
		self.jumping = False
		self.falling = False

	def jumploop(self):
		"""Updates the player's jumping status, returns if player is not jumping
		Return Value:
			None"""
		self.jump_dir = 0
		if not self.is_jumping: return
		if self.jumptimer.elapsed >= self.jumptime:
			self.jumptimer.restart()
			if self.jump_dir == 0:
				if self.rect.y < self.max_h:
					self.rect.y += 1
					#Wall and platform detection code should go here
					#Basically should look like this:
					#if self.x and self.y == wall, self.jump_dir = 0
					#elif self.x and self.y == platform, self.land()
				else: self.jump_dir = 1
			else:
				if self.rect.y > self.min_h:
					self.rect.y -= 1
					#Same deal with the wall and platform detection code, you should probably put those in a function or something to save redundency
				#else:
					#You need to add in another wall and platform check here. This is the best way of doing this that I've found, as not adding it in could cause the user to land on air... after all, we can miss a platform while jumping.
					#ATTENSION!!! The line below should only be uncommented when you've implemented the platform./wall detection code
					#else:
						#self.jumping = False
						#self.falling = True

	def fallingloop(self):
		"""Updates the player's status if they are falling, returns otherwise.
		Return Value:
			None"""
		if not self.is_falling: return
		if self.jumptimer.elapsed >= self.jumptime:
			#I typically do different values for jumping and falling, but this will do for now
			self.jumptimer.restart()
			#Must add a check for the player's y being greater than the minimum map boundary, land regardless of platforms or walls actually being there if y is equal to it
			#When the if statement will be added, this code will need to move up by 1 indention level (add 1 more tab)
			self.rect.y -= 1 #Probably want to change this if you want the speed of falling to increase
			#Wall and platform checking code should go here, a player must land if either one is encountered. Throughout my development, I have not figured out a solution for dealing with people landing on walls, so I always take the simplest approach, land them if there is no air on their tile
			#Call the landing function, self.land() to land the player as usual

	#Sudo code for the wall/platform checking function
	#def check_for_walls_and_platforms(self, x, y):
		#if map.get_tile_at(self.rect.x, self.rect.y) == platform: return 0
		#elif map.get_tile_at(self.rect.x, self.rect.y) == wall: return 1
		#return 2 because only air is found
		#This check should also be used in the movement function, though it should only be useful if the x and y the player moves to is a wall, in which case we will just bounce them back
