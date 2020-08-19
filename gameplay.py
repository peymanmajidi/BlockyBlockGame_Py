import random, pygame, time, os
from contants import GREEN
import ui as UI
import threading as thread
from blocky_block import BlockyBlock
from contants import *

paint_color = GREEN
clicked = False
game_over = False

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


def blocky_generator(screen, second):
    thread.Timer(second, generate, [screen, second]).start()


def generate(screen, second):
    BlockyBlock.Generate_blocky(screen)
    thread.Timer(second, generate, [screen, second]).start()




def arrow_keys(window, events):
    global clicked, paint_color
    for event in events.get():
        if event.type == pygame.QUIT:
            os._exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN: # mouse click event
            x,y = event.pos
            print(x,y)
            if BlockyBlock.select(x,y):
                clicked = False
            else:
                clicked = True

        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False


        if clicked:
            try:
                x2,y2 = event.pos
                pygame.draw.rect(window, paint_color, [x2,y2,20,20],0)
            except:
                pass
            pygame.display.update()


        if event.type == pygame.KEYDOWN:
            pygame.display.update()
            BlockyBlock.action_manager(event.key)

            if event.key == pygame.K_TAB:
                BlockyBlock.Generate_blocky(window)

            if event.key == pygame.K_ESCAPE:
                os._exit(0)

            paint_color = change_paint_color(event.key)
            UI.mouse_color(window, paint_color)
                
            if event.key == pygame.K_c: # clear all drawing
                pygame.draw.rect(window, BLACK, [0,0,WIDTH, HEIGHT],0)
                BlockyBlock.render_all()