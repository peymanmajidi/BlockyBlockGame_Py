import pygame
OBJECT1 = (100,50,0)
OBJECT2 = (0,255,0)
OBJECT3 = (200,90,90)
OBJECT4 = (255,255,255)


def draw_object(window,WIDTH, HEIGHT):
    pygame.draw.rect(window, OBJECT4, [ WIDTH - WIDTH / 2 ,HEIGHT-70 , 170 , 70 ], 0 )

    pygame.draw.rect(window, OBJECT4, [ WIDTH - WIDTH / 2 + 300,HEIGHT-290, 150 , 50 ], 0 )
    pygame.draw.rect(window, OBJECT4, [ WIDTH - WIDTH / 2 + 70,HEIGHT-360, 150 , 50 ], 0 )
    pygame.draw.polygon(window, OBJECT3,[(0,0),(30,40),(23,100)],0)

    pygame.draw.circle(window, OBJECT4, [ WIDTH - int( WIDTH / 2) ,HEIGHT],300,0)

    pygame.draw.rect(window, OBJECT4, [ WIDTH - WIDTH / 2 - 100,HEIGHT-100, 110 , 105 ], 0 )
    pygame.draw.line(window, OBJECT4, [0,HEIGHT/5 + 200],[WIDTH / 2,HEIGHT],10)



    pygame.draw.rect(window, OBJECT4, [ 5 ,5, WIDTH-5 , HEIGHT-5 ], 15 ) # GAME BOARD

