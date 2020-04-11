import pygame, random, math
import threading as thread

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


class Character_Size:
    SuperBig = 110
    Big = 70
    Normal = 50
    Small = 40
    Tiny = 30
    def random():
        r = random.randint(1,80)
        if r in range(1,30):
            return Character_Size.Normal
        if r in range(30,50):
            return Character_Size.Big
        if r in range(50,60):
            return Character_Size.Small
        if r in range(60, 65):
            return Character_Size.SuperBig
        return Character_Size.Normal

def text_to_screen(screen, text, x, y, color = (255,255,255), size = 50, font_type = './fonts/font2.ttf'):
    text = str(text)
    font = pygame.font.Font(font_type, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))


def random_color_generator():
    return (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))

def play_audio(soundname):
    pygame.mixer.music.load("sounds/"+soundname)
    pygame.mixer.music.play(0)


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