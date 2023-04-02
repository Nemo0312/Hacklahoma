import pygame as pg
from states.state import State
import os
from widgets import Text, Button, Image, ImageButton, MultilineText
from dynamic_sprite import DynamicSprite
from player_sprite import PlayerSprite
from static_sprite import StaticSprite
from minigames.memory_game import run_match_game
from minigames.maze import run_maze_game
from random import random
from minigames.pic_puzzle import main
import time
from pdf_generator import make_pdf, dropbox_upload


class NewsRoom(State):
    """A class to manage the news room state"""

    def __init__(self, game):
        """Create an instance of a news room"""
        State.__init__(self, game)

        self.background = Image(self.game, 
                                os.path.join(self.game.assets_dir, "news_room.png"), 
                                self.game.SCREEN_WIDTH / 2,
                                self.game.SCREEN_HEIGHT / 2,
                                self.game.SCREEN_WIDTH,
                                self.game.SCREEN_HEIGHT)
        self.exit_ramp = StaticSprite(self.game,
                                os.path.join(self.game.assets_dir, "stairs.png"), 
                                self.game.SCREEN_WIDTH / 2,
                                self.game.SCREEN_HEIGHT - 150,
                                300,
                                300)
        
        self.player = PlayerSprite(self.game,
                               self.game.SCREEN_WIDTH / 2,
                               self.game.SCREEN_HEIGHT / 2,
                               )
        
        self.computer = StaticSprite(self.game,
                               os.path.join(self.game.assets_dir, "computer.png"), 
                               self.game.SCREEN_WIDTH - 200,
                               200,
                               300,
                               300)
        self.view_finder = StaticSprite(self.game,
                               os.path.join(self.game.assets_dir, 'view_finder.png'), 
                               200,
                               200,
                               300,
                               300)
        self.success_message = Image(self.game,
                               os.path.join(self.game.assets_dir, "success_message.png"), 
                               self.game.SCREEN_WIDTH / 2,
                               self.game.SCREEN_HEIGHT / 2,
                               self.game.SCREEN_WIDTH,
                               self.game.SCREEN_HEIGHT)
        
        self.intro_message = MultilineText(self.game,
                               ['Welcome to the Galaxy News Network! The location where us rebels',
                                'hack into the Imperial News Network and upload the truth! In order',
                                'hack the Imperial Netowrk, go to your computer terminal in the top right of the room'],
                                self.game.SCREEN_WIDTH / 2,
                                self.game.SCREEN_HEIGHT * 0.8,
                                background=True)
        
        self.has_cords_message = MultilineText(self.game,
                               ['Awesome work hacking the empire, Jawa Bloom. I new you could do it!',
                                'Now, using you link into the Imperial News Network, use the view finder in the top left ',
                                'of the room to upload your news article. Make sure all file packets are transmited in the propper order!'],
                                self.game.SCREEN_WIDTH / 2,
                                self.game.SCREEN_HEIGHT * 0.8,
                                background=True)
        
        self.has_cords = False
        self.display_success = False
        
    def render(self, surface):
        """Render page onto surface"""
        
        self.background.render(surface)
        self.exit_ramp.render(surface)
        self.computer.render(surface)
        self.view_finder.render(surface)
        self.player.render(surface)
        if self.display_success:
            self.success_message.render(surface)
        if not self.has_cords and not self.display_success:
            self.intro_message.render(surface)
        if self.has_cords:
            self.has_cords_message.render(surface)


    def update(self, delta_time, actions):
        if self.display_success:
            index = make_pdf()
            # os.system(str(index) + '.pdf')
            dropbox_upload(index)

            self.display_success = False
        if self.exit_ramp.contains_point(self.player.center_point['x'], self.player.center_point['y']):
            self.exit()
        if self.computer.contains_point(self.player.center_point['x'], self.player.center_point['y']) and not self.has_cords:
            self.player.go_to(self.game.SCREEN_WIDTH / 2, self.game.SCREEN_HEIGHT / 2)

            if random() < 0.5:
                run_match_game(self.game.screen)
            else:
                run_maze_game(self.game.screen)
            self.game.reset_actions()
            self.has_cords = True
            self.player.go_to(self.game.SCREEN_WIDTH / 2, self.game.SCREEN_HEIGHT / 2)
        if self.view_finder.contains_point(self.player.center_point['x'], self.player.center_point['y']) and self.has_cords:
            main(self.game.screen)
            self.has_cords = False
            self.game.reset_actions()
            self.player.go_to(self.game.SCREEN_WIDTH / 2, self.game.SCREEN_HEIGHT / 2)
            self.display_success = True
            

        self.player.update(delta_time, actions)