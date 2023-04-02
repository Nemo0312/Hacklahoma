import pygame as pg

class Widget:
    """An abstract class for widgets"""
    def __init__(self, game):
        """Create an instance of widget"""
        self.game = game
    
    def render(self, surface):
        """Render the widget onto the surface"""
        pass

class Button(Widget):
    """A class to make a button in pygame"""

    def __init__(self, game, text, x, y, x_size, y_size, action=None, font_size=16, background_color='white'):
        """Create a button object centered at (x, y) with size (x_size, y_size)"""
        Widget.__init__(self, game)
        self.background_color = background_color
        self.text = Text(self.game, text, x, y, font_size=font_size)
        self.rect = pg.Rect(x - x_size / 2, y - y_size / 2, x_size, y_size)
        self.action = action
        self.x_range = (x - x_size / 2, x + x_size / 2)
        self.y_range = (y - y_size / 2, y + y_size / 2)

    def render(self, surface):
        """Render button onto the surface"""
        pg.draw.rect(surface, self.background_color, self.rect)
        self.text.render(surface)

    def is_pressed(self, actions):
        """Test if button is pressed, and react"""
        if actions['mouse click'] == False:
            return
        else:
            x_pos = actions['mouse pos'][0] * \
                self.game.GAME_W / self.game.SCREEN_WIDTH
            y_pos = actions['mouse pos'][1] * \
                self.game.GAME_H / self.game.SCREEN_HEIGHT
            if self.x_range[0] <= x_pos <= self.x_range[1] and self.y_range[0] <= y_pos <= self.y_range[1]:
                # Button has been pressed
                if self.action != None:
                    self.action()


class ImageButton(Widget):
    """A class to make a image button in pygame"""

    def __init__(self, game, image_url, x, y, x_size, y_size, action=None):
        """Create a image button object centered at (x, y) with size (x_size, y_size)"""
        Widget.__init__(self, game)
        self.x_size = x_size
        self.y_size = y_size
        self.x, self.y = x, y
        self.img = Image(self.game, image_url, x, y, x_size, y_size)
        self.rect = pg.Rect(x - x_size / 2, y - y_size / 2, x_size, y_size)
        self.action = action
        self.x_range = (x - x_size / 2, x + x_size / 2)
        self.y_range = (y - y_size / 2, y + y_size / 2)

    def render(self, surface):
        """Render image button onto the surface"""
        self.img.render(surface)

    def is_pressed(self, actions):
        """Test if button is pressed, and react"""
        if actions['mouse click'] == False:
            return
        else:
            x_pos = actions['mouse pos'][0] * \
                self.game.GAME_W / self.game.SCREEN_WIDTH
            y_pos = actions['mouse pos'][1] * \
                self.game.GAME_H / self.game.SCREEN_HEIGHT
            if self.x_range[0] <= x_pos <= self.x_range[1] and self.y_range[0] <= y_pos <= self.y_range[1]:
                # Button has been pressed
                if self.action != None:
                    self.action()

    def __repr__(self):
        return f'(x, y): ({self.x}, {self.y}), (x-size, y-size): ({self.x_size}, {self.y_size})'


class Text(Widget):
    """A class to make a text widget in pygame"""

    def __init__(self, game, text, x, y, font_size=16, color='black'):
        """Create a text object centered at (x, y)"""
        Widget.__init__(self, game)
        self.font = pg.font.Font(self.game.font_dir, font_size)
        self.text = self.font.render(text, False, color)
        self.text_rect = self.text.get_rect(center=(x, y))

    def render(self, surface):
        """Render text onto the surface"""
        surface.blit(self.text, self.text_rect)

class MultilineText(Widget):
    """A class to make a multiline text widget in pygame"""

    def __init__(self, game, text_lines, x, y, font_size=16, background=False, text_color='black', background_color='white', padding=10):
        """Create len(text_lines) lines of text centered at (x, y)"""
        Widget.__init__(self, game)
        self.font_size = 16
        self.num_lines = len(text_lines)
        self.font = pg.font.Font(self.game.font_dir, font_size)
        test_word_surface = self.font.render('TEST', False, 'black')
        word_height = test_word_surface.get_size()[1]
        total_height = word_height * self.num_lines
        self.texts = []

        height = y - total_height / 2 + word_height / 2
        initial_height = height
        for index, line in enumerate(text_lines):
            self.texts.append(Text(self.game, line, x, height, color=text_color, font_size=self.font_size))
            height += word_height
        rect_width = max([text.text_rect.width for text in self.texts]) + padding * 2
        rect_height = height - initial_height
        self.background = pg.Rect(x - rect_width / 2,
                                  y - rect_height / 2,
                                  rect_width,
                                  rect_height)
        self.render_background = background
        self.background_color = background_color
    
    def render(self, surface):
        """Render multiline text onto surface"""
        if self.render_background:
            pg.draw.rect(surface, self.background_color, self.background)
        for text in self.texts:
            text.render(surface)



class Image(Widget):
    """A class to make a image widget in pygame"""

    def __init__(self, game, image_url, x, y, x_size, y_size):
        """Create an image object centered at (x, y) of size (x_size, y_size)"""
        Widget.__init__(self, game)
        self.img = pg.image.load(image_url)
        self.img = pg.transform.scale(self.img, (x_size, y_size))
        self.img_rect = self.img.get_rect(center=(x, y))

    def render(self, surface):
        """Render image onto the surface"""
        surface.blit(self.img, self.img_rect)
