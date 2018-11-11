# Library imports
import random
import pygame
import playground as pg

# Initiate pygame
pygame.init()





# Game window
WIDTH = 1200
HEIGHT = 600
CHARCTER = 50
MOVE = 1
COLOR = (255,0,0)
BLACK = (0,0,0)
JUMP = 100
jumping = False
rising = False
falling = False
fall = 0
rise= 0
window = pygame.display.set_mode((WIDTH, HEIGHT))


x=int(CHARCTER)*5
y= CHARCTER 
# Game title
pygame.display.set_caption("BBlocki BBlock")
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
    for i in range(CHARCTER): # BOTTOM
        dot = window.get_at((x+i,y+CHARCTER+MOVE))
        if dot[0] > 0:
            return True
        if dot[1] > 0:
            return True
        if dot[2] > 0:
            return True

    return False





while not game_over:    
    pg.draw_object(window, WIDTH, HEIGHT)
    surface = pygame.Surface((WIDTH,HEIGHT))

    pygame.draw.rect(window, COLOR, [ x ,y  , CHARCTER , CHARCTER ], 0 )
    pygame.draw.circle(window, BLACK,[x+int(CHARCTER/2)-10,y+int(CHARCTER/2)-10],3,0)
    pygame.draw.circle(window, BLACK,[x+int(CHARCTER/2)+10,y+int(CHARCTER/2)-10],3,0)
    pygame.draw.rect(window, BLACK, [ x + int(CHARCTER/3) ,y+ CHARCTER - int(CHARCTER/3)-5  , int(CHARCTER/2)-5 , int(CHARCTER/2)-20 ], 0 )


    pygame.display.update()
    me= window.get_at((0,0))

    # print(me)
    if falling:
        pygame.time.delay(2)
    else:
        pygame.time.delay(4)

    keys = pygame.key.get_pressed()  #checking pressed keys

    if keys[pygame.K_LEFT]:
        pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
        if x - MOVE >= 0:
             me= window.get_at((x-1,y+ CHARCTER))
             if not is_colored_left(x,y):
                x-= MOVE
             elif not is_colored_left(x-MOVE+1,y-(MOVE*5)):
               x-= MOVE
               y-=MOVE


    if keys[pygame.K_RIGHT]:
        pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
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

        if event.type == pygame.KEYDOWN:
            pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
            pygame.display.update()
            if event.key == pygame.K_SPACE:
                if jumping or falling:
                    break
                pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
                jumping = True
                rising = True
                rise=0
    

    if not is_colored_bottom(x,y) and not jumping:
        pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
        y+=1
        falling = True
    else:
        falling = False

    





                

        


