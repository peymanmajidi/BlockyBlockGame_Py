import pygame, os, time
from blocky_block import BlockyBlock
from game_contants import *
import menu
import game_tools

pygame.init()

pygame.display.set_caption(GAME_TITLE)
window = pygame.display.set_mode((WIDTH, HEIGHT))
clicked = False

player1 = BlockyBlock(window, "player1", YELLOW, x= int(WIDTH/2), size= Character_Size.Normal)
player1.assign_keystrock(STANDARD_INPUT)
player1.select_me()

player2 = BlockyBlock(window, "player2", RED, x= 150, size=Character_Size.SuperBig )
player2.assign_keystrock(SECONDARY_INPUT)
player2.direction = Direction.RIGHT
# auto(player2)


menu.PrintHelpOnConsole()

game_tools.auto_generate_blocky(window, BlockyBlock)
pygame.display.update()
game_over = False
paint_color = GREEN

while not game_over:
    menu.draw_object(window)
    keys = pygame.key.get_pressed() 

    BlockyBlock.event_listener(keys)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over= True

        if event.type == pygame.MOUSEBUTTONDOWN: # mouse click event
            x,y = event.pos
            if BlockyBlock.select(x,y, Character_Size.Normal):
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
                BlockyBlock.Generate_blocky(window)

            paint_color = game_tools.change_paint_color(event.key)
            menu.mouse_color(window, paint_color)
                
            if event.key == pygame.K_c: # clear all drawing
                pygame.draw.rect(window, BLACK, [0,0,WIDTH, HEIGHT],0)
                BlockyBlock.render_all()
                

    pygame.display.update()
    pygame.time.delay(REFRESH) # refresh rate
    game_over = BlockyBlock.game_over
    # end of main loop
menu.game_is_over(window)
os._exit(0)



