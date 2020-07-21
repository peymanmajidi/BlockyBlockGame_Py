import pygame, math
import threading as thread
import gameplay
from contants import *

class BlockyBlock:
    players = list()
    def __init__(self, screen, character_name="NO NAME", color= YELLOW, x=0, y=0, emotion = Emotion.NORMAL, automatic=False, size = Character_Size.Normal):
        self.id = BlockyBlock.players.__len__()
        self.screen = screen
        self.input = Input()
        self.assign_keystrock(NONE_INPUT)
        self.name = character_name
        self.color = color
        self.primecolor = color
        self.eyes = Eyes()
        
        self.size = size
        self.jump_rate = int(self.size * 2.2)
        
        self.emotion = emotion
        self.jumping = False
        self.rising = False
        self.falling = False
        self.fall_played = True
        self.fall = 0
        self.rise= 0
        self.alive = True
        self.destroyed = False
        self.selected = False
        self.direction = Direction.FRONT

        self.auto = automatic

        self.set_x(x)
        self.set_y(y)
        self.falling_height = self.y

        BlockyBlock.players.append(self)
        if automatic:
            self.automatic()
        self.render_character()

    # static methods:
    numbers_of_kills = 0
    game_over = False
    def Generate_blocky(screen):
        size = Character_Size.random()
        x = random.randint(size ,WIDTH /2)
        emotion = Emotion.SAD
        automatic = True

        emotion = Emotion.SAD
        if x %3 ==0:
            automatic = False
            emotion = Emotion.NORMAL
        if x%20 == 0:
            x= (WIDTH //2)+ (WIDTH //3)
        player = BlockyBlock(screen, color=gameplay.random_color_generator(),x=x,y=1, emotion= emotion, automatic= automatic, size=size)
        player.assign_keystrock(NONE_INPUT)
        if x%3 == 0: player.direction = Direction.RIGHT
        if not player.auto:
            player.assign_keystrock(SECONDARY_INPUT)
        BlockyBlock.render_all()


    def update(keys):
        for player in BlockyBlock.players:
            player.proccess(keys)

    def action_manager(key):
        for player in BlockyBlock.players:
            player.action(key)

    def select(x, y):
        for player in BlockyBlock.players:
            if (x >= player.x and x <= (player.x + player.size)) and (y <= (player.y + player.size) and y >= player.y):
                if player.alive==False:
                    player.destroy()
                    return True
                if player.selected:
                    if player.direction == Direction.FRONT:
                        player.direction = Direction.RIGHT
                    player.shot()
                    return True
                if player.auto == False:
                    player.auto = True
                    player.automatic()
                    player.do_jump()
                else:
                    player.auto = False
                    player.automatic()

                return True
        return False
    
    def render_all():
        for player in BlockyBlock.players:
            player.render_character()
        return BlockyBlock.game_over

    # nonstatic methods:
    def set_as_player1(self):
        if self.alive == False:
            return
        self.auto = False
        list_of_selected = list(filter(lambda b: b.selected == True and b.alive == True, BlockyBlock.players))
        for selected in list_of_selected:
            selected.color = selected.primecolor
            selected.assign_keystrock(SECONDARY_INPUT)
            selected.emotion = Emotion.NORMAL
            selected.selected = False # deselect all
            selected.render_character()
        self.selected = True
        self.color = YELLOW
        self.emotion = Emotion.HAPPY
        self.assign_keystrock(STANDARD_INPUT)
        self.render_character()

    def assign_keystrock(self, input):
        self.input = input


    def set_x(self, x):
        if x + self.size >= WIDTH:
            x = WIDTH - self.size - 1
        if x <= 3:
            x = 3
        self.x = x

    def set_y(self, y):
        if y + self.size >= HEIGHT:
            self.destroy()
            return
        if y <= 1:
            y = self.size
            self.rising = False
            self.jumping= False
        self.y = y

    def move_x(self, move=1):
        self.set_x( self.x + move)

    def move_y(self, move=1):
        self.set_y( self.y + move)


    def render_character(self, emo = Emotion.NOT_SET):
        if self.destroyed:
            return
        x = self.x
        y = self.y
        if emo == Emotion.NOT_SET:
            emo = self.emotion
        pygame.draw.rect(self.screen, self.color, [ x ,y  , self.size , self.size ], 0 ) # [ ]
        self.eyes.left.x = x+int(self.size/2)- int(self.size / 5)
        self.eyes.left.y = y+int(self.size/2)-int(self.size / 5)

        self.eyes.right.x = x+int(self.size/2)+int(self.size / 5)
        self.eyes.right.y = y+int(self.size/2)-int(self.size / 5)

        if self.direction == Direction.RIGHT:
            self.eyes.move(int(self.size / 10))
            self.eyes.left.y +=1

        elif self.direction == Direction.LEFT:
            self.eyes.move(-int(self.size / 10))
            self.eyes.right.y +=1

        if self.alive:
            if  self.eyes.keep > 5: # winking
                pygame.draw.circle(self.screen, BLACK, self.eyes.left.get(), int(self.size / 15),0)
                pygame.draw.circle(self.screen, BLACK, self.eyes.right.get(),int(self.size / 15),0) 
                self.eyes.wink_period = random.randrange(100,1000) # random period for winking
            else:  # normal
                pygame.draw.circle(self.screen, BLACK,self.eyes.left.get(),int(self.size / 10),0)
                pygame.draw.circle(self.screen, BLACK,self.eyes.right.get(),int(self.size / 10),0) 
        else: # renser eyes when blocky is dead X:
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/10)+5,y+ int(self.size/8)+2),(x + int(self.size/3)+5,y+ int(self.size/3)+5))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/10)+5,y+ int(self.size/8)+2+1),(x + int(self.size/3)+5,y+ int(self.size/3)+5+1))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/10)+5,y+ int(self.size/8)+2+2),(x + int(self.size/3)+5,y+ int(self.size/3)+5+2))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/3)+5,y+ int(self.size/8)+2),(x + int(self.size/10)+5,y+ int(self.size/3)+5))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/3)+5,y+ int(self.size/8)+2+1),(x + int(self.size/10)+5,y+ int(self.size/3)+5+1))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/3)+5,y+ int(self.size/8)+2+2),(x + int(self.size/10)+5,y+ int(self.size/3)+5+2))

            pygame.draw.line(self.screen, BLACK, (x + int(self.size/10) + int(self.size/2),y+ int(self.size/8)+2),(x + int(self.size/3)+ int(self.size/2),y+ int(self.size/3)+5))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/10) + int(self.size/2),y+ int(self.size/8)+2+1),(x + int(self.size/3)+ int(self.size/2),y+ int(self.size/3)+5+1))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/10) + int(self.size/2),y+ int(self.size/8)+2+2),(x + int(self.size/3)+ int(self.size/2),y+ int(self.size/3)+5+2))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/3)+ int(self.size/2),y+ int(self.size/8)+2),(x + int(self.size/10)+ int(self.size/2),y+ int(self.size/3)+5))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/3)+ int(self.size/2),y+ int(self.size/8)+2+1),(x + int(self.size/10)+ int(self.size/2),y+ int(self.size/3)+5+1))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/3)+ int(self.size/2),y+ int(self.size/8)+2+2),(x + int(self.size/10)+ int(self.size/2),y+ int(self.size/3)+5+2))
        
    
        if emo == Emotion.SAD: # :(
            pygame.draw.arc(self.screen, BLACK, (x+( int(self.size/7)),y+int(self.size/1.7) , self.size-int(self.size / 5), self.size-int(self.size / 5)), math.pi/4,3* math.pi / 4 , int(self.size / 10))
        elif emo == Emotion.HAPPY: # :)
            pygame.draw.arc(self.screen, BLACK, (x+int(self.size / 10),y , self.size-int(self.size / 5), self.size-int(self.size / 5)), 5*math.pi/4,7* math.pi / 4 , int(self.size / 10))
        elif emo == Emotion.NORMAL or emo == Emotion.DEAD: # :|
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/5),y+ int(self.size/3 * 2)),(x+ self.size - int(self.size/5),y+ int(self.size/3 * 2)))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/5),y+ int(self.size/3 * 2)+1),(x+ self.size - int(self.size/5),y+ int(self.size/3 * 2)+1))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/5),y+ int(self.size/3 * 2)+2),(x+ self.size - int(self.size/5),y+ int(self.size/3 * 2)+2))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/5),y+ int(self.size/3 * 2)+3),(x+ self.size - int(self.size/5),y+ int(self.size/3 * 2)+3))
            pygame.draw.line(self.screen, BLACK, (x + int(self.size/5),y+ int(self.size/3 * 2)+4),(x+ self.size - int(self.size/5),y+ int(self.size/3 * 2)+4))
        elif emo == Emotion.WOW or not self.falling: # :o
            pygame.draw.arc(self.screen, BLACK, (x+int(self.size / 2.5),y+int(self.size / 1.8) , int(self.size / 3.5),  int(self.size / 3.5)), 0,2* math.pi  , int(self.size / 7))


    def clear_shadow(self):
        pygame.draw.rect(self.screen, BLACK, [ self.x, self.y, self.size , self.size ], 0)

    def turn_left(self):
        result = False
        self.clear_shadow()
        self.direction = Direction.LEFT

        if self.x - MOVE >= 0:
             if not Is_filled_pixel.left(self.screen, self.x, self.y, self.size):
                result = True
                self.move_x(-MOVE)
             elif not Is_filled_pixel.left(self.screen,self.x-MOVE+1, self.y-(MOVE*5), self.size):
                 result = True
                 self.move_x(-MOVE)
                 self.move_y(-MOVE)
        self.pushing_left()
        self.render_character()
        return result

    def turn_right(self):
        result = False
        self.clear_shadow()
        self.direction = Direction.RIGHT
        if self.x + self.size + MOVE <= WIDTH:
             if not Is_filled_pixel.right(self.screen,self.x, self.y, self.size):
                self.move_x(MOVE)
                result = True
             elif not Is_filled_pixel.right(self.screen,self.x + MOVE+1, self.y - (MOVE*5), self.size):
                self.move_x(MOVE)
                self.move_y(-MOVE)
                result = True
        self.pushing_right()
        self.render_character()
        return result

    def zoom_in(self):
        if self.size < 400:
            self.y-=10
            self.size+=10
            self.jump_rate = int(self.size * 1.8)
    
    def zoom_out(self):
        if self.size > 10:
            self.y+=10
            self.size-=10
            self.jump_rate = int(self.size * 1.8)

    def do_jump(self):
        if self.jumping or self.falling:
            return
        self.clear_shadow()
        self.jumping = True
        self.rising = True
        gameplay.play_audio("jump.wav")
        self.rise=0
        self.render_character()

    def action(self, key):
        if key == self.input.jump:
            self.do_jump()
        elif key == self.input.shot:
            self.shot()


    def proccess(self, keys): # run every miliseconds
        self.eyes.winking()
        if not Is_filled_pixel.bottom(self.screen,self.x, self.y, self.size) and not self.jumping:
            self.clear_shadow()
            if self.falling == False:
                self.falling_height = self.y
            self.falling = True
            self.fall_played = True
            
            self.move_y()
            self.render_character(emo= Emotion.WOW)
        else:
            self.falling = False

            if self.fall_played:
                if not self.auto:
                    gameplay.play_audio("fall.wav")     
                else:
                    if (self.y - self.falling_height) > 20: # hight fall
                        self.direction = Direction.LEFT if self.direction == Direction.RIGHT else Direction.RIGHT
                        self.render_character(Emotion.DEAD)

                self.fall_played = False
            self.falling_height = 0
        try:
            if(keys[self.input.left]):
                self.turn_left()
                

            elif(keys[self.input.right]):
                self.turn_right()
            

            if self.jumping:
                self.clear_shadow()
                if self.rising:
                    self.rise+=1
                    if not Is_filled_pixel.top(self.screen,self.x, self.y-1, self.size):
                        self.move_y(-1)
                    else:
                        self.jumping = False
                if self.rise > self.jump_rate:
                    self.rising = False
                    self.jumping= False
                self.render_character()
        except:
            pass
        

    def pushing_left(self): # pushing other players to left
        x1 = self.x - self.size - 1
        x2 = self.x + (2*self.size) + 1
        y1 = self.y - self.size - 1
        y2 = self.y + (2*self.size) + 1
        # players_arround = list(filter(lambda p: x1 <= p.x and x2 >= p.x + p.size and y1 <= p.y and y2 >= p.y + p.size, BlockyBlock.players) )
        for player in BlockyBlock.players:
            if player.id == self.id:
                continue
            if (self.x == player.x+ player.size ) or (self.x  == player.x+ player.size +1):
                if (self.y >= player.y and self.y <= (player.y + player.size)) or (self.y <= player.y and self.y + self.size >= player.y) or (self.y <= player.y and self.y+ self.size >= player.y + player.size) or ( self.y <= player.y and self.y+self.size <= player.size) :
                    player.turn_left()
    
    def pushing_right(self): # pushing other players to right
        x1 = self.x - self.size - 1
        x2 = self.x + (2*self.size) + 1
        y1 = self.y - self.size - 1
        y2 = self.y + (2*self.size) + 1
        # players_arround = list(filter(lambda p: x1 <= p.x and x2 >= p.x + p.size and y1 <= p.y and y2 >= p.y + p.size, BlockyBlock.players) )
        for player in BlockyBlock.players:
            if player.id == self.id:
                continue
            if (self.x + self.size == player.x) or (self.x + self.size +1 == player.x):
                if (self.y >= player.y and self.y <= (player.y + player.size)) or (self.y <= player.y and self.y + self.size >= player.y) or (self.y <= player.y and self.y+ self.size >= player.y + player.size) or ( self.y <= player.y and self.y+self.size <= player.size) :
                    player.turn_right()

    def kill_me(self):
        self.alive = False
        self.color = DEAD
        self.emotion = Emotion.DEAD
        self.assign_keystrock(NONE_INPUT)
        self.render_character()
    
    def destroy(self):
        BlockyBlock.numbers_of_kills+=1
        title = GAME_TITLE + " | kills: " + BlockyBlock.numbers_of_kills.__str__()
        pygame.display.set_caption(title)
        if self.selected:
            BlockyBlock.game_over = True

        self.destroyed = True
        self.clear_shadow()
        BlockyBlock.players.remove(self)



    def shot(self):
        auto = self.auto
        self.auto = False

        # killing other players
        if self.direction == Direction.RIGHT:
            laser_x = WIDTH
            x=self.eyes.left.x
            y=self.eyes.left.y
            list_of_blocky = list(filter(lambda p:p.id!= self.id and 
                    x< p.x and (y>=p.y and y<= p.y+p.size) ,BlockyBlock.players))
            list_of_blocky.sort(key= lambda p: p.x, reverse= False)
            for p in list_of_blocky:
                laser_x = p.x
                if p.alive:
                    p.kill_me()
                else:
                    p.destroy()
                break
        else:
            laser_x = 0
            x=self.eyes.right.x
            y=self.eyes.right.y
            list_of_blocky = list(filter(lambda p:p.id!= self.id and 
                    x> p.x and (y>=p.y and y<= p.y+p.size) ,BlockyBlock.players))
            list_of_blocky.sort(key= lambda p: p.x, reverse= True)
            for p in list_of_blocky:
                laser_x = p.x + p.size
                if p.alive:
                    p.kill_me()
                else:
                    p.destroy()
                    
                break

        # draw laser
        if self.direction == Direction.RIGHT or  self.direction == Direction.FRONT:
            pygame.draw.line(self.screen, LASER, self.eyes.left.get2(), (laser_x,self.eyes.left.y),int(self.size/10))
            pygame.draw.line(self.screen, LASER2, self.eyes.right.get2(), (laser_x,self.eyes.left.y),int(self.size/10))
        else:
            pygame.draw.line(self.screen, LASER, self.eyes.left.get2(), (laser_x,self.eyes.left.y),int(self.size/10))
            pygame.draw.line(self.screen, LASER2, self.eyes.right.get2(), (laser_x,self.eyes.left.y),int(self.size/10))

        gameplay.play_audio("laser.wav")

        self.render_character(Emotion.SAD)
        pygame.display.update()
        pygame.time.wait(30)

        # clean laser
        if self.direction == Direction.RIGHT or  self.direction == Direction.FRONT:
            pygame.draw.line(self.screen, BLACK, (self.eyes.left.x +1,self.eyes.left.y-int(self.size/5)), (WIDTH,self.eyes.left.y-int(self.size/5)),int(self.size/2))
        else:
            pygame.draw.line(self.screen, BLACK, (self.eyes.right.x+1,self.eyes.right.y-int(self.size/5)), (0,self.eyes.right.y-int(self.size/5)),int(self.size/2))

        
        self.auto = auto
        if auto:
            self.automatic()
        BlockyBlock.render_all()


    def automatic(self):
        if self.auto == False:
            return
        if self.selected:
            self.auto = False
            return
        if self.destroyed or self.alive == False:
            return
        if not self.falling:
            if self.direction == Direction.RIGHT:
                r = self.turn_right()
                if r == False:
                    self.direction = Direction.LEFT
            else:
                r = self.turn_left()
                if r == False:
                    self.direction = Direction.RIGHT
        thread.Timer(0.0001, self.automatic).start()


class Eyes:
    def __init__(self):
        self.left = Point()
        self.right = Point()
    def move(self, x):
        self.left.x +=x
        self.right.x +=x
    # winking eyes        
    wink = False # last wink status
    wink_idle = 0 # eye winking when blocky is idle
    wink_period = 20
    keep = 0
    def winking(self):
        self.wink_idle +=1 
        if self.wink_idle % self.wink_period == 0:
            self.wink_idle = 0
            self.wink = True
            self.keep = 30
    
        if self.wink:
            self.keep -=1

class Is_filled_pixel:
    def left(screen, x,y,size):
        for i in range(size):
            dot = screen.get_at((x-MOVE,y+i))
            if dot[0] > 0:
                return True
            if dot[1] > 0:
                return True
            if dot[2] > 0:
                return True
        return False

    def right(screen, x,y,size):        
        for i in range(size):
            dot = screen.get_at((x+MOVE + size,y+i))
            if dot[0] > 0:
                return True
            if dot[1] > 0:
                return True
            if dot[2] > 0:
                return True
        return False

    def top(screen, x,y,size):     
        for i in range(size):
            dot = screen.get_at((x+i,y-MOVE))
            if dot[0] > 0:
                return True
            if dot[1] > 0:
                return True
            if dot[2] > 0:
                return True
        return False

    def bottom(screen, x,y,size):
        try:
            for i in range(size):
                dot = screen.get_at((x+i,y+size+MOVE))
                if dot[0] > 0:
                    return True
                if dot[1] > 0:
                    return True
                if dot[2] > 0:
                    return True
        except:
            pass  

        return False



class Point:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    def set(self, x,y):
        self.x = x
        self.y = y
    def get(self):
        return [self.x, self.y]
    def get2(self):
        return (self.x, self.y)

