from gameplay import *
from contants import *

pygame.init()
pygame.display.set_caption(GAME_TITLE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player1 = BlockyBlock(screen, "player1", x=10, color = YELLOW, size= Character_Size.Normal)
player1.assign_keystrock(STANDARD_INPUT)
player1.set_as_player1()




BlockyBlock(screen, x=950, color = GREEN, size= Character_Size.SuperBig)
BlockyBlock(screen, x=1200, color = LIGHT_BLUE, size= Character_Size.SuperTiny, automatic= True)


for i in range(1,20):
    BlockyBlock(screen, x=900-i+ random.randint(-10,10) ,y=i*10, color = random_color_generator(), size= Character_Size.Tiny)


UI.console_help()

blocky_generator(screen, second=5)
pygame.display.update()

while not game_over:
    UI.level_01(screen)

    BlockyBlock.update(pygame.key.get_pressed())

    arrow_keys(screen, pygame.event)
                
    pygame.display.update()
    pygame.time.wait(REFRESH)
    game_over = BlockyBlock.render_all()


UI.game_over(screen)
os._exit(0)



