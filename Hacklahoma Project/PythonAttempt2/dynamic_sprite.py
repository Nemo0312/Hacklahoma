import pygame as pg
import os

class DynamicSprite(pg.sprite.Sprite):
    """A class to manage a sprite"""

    def __init__(self, game, img_path, x, y, x_size, y_size):
        """Create a dynamic sprite with image, img_path, centered at (x, y) with size (x_size, y_size)"""
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.images = []
        self.image = pg.image.load(img_path)
        self.image = pg.transform.scale(self.image, (x_size, y_size))
        self.rect = self.image.get_rect(center=(x, y))
        self.x_size, self.y_size = x_size, y_size
        self.x, self.y = x, y
        self.direction = "RIGHT"

    @property
    def center_point(self):
        x = self.x 
        y = self.y 

        return {'x': x,
                'y': y
                }
    
    def render(self, surface):
        """Render the sprite to the surface"""
        self.update_rect()
        surface.blit(self.image, self.rect)
    
    def move_by(self, x, y):
        """Move the sprite by (x, y)"""
        self.x +=x
        self.y += y
    
    def go_to(self, x, y):
        """Move center of sprite to (x, y)"""
        self.x = x
        self.y = y
    
    def set_direction(self, direction):
        """Set the direction the sprite should face, 'LEFT' or 'RIGHT """
        if direction != self.direction:
            self.image = pg.transform.flip(self.image, True, False)
        self.direction = direction
    
    def update(self, delta_time, actions):
        """Update display in response to actions"""
    
    def update_rect(self):
        """Update rect to be centered on (self.x, self.y)"""
        self.rect = self.image.get_rect(center=(self.x, self.y))