import random, pygame
from game_contants import GREEN
import threading as thread

def random_color_generator():
    return (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))

def play_audio(soundname):
    pygame.mixer.music.load("assets/sounds/"+soundname)
    pygame.mixer.music.play(0)

def change_paint_color(key):
    paint_color = GREEN
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

    return paint_color


def auto_generate_blocky(screen, BlockyBlock):    
    BlockyBlock.Generate_blocky(screen)
    thread.Timer(3, auto_generate_blocky, [screen, BlockyBlock]).start()
