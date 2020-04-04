# Library imports
from libraries import *
from blocky_block import BlockyBlock, window
from game_contants import *

def draw_object(pygame, window,WIDTH, HEIGHT):
    pygame.draw.rect(window, OBJECT4, [ WIDTH - WIDTH / 2 ,HEIGHT-70 , 170 , 70 ], 0 )
    pygame.draw.rect(window, OBJECT4, [ 5 ,5, WIDTH-5 , HEIGHT-5 ], 15 ) # GAME BOARD FRAME


def print_current_color(paint_color): 
    pygame.draw.rect(window, paint_color, [0,0,30,30],0)


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
    
    print_current_color(paint_color)


def main():
    global paint_color
    pygame.init()
    pygame.display.update()
    pygame.display.set_caption("Welcome to Blockyblock game | by Peyman")
    paint_color = (0,255,0)
    clicked = False # mouse button down to starting to draw
    pygame.display.update()

    player1 = BlockyBlock("player1", YELLOW)
    player1.assign_keystrock(STANDARD_INPUT)
    player1.select_me()

    player2 = BlockyBlock("player2", RED)
    player2.assign_keystrock(SECONDARY_INPUT)
    player2.set_x(100)


    PrintHelpOnConsole()
    print_current_color(paint_color)
    pygame.display.update()

    game_over = False
    while not game_over: # Main Game Loop   
        draw_object(pygame, window, WIDTH, HEIGHT)
        keys = pygame.key.get_pressed()  #checking pressed keys
        
        BlockyBlock.event_listener(keys)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over= True

            if event.type == pygame.MOUSEBUTTONDOWN: # mouse click event
                x,y = event.pos
                if BlockyBlock.select(x,y):
                    clicked = False
                else:
                    clicked = True

            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False
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
                    emotion = Emotion.NORMAL
                    player = BlockyBlock("Blockiii", random_color_generator(), emotion= emotion)
                    player.assign_keystrock(SECONDARY_INPUT)

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