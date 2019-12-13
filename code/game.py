from GameEngine import *
from player import Player


class Game(GameState):
    """
    is game state of the game
    """

    def __init__(self, screen):
        """
        create game references does not initialize
        :param screen:
        """
        GameState.__init__(self)

        self.screen = screen
        self.camera = None
        self.game_object_handler = None
        self.player = None
        self.label = None
        self.button = None

    def start(self):
        """
        starts the game, by initializing game parameters
        """
        self.camera = Camera(self.screen)  # creates an instance of the camera class
        self.game_object_handler = GameObjectHandler(
            tmxmaphandler.load_map('Assets/test_map.tmx'))
        self.player = self.game_object_handler.get_game_object_of_type(Player)
        self.camera.set_pos(self.player.rect.x, self.player.rect.y)
        self.button = Button('reset player button', text='Reset Player', background=(255, 255, 255),
                             command=self.kill_player, position=(0, 50))
        self.label = Label('player position', 'Player x:0 y:0', (255, 255, 255))
        self.ui_element_manager.add(self.label)
        self.ui_element_manager.add(self.button)

    def update(self):
        """
        updates this specific game state, such as camera and game object handler, and runs game logic
        """
        self.game_object_handler.update()  # updates all sprites contained in group
        pos = self.camera.get_pos()
        self.camera.set_pos(pos[0] + 0.01 * (self.player.rect.x - pos[0]),
                            pos[1] + 0.01 * (self.player.rect.y - pos[1]))
        # self.camera.set_pos(pos[0] + 1.5, pos[1] + 0.01 * (self.player.rect.y - pos[1]))
        self.camera.draw(self.game_object_handler.get_images(),
                         self.game_object_handler.get_rects(),
                         self.game_object_handler.get_angles())  # draws the sprites onto screen
        self.label.set_label('Player x:' + str(self.player.rect.x) + " y:" + str(self.player.rect.y))

        if self.player.rect.right < self.camera.x:
            self.player.dead = True

        if self.player.dead:
            self.game_state_manager.change_state(Game(self.screen))

    def kill_player(self):
        self.player.dead = True

    def exit(self):
        """
        destroys instances of camera, player, game_object_handler
        """
        del self.camera
        del self.player
        self.game_object_handler.exit()
        del self.game_object_handler
