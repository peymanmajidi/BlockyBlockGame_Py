from gameplay import *
from contants import *

pygame.init()
pygame.display.set_caption(GAME_TITLE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player1 = BlockyBlock(screen, "player1", color = YELLOW, size= Character_Size.Normal)
player1.assign_keystrock(STANDARD_INPUT)
player1.set_as_player1()

UI.console_help()

blocky_generator(screen, second=3)
pygame.display.update()

while not game_over:
    UI.level_design(screen)

    BlockyBlock.update(pygame.key.get_pressed())

    arrow_keys(screen, pygame.event)
    mouse_click(screen, pygame.event)
                
    pygame.display.update()
    pygame.time.delay(REFRESH)
    BlockyBlock.render_all()
    game_over = BlockyBlock.game_over

UI.game_over(screen)
os._exit(0)



