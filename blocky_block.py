from libraries import *
from game_contants import *

window = pygame.display.set_mode((WIDTH, HEIGHT))

class BlockyBlock:
    players = list()
    def __init__(self, character_name, color, x=0, y=0):
        self.id = BlockyBlock.players.__len__()
        self.name = character_name
        self.color = color
        self.primecolor = color
        self.eyes = Eyes()
        self.x = x
        self.y = y
        self.jumping = False
        self.rising = False
        self.falling = False
        self.fall_played = True
        self.fall = 0
        self.rise= 0
        self.selected = False
        self.direction = Direction.FRONT
        self.input = Input()
        if x == 0:
            self.x = int(CHARCTER) * 5
        if y == 0:
            self.y = int(CHARCTER)

        BlockyBlock.players.append(self)
        self.render_character()

    # static methods:
    def event_listener(keys):
        for player in BlockyBlock.players:
            player.event_handler(keys)

    def action_manager(key):
        for player in BlockyBlock.players:
            player.action(key)

    def select(x, y):
        for player in BlockyBlock.players:
            if (x >= player.x and x <= (player.x + CHARCTER)) and (y <= (player.y + CHARCTER) and y >= player.y):
                player.select_me()
                player.color = WHITE
                player.render_character()
                return True
        return False

    # nonstatic methods:
    def select_me(self):
        list_of_selected = list(filter(lambda b: b.selected == True, BlockyBlock.players))
        for selected in list_of_selected:
            selected.color = selected.primecolor
            selected.assign_keystrock(SECONDARY_INPUT)
            selected.selected = False # deselect all
        self.selected = True
        self.color = WHITE
        self.assign_keystrock(STANDARD_INPUT)
        self.render_character()

    def assign_keystrock(self, input):
        self.input = input

    def set_x(self, x):
        if x + CHARCTER >= WIDTH:
            x = WIDTH - CHARCTER - 1
        if x < 3:
            x = 3
        self.x = x

    def set_y(self, y):
        if y + CHARCTER >= HEIGHT:
            y = HEIGHT - CHARCTER - 1
        if y < 3:
            y = 3
        self.y = y


    def render_character(self, emo = Emotion.HAPPY):
        x = self.x
        y = self.y
        pygame.draw.rect(window, self.color, [ x ,y  , CHARCTER , CHARCTER ], 0 ) # [ ]
        self.eyes.left.x = x+int(CHARCTER/2)- int(CHARCTER / 5)
        self.eyes.left.y = y+int(CHARCTER/2)-int(CHARCTER / 5)

        self.eyes.right.x = x+int(CHARCTER/2)+int(CHARCTER / 5)
        self.eyes.right.y = y+int(CHARCTER/2)-int(CHARCTER / 5)

        if self.direction == Direction.RIGHT:
            self.eyes.move(int(CHARCTER / 10))
            self.eyes.left.y +=1

        elif self.direction == Direction.LEFT:
            self.eyes.move(-int(CHARCTER / 10))
            self.eyes.right.y +=1


        if  self.eyes.keep > 5:
            pygame.draw.circle(window, BLACK, self.eyes.left.get(), int(CHARCTER / 15),0) #[.]
            pygame.draw.circle(window, BLACK, self.eyes.right.get(),int(CHARCTER / 15),0) # [..]
            self.eyes.wink_period = random.randrange(100,1000) # random period for winking
        else:       
            pygame.draw.circle(window, BLACK,self.eyes.left.get(),int(CHARCTER / 10),0) #[.]
            pygame.draw.circle(window, BLACK,self.eyes.right.get(),int(CHARCTER / 10),0) # [..]
        
    
        if emo == Emotion.SAD:
            pygame.draw.arc(window, BLACK,  (x+(x+int(CHARCTER / 10)),y+(x+int(CHARCTER / 2)) , CHARCTER-int(CHARCTER / 5), CHARCTER-int(CHARCTER / 5)), math.pi/4,3* math.pi / 4 , int(CHARCTER / 10)) # :(

        elif not self.falling:
            pygame.draw.arc(window, BLACK,  (x+int(CHARCTER / 10),y , CHARCTER-int(CHARCTER / 5), CHARCTER-int(CHARCTER / 5)), 5*math.pi/4,7* math.pi / 4 , int(CHARCTER / 10)) # :)
        else:
            pygame.draw.arc(window, BLACK,  (x+int(CHARCTER / 2.5),y+int(CHARCTER / 1.8) , int(CHARCTER / 3.5),  int(CHARCTER / 3.5)), 0,2* math.pi  , int(CHARCTER / 7)) # :O

    def clear_shadow(self):
        pygame.draw.rect(window, BLACK, [ self.x, self.y, CHARCTER , CHARCTER ], 0)

    def turn_left(self):
        self.clear_shadow()
        self.direction = Direction.LEFT
        if self.x - MOVE >= 0:
             if not Is_filled_pixel.left(self.x, self.y):
                self.x-= MOVE
             elif not Is_filled_pixel.left(self.x-MOVE+1, self.y-(MOVE*5)):
               self.x-= MOVE
               self.y-= MOVE
        self.pushing_left()
        self.render_character()

    def turn_right(self):
        self.clear_shadow()
        self.direction = Direction.RIGHT
        if self.x + CHARCTER + MOVE <= WIDTH:
             if not Is_filled_pixel.right(self.x, self.y):
                self.x+= MOVE
             elif not Is_filled_pixel.right(self.x + MOVE+1, self.y - (MOVE*5)):
               self.x+= MOVE
               self.y-= MOVE
        self.pushing_right()
        self.render_character()

    def zoom_in(self):
        global CHARCTER
        global JUMP
        if CHARCTER < 400:
            self.y-=10
            CHARCTER+=10
            JUMP = int(CHARCTER * 1.8)
    
    def zoom_out(self):
        global CHARCTER
        global JUMP
        if CHARCTER > 10:
            self.y+=10
            CHARCTER-=10
            JUMP = int(CHARCTER * 1.8)

    def do_jump(self):
        if self.jumping or self.falling:
            return
        self.clear_shadow()
        self.jumping = True
        self.rising = True
        play_audio("jump.wav")
        self.rise=0

    def action(self, key):
        if key == self.input.jump:
            self.do_jump()
        elif key == self.input.shot:
            self.shot()


    def event_handler(self, keys):
        self.eyes.winking()
        if not Is_filled_pixel.bottom(self.x, self.y) and not self.jumping:
            self.clear_shadow()
            self.y+=1
            self.falling = True
            self.fall_played = True
        else:
            self.falling = False
            if self.fall_played:
                play_audio("fall.wav")
                self.fall_played = False

        if(keys[self.input.left]):
            self.turn_left()
            

        elif(keys[self.input.right]):
            self.turn_right()
           

        if self.jumping:
            self.clear_shadow()
            if self.rising:
                self.rise+=1
                if not Is_filled_pixel.top(self.x, self.y-1):
                    self.y-=1
                else:
                    self.jumping = False
            if self.rise > JUMP:
                self.rising = False
                self.jumping= False
        
        self.render_character()

    def pushing_left(self): # pushing other players to left
        x1 = self.x - CHARCTER - 1
        x2 = self.x + (2*CHARCTER) + 1
        y1 = self.y - CHARCTER - 1
        y2 = self.y + (2*CHARCTER) + 1
        players_arround = list(filter(lambda p: x1 <= p.x and x2 >= p.x + CHARCTER and y1 <= p.y and y2 >= p.y + CHARCTER, BlockyBlock.players) )
        for player in players_arround:
            if player.id == self.id:
                continue
            if (self.x == player.x+ CHARCTER ) or (self.x  == player.x+ CHARCTER +1):
                if (self.y - CHARCTER <= player.y-CHARCTER and self.y > player.y-CHARCTER) or ( self.y - CHARCTER > player.y - CHARCTER and self.y - CHARCTER < player.y ):
                    player.turn_left()
    
    def pushing_right(self): # pushing other players to right
        x1 = self.x - CHARCTER - 1
        x2 = self.x + (2*CHARCTER) + 1
        y1 = self.y - CHARCTER - 1
        y2 = self.y + (2*CHARCTER) + 1
        players_arround = list(filter(lambda p: x1 <= p.x and x2 >= p.x + CHARCTER and y1 <= p.y and y2 >= p.y + CHARCTER, BlockyBlock.players) )
        for player in players_arround:
            if player.id == self.id:
                continue
            if (self.x + CHARCTER == player.x) or (self.x + CHARCTER +1 == player.x):
                if (self.y - CHARCTER <= player.y-CHARCTER and self.y > player.y-CHARCTER) or ( self.y - CHARCTER > player.y - CHARCTER and self.y - CHARCTER < player.y ):
                    player.turn_right()

    def shot(self):
        global WIDTH
        self.render_character(Emotion.SAD)

        eyes2 = Eyes()
        eyes2.left = self.eyes.left
        eyes2.right = self.eyes.right
        
        # draw laser
        if self.direction == Direction.RIGHT or  self.direction == Direction.FRONT:
            pygame.draw.line(window, LASER, eyes2.left.get2(), (WIDTH,eyes2.left.y),int(CHARCTER/10))
            pygame.draw.line(window, LASER2, eyes2.right.get2(), (WIDTH,eyes2.left.y),int(CHARCTER/10))
        else:
            pygame.draw.line(window, LASER, eyes2.left.get2(), (0,eyes2.left.y),int(CHARCTER/10))
            pygame.draw.line(window, LASER2, eyes2.right.get2(), (0,eyes2.left.y),int(CHARCTER/10))

        play_audio("laser.wav")

        pygame.display.update()
        pygame.time.delay(40)
        self.render_character(Emotion.SAD)

        # clean laser
        if self.direction == Direction.RIGHT or  self.direction == Direction.FRONT:
            pygame.draw.line(window, BLACK, (eyes2.left.x +1,eyes2.left.y-int(CHARCTER/5)), (WIDTH,eyes2.left.y-int(CHARCTER/5)),int(CHARCTER/2))
        else:
            pygame.draw.line(window, BLACK, (eyes2.right.x+1,eyes2.right.y-int(CHARCTER/5)), (0,eyes2.right.y-int(CHARCTER/5)),int(CHARCTER/2))

        pygame.display.update()

class Eyes:
    left = Point()
    right = Point()
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
    def left(x,y):
        for i in range(CHARCTER):
            dot = window.get_at((x-MOVE,y+i))
            if dot[0] > 0:
                return True
            if dot[1] > 0:
                return True
            if dot[2] > 0:
                return True
        return False

    def right(x,y):        
        for i in range(CHARCTER):
            dot = window.get_at((x+MOVE + CHARCTER,y+i))
            if dot[0] > 0:
                return True
            if dot[1] > 0:
                return True
            if dot[2] > 0:
                return True
        return False

    def top(x,y):     
        for i in range(CHARCTER):
            dot = window.get_at((x+i,y-MOVE))
            if dot[0] > 0:
                return True
            if dot[1] > 0:
                return True
            if dot[2] > 0:
                return True
        return False

    def bottom(x,y):
        try:
            for i in range(CHARCTER):
                dot = window.get_at((x+i,y+CHARCTER+MOVE))
                if dot[0] > 0:
                    return True
                if dot[1] > 0:
                    return True
                if dot[2] > 0:
                    return True
        except:
            pass  

        return False


