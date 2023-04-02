 
import os
import sys
import random
import pygame
 
 
# Class for the orange dude
def run_maze_game(screen):
    class Player(object):
        
        def __init__(self):
            self.rect = pygame.Rect(230, 330, 16, 16)
    
        def move(self, dx, dy):
            
            # Move each axis separately. Note that this checks for collisions both times.
            if dx != 0:
                self.move_single_axis(dx, 0)
            if dy != 0:
                self.move_single_axis(0, dy)
        
        def move_single_axis(self, dx, dy):
            
            # Move the rect
            self.rect.x += dx
            self.rect.y += dy
    
            # If you collide with a wall, move out based on velocity
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if dx > 0: # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                    if dx < 0: # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                    if dy < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom
    
    # Nice class to hold a wall rect
    class Wall(object):
        
        def __init__(self, pos):
            walls.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
    
    # Initialise pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    # pygame.init()
    
    # Set up the display
    pygame.display.set_caption("Get to the red square!")
    # screen = pygame.display.set_mode((1500, 1000))
    
    clock = pygame.time.Clock()
    walls = [] # List to hold the walls
    player = Player() # Create the player
    
    # Holds the level layout in a list of strings.
    level1 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                             W                                     WW",
    "W   WWWWWWW   WWWWWWWWWWWWW   W   WWWWWWWWWWWWWWWWWWWWWW   WWWWWWW   W",
    "W   W     W               W   W                         W         WWWW",
    "W   W     W   WWWWWWWWW   W   W   WWWWWWWWWWWWWWWWWWWWW   WWWWWWW   WW",
    "W   W     W   W         W   W   W                             W   WWWW",
    "W   WWWWWWW   W   WWW   W   W   W   WWWWWWWWWWWWWWWWWWWWWWW   W   WWWW",
    "W             W   W   W   W   W   W                     W   W   WWWWWW",
    "W   WWWWWWWWWWW   W   W   W   W   WWWWWWWWWWWWWWWWWWWWWW   W   W   WWW",
    "W                 W   W   W   W                             W   WWWWWW",
    "W   WWWWWWWWWWWWWWWWW   W   W   WWWWWWWWWWWWWWWWWWWWWWWWW   W   W   WW",
    "W                       W   W                             W   W   WWWW",
    "W   WWWWWWWWWWWWWWWWWWWWWW   WWWWWWWWWWWWWWWWWWWWWW   WWWWWWW   W   WW",
    "W                                       W         W           W   WWWW",
    "W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W   WWW   W   WWWWWWWWW   WW",
    "W                                   W   W   W     W   W             WW",
    "W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W   W   W     W   W   WWWWWWWWWW",
    "W                               W   W   W   W     W   W             WW",
    "W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W   W   WWWWWWW   W   WWWWWWW  W",
    "W                                   W   W             W           WWWW",
    "W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W   WWWWWWWWWWWWWWWWW   WWWWWW",
    "W                                                                 WWWW",
    "W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W   WWWWWWWWWWW   WW",
    "W                                               W               WWWWWW",
    "W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W   WWWWWWWWWWW   WW",
    "W                                                   E             WWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",

    ]
    level2 =[
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W           W           W       W               W                   W",
    "W   WWWWW   W   WWWWW   W   W   W   WWWWWWWWW   W   WWWWWWWWWWWWW   W",
    "W       W   W       W   W   W   W           W   W   W           W   W",
    "W   W   W   W   W   W   W   W   W   WWWWW   W   W   W   WWWWW   W   W",
    "W   W   W   W   W   W   W   W   W           W   W   W       W   W   W",
    "W   W   W   W   W   W   W   W   WWWWWWWWW   W   W   WWWWW   W   W   W",
    "W   W   W   W   W   W   W   W               W   W       W   W   W   W",
    "W   W   W   W   W   W   W   WWWWWWWWWWWWW   W   WWWWW   W   W   W   W",
    "W   W   W           W   W               W           W   W           W",
    "W   W   WWWWW   W   W   WWWWWWWWWWWWW   W   WWWWW   W   W   WWWWWWWWW",
    "W           W   W           W           W       W                   W",
    "W   WWWWW   W   W   WWWWW   W   WWWWW   W   W   W   WWWWWWWWWWWWW   W",
    "W       W   W   W       W   W       W   W   W               W       W",
    "W   W   W   W   W   W   W   W   W   W   W   W   WWWWWWWWW   W   W   W",
    "W   W   W   W   W   W   W   W   W   W   W   W           W   W   W   W",
    "W   W   W   W   W   W   W   W   W   W   W   WWWWW   W   W   W   W   W",
    "W   W   W   W   W   W   W   W   W   W           W   W   W   W   W   W",
    "W   W   W   W   W   W   W       W   WWWWWWWWW   W   W       W   W   W",
    "W   W   W   W   W   W   W   W   W               W   W   W   W   W   W",
    "W   W   W   W   W   W   W   W   WWWWWWWWWWWWW   W   W   W   W   W   W",
    "W   W   W   W   W   W   W   W                   W   W   W   W   W   W",
    "W   WWWWW   W   W   WWWWWWWWWWWWWWWWWWWWWWW   W   W   W   W       W W",
    "W           W                               W       W   W   W    E  W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"

    ]
    level3 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W               W                   W                           W   W",
    "W   WWWWWWWWW   W   WWWWWWWWWWWWW   W   WWWWWWWWWWWWWWWWWWWWW   W   W",
    "W   W       W   W   W           W   W                       W   W   W",
    "W   W   W   W   W   W   WWWWW   W   W   WWWWWWWWWWWWWWWWWWW   W   W W",
    "W   W   W   W   W   W           W   W                       W   W   W",
    "W   W   W   WWWWWWWWW   WWWWWWWWW   WWWWWWWWWWWWWWWWWWWWW   W   W   W",
    "W   W   W               W                                   W   W   W",
    "W   W   WWWWWWWWWWWWWWWWW   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W   W W",
    "W   W                       W                           W   W   W   W",
    "W   WWWWWWWWWWWWWWWWWWWWW   W   WWWWWWWWWWWWWWWWWWWWWWW   W   W   W W",
    "W               W           W                       W   W   W   W   W",
    "W   WWWWWWWWW   W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W   W   W   W W",
    "W   W       W   W                                   W   W   W   W   W",
    "W   W   W   W   WWWWWWWWW WWWWWWWWWWWWWWWWWW WWWWWW   W   W   W   W W",
    "W   W   W   W                           W           W   W   W   W   W",
    "W   W   W   WWWWWWWWWWWWWWWWWWWWWWW   W   WWWWWWWWWWWWWWWWW   W   W W",
    "W   W                           W   W                       W   W   W",
    "W   WWWWWWWWWWWWWWWWWWWWWWW   W   W   WWWWWWWWWWWWWWWWWWW   W   W   W",
    "W                           W   W                           W   W   W",
    "W   WWWWWWWWWWWWWWWWWWWWW   W   W   WWWWWWWWWWWWWWWWWWW   W   W   W W",
    "W                       W   W   W                    E  W   W   W   W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"


    ]
    level4 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                                               WWWWW",
        "W   WWWWWWWWWWW   WWWW   WWWWWWWWWWWWWWWWWWWWW   WWWWWWWWWWW   WWWWWW",
        "W   W         W   W  W   W                     W         W   WWWWWWWW",
        "W   W   WWW   W   W  W   WWWWWWWWWWWWWWWWWWWWW   W   WWW   W   WWWWWW",
        "W   W   W     W   W  W                           W   W   W   WWWWWWWW",
        "W   W   W     W   W  WWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W   W   WWWWWWWW",
        "W   W   W     W   W                                   W   W   WWWWWWW",
        "W   W   WWWWWWW   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   WWWWWWW   WWWWW",
        "W   W                                             W         WWWWWWWWW",
        "W   W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   WWWWWWWWWWWWW   WWWWW",
        "W   W   W                                       W               WWWWW",
        "W   W   W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W   WWWWWWWWWWW   WWW",
        "W   W   W   W                                 W   W             WWWWW",
        "W   W   W   W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W   WWWWWWWWWWWWW",
        "W   W   W   W   W                                             WWWWWWW",
        "W   W   W   W   W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWW   WWWWWWWWWWW   WWW",
        "W   W   W   W   W   W                             W             WWWWW",
        "W   W   W   W   W   W   WWWWWWWWWWWWWWWWWWWWWWW   W   WWWWWWWWWWW   W",
        "W   W   W   W   W   W   W                                       WWWWW",
        "W   W   W   W   W   W   W   WWWWWWWWWWWWWWWWWWWWW   WWWWWWWWWWW   WWW",
        "W   W   W   W   W   W   W   W                                 E WWWWW",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"

    ]
    level5=[
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                                        WWWWW",
    "W   WWWWWWWWWWWWW   WWWWWWWWWWWWW   WWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W             W                 W                         WWWW",
    "W   WWWWWWW   W   WWWWWWWWWWWWW   W   WWWWWWWWWWWWWWWWW   W WW",
    "W           W   W             W   W                     W  WWW",
    "W   WWWWW   W   W   WWWWWWW   W   W   WWWWWWWWWWWWWWW   W   WW",
    "W         W   W   W         W   W                 W   W   WWWW",
    "W   WWW   W   W   W   WWWWWWW   W   WWWWWWWWWWWWW   W   W  WWW",
    "W       W   W   W   W             W             W   W   WWWWWW",
    "W   WWW   W   W   W   WWWWWWW   W   W   WWWWWWWWWWW   W   WWWW",
    "W           W   W             W   W   W             W   WWWWWW",
    "W   WWWWW   W   WWWWWWWWWWWWW   W   W   W   WWWWWWW   W   WWWW",
    "W         W                   W   W   W   W       W   WWWWWWWW",
    "W   WWW   W   WWWWWWWWWWWWWWW W         W   W   W   W   WWWWWW",
    "W     W   W                   W   W   W   W   W   W   WWWWWWWW",
    "W   WWW   WWWWWWWWWWWWW   W   W   W   W   W   W   W   WWWWWWWW",
    "W   W                 W   W   W   W   W   W   W   W   WWWWWWWW",
    "W   W   WWWWWWWWWWWWWWW   W   W   W       W   W   W   WWWWWWWW",
    "W   W                     W       W   W   W   W   W   WWWWWWWW",
    "W   WWWWWWWWWWWWWWWWWWWWWWWWW   W   W       W   W   W   WWWWWW",
    "W                             W   W   W   W   W   W   WWWWWWWW",
    "W   WWWWWWWWWWWWWWWWWWWWWWW   W   W   W   W   W   W   WWWWWWWW",
    "W   W                     W   W   W   W   W   W   W   WWWWWWWW",
    "W   W   WWWWWWWWWWWWWWW   W   W   W   W   W   W   W   WWWWWWWW",
    "W   W   W             W   W   W   W   W       W   W   WWWWWWWW",
    "W   W   W   WWWWWWW   W   W   W   W   W   W       W   WWWWWWWW",
    "W   W   W   W       W   W   W   W   W   W   W   W   WWWWWWWWWW",
    "W   W   W   W   W   W   W   W   W   W   W   W E  W  WWWWWWWWWW",
    "W   W   W   W   W   W   W   W   W   W   W   W   W   WWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]

    levels = [level1, level2, level3, level4, level5]
    # Parse the level string above. W = wall, E = exit
    x = 200
    y = 300
    for row in levels[random.randint(0, len(levels) - 1)]:
        for col in row:
            if col == "W":
                Wall((x, y))
            if col == "E":
                end_rect = pygame.Rect(x, y, 16, 16)
            x += 16
        y += 16
        x = 200
    
    running = True
    while running:
        
        clock.tick(60)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
    
        # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2, 0)
        if key[pygame.K_RIGHT]:
            player.move(2, 0)
        if key[pygame.K_UP]:
            player.move(0, -2)
        if key[pygame.K_DOWN]:
            player.move(0, 2)
    
        # Just added this to make it slightly fun ;)
        if player.rect.colliderect(end_rect):
            # pygame.quit()
            # sys.exit()
            break
    
        # Draw the scene
        screen.fill((100, 105, 108))
        for wall in walls:
            pygame.draw.rect(screen, (0, 0, 0), wall.rect)
        pygame.draw.rect(screen, (188, 30, 34), end_rect)
        pygame.draw.rect(screen, (50, 8, 5), player.rect)
        #gfxdraw.filled_circle(screen, 255, 200, 5, (0,128,0))
        pygame.display.flip()
        clock.tick(360)
    
    # pygame.quit()