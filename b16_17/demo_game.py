import pygame # pip / pip3 install pygame

from pygame.locals import *

#? KHỞI TẠO GAME
pygame.init()

#? SETUP TÊN, CỬA SỔ (WINDOW), MÀU SẮC

pygame.display.set_caption("DEMO PYGAME") # tên game
DISPLAY_WINDOW = pygame.display.set_mode((800, 500)) # setup cửa sổ (chiều dài x chiều rộng) 

#? 1. KHỞI TẠO 1 MẶT PHẲNG
surface1 = pygame.Surface((150, 80))
surface1.fill((255, 0, 0))

surface2 = pygame.Surface((200, 180))
surface2.fill((0, 255, 0))

coor1 = surface1.get_rect(topleft=(0, 30))
coor2 = surface2.get_rect(topleft=(200, 30))

#? VÒNG LẶP GAME
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    DISPLAY_WINDOW.fill((255, 255, 255)) # màu sắc - set màu rgb
    
    DISPLAY_WINDOW.blit(surface1, coor1) # block item target - biến 1: mặt phẳng cần lắp đặt, biến 2: toạ độ
    DISPLAY_WINDOW.blit(surface2, coor2) # block item target - biến 1: mặt phẳng cần lắp đặt, biến 2: toạ độ
    
    #? GIÚP CHO MẶT PHẲNG QUAY LẠI
    if coor1.x >= 650:
        coor1.x = 0
    else:
        coor1.x += 4
    
    #? XỬ LÍ VA CHẠM
    if coor1.colliderect(coor2):
        surface1.fill((255, 255, 0))
    else:
        surface1.fill((255, 0, 0))
    
    pygame.display.update() # cập nhật state (trạng thái của game)
    pygame.time.Clock().tick(60) # FPS: tốc độ xử lí khung hình 

# CMD + SHIFT + P