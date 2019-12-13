import pygame


class Camera:

    def __init__(self, surface):
        """
        initializes variables for utilization throughout the class
        """
        self.surface = surface
        self.x = -surface.get_width() / 2
        self.y = -surface.get_height() / 2

    def set_surface(self, surface):
        """
        allows surface to be change
        """

        self.surface = surface

    def clear(self, color=(0, 0, 0)):
        """
         clears screen with a specified colour, the default colour is black
        """
        self.surface.fill(color)

    def draw(self, images, rects, angles):
        """
        draws images onto the surface
        """
        for i in range(len(images)):
            rect = rects[i].copy()
            rect.x -= self.x
            rect.y -= self.y
            self.blit_rotated_image(images[i].copy(), rect.topleft, angles[i])

    def blit_rotated_image(self, image, top_left, angle):
        """
        allows the image to be rotated
        """
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
        self.surface.blit(rotated_image, new_rect.topleft)

    def set_pos(self, x, y):
        """
        sets the position of the camera
        """
        self.x = x - self.surface.get_width() / 2
        self.y = y - self.surface.get_height() / 2

    def get_pos(self):
        """"
        returns the current position of the camera
        """
        x = self.x + self.surface.get_width() / 2
        y = self.y + self.surface.get_height() / 2
        return x, y
