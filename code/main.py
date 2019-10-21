import pygame, player, sys, Camera, GameObjectHandler, Block, TMXMapHandler, pygame.key as pgk, pygame.locals as pl, Box2D

class Main:
 
 """The main class for the game"""
 def __init__(self):
  """Initializes the game and begins the execution of the app"""
  pygame.init()
  self.screen = pygame.display.set_mode((720, 640)) # initilize screen, and sets screen size
  pygame.display.set_caption("Testing stuff") 
  self.camera = Camera.Camera(self.screen) # creates an instance of the camera class
  self.player = player.Player(0, 0, "mario.PNG") #The player handler
  self.clock = pygame.time.Clock() # creates instance of clock class
  self.game_object_handler = GameObjectHandler.GameObjectHandler(TMXMapHandler.load_map('test_map.tmx') + [self.player])
  self.mainloop() #This should be replaced with the main menu when we can get it working

 def mainloop(self):
  """The main state of the game will be in this function"""
  while 1: #Same as while loop forever
   self.key_loop()
   self.camera.clear() # erase drawing
   self.game_object_handler.update()  # updates all sprites contained in group
   self.camera.set_pos(self.player.rect.x, self.player.rect.y)
   self.camera.draw(self.game_object_handler.get_images(), self.game_object_handler.get_rects())  # draws the sprites onto screen
   pygame.display.update() # apply changes
   self.clock.tick(60) #BPA reqs say the project must run at 60 FPS
   
 def key_loop(self):
  """Handles events done by the user such as key and mouse presses"""
  for event in pygame.event.get():
   if event.type == pygame.QUIT: #The user hit the close button
    pygame.quit()
    sys.exit()
   if event.type == pygame.KEYDOWN:
    if event.key == pl.K_q:
     pygame.quit()
     sys.exit()
  keylist = pgk.get_pressed()
  if self.player.can_move:
   if keylist[pl.K_UP]: self.player.move(1)
   elif keylist[pl.K_RIGHT]: self.player.move(2)
   elif keylist[pl.K_DOWN]: self.player.move(3)
   elif keylist[pl.K_LEFT]: self.player.move(4)

test = Main()