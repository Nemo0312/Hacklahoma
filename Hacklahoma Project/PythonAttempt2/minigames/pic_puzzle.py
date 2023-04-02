import pygame, sys, os

import tkinter
from tkinter import filedialog
from tkinter import *
from random import shuffle
from pygame import event
import random



# gs - grid size
# ts - tile size
# ms - margin size

class SlidePuzzle:
    def __init__(self, gs, ts, ms):
        self.gs, self.ts, self.ms = gs, ts, ms
        self.tiles_len = (gs[0]*gs[1]) - 1
        self.tiles = [(x,y) for x in range(gs[0]) for y in range(gs[1])]
        self.tilesOG = [(x,y) for x in range(gs[0]) for y in range(gs[1])]    
        self.tilespos = {(x,y):(x*(ts+ms)+ms,y*(ts+ms)+ms) for y in range(gs[1]) for x in range(gs[0])}    
        self.font = pygame.font.Font(None, 120)    
        w,h = gs[0]*(ts+ms)+ms, gs[1]*(ts+ms)+ms
        #w,h = 1500, 1000
        
        root = Tk()
        #root.filename =  filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        #/home/nima-n/Documents/code/codez/Hacklahoma Project/Python Attempt
        # root.filename =  r'C:\Users\noaha\OneDrive - University of Oklahoma\Spring 2023\Hacklahoma\Hacklahoma Project\assets\view_finder.png'
        base_dir =r'C:\Users\noaha\OneDrive - University of Oklahoma\Spring 2023\Hacklahoma\Hacklahoma Project' 
        folders = []
        for folder in os.listdir():
            try:
                folders.append(int(folder))
            except:
                pass
        folder = folders[random.randint(0, len(folders) - 1)]
        pics = [pic for pic in os.listdir(os.path.join(base_dir, str(folder)))]
        pic = pics[random.randint(0, len(pics) - 1)]
        root.filename = os.path.join(base_dir, str(folder), pic)

        pic = pygame.image.load(root.filename)
        pic = pygame.transform.scale(pic, (w,h))
        root.destroy()
        
        self.images = []
        for i in range(self.tiles_len):
            x,y = self.tilespos[self.tiles[i]]
            image = pic.subsurface(x,y,ts,ts)
            self.images += [image] 
            
        self.temp = self.tiles[:-1]
        shuffle(self.temp)
        self.temp.insert(len(self.temp), self.tiles[-1])
        self.tiles = self.temp

    def getBlank(self): return self.tiles[-1]
    def setBlank(self, pos): self.tiles[-1] = pos
    
    opentile = property(getBlank, setBlank)
    
    def switch(self, tile):
        n = self.tiles.index(tile)
        self.tiles[n], self.opentile = self.opentile, self.tiles[n]
        if self.tiles == self.tilesOG:
            print("COMPLETE")
            return True
        return False

    
    def is_grid(self, tile): 
        return tile[0] >= 0 and tile[0] < self.gs[0] and tile[1] >= 0 and tile[1] < self.gs[1]
    
    def adjacent(self):
        x,y = self.opentile;
        return (x-1, y), (x+1,y), (x,y-1), (x,y+1)
    
    def update(self, dt):
        """
        # Find the tile mouse is on
        # Switch as long as open tile is adjacent
        """
        
        mouse = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()

        current_events = event.get()

        
        # Convert mouse position relative to tile position and check in grid
        if mouse[0]:
            tile = mpos[0]//self.ts, mpos[1]//self.ts
            
            if self.is_grid(tile): 
                if tile in self.adjacent():
                    done = self.switch(tile)
                    if done:
                        return True
        return False
    
    def draw(self, screen):
        for i in range(self.tiles_len):
            x,y = self.tilespos[self.tiles[i]]
            screen.blit(self.images[i], (x,y))            

def main(screen):
    # pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption("Upload Your Pic!!")
    # screen = pygame.display.set_mode((1000,1000))
    fpsclock = pygame.time.Clock()
    program = SlidePuzzle((3, 3), 330, 5)
    
    while True:
        dt = fpsclock.tick()/1000
        
        screen.fill((1,1,1))
        
        program.draw(screen)
        pygame.display.flip()
        done = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit();
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True

        if done:
            break       
        done = program.update(dt)
        if done: 
            break
