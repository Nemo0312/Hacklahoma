import pygame as pg
from states.state import State
import os
from widgets import Text, Button, Image, ImageButton, MultilineText
from dynamic_sprite import DynamicSprite
from player_sprite import PlayerSprite
from static_sprite import StaticSprite
from states.news_room import NewsRoom

class Courtyard(State):
    """A class to manage the courtyard state"""

    def __init__(self, game):
        """Create an instance of Courtyarrd"""
        State.__init__(self, game)

        self.background = Image(self.game,
                                os.path.join(self.game.assets_dir, 'courtyard_background.png'),
                                self.game.SCREEN_WIDTH / 2,
                                self.game.SCREEN_HEIGHT / 2,
                                self.game.SCREEN_WIDTH,
                                self.game.SCREEN_HEIGHT)
        
        self.galactic_news_network = StaticSprite(self.game,
                                os.path.join(self.game.assets_dir, "galactic_news_network_building.png"),
                                self.game.SCREEN_WIDTH / 2 + 20,
                                140,
                                550,
                                550)
        
                                

        self.player = PlayerSprite(self.game,
                               self.game.SCREEN_WIDTH / 2,
                               self.game.SCREEN_HEIGHT / 2,
                               )
        
        self.info_message = MultilineText(self.game,
                                          ['Welcom to Corscant,  Jawa Bloom! We have head a lot about you! As our newest hacker and news reporter',
                                           'for the Galactic News Netowrk, we are sure that your ability to hack the empires media',
                                           'will enable us to stop the flood of Imperial Propaganda, and tell the citizens of the Galaxy the truth about the Galactic Civil War!',
                                           'Feel free to begin you work as soon as possible by going into the control room at the top of the screen!'],
                                           self.game.SCREEN_WIDTH / 2,
                                           self.game.SCREEN_HEIGHT - 100,
                                           font_size=24,
                                           background=True)
    
    def render(self, surface):
        """Render page onto surface"""
        self.background.render(surface)
        self.galactic_news_network.render(surface)
        self.player.render(surface)
        self.info_message.render(surface)
    
    def update(self, delta_time, actions):
        """Update the state based on the elapsed time and the 
        actions that are occuring
        """
        if self.galactic_news_network.contains_point(self.player.center_point['x'], self.player.center_point['y'] + 400):
            self.player.go_to(self.game.SCREEN_WIDTH / 2, self.game.SCREEN_HEIGHT / 2)
            NewsRoom(self.game).enter_state()
        self.player.update(delta_time, actions)


        
        

