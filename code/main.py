import pygame
import pygame.locals as pl
import sys
from mainmenu import MainMenu
from GameEngine import GameStateManager


class Application:
    """
    the main class
    """

    def __init__(self):
        """
        initializes main game paremeters
        """
        pygame.init()
        # Initialize screen, and sets screen size
        self.surface = pygame.display.set_mode(size=(720, 640), flags=pygame.DOUBLEBUF)
        pygame.display.set_caption('Testing Game')
        self.game_state_manager = GameStateManager(self.surface, MainMenu(self.surface))
        self.clock = pygame.time.Clock()  # Creates instance of clock class

    def main_loop(self):
        """
        Main loop of the game
        """
        while True:  # Same as while loop forever
            self.check_events()
            self.game_state_manager.update()
            pygame.display.flip()  # Apply changes
            pygame.display.get_surface().fill((0, 0, 0))
            self.clock.tick(60)  # BPA requirements say the project must run at 60 FPS

    def check_events(self):
        """Handles events done by the user such as key and mouse presses"""
        self.game_state_manager.current_state.ui_element_manager.click = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # The user hit the close button
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                self.game_state_manager.current_state.ui_element_manager.click = event.dict['button']

            if event.type == pygame.KEYDOWN:
                if event.key == pl.K_q:
                    pygame.quit()
                    sys.exit()


app = Application()
app.main_loop()
