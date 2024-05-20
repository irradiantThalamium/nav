# okay lets do this
# uhhhhh

import pygame
import random
from datetime import datetime
# v MY FILES v
from fhandler import conRead

pygame.init()
screen = pygame.display.set_mode((160, 120),conRead("startup.con"))
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("Null and Vøid | v0.0")
clock = pygame.time.Clock()
running = True

now = datetime.now()
logInit = now.strftime("%d-%m-%Y-%H%M%S")
logfl = open("logs/"+logInit+".txt", "w")
logfl.write(f"-- LOG START --\n- Time: {logInit} -\n")
logfl.close()

def log(txt):
    logfl = open("logs/"+logInit+".txt", "a")
    logfl.write(f"--{txt}")
    logfl.close()
    print(txt)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

    screen.fill("white") #remove this later, i love screen bleed
    
    clock.tick(60) 
pygame.quit()
logInit = now.strftime("%d-%m-%Y-%H%M%S")
logfl = open("logs/"+logInit+".txt", "w")
logfl.write(f"-- LOG END --\n- Time: {logInit} -\n")
logfl.close()
