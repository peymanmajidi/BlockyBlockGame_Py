import pygame, time
from contants import *
import gameplay



def text(screen, text, x, y, color = (255,255,255), size = 50, font_type = './assets/fonts/font2.ttf'):
    text = str(text)
    font = pygame.font.Font(font_type, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))
    
def game_over(screen):
    text(screen, "GAME_OVER", x= int(WIDTH/2) - 230, y=int(HEIGHT/10),size= 85, color= WHITE)
    pygame.display.update()
    gameplay.play_audio("game_over.mp3")
    time.sleep(2)

def mouse_color(screen, paint_color):
    pygame.draw.rect(screen, paint_color, [0,0,30,30],0)
    

def console_help():
    print("""Welcome to Blocky Blocky (B.b)
It is a fight between mouse cursor and Blocky Block !

Use Arrow keys to move around, press [space bar] to jump: yellow blocky
Press a-w-d to move other blockies
Hit [Enter] to shot laser gun
Press [+] and [-] keys to make the B.b bigger or smaller
Finally, [click] anywhere of playground by Mouse to draw anything you like; B.B can move and jump over them

Other useful trick:
C: Clear the playground
G: Green brush
R: Red brush

Press [tab] to generate new blocky
""")

def full_frame(screen, thickness):
    pygame.draw.rect(screen, WHITE, [ 0 ,0, WIDTH , HEIGHT+thickness ], thickness ) # Full FRAME

def level_01(screen):
    full_frame(screen, 15)

    pygame.draw.line(screen, WHITE, (500,630), (WIDTH-500,630),10)

    pygame.draw.line(screen, WHITE, (1100,480), (WIDTH,480),10)


    pygame.draw.line(screen, WHITE, (250,720), (1000,720),10)


    pygame.draw.line(screen, GREEN, (90,140), (250,145),10)
    pygame.draw.line(screen, GREEN, (200,240), (360,230),15)
    pygame.draw.line(screen, GREEN, (50,335), (250,330),18)
    pygame.draw.line(screen, GREEN, (150,430), (350, 425),22)
    pygame.draw.line(screen, GREEN, (90,515), (480, 525),15)

    pygame.draw.line(screen, WHITE, (890,1), (950,1),50)

    x = 10
    y = 90

    pygame.draw.polygon(screen, RED, ((0 +x, 10+y), (0+x, 20+y), (20+x, 20+y), (20+x, 30+y), (30+x, 15+y), (20+x, 0+y), (20+x, 10+y)))


    text(screen, "LEVEL 01", 600,200, WHITE, 35)

    




    



