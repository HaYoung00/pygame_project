#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys, random

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf


# [loc, velocity, timer]
particles = []

game_display_flag = False
new_surf = pygame.Surface((500, 500))
rad = 0
circle_pause = False
loop_cnt = 0
# Loop ------------------------------------------------------- #
while True:

    # Background --------------------------------------------- #
    screen.fill((20,20,60))
    mx, my = pygame.mouse.get_pos()
    if not game_display_flag:
        new_surf.fill((0,0,0))
        new_surf.blit(circle_surf(rad, (255,255,255)), (mx - rad, my - rad))
        screen.blit(new_surf, pygame.math.Vector2(), special_flags=BLEND_RGB_MULT)
        if not circle_pause: rad += 10
        if rad > 100:
            loop_cnt += 1
            circle_pause = True
            if loop_cnt == 1:
                pause_start = pygame.time.get_ticks()
            else:
                pause_end = pygame.time.get_ticks()
                if pause_end - pause_start > 300:
                    circle_pause = False
        if rad > 700: game_display_flag = True


    particles.append([[mx, my], [random.randint(0, 20) / 10 - 1, -5], random.randint(6, 11)])
    for particle in particles:
        particle[0][1] += particle[1][1]
        particle[2] -= 0.5
        particle[1][1] += 0.15
        pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        radius = particle[2] * 2
        screen.blit(circle_surf(radius, (20, 20, 60)), (int(particle[0][0] - radius), int(particle[0][1] - radius)), special_flags=BLEND_RGB_ADD)
        if particle[2] <= 0:
            particles.remove(particle)

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)