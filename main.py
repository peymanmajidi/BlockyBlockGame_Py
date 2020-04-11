# Library imports
from libraries import *
from blocky_block import BlockyBlock, window
from game_contants import *
import time
class Main:
    def __init__(self):
        pygame.init()
        pygame.display.update()
        pygame.display.set_caption(GAME_TITLE)
        clicked = False # mouse button down to starting to draw
        pygame.display.update()

        player1 = BlockyBlock("player1", YELLOW, x= int(WIDTH/2), size= Character_Size.Normal)
        player1.assign_keystrock(STANDARD_INPUT)
        player1.select_me()

        player2 = BlockyBlock("player2", RED, x= 150, size=Character_Size.SuperBig )
        player2.assign_keystrock(SECONDARY_INPUT)
        player2.direction = Direction.RIGHT
        # auto(player2)

        PrintHelpOnConsole()
        Main.draw_by_mouse()
        pygame.display.update()

        Main.auto_generate_blocky()


        game_over = False
        while not game_over: # Main Game Loop   
            Main.draw_object(pygame, window, WIDTH, HEIGHT)
            keys = pygame.key.get_pressed()  #checking pressed keys
            
            BlockyBlock.event_listener(keys)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over= True

                if event.type == pygame.MOUSEBUTTONDOWN: # mouse click event
                    x,y = event.pos
                    print(x,",",y)
                    if BlockyBlock.select(x,y, Character_Size.Normal):
                        clicked = False
                    else:
                        clicked = True

                if event.type == pygame.MOUSEBUTTONUP:
                    clicked = False
                try:
                    if clicked:
                        x2,y2 = event.pos
                        pygame.draw.rect(window, Main.paint_color, [x2,y2,20,20],0)
                        pygame.display.update()
                except:
                    pass         
                if event.type == pygame.KEYDOWN:
                    pygame.display.update()
                    BlockyBlock.action_manager(event.key)

                    if event.key == pygame.K_TAB:
                        Main.generate_blocky()

                    Main.change_paint_color(event.key)
                        
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
        Main.game_is_over()
    def game_is_over():
        text_to_screen(window, "GAME_OVER", x= int(WIDTH/2) - 230, y=int(HEIGHT/10),size= 85, color= WHITE)
        pygame.display.update()
        play_audio("game_over.mp3")
        time.sleep(2)
    paint_color = GREEN
    def draw_object(pygame, window,WIDTH, HEIGHT): # GAME BOARD FRAME
        # pygame.draw.rect(window, OBJECT4, [ WIDTH - WIDTH / 2 ,HEIGHT-70 , 170 , 70 ], 0 )
        # pygame.draw.rect(window, WHITE, [ 5 ,5, WIDTH-5 , HEIGHT-5 ], 15 ) # Full FRAME
        
        pygame.draw.rect(window, WHITE, [ 0 ,0, 15 , HEIGHT ], 15 )

        pygame.draw.rect(window, WHITE, [ WIDTH-15 ,0, 15 , HEIGHT ], 15 )

        pygame.draw.rect(window, WHITE, [ 750 , 250, 500, 15  ], 0)
        pygame.draw.rect(window, WHITE, [ 150 , 300, 300, 15  ], 0)
        pygame.draw.rect(window, WHITE, [ 400 , 450, 300, 15  ], 0)
        pygame.draw.rect(window, WHITE, [ 0 , 550, 300, 15  ], 0)
        pygame.draw.rect(window, WHITE, [ 700 , 575, 400, 15  ], 0)

        # pygame.draw.rect(window, GREEN, [ 36 , 450, 20, 20  ], 0)
        # pygame.draw.rect(window, GREEN, [ 124 , 369, 20, 20  ], 0)
        # pygame.draw.rect(window, GREEN, [ 815 , 474, 20, 20  ], 0)
        # pygame.draw.rect(window, GREEN, [ 550 , 224, 20, 20  ], 0)

    def draw_by_mouse(): 
        pygame.draw.rect(window, Main.paint_color, [0,0,30,30],0)

    def generate_blocky():
        size = Character_Size.random()
        x = random.randint(size ,WIDTH - size  )
        emotion = Emotion.SAD
        automatic = True

        emotion = Emotion.SAD
        if x %3 ==0:
            automatic = False
            emotion = Emotion.NORMAL
        player = BlockyBlock("Blockiii", random_color_generator(),x=x, emotion= emotion, automatic= automatic, size=size)
        player.assign_keystrock(NONE_INPUT)
        if x%3 == 0: player.direction = Direction.RIGHT
        if not player.auto:
            player.assign_keystrock(SECONDARY_INPUT)
        BlockyBlock.render_all()

    def auto_generate_blocky():
        Main.generate_blocky()
        thread.Timer(3, Main.auto_generate_blocky).start()


    def change_paint_color(key):
        if key == pygame.K_RSHIFT:
            Main.paint_color = random_color_generator()

        if key == pygame.K_b:
            Main.paint_color = (0,0,0)
            
        if key == pygame.K_r:
            Main.paint_color = (255,0,0)
            
        if key== pygame.K_g:
            Main.paint_color = (0,255,0)
            
        if key == pygame.K_y:
            Main.paint_color = (255,255,0)

        Main.draw_by_mouse()



if __name__ == "__main__":
    Main()

