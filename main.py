import pygame
import player
import platforms
# from pygame.locals import *

def main():
    pygame.init()
    bgcolor = (255, 255, 255)
    running = True
    gamex, gamey = 960,540 
    screen = pygame.display.set_mode((gamex, gamey), pygame.RESIZABLE)
    cube = player.cube(gamex, gamey)
    logs = platforms.platforms(gamex, gamey)
    dt = 0
    timenow, timebefore = 0, 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_s:
                    print(cube.currentstate)
                   
        pressed = pygame.key.get_pressed()
          
        if pressed[pygame.K_LEFT]:
            if cube.currentstate == 'GROUNDED':
                cube.x -= 0.7
            else:
                cube.x -= 1.1
            if cube.x < 0:
                cube.x = 0  
        if pressed[pygame.K_RIGHT]:
            if cube.currentstate == 'GROUNDED':
                cube.x += 0.7
            else:
                cube.x += 1.1
            if cube.x + cube.xdim > gamex:
                cube.x = gamex - cube.xdim

        if pressed[pygame.K_UP]:
            if cube.currentstate == 'GROUNDED':
                cube.currentstate = 'AIRBORNE'
                cube.yvel = 1500
        
        timenow = pygame.time.get_ticks()

        dt = (timenow - timebefore)/1000
        cube.update(dt)
        timebefore = timenow
              
        screen.fill(bgcolor)

        for platform in logs.rectangles:
            pygame.draw.rect(screen, (119,92,44),platform)
        screen.blit(cube.img, (cube.x, cube.y))

        pygame.display.flip()

    
if __name__=="__main__":
    main()