import pygame

from pygame.locals import *

pygame.init()

pygame.display.set_caption("KYO GAME")

DISPLAY_WINDOW = pygame.display.set_mode((800, 500))

#? KHỞI TẠO NHÂN VẬT
player_surface = pygame.Surface((150, 105), pygame.SRCALPHA) # Làm background trong suốt
# player_surface = pygame.Surface((150, 105))

player_l_sprite = pygame.image.load("./img/kyo_left.png") # Hoạt ảnh di chuyển qua trái
player_r_sprite = pygame.image.load("./img/kyo_r.png") # Hoạt ảnh di chuyển qua phải

running = True

KYO_R_OPTIONS = {
    0: (0, 0, 150, 105),
    1: (150, 0, 150, 105),
    2: (290, 0, 150, 105),
    3: (430, 0, 150, 105),
    4: (570, 0, 150, 105),
    5: (720, 0, 150, 105)
}

KYO_L_OPTIONS = {
    0: (720, 0, 150, 105),
    1: (570, 0, 150, 105),
    2: (430, 0, 150, 105),
    3: (290, 0, 150, 105),
    4: (150, 0, 150, 105),
    5: (0, 0, 150, 105)
}

def animate(option, source, sprite):
    coordinates = source[option]
    player_surface.blit(sprite, (0, 0), coordinates)


#? SETUP ANIMATION CHO NHÂN VẬT
SPEED = 5
time_count = 0
option = 0


#? SETUP STATE (TRẠNG THÁI)
left = False
right = False
jump = False

source = KYO_R_OPTIONS
sprite = player_r_sprite

x = 200
y = 300

high = 20

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Tắt game!!!")
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_q:
                print("Nhấn Q để tắt game!!!")
                pygame.quit()
                
            if event.key == K_LEFT:
                left = True
                
            if event.key == K_RIGHT:
                right = True
                
            if event.key == K_UP:
                # hoạt động nhảy
                jump = True
                
        if event.type == KEYUP:
            if event.key == K_q:
                print("Nhấn Q để tắt game!!!")
                pygame.quit()
                
            if event.key == K_LEFT:
                left = False
                
            if event.key == K_RIGHT:
                right = False
                
            if event.key == K_UP:
                y -= 10
            
    if left:
        x -= 5
        time_count += 1
        source = KYO_L_OPTIONS
        sprite = player_l_sprite
        
    if right: 
        x += 5
        time_count += 1
        source = KYO_R_OPTIONS
        sprite = player_r_sprite
        
    #* C1
    # if jump:
    #     if y >= 60:
    #         y -= 10
    #     else: 
    #         jump = False
    # else:
    #     if y <= 150:
    #         y += 10
    
    #* C2
    if jump:
        # if event.type == KEYDOWN and event.key == K_UP:
        #     jump = True
        
        if high >= -20: # high = 30 -> 20 -> 10 -> 0
            y -= high 
            high -= 1 
        else:
            jump = False
            high = 20
                
            
    DISPLAY_WINDOW.fill((255, 255, 255))
    player_surface.fill((0, 0, 0, 0))
    
    if time_count <= SPEED:
        option = 5
    elif time_count <= SPEED * 2:
        option = 4
    elif time_count <= SPEED * 3:
        option = 3
    elif time_count <= SPEED * 4:
        option = 2
    elif time_count <= SPEED * 5:
        option = 1
    elif time_count <= SPEED * 6:
        option = 0
    
    if time_count > SPEED * 6:
        time_count = 0
    
    animate(option, source, sprite)
    
    DISPLAY_WINDOW.blit(player_surface, (x, y))
    
    pygame.display.update()
    pygame.time.Clock().tick(60)
    