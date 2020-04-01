# Library imports
from libraries import *
from blocky_block import BlockyBlock, window

def draw_object(pygame, window,WIDTH, HEIGHT):
    pygame.draw.rect(window, OBJECT4, [ WIDTH - WIDTH / 2 ,HEIGHT-70 , 170 , 70 ], 0 )
    pygame.draw.rect(window, OBJECT4, [ 5 ,5, WIDTH-5 , HEIGHT-5 ], 15 ) # GAME BOARD

def print_current_color(paint_color): 
    pygame.draw.rect(window, paint_color, [0,0,30,10],0)

def main():
    clicked = False # mouse button down to starting to draw
    paint_color = (0,255,0)
    pygame.init()
    pygame.display.set_caption("Welcome to Blockyblock game | by Peyman")
    pygame.display.update()
    PrintHelpOnConsole()

    # make a blocky character
    blocky = BlockyBlock("yellowish blocki", YELLOW) 
    player2 = BlockyBlock("redish blocki", RED)
    player2.assign_keystrock(pygame.K_a, pygame.K_d, pygame.K_s,pygame.K_w)
    player2.x = 100
    
    game_over = False
    while not game_over: # Main Game Loop   
        draw_object(pygame, window, WIDTH, HEIGHT)
        print_current_color(paint_color)
        keys = pygame.key.get_pressed()  #checking pressed keys

        blocky.alive(keys)
        player2.alive(keys)

        if keys[pygame.K_RIGHT]:
            print(f"peyman.x: {player2.x} blocky.x {blocky.x}\r",end = '')

            if (blocky.x + CHARCTER == player2.x) or (blocky.x + CHARCTER +1 == player2.x):
                if (blocky.y - CHARCTER <= player2.y-CHARCTER and blocky.y > player2.y-CHARCTER) or ( blocky.y - CHARCTER > player2.y - CHARCTER and blocky.y - CHARCTER < player2.y ):
                    player2.turn_right()
                        
        if keys[pygame.K_LEFT]:
            print(f"peyman.x: {player2.x} blocky.x {blocky.x}\r",end = '')

            if (blocky.x == player2.x+ CHARCTER ) or (blocky.x  == player2.x+ CHARCTER +1):
                if (blocky.y - CHARCTER <= player2.y-CHARCTER and blocky.y > player2.y-CHARCTER) or ( blocky.y - CHARCTER > player2.y - CHARCTER and blocky.y - CHARCTER < player2.y ):
                    player2.turn_left()

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
                player2.event(event.key)

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

if __name__ == "__main__":
    main()