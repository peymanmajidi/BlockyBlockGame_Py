import pygame
import gameplay
from blocky_block import BlockyBlock
from contants import *



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


gameplay.Menu.PrintHelpOnConsole()

gameplay.auto_generate_blocky(window, BlockyBlock)
pygame.display.update()
game_over = False
paint_color = GREEN

while not game_over:
    gameplay.Menu.draw_object(window)
    BlockyBlock.control(pygame.key.get_pressed() )
    game_over = gameplay.game_loop(window, pygame.event, BlockyBlock)
                
    pygame.display.update()
    pygame.time.delay(REFRESH)
    game_over = BlockyBlock.game_over

    # end of main loop

gameplay.Menu.game_is_over(window)
gameplay.os._exit(0)



