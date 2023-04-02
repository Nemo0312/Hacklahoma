import pygame as pg
from states.state import State
import os
from widgets import Text, Button, Image, ImageButton, MultilineText

class Credits(State):
    """A class to manage the credits state"""

    def __init__(self, game):
        """Create an instance of credits"""
        credits = ["Lead Grapgic Designer & Moral Support: Lauren Rush", "Everything else: Noah Pursell"]
        State.__init__(self, game)
        self.background = Button(self.game, '', self.game.CENTER_W, self.game.CENTER_H, self.game.GAME_W, self.game.GAME_H, background_color='gray')
        self.txt_title = Text(self.game, "CREDITS: A special thanks to...", self.game.CENTER_W, 50)
        self.mltxt_credits = MultilineText(game, credits, self.game.CENTER_W, self.game.CENTER_H)
        self.btn_back = ImageButton(self.game, os.path.join(
                    self.game.assets_dir, 'close_icon.png'), 20, 20, 40, 40, action=self.btn_back_action)
    
    def render(self, surface):
        """Render credits onto surface"""
        self.background.render(surface)
        self.mltxt_credits.render(surface)
        self.btn_back.render(surface)
        self.txt_title.render(surface)
    
    def update(self, delta_time, actions):
        """Update display in response to actions"""
        self.btn_back.is_pressed(actions)
    
    def btn_back_action(self):
        """Action for the back button --> takes user back to title page"""
        self.exit()