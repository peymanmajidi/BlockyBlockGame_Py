import pygame, random

class Direction:
    LEFT = '👈'
    FRONT = '😶'
    RIGHT = '👉'

class Emotion:
    SAD = '😞'
    WOW = '😲'
    HAPPY = '😊'
    DEAD = '🥴'
    NORMAL = '😐'
    NOT_SET = '❌'


class Input:
    def __init__(self, left=pygame.K_LEFT, right=pygame.K_RIGHT, shot=pygame.K_RETURN, jump=pygame.K_SPACE):
        self.left = left
        self.right = right
        self.jump = jump
        self.shot = shot



class Character_Size:
    SuperBig = 170
    Big = 70
    Normal = 50
    Small = 40
    Tiny = 30
    SuperTiny = 20
    def random():
        r = random.randint(1,80)
        if r in range(1,30):
            return Character_Size.SuperTiny
        if r in range(30,50):
            return Character_Size.Tiny
        if r in range(50,60):
            return Character_Size.Normal
        if r in range(60, 65):
            return Character_Size.Big
        return Character_Size.Normal



# Application
GAME_TITLE = "Welcome to Blockyblock game by Peyman Majidi"


# Playground Consts
WIDTH = 1400
HEIGHT = 800
MOVE = 1

# Colors Consts
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (0,255,255)
LASER = (255, 102, 0)
LASER2 = (255, 80, 80)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DEAD = (70, 70, 70)


BOX_CURSOR = (            #sized 24x24
      "XXXXXXXXXXXXXXXXXXXXXXXX",
      "X                      X",
      "X                      X",
      "X                      X",
      "X                      X",
      "X                      X",
      "X                      X",
      "X                      X",
      "X                      X",
      "X                      X",
      "X          X           X",
      "X                      X",
      "X                      X",
      "X                      X",
      "X                      X",
      "X                      X",
      "X                      X",
      "X                      X",
      "X                      X",
      "X                      X",
      "XXXXXXXXXXXXXXXXXXXXXXXX",
      "                        ",
      "                        ",
      "                        ")


# Objects
OBJECT1 = (100,50,0)
OBJECT2 = (0,255,0)
OBJECT3 = (200,90,90)
OBJECT4 = (255,255,255)

# Parameters
REFRESH = 1

# Fonts
FONT1 = 'assets/fonts/font1.ttf'
FONT2 = 'assets/fonts/font2.ttf'
FONT3 = 'assets/fonts/font3.ttf'

# Inputs
STANDARD_INPUT = Input(left=pygame.K_LEFT, right=pygame.K_RIGHT, shot=pygame.K_RETURN, jump=pygame.K_SPACE)
SECONDARY_INPUT = Input(left=pygame.K_a, right=pygame.K_d, shot=pygame.K_s, jump=pygame.K_w)
NONE_INPUT = Input(left=pygame.K_ASTERISK, right=pygame.K_ASTERISK, shot=pygame.K_ASTERISK, jump=pygame.K_ASTERISK)
