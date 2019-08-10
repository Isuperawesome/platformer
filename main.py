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
                 
        # INPUTS                    
                    
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
        

        # UPDATES

        timenow = pygame.time.get_ticks()

        dt = (timenow - timebefore)/1000

        cube.update(dt)

        #collision check

        if cube.currentstate == "GROUNDED":
            pass
            # handles when you walk off of a platform
        elif cube.currentstate == "AIRBORNE":
            # check if player has landed onto a platform
            if cube.dy < 0: 
                for platform in [ platform for platform in logs.rectangles if (
                                            # left side of the platform is to the left of the player's right
                                            (platform[0] < cube.x + cube.xdim) and
                                            # right side of the platform is to the right of the player's left
                                            (platform[0] + platform[2] > cube.x) and
                                            # top of platform is below the bottom of the player
                                            (platform[1] > cube.y + cube.ydim)
                                            )]:
                    # print("projected y position", cube.y + cube.ydim +  cube.get_next_dy(dt), "current platform top: ", platform[1])
                    if (cube.y + cube.ydim - cube.get_next_dy(dt)) > platform[1]:
                        print("land")
                        cube.ground_to(platform[1])

        timebefore = timenow

        # DRAWING

        screen.fill(bgcolor)

        for platform in logs.rectangles:
            pygame.draw.rect(screen, (119,92,44),platform)
        screen.blit(cube.img, (cube.x, cube.y))

        pygame.display.flip()

    
if __name__=="__main__":
    main()