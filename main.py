# okay lets do this
# uhhhh

import random
import pygame
from pypresence import Presence
import math
# v MY FILES v
from fhandler import conRead, startLog, log, endLog, randInit
from tzmath import hypoCalc, radToDeg, degToRad

pygame.init()
screen = pygame.display.set_mode((160, 120),conRead("startup.con")[0])
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("Null and Vøid | v0.0")
clock = pygame.time.Clock()
discID = "1241919126453227621"
pres = Presence(discID)
pres.connect()
running = True

rand = randInit()

lines=["Terrah is regretting her life choices.", "// why did i st4rt this 464in?", "This really sucks.", "What the FUCK is a binary space partition", "Shade and Furia have it easy. I have to code.", "Triple D! ...I hate it.", "I fucking HATE angles."]
line=random.choice(lines)

def drpx(lx,ly,col):
    tp = pygame.Rect(lx,ly,1,1)
    pygame.draw.rect(screen,col,tp)

class plyr:
    def __init__(self):
        self.x,self.y,self.z = 70,-110,20
        self.dx,self.dy,self.dz = 0,0,0
        self.a,self.l,self.spd = 0,0,4

    def upd(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.a-=4
        if keys[pygame.K_d]:
            self.a+=4
            
        if keys[pygame.K_UP]:
            self.l+=4
        if keys[pygame.K_DOWN]:
            self.l-=4
        
                
        mmv = pygame.mouse.get_rel()
        
        self.a += round(mmv[0]/100)
        self.l += round(mmv[1]/100)
        
        if self.a<0:
            self.a+=360
        elif self.a>359:
            self.a-=360
            
        
        if self.l<0:
            self.l+=360
        elif self.l>350:
            self.l-=360
                
        self.dx=math.sin(self.a)*self.spd
        self.dy=math.cos(self.a)*self.spd
        
        if keys[pygame.K_w]:
            self.x += self.dx
            self.y += self.dy
        if keys[pygame.K_s]:
            self.x -= self.dx
            self.y -= self.dy
            
        if keys[pygame.K_LEFT]:
            self.x += self.dy
            self.y -= self.dx
        if keys[pygame.K_RIGHT]:
            self.x -= self.dy
            self.y += self.dx
            
        if keys[pygame.K_q]:
            self.z -= 4
        if keys[pygame.K_e]:
            self.z += 4
        
        
        
pl = plyr()

def draw3d():
    wx, wy, wz = [0,0,0,0],[0,0,0,0],[0,0,0,0]
    cs, sn = math.cos(degToRad(pl.a)), math.sin(degToRad(pl.a)) # it would be REALLY FUNNY WOULDNT IT
    x1, y1 = 40-pl.x, 10-pl.y 
    x2, y2 = 40-pl.x, 290-pl.y
    wx[0]=(x1*cs)-(y1*sn)
    wx[1]=(x2*cs)-(y2*sn)
    
    wy[0]=(y1*cs)-(x1*sn)
    wy[1]=(y2*cs)-(x2*sn)
    
    wz[0]=0-pl.z+((pl.l*wy[0])/64)
    wz[1]=0-pl.z+((pl.l*wy[1])/32)
    
    if wy[0]!=0:
        wx[0],wy[0]=wx[0]*200/wy[0]+80, wz[0]*200/wy[0]+60
    else:
        wx[0],wy[0]=80,60
    if wy[1]!=0:
        wx[1],wy[1]=wx[1]*200/wy[1]+80, wz[1]*200/wy[1]+60
    else:
        wx[1],wy[1]=80,60
    
    if wx[0]>0 and wx[0]<160 and wy[0]>0 and wy[0]<120: 
        drpx(wx[0],wy[0],"red")
    if wx[1]>0 and wx[1]<160 and wy[1]>0 and wy[1]<120: 
        drpx(wx[1],wy[1],"red")
#     pygame.draw.line(screen,"black",[wx[0],wy[0]],[wx[1],wy[1]])
    

#startLog()
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pl.upd()
    draw3d()
    
    pygame.display.flip()

    screen.fill("white") #remove this later, i love screen bleed
    
    pres.update(state=line,details="Coding...")
    clock.tick(30) 
pygame.quit()
pres.close()
#endLog()

