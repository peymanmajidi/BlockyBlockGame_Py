# Library imports
import random
import pygame
import math
import playground as pg

OBJECT = (0,255,0)

# Initiate pygame
pygame.init()

class Direction:
    LEFT = 99,
    RIGHT = -99,
    FRONT = 88
class Emotion:
    SAD = 1,
    HAPPY = 2,
    O = 3


def playsound(soundname):

    pygame.mixer.music.load("sounds/"+soundname)
    pygame.mixer.music.play(0)



dir = Direction().FRONT


# Game window


WIDTH = 1200
HEIGHT = 600
CHARCTER = 100
MOVE = 1

COLOR = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
LASER = (255, 102, 0)
LASER2 = (255, 80, 80)

JUMP = int(CHARCTER * 1.5)
jumping = False
rising = False
falling = False
fall = 0
rise= 0
window = pygame.display.set_mode((WIDTH, HEIGHT))
clicked = False
wink = False
winking =0
target = 20
keep = 0
eyex=0
eyexx=0
eyey=0
eyeyy=0
fall_played = True


x=int(CHARCTER)*5
y= CHARCTER 
# Game title
pygame.display.set_caption("Blocki Block")
# pygame.draw.rect(window, COLOR, [ x ,HEIGHT  , CHARCTER , CHARCTER ], 0 )
pygame.display.update()
game_over = False


def is_colored_left(x,y):
    for i in range(CHARCTER): # LEFT
        dot = window.get_at((x-MOVE,y+i))
        if dot[0] > 0:
            return True
        if dot[1] > 0:
            return True
        if dot[2] > 0:
            return True
    return False

def is_colored_right(x,y):        
    for i in range(CHARCTER): # RIGHT
        dot = window.get_at((x+MOVE + CHARCTER,y+i))
        if dot[0] > 0:
            return True
        if dot[1] > 0:
            return True
        if dot[2] > 0:
            return True
    return False

def is_colored_top(x,y):     
    for i in range(CHARCTER): # TOP
        dot = window.get_at((x+i,y-MOVE))
        if dot[0] > 0:
            return True
        if dot[1] > 0:
            return True
        if dot[2] > 0:
            return True
    return False

def is_colored_bottom(x,y):
    try:
        for i in range(CHARCTER): # BOTTOM
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

def render_character(emo = Emotion.HAPPY):
    global eyex
    global eyexx
    global eyey
    global eyeyy
    global dir
    global keep
    global target
    global falling

    
# draw charcter

    pygame.draw.rect(window, COLOR, [ x ,y  , CHARCTER , CHARCTER ], 0 ) # [ ]

    eyex = x+int(CHARCTER/2)- int(CHARCTER / 5)
    eyey = y+int(CHARCTER/2)-int(CHARCTER / 5)

    eyexx = x+int(CHARCTER/2)+int(CHARCTER / 5)
    eyeyy= y+int(CHARCTER/2)-int(CHARCTER / 5)
    

    if dir == Direction.RIGHT:
        eyex+=int(CHARCTER / 10)
        eyexx+=int(CHARCTER / 10)
        eyey+=1
    elif dir == Direction.LEFT:
        eyex-=int(CHARCTER / 10)
        eyexx-=int(CHARCTER / 10)
        eyeyy+=1



    if  keep > 5:
        pygame.draw.circle(window, BLACK,[eyex,eyey],int(CHARCTER / 15),0) #[.]
        pygame.draw.circle(window, BLACK,[eyexx,eyey],int(CHARCTER / 15),0) # [..]
        target = random.randrange(100,1000)
    else:       
        pygame.draw.circle(window, BLACK,[eyex,eyey],int(CHARCTER / 10),0) #[.]
        pygame.draw.circle(window, BLACK,[eyexx,eyeyy],int(CHARCTER / 10),0) # [..]
    
  
    if emo == Emotion.SAD:
        pygame.draw.arc(window, BLACK,  (x+5,y+30 , CHARCTER-int(CHARCTER / 5), CHARCTER-int(CHARCTER / 5)), math.pi/4,3* math.pi / 4 , int(CHARCTER / 10)) # :(

    elif not falling:
        pygame.draw.arc(window, BLACK,  (x+int(CHARCTER / 10),y , CHARCTER-int(CHARCTER / 5), CHARCTER-int(CHARCTER / 5)), 5*math.pi/4,7* math.pi / 4 , int(CHARCTER / 10)) # :)
    else:
        pygame.draw.arc(window, BLACK,  (x+int(CHARCTER / 2.5),y+int(CHARCTER / 1.8) , int(CHARCTER / 3.5),  int(CHARCTER / 3.5)), 0,2* math.pi  , int(CHARCTER / 7)) # :O






def shot():
    global eyex
    global eyey
    global eyexx
    global eyeyy
    global dir
    global WIDTH
    render_character(Emotion.SAD)

    tempx= eyex
    tempy = eyey
    tempxx= eyexx
    tempyy = eyeyy
    
    if dir == Direction.RIGHT or  dir == Direction.FRONT:
        pygame.draw.line(window, LASER, ( tempx,tempy), (WIDTH,tempy),5)
        pygame.draw.line(window, LASER2, ( tempxx,tempyy), (WIDTH,tempy),5)
    else:
        pygame.draw.line(window, LASER, ( tempx,tempy), (0,tempy),5)
        pygame.draw.line(window, LASER2, ( tempxx,tempyy), (0,tempy),5)

    playsound("laser.wav")

    pygame.display.update()
    pygame.time.delay(50)
    render_character(Emotion.SAD)
    if dir == Direction.RIGHT or  dir == Direction.FRONT:
        pygame.draw.line(window, BLACK, (tempx,tempy-10), (WIDTH,tempy-10),30)
    else:
        pygame.draw.line(window, BLACK, (tempx,tempy-10), (0,tempy-10),30)

    pygame.display.update()


def print_current_color():
    pygame.draw.rect(window, OBJECT, [0,0,30,10],0)


print("Welcome to Blocky Blocky")
print("space: jump")
print("click: draw object on screen")
print("c: clear")
print("R-SHIFT: change mouse clicker color")

while not game_over:    
    pg.draw_object(window, WIDTH, HEIGHT)
    print_current_color()
    surface = pygame.Surface((WIDTH,HEIGHT))

    render_character()

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
             if not is_colored_left(x,y):
                x-= MOVE
             elif not is_colored_left(x-MOVE+1,y-(MOVE*5)):
               x-= MOVE
               y-=MOVE

    
    if keys[pygame.K_RIGHT]:
        pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
        dir =Direction.RIGHT
        if x + CHARCTER + MOVE <= WIDTH:
             me= window.get_at((x+1+ CHARCTER,y+CHARCTER))
             if not is_colored_right(x,y):
                x+= MOVE
             elif not is_colored_right(x+ MOVE+1,y-(MOVE*5)):
               x+= MOVE
               y-= MOVE



    if jumping:
        pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
        if rising:
            rise+=1
            if not is_colored_top(x,y-1):
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
                pygame.draw.rect(window, OBJECT, [x2,y2,20,20],0)
                pygame.display.update()

        except:
            pass         



        if event.type == pygame.KEYDOWN:
            pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
            pygame.display.update()
            if event.key == pygame.K_SPACE:
                if jumping or falling:
                    break
                pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
                jumping = True
                rising = True
                playsound("jump.wav")
                rise=0
            
            if event.key == pygame.K_RETURN:
                shot()
            if event.key == pygame.K_c:
                pygame.draw.rect(window, BLACK, [0,0,WIDTH, HEIGHT],0)

            

            if event.key == pygame.K_RSHIFT:
                OBJECT = (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))
    
            if event.key == pygame.K_b:
                OBJECT = (0,0,0)
                
            if event.key == pygame.K_r:
                OBJECT = (255,0,0)
                
            if event.key == pygame.K_g:
                OBJECT = (0,255,0)
                
            if event.key == pygame.K_y:
                OBJECT = (255,255,0)
                
    


    if not is_colored_bottom(x,y) and not jumping:
        pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
        y+=1
        # dir = Direction.FRONT
        falling = True
        fall_played = True
    else:
        falling = False
        if fall_played:
            playsound("fall.wav")
            fall_played = False

    
    




                

        


