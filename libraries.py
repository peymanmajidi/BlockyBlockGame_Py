import pygame, random, math

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

def play_audio(soundname):
    pygame.mixer.music.load("sounds/"+soundname)
    pygame.mixer.music.play(0)

class Input:
    def __init__(self, left=pygame.K_LEFT, right=pygame.K_RIGHT, shot=pygame.K_RETURN, jump=pygame.K_SPACE):
        self.left = left
        self.right = right
        self.jump = jump
        self.shot = shot


class Point:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    def set(self, x,y):
        self.x = x
        self.y = y
    def get(self):
        return [self.x, self.y]
    def get2(self):
        return (self.x, self.y)


def random_color_generator():
    return (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))


def PrintHelpOnConsole():
    print("""Welcome to Blocky Blocky (B.b)
It is a fight between mouse cursor and Blocky Block !

Use Arrow keys to move around, press [space bar] to jump: yellow blocky
Press a-w-d to move other blockies
Hit [Enter] to shot laser gun
Press [+] and [-] keys to make the B.b bigger or smaller
Finally, [click] anywhere of playground by Mouse to draw anything you like; B.B can move and jump over them

Other useful trick:
C: Clear the playground
G: Green brush
R: Red brush

Press [tab] to generate new blocky
""")