import pygame

class cube:

    def __init__(self, gamex, gamey):
        self.gamex = gamex
        self.gamey = gamey
        self.x = 50
        self.y = 100
        self.img = pygame.image.load('sqaureblue.jpg')
        self.xdim = self.img.get_rect().size[0]
        self.ydim = self.img.get_rect().size[1]
        self.yvel = 0
        self.xvel = 0
        self.gravity = -10
        self.dy = 0
        self.plat_bounds = []
        self.on_ground = False

        self.states = ['GROUNDED',"AIRBRONE"]
        # self.currentstate = 'GROUNDED'
        self.currentstate = 'AIRBORNE'
        
    def get_next_dy(self,dt):
        return (self.yvel+self.gravity)*dt
    
    def update(self, dt):
 
        if self.currentstate == 'AIRBORNE':
            self.yvel = self.yvel + self.gravity
            self.dy = self.yvel*dt
            self.y -= self.dy

        # grounding 
        if self.y + self.ydim > self.gamey:
            self.ground_to((0,self.gamey,self.gamex,0),True)

    def ground_to(self, rect,isGround):
        self.currentstate = 'GROUNDED'
        self.yvel = 0
        self.y = rect[1] - self.ydim
        self.plat_bounds = [rect[0],rect[0]+rect[2]]
        self.on_ground = isGround

    def keydown_handle(self, keydowns):
        if keydowns[pygame.K_LEFT]:
            if self.currentstate == "GROUNDED":
                self.x -= 0.7
            else:
                self.x -= 1.1
            if self.x < 0:
                self.x = 0
        if keydowns[pygame.K_RIGHT]:
            if self.currentstate == "GROUNDED":
                self.x += 0.7
            else:
                self.x += 1.1
            if self.x + self.xdim > self.gamex:
                self.x = self.gamex - self.xdim
        if keydowns[pygame.K_UP]:
            if self.currentstate == "GROUNDED":
                self.currentstate = "AIRBORNE"
                self.yvel = 1500

    def draw(self, surface):
        surface.blit(self.img,(self.x, self.y))
