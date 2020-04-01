# Library imports
import pygame
import math
import random
from howToPlay import *
from game_contants import *


class Direction:
    LEFT = '👈'
    FRONT = '🐥'
    RIGHT = '👉'

class Emotion:
    SAD = '😞'
    WOW = '😲'
    HAPPY = '😊'

def play_audio(soundname):
    pygame.mixer.music.load("sounds/"+soundname)
    pygame.mixer.music.play(0)

# Initilize Variables
game_over = False
window = pygame.display.set_mode((WIDTH, HEIGHT))
clicked = False # mouse button down to starting to draw
paint_color = (0,255,0)


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

class Eyes:
    left = Point()
    right = Point()
    def move(self, x):
        self.left.x +=x
        self.right.x +=x
    # winking eyes        
    wink = False # last wink status
    wink_idle = 0 # eye winking when blocky is idle
    wink_period = 20
    keep = 0
    def winking(self):
        self.wink_idle +=1 
        if self.wink_idle % self.wink_period == 0:
            self.wink_idle = 0
            self.wink = True
            self.keep = 30
    
        if self.wink:
            self.keep -=1


class Is_filled_pixel:
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

class BlockyBlock:
    def __init__(self, character_name, color):
        self.name = character_name
        self.color = color
        self.eyes = Eyes()
        self.x= int(CHARCTER)*5
        self.y= CHARCTER
        self.jumping = False
        self.rising = False
        self.falling = False
        self.fall_played = True
        self.fall = 0
        self.rise= 0
        self.direction = Direction.FRONT
        self.assign_keystrock(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RETURN, pygame.K_SPACE)
        self.render_character()
    
    def assign_keystrock(self, left, right, shot, jump):
        self.key_left = left
        self.key_right = right
        self.key_shot = shot
        self.key_jump = jump



    def render_character(self, emo = Emotion.HAPPY):
        x = self.x
        y = self.y
        pygame.draw.rect(window, self.color, [ x ,y  , CHARCTER , CHARCTER ], 0 ) # [ ]
        self.eyes.left.x = x+int(CHARCTER/2)- int(CHARCTER / 5)
        self.eyes.left.y = y+int(CHARCTER/2)-int(CHARCTER / 5)

        self.eyes.right.x = x+int(CHARCTER/2)+int(CHARCTER / 5)
        self.eyes.right.y = y+int(CHARCTER/2)-int(CHARCTER / 5)

        if self.direction == Direction.RIGHT:
            self.eyes.move(int(CHARCTER / 10))
            self.eyes.left.y +=1

        elif self.direction == Direction.LEFT:
            self.eyes.move(-int(CHARCTER / 10))
            self.eyes.right.y +=1


        if  self.eyes.keep > 5:
            pygame.draw.circle(window, BLACK, self.eyes.left.get(), int(CHARCTER / 15),0) #[.]
            pygame.draw.circle(window, BLACK, self.eyes.right.get(),int(CHARCTER / 15),0) # [..]
            self.eyes.wink_period = random.randrange(100,1000) # random period for winking
        else:       
            pygame.draw.circle(window, BLACK,self.eyes.left.get(),int(CHARCTER / 10),0) #[.]
            pygame.draw.circle(window, BLACK,self.eyes.right.get(),int(CHARCTER / 10),0) # [..]
        
    
        if emo == Emotion.SAD:
            pygame.draw.arc(window, BLACK,  (x+(x+int(CHARCTER / 10)),y+(x+int(CHARCTER / 2)) , CHARCTER-int(CHARCTER / 5), CHARCTER-int(CHARCTER / 5)), math.pi/4,3* math.pi / 4 , int(CHARCTER / 10)) # :(

        elif not self.falling:
            pygame.draw.arc(window, BLACK,  (x+int(CHARCTER / 10),y , CHARCTER-int(CHARCTER / 5), CHARCTER-int(CHARCTER / 5)), 5*math.pi/4,7* math.pi / 4 , int(CHARCTER / 10)) # :)
        else:
            pygame.draw.arc(window, BLACK,  (x+int(CHARCTER / 2.5),y+int(CHARCTER / 1.8) , int(CHARCTER / 3.5),  int(CHARCTER / 3.5)), 0,2* math.pi  , int(CHARCTER / 7)) # :O

    def clear_shadow(self):
        pygame.draw.rect(window, BLACK, [ self.x, self.y, CHARCTER , CHARCTER ], 0)

    def turn_left(self):
        self.clear_shadow()
        self.direction = Direction.LEFT
        if self.x - MOVE >= 0:
             if not Is_filled_pixel.left(self.x, self.y):
                self.x-= MOVE
             elif not Is_filled_pixel.left(self.x-MOVE+1, self.y-(MOVE*5)):
               self.x-= MOVE
               self.y-= MOVE
        self.render_character()

    def turn_right(self):
        self.clear_shadow()
        self.direction = Direction.RIGHT
        if self.x + CHARCTER + MOVE <= WIDTH:
             if not Is_filled_pixel.right(self.x, self.y):
                self.x+= MOVE
             elif not Is_filled_pixel.right(self.x + MOVE+1, self.y - (MOVE*5)):
               self.x+= MOVE
               self.y-= MOVE
        self.render_character()

    def zoom_in(self):
        global CHARCTER
        global JUMP
        if CHARCTER <400:
                    self.y-=10
                    CHARCTER+=10
                    JUMP = int(CHARCTER * 1.8)
    
    def zoom_out(self):
        global CHARCTER
        global JUMP
        if CHARCTER > 10:
            self.y+=10
            CHARCTER-=10
            JUMP = int(CHARCTER * 1.8)

    def do_jump(self):
        if self.jumping or self.falling:
            return
        self.clear_shadow()
        self.jumping = True
        self.rising = True
        play_audio("jump.wav")
        self.rise=0

    def event(self, key):
        if key == self.key_jump:
            self.do_jump()
        elif key == self.key_shot:
            self.shot()


    def alive(self, key):
        self.eyes.winking()
        if not Is_filled_pixel.bottom(self.x, self.y) and not self.jumping:
            self.clear_shadow()
            self.y+=1
            self.falling = True
            self.fall_played = True
        else:
            self.falling = False
            if self.fall_played:
                play_audio("fall.wav")
                self.fall_played = False

        if(keys[self.key_left]):
            self.turn_left()
        elif(keys[self.key_right]):
            self.turn_right()

        if self.jumping:
            self.clear_shadow()
            if self.rising:
                self.rise+=1
                if not Is_filled_pixel.top(self.x, self.y-1):
                    self.y-=1
                else:
                    self.jumping = False
            if self.rise > JUMP:
                self.rising = False
                self.jumping= False
        self.render_character()

    def shot(self):
        global WIDTH
        self.render_character(Emotion.SAD)

        eyes2 = Eyes()
        eyes2.left = self.eyes.left
        eyes2.right = self.eyes.right
        
        # draw laser
        if self.direction == Direction.RIGHT or  self.direction == Direction.FRONT:
            pygame.draw.line(window, LASER, eyes2.left.get2(), (WIDTH,eyes2.left.y),int(CHARCTER/10))
            pygame.draw.line(window, LASER2, eyes2.right.get2(), (WIDTH,eyes2.left.y),int(CHARCTER/10))
        else:
            pygame.draw.line(window, LASER, eyes2.left.get2(), (0,eyes2.left.y),int(CHARCTER/10))
            pygame.draw.line(window, LASER2, eyes2.right.get2(), (0,eyes2.left.y),int(CHARCTER/10))

        play_audio("laser.wav")

        pygame.display.update()
        pygame.time.delay(50)
        self.render_character(Emotion.SAD)

        # clean laser
        if self.direction == Direction.RIGHT or  self.direction == Direction.FRONT:
            pygame.draw.line(window, BLACK, (eyes2.left.x +1,eyes2.left.y-int(CHARCTER/5)), (WIDTH,eyes2.left.y-int(CHARCTER/5)),int(CHARCTER/2))
        else:
            pygame.draw.line(window, BLACK, (eyes2.right.x+1,eyes2.right.y-int(CHARCTER/5)), (0,eyes2.right.y-int(CHARCTER/5)),int(CHARCTER/2))

        pygame.display.update()

def draw_object(pygame, window,WIDTH, HEIGHT):
    pygame.draw.rect(window, OBJECT4, [ WIDTH - WIDTH / 2 ,HEIGHT-70 , 170 , 70 ], 0 )
    pygame.draw.rect(window, OBJECT4, [ 5 ,5, WIDTH-5 , HEIGHT-5 ], 15 ) # GAME BOARD

# Initiate pygame
pygame.init()
pygame.display.set_caption("Welcome to Blockyblock game | by Peyman")
pygame.display.update()

def print_current_color(): 
    pygame.draw.rect(window, paint_color, [0,0,30,10],0)

PrintHelpOnConsole()
blocky = BlockyBlock("redi block", YELLOW) # make a blocky character
peyman = BlockyBlock("peymani block", RED) # make a blocky character
peyman.x = 100
# Main Game Loop
while not game_over:    
    
    draw_object(pygame, window, WIDTH, HEIGHT)
    print_current_color()
    surface = pygame.Surface((WIDTH,HEIGHT))
    
    keys = pygame.key.get_pressed()  #checking pressed keys
    
    blocky.alive(keys)
    peyman.alive(keys)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game_over= True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = not clicked


        try:
            if clicked:
                x2,y2 = event.pos
                pygame.draw.rect(window, paint_color, [x2,y2,20,20],0)
                pygame.display.update()

        except:
            pass         

        if event.type == pygame.KEYDOWN:
            pygame.display.update()

            blocky.event(event.key)
            peyman.event(event.key)

            if event.key == pygame.K_c:
                pygame.draw.rect(window, BLACK, [0,0,WIDTH, HEIGHT],0)

            if event.key == pygame.K_RSHIFT:
                paint_color = (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))
    
            if event.key == pygame.K_b:
                paint_color = (0,0,0)
                
            if event.key == pygame.K_r:
                paint_color = (255,0,0)
                
            if event.key == pygame.K_g:
                paint_color = (0,255,0)
                
            if event.key == pygame.K_y:
                paint_color = (255,255,0)
                
            if event.key == pygame.K_KP_PLUS or  event.key ==pygame.K_PLUS or event.key == pygame.K_l:
                blocky.zoom_in()
                    
            if event.key == pygame.K_MINUS or  event.key ==pygame.K_KP_MINUS:
                blocky.zoom_out()
    
    pygame.display.update()
    pygame.time.delay(2)
    # end of main loop
                