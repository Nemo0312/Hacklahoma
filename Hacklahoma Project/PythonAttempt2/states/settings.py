import pygame as pg
from states.state import State
import os
from widgets import Text, Button, Image, ImageButton
from states.credits import Credits

class Settings(State):
    """A class to manage the settings state"""

    def __init__(self, game):
        """create an instance of Settings"""
        State.__init__(self, game)
        self.btn_back = ImageButton(self.game, os.path.join(
            self.game.assets_dir, 'close_icon.png'), 20, 20, 40, 40, action=self.btn_back_action)
        self.btn_credits = Button(self.game, "Credits", self.game.CENTER_W, self.game.CENTER_H, 75, 20, action=self.btn_credits_action)
        self.background = Button(self.game, '', self.game.CENTER_W, self.game.CENTER_H, self.game.GAME_W, self.game.GAME_H, background_color='gray')
        self.txt_title = Text(self.game, "Settings:", self.game.CENTER_W, 50)   

    def render(self, surface):
        """Render Settings onto surface"""
        self.background.render(surface)
        self.txt_title.render(surface)
        self.btn_back.render(surface)
        self.btn_credits.render(surface)
    
    def update(self, delta_time, actions):
        """Update display in response to actions"""
        self.btn_back.is_pressed(actions)
        self.btn_credits.is_pressed(actions)
    
    def btn_back_action(self):
        """Action for the back button --> takes user back to title page"""
        self.exit()
    
    def btn_credits_action(self):
        """Action for the credits button --> takes user to the credits page"""
        Credits(self.game).enter_state()
        