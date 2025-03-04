import pygame

# window width, height
WINDOW_WITH = 900
WINDOW_HEIGHT = 400

# sprite source
IMG_GROUND = pygame.image.load("./img/ground.png")
IMG_TREX = pygame.image.load("./img/tRex.png")

TREX_OPTIONS = {
    0: (0, 0, 40, 43),
    1: (40, 0, 40, 43),
    2: (80, 0, 40, 43),
    3: (120, 0, 40, 43),
    4: (160, 0, 55, 43),
    5: (215, 0, 55, 43)
}

CACTUS_OPTIONS = {
    0: (23, 46),
    1: (47, 46),
    2: (73, 46),
    3: (49, 46)
}

CACTUS_RANGE = {
    0: (150, 350),
    1: (350, 550),
    2: (550, 750),
    3: (750, 950),
}

# TRex position
X_TREX = 10
Y_TREX = 245

# # TRex standing
# self.surface = pygame.Surface((40, 43),pygame.SRCALPHA)

# # TRex sit
# self.surface = pygame.Surface((55, 43),pygame.SRCALPHA) # nếu có phím ngồi