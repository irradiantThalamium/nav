# okay lets do this
# uhhhh

import pygame
import random
from pypresence import Presence
from datetime import datetime
# v MY FILES v
from fhandler import conRead, startLog, log, endLog
from tzmath import hypoCalc

pygame.init()
screen = pygame.display.set_mode((160, 120),conRead("startup.con")[0])
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("Null and Vøid | v0.0")
clock = pygame.time.Clock()
discID = "1241919126453227621"
pres = Presence(discID)
pres.connect()
running = True

lines=["Terrah is regretting her life choices...", "// why did i st4rt this 464in?", "This really sucks.", "What the FUCK is a binary space partition and why is it important?!", "Shade and Furia have it easy. I have to code.", "Triple D! ...i hate it."]
line=random.choice(lines)

#startLog()
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

    screen.fill("white") #remove this later, i love screen bleed
    
    pres.update(state=line,details="Coding...")
    clock.tick(60) 
pygame.quit()
#endLog()

