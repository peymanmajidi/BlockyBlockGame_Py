# Library imports
from libraries import *
from blocky_block import BlockyBlock, window

def draw_object(pygame, window,WIDTH, HEIGHT):
    pygame.draw.rect(window, OBJECT4, [ WIDTH - WIDTH / 2 ,HEIGHT-70 , 170 , 70 ], 0 )
    pygame.draw.rect(window, OBJECT4, [ 5 ,5, WIDTH-5 , HEIGHT-5 ], 15 ) # GAME BOARD

def change_paint_color(key):
    global paint_color
    if key == pygame.K_RSHIFT:
        paint_color = random_color_generator()

    if key == pygame.K_b:
        paint_color = (0,0,0)
        
    if key == pygame.K_r:
        paint_color = (255,0,0)
        
    if key== pygame.K_g:
        paint_color = (0,255,0)
        
    if key == pygame.K_y:
        paint_color = (255,255,0)
    
    pygame.draw.rect(window, paint_color, [0,0,30,10],0)



def main():
    global paint_color
    pygame.init()
    pygame.display.update()
    pygame.display.set_caption("Welcome to Blockyblock game | by Peyman")
    paint_color = (0,255,0)
    clicked = False # mouse button down to starting to draw
    pygame.display.update()

    blocky_yellow = BlockyBlock("yellowish blocki", YELLOW)
    blocky_red = BlockyBlock("redish blocki", RED)
    #customize keystrock
    blocky_red.assign_keystrock(pygame.K_a, pygame.K_d, pygame.K_s,pygame.K_w)
    blocky_red.set_x(100)

    pygame.display.update()
    PrintHelpOnConsole()
    game_over = False
    while not game_over: # Main Game Loop   
        draw_object(pygame, window, WIDTH, HEIGHT)
        keys = pygame.key.get_pressed()  #checking pressed keys
        
        BlockyBlock.event_manager(keys)
        
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

                BlockyBlock.action_manager(event.key)

                if event.key == pygame.K_TAB:
                    player = BlockyBlock("Blockiii", random_color_generator())
                    player.assign_keystrock(pygame.K_a, pygame.K_d, pygame.K_s,pygame.K_w)

                change_paint_color(event.key)
                    
                if event.key == pygame.K_c:
                    pygame.draw.rect(window, BLACK, [0,0,WIDTH, HEIGHT],0)
                    
                # if event.key == pygame.K_KP_PLUS or  event.key ==pygame.K_PLUS or event.key == pygame.K_l:
                #     for player in players:
                #         player.zoom_in()
                        
                # if event.key == pygame.K_MINUS or  event.key ==pygame.K_KP_MINUS:
                #     for player in players:
                #         player.zoom_out()
        
        pygame.display.update()
        pygame.time.delay(REFRESH) # refresh rate
        # end of main loop

if __name__ == "__main__":
    main()