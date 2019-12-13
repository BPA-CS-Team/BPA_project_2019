import pygame
import pygame.key as pgk
import pygame.locals as pl

from GameEngine import Button


class UIElementManager:

    def __init__(self, surface):
        self.surface = surface
        self.elements = []
        self.click = 0
        self.button_list = []
        self.focused_button_index = -1
        self.last_key = None

    def update(self):

        if self.button_list:
            keys = pgk.get_pressed()
            if keys[pl.K_TAB] == 1 and self.last_key != pl.K_TAB:
                self.focused_button_index += 1
                self.last_key = pl.K_TAB

                if self.focused_button_index >= len(self.button_list):
                    self.focused_button_index = 0

                print(self.button_list[self.focused_button_index].name)
            if keys[pl.K_RETURN] == 1 and self.focused_button_index > -1 and self.last_key != pl.K_RETURN:
                self.button_list[self.focused_button_index].clicked_on(1)
                self.last_key = pl.K_RETURN

            if not keys[pl.K_TAB] and not keys[pl.K_RETURN]:
                self.last_key = None

        for element in self.elements:
            if element.visible:
                element.update()
                self.surface.blit(element.image, element.rect)

                if self.click != 0 and element.rect.collidepoint(pygame.mouse.get_pos()):
                    element.clicked_on(self.click)

    def add(self, element):
        element.ui_element_manager = self
        self.elements.append(element)
        self.button_list = self.get_ui_elements_of_type(Button)

    def get_ui_elements_of_type(self, type_of):

        """
        returns a list of all game objects of a specified type
        """
        elements = []
        for element in self.elements:
            if isinstance(element, type_of):
                elements.append(element)
        return elements
