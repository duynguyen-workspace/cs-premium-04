import pygame
from pygame.locals import *
import random
import math

#? KHỞI TẠO GAME
pygame.init()
pygame.display.set_caption("The Dinosaur Game")

#? 1. KHỞI TẠO WINDOW
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 550

DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
DISPLAY_BG = (30, 30, 30)

#? LOAD TÀI NGUYÊN GAME (SPRITES, MUSIC...)
IMG_DINO = pygame.image.load("./img/tRex.png")
IMG_GROUND = pygame.image.load("./img/ground.png")
IMG_CACTUS = pygame.image.load("./img/cactus.png")

FONT = pygame.font.Font(pygame.font.get_default_font(), 16)

DINO_OPTIONS = {
    0: (0, 0, 40, 43),
    1: (40, 0, 40, 43),
    2: (80, 0, 40, 43),
    3: (120, 0, 40, 43), # nhảy
    4: (160, 0, 55, 40), # ngồi (1)
    5: (215, 0, 55, 40) # ngồi (2)
}

CACTUS_OPTIONS = {
    0: (0, 0, 23, 46),
    1: (0, 0, 47, 46),
    2: (47, 0, 49, 46),
    3: (98, 0, 50, 43)
}

CACTUS_RANGE = {
    0: (450, 600),
    1: (650, 800),
    2: (900, 1100),
}

#? CONSTANTS - POSITION
X_DINO = 20
Y_DINO = WINDOW_HEIGHT - 200

HEIGHT_DINO_STAND = 43
HEIGHT_DINO_SIT = 40

WIDTH_DINO_STAND = 40
WIDTH_DINO_SIT = 55

Y_GROUND = Y_DINO + HEIGHT_DINO_STAND - 5
GROUND_WIDTH = 1200

X_SCOREBOARD = WINDOW_WIDTH - 150
Y_SCOREBOARD = 30

#? CONSTANTS - JUMP
JUMP_VELOCITY = 25
GRAVITY = 1.7

SPEED = 5

#TODO: CLASS KHỦNG LONG (DINO)
class Dino:
    def __init__(self):
        self.x = X_DINO
        self.y = Y_DINO
        self.img = IMG_DINO
        
        self.surface = pygame.Surface((WIDTH_DINO_STAND, HEIGHT_DINO_STAND), pygame.SRCALPHA)
        self.surface.blit(self.img, (0, 0))
        
        self.time_count = 0
        self.option = 2
        self.high = JUMP_VELOCITY
        self.jumping = False
        
        self.rect = self.surface.get_rect()
        
    def draw(self):
        DISPLAY.blit(self.surface, (self.x, self.y))    
        
    def animate(self):
        if self.option in DINO_OPTIONS:
            coords = DINO_OPTIONS[self.option]
            self.surface.blit(self.img, (0, 0), coords)  
            
    def update(self, up, down):
        #? KIỂM TRA TRẠNG THÁI DI CHUYỂN
        if down and up:
            up = False # khi ngồi -> k cho nhảy
        
        if up and down: 
            down = False # khi nhảy -> k cho ngồi
            
        #? CLEAR SURFACE KHỦNG LONG
        self.surface.fill((0, 0, 0, 0)) # opacity / alpha
        if down:
            self.surface = pygame.Surface((WIDTH_DINO_SIT, HEIGHT_DINO_SIT), pygame.SRCALPHA)
        else:
            self.surface = pygame.Surface((WIDTH_DINO_STAND, HEIGHT_DINO_STAND), pygame.SRCALPHA)
        
        self.time_count += 1
        
        # Kiểm tra khủng long đang đứng hoặc nhảy
        if self.jumping is False: 
            if self.time_count <= SPEED:
                self.option = 2
            elif self.time_count <= SPEED*2: 
                self.option = 1
            elif self.time_count <= SPEED*3:
                self.option = 0

            if self.time_count > SPEED*3:
                self.time_count = 0
                
            if up:
                self.option = 3
                self.jumping = True
                
            if down:
                self.option = 5
                
                if self.time_count <= SPEED:
                    self.option = 5
                elif self.time_count <= SPEED*2: 
                    self.option = 4
                
                if self.time_count > SPEED*2:
                    self.time_count = 0
                    
        else:
            if self.high >= -JUMP_VELOCITY:
                self.y -= self.high
                self.high -= GRAVITY # 20 gỉam dần -> -20
            else:
                self.y = Y_DINO
                self.high = JUMP_VELOCITY
                self.jumping = False
            
        self.animate()
        
    def update_rect(self):
        self.rect.topleft = (self.x, self.y)


#TODO: CLASS MẶT ĐẤT (GROUND)
class Ground:
    def __init__(self):
        self.x = 0
        self.y = Y_GROUND
        self.img = IMG_GROUND
        
    def draw(self):
        DISPLAY.blit(self.img, (self.x, self.y))
        DISPLAY.blit(self.img, (self.x + GROUND_WIDTH, self.y))
        
    def update(self):
        self.x -= SPEED
        
        # RESET VỊ TRÍ MẶT ĐẤT
        if self.x <= -GROUND_WIDTH: 
            self.x = 0

#TODO: CLASS CHƯỚNG NGẠI VẬT (CACTUS)
class Cactus:
    def __init__(self, min_range, max_range):
        self.x = random.randint(min_range, max_range)
        self.y = Y_DINO
        self.img = IMG_CACTUS
        
        self.surface_height = 46
        self.surface_width = 23
        
        self.option = random.randint(0, 3)
        
        self.surface = None
        self.time_spawn = 0
        
        self.rect = None
        
    def setup(self):
        
        if self.option == 1:
            self.surface_width = 47
        
        if self.option == 2:
            self.surface_width = 49
            
        if self.option == 3:
            self.surface_width = 50
            self.surface_height = 43
        
        self.surface = pygame.Surface((self.surface_width, self.surface_height), pygame.SRCALPHA)
        self.surface.blit(self.img, (0, 0), CACTUS_OPTIONS[self.option])
        self.rect = self.surface.get_rect()
    
    def draw(self):
        DISPLAY.blit(self.surface, (self.x, self.y))  
        
    def update_rect(self):
        self.rect.topleft = (self.x, self.y)
        
    def update(self):
        self.x -= SPEED

        # C1: Respawn theo thời gian 
        
        # C2: Reset x cho cactus
        if self.x <= -self.surface_width:
            self.option = random.randint(0, 3)
            self.setup()
            self.x = random.randint(50, 150) + WINDOW_WIDTH
        
# TODO: BẢNG ĐIỂM (SCOREBOARD):
class ScoreBoard:
    def __init__(self):
        self.x = X_SCOREBOARD
        self.y = Y_SCOREBOARD
        self.width = 100
        self.height = 20
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        
        self.score = 0
        
    def draw(self):
        DISPLAY.blit(self.surface, (self.x, self.y))
        
    def update(self, score):
        self.score = score 
        text = FONT.render(f"Score: {self.score}", True, (10, 10, 10))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.surface.fill((255,255,0))
        self.surface.blit(text, text_rect)
        
# TODO: BẢNG HIỂN THỊ THÔNG TIN (MESSAGEBOARD):
class MessageBoard:
    def __init__(self, x, y, message, width, height, text_color, bg_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_color = text_color
        self.bg_color = bg_color
        
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        self.message = message
        
    def draw(self):
        text = FONT.render(self.message, True, self.text_color)
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.surface.fill(self.bg_color)
        self.surface.blit(text, text_rect)
        DISPLAY.blit(self.surface, (self.x, self.y))

#? STATES
up = False
down = False

#? 2. VÒNG LẶP GAME
game_start = False
game_over = False
running = True
restart = False

ground = Ground()
dino = Dino()

cactus1 = Cactus(450, 600)
cactus2 = Cactus(700, 850)
cactus3 = Cactus(950, 1200)

scoreboard = ScoreBoard()
score = 0
highscore = 0 # đọc file

game_start_message = MessageBoard(x=WINDOW_WIDTH // 2 - 150, y=WINDOW_HEIGHT // 2 - 10, width=300, height=20, message="PRESS SPACEBAR TO START GAME", text_color=(30, 30, 30), bg_color=(0, 255, 255))

game_over_message_1 = MessageBoard(x=WINDOW_WIDTH // 2 - 50, y=100, width=100, height=20, message="GAME OVER", text_color=(255, 0, 0), bg_color=(30, 30, 30))
game_over_message_2 = MessageBoard(x=WINDOW_WIDTH // 2 - 150, y=120, width=300, height=20, message="PLEASE TYPE R TO RESTART GAME!", text_color=(100, 255, 100), bg_color=(30, 30, 30))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key == K_UP:
                up = True
            
            if event.key == K_DOWN:
                down = True
                
            if event.key == K_r:
                restart = True
            
            if event.key == K_SPACE:
                game_start = True
        
        if event.type == KEYUP:
            if event.key == K_UP:
                up = False
            
            if event.key == K_DOWN:
                down = False
            
    #? CLEAR DISPLAY
    DISPLAY.fill(DISPLAY_BG)  
    
    if game_start is False:
        game_start_message.draw()
    else:
        #? VẼ INSTANCES (NHÂN VẬT / CHƯỚNG NGẠI VẬT ...)
        ground.draw()
        
        dino.draw()
        
        cactus1.setup()
        cactus1.draw()
        
        cactus2.setup()
        cactus2.draw()
        
        cactus3.setup()
        cactus3.draw()
        
        scoreboard.draw()
        
        if game_over is False:
            
            #? CẬP NHẬT STATES THEO THỜI GIAN
            dino.update(up, down)
            
            ground.update()
            
            cactus1.update()
            cactus2.update()
            cactus3.update()
            
            dino.update_rect()
            
            cactus1.update_rect()
            cactus2.update_rect()
            cactus3.update_rect()
            
            #? TÍNH TOÁN ĐIỂM SỐ:
            score += 0.1
            display_score = math.floor(score)
            scoreboard.update(display_score)
            
            #? XỬ LÍ VA CHẠM:
            if dino.rect.colliderect(cactus1) or dino.rect.colliderect(cactus2) or dino.rect.colliderect(cactus3):
                print("Va Chạm")
                game_over = True
        else:
            game_over_message_1.draw()
            game_over_message_2.draw()
            
            # Restart game hay k:
            if restart == True:
                ground = Ground()
                dino = Dino()   

                cactus1 = Cactus(450, 600)
                cactus2 = Cactus(700, 850)
                cactus3 = Cactus(950, 1200)
                
                score = 0
                
                game_over = False
                restart = False
                
        
    
    #? CẬP NHẬT TRẠNG THÁI CỦA GAME
    pygame.display.update()
    pygame.time.Clock().tick(60)  

#? KẾT THÚC GAME
pygame.quit()

# ghi highscore
def write_highscore(new_score):
    try:
        # Đọc điểm highscore hiện tại từ file
        current_highscore = read_highscore()

        # So sánh điểm mới với điểm highscore hiện tại
        if new_score > current_highscore:
            with open("highscore.txt", "w") as file:
                file.write(str(new_score))
            print(f"🎉 New highscore: {new_score} points!")
        else:
            print(f"Your score: {new_score}. Try again to beat the highscore of {current_highscore}!")

    except Exception as e:
        print("Error writing highscore:", e)

# đọc điểm highscore
def read_highscore():
    try:
        with open("highscore.txt", "r") as file:
            highscore = file.read()
            return int(highscore)
    except FileNotFoundError:
        # Nếu file không tồn tại, trả về điểm mặc định là 0
        return 0
    except Exception as e:
        print("Error reading highscore:", e)
        return 0