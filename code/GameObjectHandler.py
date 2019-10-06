import pygame

class GameObjectHandler:

    def __init__(self, gameobjects=None):
        self.gameobjects = gameobjects

    def update(self):
        for gameobject in self.gameobjects:
            gameobject.update()

    def get_images(self):
        images = []
        for gameobject in self.gameobjects:
            images.append(gameobject.image)
        return images

    def get_rects(self):
        rects = []
        for gameobject in self.gameobjects:
            rects.append(gameobject.rect)
        return rects