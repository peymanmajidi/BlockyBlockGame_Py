import pygame
import math
OBJECT1 = (100,50,0)
OBJECT2 = (0,255,0)
OBJECT3 = (200,90,90)
OBJECT4 = (255,255,255)


def draw_object(window,WIDTH, HEIGHT):
    pygame.draw.rect(window, OBJECT4, [ WIDTH - WIDTH / 2 ,HEIGHT-70 , 170 , 70 ], 0 )
    pygame.draw.arc(window, OBJECT3, [100,100,500,500], 35,1)
    pygame.draw.arc(window, (255, 255, 255), (50, 50, 500, 500), 5*math.pi/4,7* math.pi / 4 , 10)
    pygame.draw.rect(window, OBJECT4, [ 5 ,5, WIDTH-5 , HEIGHT-5 ], 15 ) # GAME BOARD

