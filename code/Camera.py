import pygame

class Camera():

    def __init__(self, surface):
        self.surface = surface
        self.x = -surface.get_width() / 2
        self.y = -surface.get_height() / 2

    def set_surface(self, surface):
        self.surface = surface

    def clear(self, color=(0, 0, 0)):
        self.surface.fill(color)

    def draw(self, images, rects):
        for i in range(len(images)):
            rect = rects[i].copy()
            rect.x -= self.x
            rect.y -= self.y
            self.surface.blit(images[i], rect)

    def set_pos(self, x, y):
        self.x = x - self.surface.get_width() / 2
        self.y = y - self.surface.get_height() / 2

    def get_pos(self):
        return self.x, self.y