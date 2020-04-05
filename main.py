# Library imports
from libraries import *
from blocky_block import BlockyBlock, window
from game_contants import *
import time

def draw_object(pygame, window,WIDTH, HEIGHT): # GAME BOARD FRAME
    # pygame.draw.rect(window, OBJECT4, [ WIDTH - WIDTH / 2 ,HEIGHT-70 , 170 , 70 ], 0 )
    # pygame.draw.rect(window, WHITE, [ 5 ,5, WIDTH-5 , HEIGHT-5 ], 15 ) # Full FRAME
    pygame.draw.rect(window, WHITE, [ 0 ,0, 15 , HEIGHT ], 15 )
    pygame.draw.rect(window, WHITE, [ WIDTH-15 ,0, 15 , HEIGHT ], 15 )


    pygame.draw.rect(window, WHITE, [ 750 , 150, 500, 15  ], 0)
    pygame.draw.rect(window, WHITE, [ 150 , 200, 300, 15  ], 0)

    pygame.draw.rect(window, WHITE, [ 400 , 400, 300, 15  ], 0)

    pygame.draw.rect(window, WHITE, [ 0 , 550, 300, 15  ], 0)







def game_is_over():
    text_to_screen(window, "GAME_OVER", x= int(WIDTH/2) - 150, y=int(HEIGHT/2)-50 )
    pygame.display.update()
    play_audio("game_over.mp3")
    time.sleep(2)
  

def print_current_color(paint_color): 
    pygame.draw.rect(window, paint_color, [0,0,30,30],0)

def generate_blocky():
    x = random.randint(10,WIDTH - CHARCTER - 5)
    emotion = Emotion.SAD
    automatic = True
    if x % 2 == 0: emotion = Emotion.NORMAL
    if x %3 ==0: automatic = False
    player = BlockyBlock("Blockiii", random_color_generator(),x=x, emotion= emotion, automatic= automatic)
    player.assign_keystrock(SECONDARY_INPUT)
    if x%3 == 0: player.direction = Direction.RIGHT

def auto_generate_blocky():
    generate_blocky()
    thread.Timer(2, auto_generate_blocky).start()


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
    pygame.display.set_caption(GAME_TITLE)
    paint_color = (0,255,0)
    clicked = False # mouse button down to starting to draw
    pygame.display.update()

    player1 = BlockyBlock("player1", YELLOW, x= int(WIDTH/2))
    player1.assign_keystrock(STANDARD_INPUT)
    player1.select_me()

    player2 = BlockyBlock("player2", RED, x= 150 )
    player2.assign_keystrock(SECONDARY_INPUT)
    player2.direction = Direction.RIGHT
    # auto(player2)

    PrintHelpOnConsole()
    print_current_color(paint_color)
    pygame.display.update()

    auto_generate_blocky()


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
                print(x,",",y)
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
                    generate_blocky()

                change_paint_color(event.key)
                    
                if event.key == pygame.K_c: # clear all drawing
                    pygame.draw.rect(window, BLACK, [0,0,WIDTH, HEIGHT],0)
                    BlockyBlock.render_all()
                    
                # if event.key == pygame.K_KP_PLUS or  event.key ==pygame.K_PLUS or event.key == pygame.K_l:
                #     for player in players:
                #         player.zoom_in()
                        
                # if event.key == pygame.K_MINUS or  event.key ==pygame.K_KP_MINUS:
                #     for player in players:
                #         player.zoom_out()
        
        pygame.display.update()
        pygame.time.delay(REFRESH) # refresh rate
        game_over = BlockyBlock.game_over
        # end of main loop
    game_is_over()

if __name__ == "__main__":
    main()