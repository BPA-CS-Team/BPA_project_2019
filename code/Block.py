import pygame, GameObject

class Block(GameObject.GameObject):
    """The player class that is going to be used inside the game"""

    def __init__(self, x, y, image):
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
        self.image = image

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.physics = True
        self.dynamic = False