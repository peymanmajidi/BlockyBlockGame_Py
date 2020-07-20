from gameplay import *
from contants import *

pygame.init()
pygame.display.set_caption(GAME_TITLE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player1 = BlockyBlock(screen, "player1", x=10, color = YELLOW, size= Character_Size.Normal)
player1.assign_keystrock(STANDARD_INPUT)
player1.set_as_player1()




BlockyBlock(screen, x=1000, color = GREEN, size= Character_Size.SuperBig)
BlockyBlock(screen, x=1150, color = LIGHT_BLUE, size= Character_Size.Big)


for i in range(1,10):
    BlockyBlock(screen, x=800+i*3,y=i*10, color = random_color_generator(), size= Character_Size.Normal)


UI.console_help()

blocky_generator(screen, second=5)
pygame.display.update()

while not game_over:
    UI.level_01(screen)

    BlockyBlock.update(pygame.key.get_pressed())

    arrow_keys(screen, pygame.event)
                
    pygame.display.update()
    pygame.time.delay(REFRESH)
    game_over = BlockyBlock.render_all()


UI.game_over(screen)
os._exit(0)



