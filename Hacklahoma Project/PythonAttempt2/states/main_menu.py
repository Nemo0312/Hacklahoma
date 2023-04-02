import pygame as pg
from states.state import State
import os
from widgets import Text, Button, Image, ImageButton
from states.settings import Settings


class MainMenu(State):
    """A class to manage the main menu state"""

    def __init__(self, game):
        """Create an instance of MainMenu"""
        State.__init__(self, game)
        
        

    def render(self, surface):
        """Render main menu onto surface"""
        surface.blit
        self.btn_red.render(surface)
        self.btn_blue.render(surface)
        self.btn_settings.render(surface)
        self.btn_back.render(surface)

    def update(self, delta_time, actions):
        """Update display in response to actions"""
        self.btn_back.is_pressed(actions)
        self.btn_settings.is_pressed(actions)

    def btn_back_action(self):
        """Action for the back button --> takes user back to title page"""
        self.exit()
    
    def btn_settings_action(self):
        """Action for the settings button --> opens the settings page"""
        Settings(self.game).enter_state()
        print("I RAN")

