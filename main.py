# Library imports
from libraries import *
from blocky_block import BlockyBlock, window

# Initilize Variables
game_over = False

clicked = False # mouse button down to starting to draw
paint_color = (0,255,0)


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
peyman.assign_keystrock(pygame.K_a, pygame.K_d, pygame.K_s,pygame.K_w)
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
                