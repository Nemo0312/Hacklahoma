from states import state
import pygame as pg
import os
import time
from states.title_page import TitlePage
import time


class Game:
    """A class that manages a game"""

    # Class variables

    def __init__(self):
        """Create a Game instance"""
        pg.init()
        self.GAME_W, self.GAME_H = 1_500, 1_000
        self.CENTER_W, self.CENTER_H = self.GAME_W / 2, self.GAME_H / 2
        self.game_canvas = pg.Surface((self.GAME_W, self.GAME_H))
        self.screen = pg.display.set_mode(
            (self.GAME_W, self.GAME_H), pg.RESIZABLE)
        self.running, self.playing = True, True
        self.actions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False,
            'action1': False,
            'action2': False,
            'start': False,
            'mouse pos': (0, 0),
            'mouse click': False
        }
        self.dt, self.prev_time = 0, 0
        self.states_stack = []
        self.load_assets()
        self.clock = pg.time.Clock()
        self.fps = 30

    @property
    def SCREEN_WIDTH(self):
        return self.screen.get_size()[0]

    @property
    def SCREEN_HEIGHT(self):
        return self.screen.get_size()[1]
    
    def load_assets(self):
        """Load game assets"""
        self.assets_dir = os.path.join('assets')
        print(self.assets_dir)
        self.font_dir = os.path.join(
            self.assets_dir, 'nasalization', 'nasalization-rg.otf')

    def init_game(self):
        """Set up settings for a game"""
        TitlePage(self).enter_state()

    def game_loop(self):
        self.init_game()
        while self.playing:
            # Update time
            self.update_time()
            # Get events
            self.get_events()
            # Update game
            self.update(self.dt, self.actions)
            # Render game
            self.render()

    def update_time(self):
        """Update dt"""
        # self.clock.tick returns in miliseconds, so divide by 1000 to get seconds
        self.dt = self.clock.tick(self.fps) / 1000

    def get_events(self):
        """Update action dictionary based on events"""
        # Reset some actions
        self.actions['mouse click'] = False

        self.actions['mouse pos'] = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                    self.rnning = False
                if event.key == pg.K_UP:
                    self.actions['up'] = True
                if event.key == pg.K_DOWN:
                    self.actions['down'] = True
                if event.key == pg.K_LEFT:
                    self.actions['left'] = True
                if event.key == pg.K_RIGHT:
                    self.actions['right'] = True

            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.actions['up'] = False
                if event.key == pg.K_DOWN:
                    self.actions['down'] = False
                if event.key == pg.K_LEFT:
                    self.actions['left'] = False
                if event.key == pg.K_RIGHT:
                    self.actions['right'] = False

            if event.type == pg.MOUSEBUTTONUP:
                self.actions['mouse click'] = True

    def render(self):
        """Render the game to the screen"""
        self.states_stack[-1].render(self.game_canvas)
        self.screen.blit(pg.transform.scale(self.game_canvas,
                         (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0, 0))
        pg.display.flip()

    def update(self, dt, actions):
        """Update the game in response to actions"""
        self.states_stack[-1].update(self.dt, actions)

    def reset_actions(self):
        self.actions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False,
            'action1': False,
            'action2': False,
            'start': False,
            'mouse pos': (0, 0),
            'mouse click': False
        }

    


if __name__ == '__main__':
    print('HELLO WORLD')
    game = Game()
    game.game_loop()
