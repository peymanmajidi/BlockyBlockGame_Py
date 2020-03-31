# Library imports
import pygame
import math
import random
from enum import Enum
import playground as pg
from howToPlay import *


class Direction(Enum):
    LEFT = '👈',
    FRONT = '🐥',
    RIGHT = '👉'

class Emotion(Enum):
    SAD = '😞',
    WOW = '😲'
    HAPPY = '😊',

def play_audio(soundname):
    pygame.mixer.music.load("sounds/"+soundname)
    pygame.mixer.music.play(0)


# Game's Constant
WIDTH = 1200
HEIGHT = 600
CHARCTER = 50
MOVE = 1

# Game's Colors Constant
COLOR = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
LASER = (255, 102, 0)
LASER2 = (255, 80, 80)
OBJECT_COLOR = (0,255,0)

# Setup Parameters
JUMP = int(CHARCTER * 2.1)
dir = Direction.FRONT


# Initilize Variables
jumping = False
rising = False
falling = False
fall = 0
rise= 0
clicked = False # mouse button down to starting to draw
wink = False # last wink status
winking = 0 # eye winking when blocky is idle
target = 20
keep = 0

fall_played = True
game_over = False
window = pygame.display.set_mode((WIDTH, HEIGHT))
x=int(CHARCTER)*5
y= CHARCTER



class BlockyBlock:
    title = "Blocky Block"
    # eyes
    eye1_x=0
    eye1_y=0
    eye2_x=0
    eye2_y=0
    class Can_Move:
        def left(x,y):
            for i in range(CHARCTER):
                dot = window.get_at((x-MOVE,y+i))
                if dot[0] > 0:
                    return True
                if dot[1] > 0:
                    return True
                if dot[2] > 0:
                    return True
            return False
    
        def right(x,y):        
            for i in range(CHARCTER):
                dot = window.get_at((x+MOVE + CHARCTER,y+i))
                if dot[0] > 0:
                    return True
                if dot[1] > 0:
                    return True
                if dot[2] > 0:
                    return True
            return False

        def top(x,y):     
            for i in range(CHARCTER):
                dot = window.get_at((x+i,y-MOVE))
                if dot[0] > 0:
                    return True
                if dot[1] > 0:
                    return True
                if dot[2] > 0:
                    return True
            return False

        def bottom(x,y):
            try:
                for i in range(CHARCTER):
                    dot = window.get_at((x+i,y+CHARCTER+MOVE))
                    if dot[0] > 0:
                        return True
                    if dot[1] > 0:
                        return True
                    if dot[2] > 0:
                        return True
            except:
                pass  

            return False

    # render charcter

    def render_character(self, emo = Emotion.HAPPY): # default face is happy :)
        global dir
        global keep
        global target
        global falling

        pygame.draw.rect(window, COLOR, [ x ,y  , CHARCTER , CHARCTER ], 0 ) # [ ]

        eye1_x = x+int(CHARCTER/2)- int(CHARCTER / 5)
        eye1_y = y+int(CHARCTER/2)-int(CHARCTER / 5)

        eye2_x = x+int(CHARCTER/2)+int(CHARCTER / 5)
        eye2_y= y+int(CHARCTER/2)-int(CHARCTER / 5)

        if dir == Direction.RIGHT:
            eye1_x+=int(CHARCTER / 10)
            eye2_x+=int(CHARCTER / 10)
            eye1_y+=1
        elif dir == Direction.LEFT:
            eye1_x-=int(CHARCTER / 10)
            eye2_x-=int(CHARCTER / 10)
            eye2_y+=1

        if  keep > 5:
            pygame.draw.circle(window, BLACK,[eye1_x,eye1_y],int(CHARCTER / 15),0) #[.]
            pygame.draw.circle(window, BLACK,[eye2_x,eye1_y],int(CHARCTER / 15),0) # [..]
            target = random.randrange(100,1000)
        else:       
            pygame.draw.circle(window, BLACK,[eye1_x,eye1_y],int(CHARCTER / 10),0) #[.]
            pygame.draw.circle(window, BLACK,[eye2_x,eye2_y],int(CHARCTER / 10),0) # [..]
        
    
        if emo == Emotion.SAD:
            pygame.draw.arc(window, BLACK,  (x+(x+int(CHARCTER / 10)),y+(x+int(CHARCTER / 2)) , CHARCTER-int(CHARCTER / 5), CHARCTER-int(CHARCTER / 5)), math.pi/4,3* math.pi / 4 , int(CHARCTER / 10)) # :(

        elif not falling:
            pygame.draw.arc(window, BLACK,  (x+int(CHARCTER / 10),y , CHARCTER-int(CHARCTER / 5), CHARCTER-int(CHARCTER / 5)), 5*math.pi/4,7* math.pi / 4 , int(CHARCTER / 10)) # :)
        else:
            pygame.draw.arc(window, BLACK,  (x+int(CHARCTER / 2.5),y+int(CHARCTER / 1.8) , int(CHARCTER / 3.5),  int(CHARCTER / 3.5)), 0,2* math.pi  , int(CHARCTER / 7)) # :O
        
        self.eye1_x = eye1_x
        self.eye1_y = eye1_y
        self.eye2_x = eye2_x
        self.eye2_y = eye2_y


    def shot(self):
        global dir
        global WIDTH
        self.render_character(Emotion.SAD)

        tempx= self.eye1_x
        tempy = self.eye1_y
        tempxx= self.eye2_x
        tempyy = self.eye2_y
        
        if dir == Direction.RIGHT or  dir == Direction.FRONT:
            pygame.draw.line(window, LASER, ( tempx,tempy), (WIDTH,tempy),int(CHARCTER/10))
            pygame.draw.line(window, LASER2, ( tempxx,tempyy), (WIDTH,tempy),int(CHARCTER/10))
        else:
            pygame.draw.line(window, LASER, ( tempx,tempy), (0,tempy),int(CHARCTER/10))
            pygame.draw.line(window, LASER2, ( tempxx,tempy), (0,tempy),int(CHARCTER/10))

        play_audio("laser.wav")

        pygame.display.update()
        pygame.time.delay(50)
        self.render_character(Emotion.SAD)
        if dir == Direction.RIGHT or  dir == Direction.FRONT:
            pygame.draw.line(window, BLACK, (tempx+1,tempy-int(CHARCTER/5)), (WIDTH,tempy-int(CHARCTER/5)),int(CHARCTER/2))
        else:
            pygame.draw.line(window, BLACK, (tempx+1,tempy-int(CHARCTER/5)), (0,tempy-int(CHARCTER/5)),int(CHARCTER/2))

        pygame.display.update()

                



# Initiate pygame
pygame.init()
pygame.display.set_caption(BlockyBlock.title)
pygame.display.update()




def print_current_color(): 
    pygame.draw.rect(window, OBJECT_COLOR, [0,0,30,10],0)

PrintHelpOnConsole()
blocky = BlockyBlock() # make a blocky character
# Main Game Loop
while not game_over:    
    pg.draw_object(window, WIDTH, HEIGHT)
    print_current_color()
    surface = pygame.Surface((WIDTH,HEIGHT))
    
    blocky.render_character()

    pygame.display.update()
    me= window.get_at((0,0))

    winking +=1
    if winking % target == 0:
        winking = 0
        wink = True
        keep=30
    
    if wink:
        keep -=1

    if falling:
        pygame.time.delay(2)
    else:
        pygame.time.delay(4)

    keys = pygame.key.get_pressed()  #checking pressed keys

    if keys[pygame.K_LEFT]:
        pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
        dir =Direction.LEFT
        if x - MOVE >= 0:
             me= window.get_at((x-1,y+ CHARCTER))
             if not blocky.Can_Move.left(x,y):
                x-= MOVE
             elif not blocky.Can_Move.left(x-MOVE+1,y-(MOVE*5)):
               x-= MOVE
               y-=MOVE

    
    if keys[pygame.K_RIGHT]:
        pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
        dir =Direction.RIGHT
        if x + CHARCTER + MOVE <= WIDTH:
             me= window.get_at((x+1+ CHARCTER,y+CHARCTER))
             if not blocky.Can_Move.right(x,y):
                x+= MOVE
             elif not blocky.Can_Move.right(x+ MOVE+1,y-(MOVE*5)):
               x+= MOVE
               y-= MOVE



    if jumping:
        pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
        if rising:
            rise+=1
            if not blocky.Can_Move.top(x,y-1):
                y-=1
            else:
                jumping = False
            if rise > JUMP:
                rising = False
                jumping= False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over= True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = not clicked


        try:
            if clicked:
                x2,y2 = event.pos
                pygame.draw.rect(window, OBJECT_COLOR, [x2,y2,20,20],0)
                pygame.display.update()

        except:
            pass         

        if event.type == pygame.KEYDOWN:
            pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
            pygame.display.update()
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if jumping or falling:
                    break
                pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
                jumping = True
                rising = True
                play_audio("jump.wav")
                rise=0
            
            if event.key == pygame.K_RETURN:
                blocky.shot()
            if event.key == pygame.K_c:
                pygame.draw.rect(window, BLACK, [0,0,WIDTH, HEIGHT],0)

            

            if event.key == pygame.K_RSHIFT:
                OBJECT_COLOR = (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))
    
            if event.key == pygame.K_b:
                OBJECT_COLOR = (0,0,0)
                
            if event.key == pygame.K_r:
                OBJECT_COLOR = (255,0,0)
                
            if event.key == pygame.K_g:
                OBJECT_COLOR = (0,255,0)
                
            if event.key == pygame.K_y:
                OBJECT_COLOR = (255,255,0)
                
            if event.key == pygame.K_KP_PLUS or  event.key ==pygame.K_PLUS or event.key == pygame.K_l:
                if CHARCTER <400:
                    y-=10
                    CHARCTER+=10
                    JUMP = int(CHARCTER * 1.8)
                    
            if event.key == pygame.K_MINUS or  event.key ==pygame.K_KP_MINUS:
                if CHARCTER > 10:
                    y+=10
                    CHARCTER-=10
                    JUMP = int(CHARCTER * 1.8)
                
    


    if not blocky.Can_Move.bottom(x,y) and not jumping:
        pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
        y+=1
        falling = True
        fall_played = True
    else:
        falling = False
        if fall_played:
            play_audio("fall.wav")
            fall_played = False

