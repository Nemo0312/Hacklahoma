import pygame as pg
import os
from dynamic_sprite import DynamicSprite

class PlayerSprite(DynamicSprite):
    """
    a class to represent the player
    """

    def __init__(self, game, x, y):
        super().__init__(game,
                        os.path.join(game.assets_dir, "main_character.png"),
                        x,
                        y,
                        200,
                        200)
        
        self.speed = 300
        self.update_rect()

    
    def update(self, delta_time, actions):
        """
        update the state of the player Sprite
        based on the change in time and the current actions
        """


        if actions['left'] and self.center_point['x'] > 0:
            self.x -= self.speed * delta_time
            self.set_direction("LEFT")
        if actions['right'] and self.center_point['x'] < self.game.GAME_W:
            self.x += self.speed * delta_time
            self.set_direction("RIGHT")
        if actions['up'] and self.center_point['y'] > 0:
            self.y -= self.speed * delta_time
        if actions['down'] and self.center_point['y'] < self.game.GAME_H:
            self.y += self.speed * delta_time
        
        self.update_rect()





