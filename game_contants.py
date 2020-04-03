from libraries import  pygame, Input

# Inputs
STANDARD_INPUT = Input(left=pygame.K_LEFT, right=pygame.K_RIGHT, shot=pygame.K_RETURN, jump=pygame.K_SPACE)
SECONDARY_INPUT = Input(left=pygame.K_a, right=pygame.K_d, shot=pygame.K_s, jump=pygame.K_w)

# Playground Consts
WIDTH = 1200
HEIGHT = 600
CHARCTER = 60
MOVE = 1

# Colors Consts
BLACK = (0,0,0)
WHITE = (255,255,255)
LASER = (255, 102, 0)
LASER2 = (255, 80, 80)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


# Objects
OBJECT1 = (100,50,0)
OBJECT2 = (0,255,0)
OBJECT3 = (200,90,90)
OBJECT4 = (255,255,255)

# Parameters
JUMP = int(CHARCTER * 2.1)
REFRESH = 1
