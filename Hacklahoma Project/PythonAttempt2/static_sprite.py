import pygame as pg
import os

class StaticSprite(pg.sprite.Sprite):
    """A class to manage a static sprite"""

    def __init__(self, game, img_path, x, y, x_size, y_size):
        """Create a static sprite with the image, img_path,
        centered at x, y, with the specified size"""

        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.images = []
        self.image = pg.image.load(img_path)
        self.image = pg.transform.scale(self.image, (x_size, y_size))
        self.rect = self.image.get_rect(center=(x, y))
        self.x_size, self.y_size = x_size, y_size
        self.x, self.y = x, y

    def render(self, surface):
        """Render the sprite to the surface"""
        surface.blit(self.image, self.rect)
    
    def contains_point(self, x, y):
        """Returns true if the point (x, y) is inside the
        rect for the object"""

        if x < self.rect.left:
            return False
        if x > self.rect.right:
            return False
        if y < self.rect.top:
            return False
        if y > self.rect.bottom:
            return False
        return True