import pygame

class platforms:

    def __init__(self, gamex, gamey):
        self.rectangles = [
            # (x,y,w,h)
            (100,400,70,10),
            (200,500,50,10),
            (200,400,50,10),

        ]

    def draw(self, surface):
        for platform in self.rectangles:
            pygame.draw.rect(surface, (119,92,44), platform)
