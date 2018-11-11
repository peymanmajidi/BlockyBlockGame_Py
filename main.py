# Library imports
import random
import pygame

# Initiate pygame
pygame.init()





# Game window
WIDTH = 1200
HEIGHT = 600
CHARCTER = 50
MOVE = 1
COLOR = (255,0,0)
OBJECT = (0,255,0)
BLACK = (0,0,0)
JUMP = 100
jumping = False
rising = False
falling = False
fall = 0
rise= 0
window = pygame.display.set_mode((WIDTH, HEIGHT))

x=int(CHARCTER)
y= HEIGHT - CHARCTER - 5
# Game title
pygame.display.set_caption("BBlocki BBlock")
# pygame.draw.rect(window, COLOR, [ x ,HEIGHT  , CHARCTER , CHARCTER ], 0 )
pygame.display.update()
game_over = False


def is_colored_left(x,y):
    for i in range(CHARCTER): # LEFT
        dot = window.get_at((x-1,y+i))
        if dot[0] > 0:
            return True
        if dot[1] > 0:
            return True
        if dot[2] > 0:
            return True
    return False

def is_colored_right(x,y):        
    for i in range(CHARCTER): # RIGHT
        dot = window.get_at((x+1 + CHARCTER,y+i))
        if dot[0] > 0:
            return True
        if dot[1] > 0:
            return True
        if dot[2] > 0:
            return True
    return False

def is_colored_top(x,y):     
    for i in range(CHARCTER): # TOP
        dot = window.get_at((x+i,y-1))
        if dot[0] > 0:
            return True
        if dot[1] > 0:
            return True
        if dot[2] > 0:
            return True
    return False

def is_colored_bottom(x,y):  
    for i in range(CHARCTER): # BOTTOM
        dot = window.get_at((x+i,y+CHARCTER+1))
        if dot[0] > 0:
            return True
        if dot[1] > 0:
            return True
        if dot[2] > 0:
            return True

    return False



def draw_object():
    pygame.draw.rect(window, OBJECT, [ WIDTH - WIDTH / 3 ,HEIGHT-70 , 170 , 70 ], 0 )
    pygame.draw.rect(window, OBJECT, [ WIDTH - WIDTH / 3 + 70 ,HEIGHT-140 , 170 , 140 ], 0 )
    pygame.draw.rect(window, OBJECT, [ WIDTH - WIDTH / 3 + 70 +70,HEIGHT-140-70 , 170 , 140 ], 0 )
    pygame.draw.rect(window, OBJECT, [ 1 ,1, WIDTH-1 , HEIGHT-1 ], 1 )
    
    






while not game_over:    
    draw_object()
    surface = pygame.Surface((WIDTH,HEIGHT))

    pygame.draw.rect(window, COLOR, [ x ,y  , CHARCTER , CHARCTER ], 0 )
    pygame.display.update()
    me= window.get_at((0,0))

    # print(me)
    pygame.time.delay(5)
    keys = pygame.key.get_pressed()  #checking pressed keys

    if keys[pygame.K_LEFT]:
        pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
        if x - MOVE >= 0:
             me= window.get_at((x-1,y+ CHARCTER))
             if not is_colored_left(x,y):
                x-= MOVE

    if keys[pygame.K_RIGHT]:
        pygame.draw.rect(window, BLACK, [ x ,y  , CHARCTER , CHARCTER ], 0 )
        if x + CHARCTER + MOVE <= WIDTH:
             me= window.get_at((x+1+ CHARCTER,y+CHARCTER))
             if not is_colored_right(x,y):
                x+= MOVE
            

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

    





                

        


