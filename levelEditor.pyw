# level editor

import pygame
from pypresence import Presence
import time
from tzuihandler import Window
from fhandler import findPath

lvlname = input("> Level Title:")
lvlauth = input("> Level Author(s):")
lvldesc = input("> Level Description:")

newlvl = open("levels/"+lvlname+".ulm", "w")

newlvl.write("-- ULevel Map --\n")
newlvl.write("Author: "+lvlauth+"\n")
newlvl.write("MapName: "+lvlname+"\n")
newlvl.write(lvldesc+"\n")

pygame.init()
screen = pygame.display.set_mode((1600, 1200))
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("NaV Level Editor | v0.0")
discID = "1241919126453227621"
pres = Presence(discID)
pres.connect()

running = True

strt = time.time()

uhm = Window((800,600),(100,100),"testing",[])

camoffx = 0
camoffy = 0

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for i in range(0,21):
        pygame.draw.line(screen,(26,25,50),(i*80+(camoffx%80),0),(i*80+(camoffx%80),1200),2)
    for i in range(0,16):
        pygame.draw.line(screen,(26,25,50),(0,i*80+(camoffy%80)),(1600,i*80+(camoffy%80)),2)
            
    if keys[pygame.K_w]:
        camoffy += 4
    if keys[pygame.K_a]:
        camoffx += 4
    if keys[pygame.K_s]:
        camoffy -= 4
    if keys[pygame.K_d]:
        camoffx -= 4
    
    uhm.draw(screen)
    
    pygame.display.flip()
    screen.fill((14,7,27))
    
    pres.update(state="Designing levels...",start=strt,large_image="https://raw.githubusercontent.com/TerrahBlu/nav/main/lowrestrans.png",large_text="trans rights!",small_image="https://raw.githubusercontent.com/TerrahBlu/nav/main/pres.png",small_text="Not Copyrighted, Unnamed Studios 2024")
    
pygame.quit()
pres.close()
newlvl.close()