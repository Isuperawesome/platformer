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
        # self.y = gamey - self.ydim

        self.states = ['GROUNDED',"AIRBRONE"]
        # self.currentstate = 'GROUNDED'
        self.currentstate = 'AIRBORNE'
        
    
    def update(self, dt):
 
        if self.currentstate == 'AIRBORNE':
            self.yvel = self.yvel + self.gravity
            dy = self.yvel*dt
            self.y -= dy


        # grounding 
        if self.y + self.ydim > self.gamey:
            self.y = self.gamey - self.ydim
            self.yvel = 0
            self.currentstate = 'GROUNDED'
        
            


    


        
