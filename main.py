# Library imports
from libraries import *
from blocky_block import BlockyBlock, window
from game_contants import *
import time

def draw_object(pygame, window,WIDTH, HEIGHT): # GAME BOARD FRAME
    # pygame.draw.rect(window, OBJECT4, [ WIDTH - WIDTH / 2 ,HEIGHT-70 , 170 , 70 ], 0 )
    pygame.draw.rect(window, OBJECT4, [ 0 ,0, 15 , HEIGHT ], 15 )
    pygame.draw.rect(window, OBJECT4, [ WIDTH-15 ,0, 15 , HEIGHT ], 15 )


    pygame.draw.rect(window, GREEN, [ int(WIDTH/4) , int(HEIGHT /5) * 4, int(WIDTH/2) , int(HEIGHT/7) ], 10)

def auto(blocky):
    blocky.auto = True
    if blocky.destroyed or blocky.alive == False:
        return
    if blocky.direction == Direction.RIGHT:
        r = blocky.turn_right()
        if r == False:
            blocky.direction = Direction.LEFT
    else:
        r = blocky.turn_left()
        if r == False:
            blocky.direction = Direction.RIGHT
    thread.Timer(0.0001, auto, [blocky]).start()

def game_is_over():
    text_to_screen(window, "GAME_OVER", x= int(WIDTH/2) - 150, y=int(HEIGHT/2)-50 )
    pygame.display.update()
    play_audio("game_over.mp3")
    time.sleep(2)
  

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
    pygame.display.set_caption(GAME_TITLE)
    paint_color = (0,255,0)
    clicked = False # mouse button down to starting to draw
    pygame.display.update()

    player1 = BlockyBlock("player1", YELLOW, x= int(WIDTH/2))
    player1.assign_keystrock(STANDARD_INPUT)
    player1.select_me()

    player2 = BlockyBlock("player2", RED, x=int(WIDTH/2) - 2*CHARCTER )
    player2.assign_keystrock(SECONDARY_INPUT)

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
                    x = random.randint(10,WIDTH - CHARCTER - 5)
                    emotion = Emotion.SAD
                    if x % 2 == 0: emotion = Emotion.NORMAL
                    player = BlockyBlock("Blockiii", random_color_generator(),x=x, emotion= emotion)
                    player.assign_keystrock(SECONDARY_INPUT)

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