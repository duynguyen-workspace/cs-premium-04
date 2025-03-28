import pygame
from pygame.locals import *

import json

from mummy_graph import Graph

#? PHƯƠNG THỨC LOAD + READ DATA TỪ FILE JSON
with open("./assets/map.json", "r") as file:
    map_data = json.load(file)


def get_key(X, Y):
    for item in map_data:
        if item["X"] == X and item["Y"] == Y:
            return item["key"]


def get_pos(key):
    return {"X": map_data[key]["X"], "Y": map_data[key]["Y"]}

#? KHỞI TẠO MAP
graph = Graph(6, 6)
graph.add_rectangle_vertex() # Thêm 36 nút
graph.add_rectangle_edges() # Thêm cạnh cho 36 nút của bản đồ

#? KHỞI TẠO GAME
pygame.init()
pygame.display.set_caption("Mummy Maze")

#? TẠO WINDOW
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

DISPLAY = pygame.display.set_mode((600, 600))

#? ASSETS
MAP_IMG = pygame.image.load("./assets/map.jpg")

# Player's Sprites
PLAYER_UP_IMG = pygame.image.load("./assets/player/player_up.png")
PLAYER_DOWN_IMG = pygame.image.load("./assets/player/player_down.png")
PLAYER_LEFT_IMG = pygame.image.load("./assets/player/player_left.png")
PLAYER_RIGHT_IMG = pygame.image.load("./assets/player/player_right.png")

# Mummy's Sprites
MUMMY_UP_IMG = pygame.image.load("./assets/mummy/mummy_up.png")
MUMMY_DOWN_IMG = pygame.image.load("./assets/mummy/mummy_down.png")
MUMMY_LEFT_IMG = pygame.image.load("./assets/mummy/mummy_left.png")
MUMMY_RIGHT_IMG = pygame.image.load("./assets/mummy/mummy_right.png")

#? CONSTANTS
SPRITES_OPTIONS = {
    0: (0, 0, 60, 60),
    1: (60, 0, 60, 60),
    2: (120, 0, 60, 60),
    3: (180, 0, 60, 60),
    4: (240, 0, 60, 60),
}

MAP_SURFACE = pygame.transform.scale(MAP_IMG, (600, 600))

SPEED = 5

#TODO: CLASS PLAYER - NHÂN VẬT NGƯỜI CHƠI
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = PLAYER_DOWN_IMG
        self.surface = pygame.Surface((100, 100))
        self.option = 0
        
    def animate(self):
        if self.option in SPRITES_OPTIONS:
            coords = SPRITES_OPTIONS[self.option]
            self.surface.blit(self.img, (20, 20), coords)
            
    def draw(self):
        DISPLAY.blit(self.surface, (self.x, self.y))
        
    def update(self, left, down, up, right):
        
        time_count = 0
        
        if time_count < SPEED:
            self.option = 0
        elif time_count < SPEED*2:
            self.option = 1
        elif time_count < SPEED*3:
            self.option = 2
        elif time_count < SPEED*4:
            self.option = 3
        elif time_count < SPEED*5:
            self.option = 4
        
        if time_count > SPEED*5:
            self.time_count = 0
        
        if left:
            self.img = PLAYER_LEFT_IMG
            self.x -= 100
            
        if right:
            self.img = PLAYER_RIGHT_IMG
            self.x += 100
            
        if up:
            self.img = PLAYER_UP_IMG
            self.y -= 100
            
        if down:
            self.img = PLAYER_DOWN_IMG
            self.y += 100
            
        self.animate()
        
#TODO: CLASS MUMMY - NHÂN VẬT NPC XÁC UỚP
class Mummy:
    def __init__(self):
        self.x = 500
        self.y = 200
        self.img = MUMMY_DOWN_IMG
        self.surface = pygame.Surface((100, 100))
        self.option = 0
        
    def animate(self):
        if self.option in SPRITES_OPTIONS:
            coords = SPRITES_OPTIONS[self.option]
            self.surface.blit(self.img, (20, 20), coords)
            
    def draw(self):
        DISPLAY.blit(self.surface, (self.x, self.y))
        
    def update(self, left, down, up, right):
        
        time_count = 0
        
        if time_count < SPEED:
            self.option = 0
        elif time_count < SPEED*2:
            self.option = 1
        elif time_count < SPEED*3:
            self.option = 2
        elif time_count < SPEED*4:
            self.option = 3
        elif time_count < SPEED*5:
            self.option = 4
        
        if time_count > SPEED*5:
            self.time_count = 0
        
        if left:
            self.img = MUMMY_LEFT_IMG
            self.x -= 100
            
        if right:
            self.img = MUMMY_RIGHT_IMG
            self.x += 100
            
        if up:
            self.img = MUMMY_UP_IMG
            self.y -= 100
            
        if down:
            self.img = MUMMY_DOWN_IMG
            self.y += 100
            
        self.animate()

#? VÒNG LẶP GAME
running = True

player = Player()
mummy = Mummy()

#? STATES
player_up, player_down, player_left, player_right = False, False, False, False

mummy_up, mummy_down, mummy_left, mummy_right = False, False, False, False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        if event.type == KEYDOWN:
            if event.key == K_UP:
                player_up = True
            if event.key == K_DOWN:
                player_down = True
            if event.key == K_LEFT:
                player_left = True
            if event.key == K_RIGHT:
                player_right = True
            
        if event.type == KEYUP:
            if event.key == K_UP:
                player_up = False
            if event.key == K_DOWN:
                player_down = False
            if event.key == K_LEFT:
                player_left = False
            if event.key == K_RIGHT:
                player_right = False
        
            
    #? CLEAR WINDOW
    DISPLAY.fill((0, 0, 0, 0))
    
    # Setup map 
    DISPLAY.blit(MAP_SURFACE, (0, 0))
    
    #? TẠO PLAYER VÀ MUMMY TRÊN GAME
    player.draw()
    mummy.draw()
    
    #? CẬP NHẬT TRẠNG THÁI CỦA NHÂN VẬT
    player.update(up=player_up, down=player_down, left=player_left, right=player_right)
    mummy.update(up=mummy_up, down=mummy_down, left=mummy_left, right=mummy_right)
    
    #? CẬP NHẬT TRẠNG THÁI GAME
    pygame.display.update()
    pygame.time.Clock().tick(60)
    

pygame.quit()