import pygame as pg
from states.state import State
from states.main_menu import MainMenu
from states.courtyard import Courtyard
import os
from widgets import Text, Button, Image, ImageButton, MultilineText



class TitlePage(State):
    """A class to manage the title state"""

    def __init__(self, game):
        """Create an instance of TitlePage"""
        State.__init__(self, game)
        self.background = Image(self.game, os.path.join(self.game.assets_dir, 'media_stikes_hack.png'),
                                self.game.CENTER_W, self.game.CENTER_H, self.game.GAME_W, self.game.GAME_H)
        self.btn_start = Button(self.game, "Start Game", self.game.GAME_W / 2, self.game.GAME_H / 1.5,
                                self.game.GAME_W / 3, self.game.GAME_W / 15, action=self.btn_start_action)
        self.description = MultilineText(self.game, 
                                         ['Utilize your hacking skills to overide Imperial Propaganda, '
                                          'and publish the truth,  in order to inpsire the galaxy to',
                                          'fight for freedom!'],
                                          self.game.SCREEN_WIDTH / 2, 
                                          self.game.SCREEN_HEIGHT / 2 + 50,
                                          font_size=50,
                                          text_color='yellow')

    def render(self, surface):
        """Render title page onto surface"""
        self.background.render(surface)
        self.btn_start.render(surface)
        self.description.render(surface)

    def update(self, delta_time, actions):
        """Update display in response to actions"""
        self.btn_start.is_pressed(actions)

    def btn_start_action(self):
        """Action for the start button --> add main menu state to state stack"""
        Courtyard(self.game).enter_state()
