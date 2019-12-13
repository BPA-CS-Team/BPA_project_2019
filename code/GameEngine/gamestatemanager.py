from GameEngine import UIElementManager


class GameStateManager:
    """
    handles the states of the games, such as main menu, or game its self
    """

    def __init__(self, surface, initial_state):
        self.surface = surface
        self.current_state = None
        self.setup_state(initial_state)

    def update(self):
        """
        updates the state of the game
        :param self: 
        :return: nothing
        """
        self.current_state.update()
        self.current_state.ui_element_manager.update()

    def change_state(self, new_state):
        """
        redefines the current_state
        :param self:
        :param new_state: state that is replacing the old state
        :return:
        """
        self.current_state.exit()
        self.setup_state(new_state)

    def setup_state(self, new_state):
        self.current_state = new_state
        self.current_state.game_state_manager = self
        self.current_state.ui_element_manager = UIElementManager(self.surface)
        self.current_state.start()
