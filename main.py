# okay lets do this
# uhhhh

import pygame
import random
from datetime import datetime
# v MY FILES v
from fhandler import conRead, startLog, log, endLog

pygame.init()
screen = pygame.display.set_mode((160, 120),conRead("startup.con")[0])
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("Null and Vøid | v0.0")
clock = pygame.time.Clock()
running = True

startLog()
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

    screen.fill("white") #remove this later, i love screen bleed
    
    clock.tick(60) 
pygame.quit()
endLog()

