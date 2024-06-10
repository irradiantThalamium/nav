# haha the play urr lives here

import math
from tzmath import radToDeg, degToRad, magCalc
import pygame

class Player:
    def __init__(self):
        self.x = 0     # positional data
        self.y = 0
        self.z = 0
        self.dx= 0     # velocity
        self.dy= 0
        self.dz= 0
        self.sp= 1.2     # speed
        self.gr= 0     # gravity
        self.fr= 0.6  # friction
        self.a = 0     # yaw
        self.l = 0     # pitch
        self.r = 0     # roll (probably will be unused but maybe ill use it for a screen shake or smth)
        self.wquery = False
        self.blastj = False
        self.airbrn = False
        self.bhwait = False
    
    def pUp(self):
        keys = pygame.key.get_pressed()
        
        if self.bhwait:
            self.fr = 0.6
            self.bhwait = False
        
        if keys[pygame.K_a]:
            self.a -= 3
        if keys[pygame.K_d]:
            self.a += 3
            
        if self.a > 359:
            self.a -= 360
        if self.a < 0:
            self.a += 360
        
        if keys[pygame.K_w]:
            self.dx+= math.cos(degToRad(self.a))*self.sp
            self.dy+= math.sin(degToRad(self.a))*self.sp
            self.wquery = True
        else:
            self.wquery = False 
            
        if keys[pygame.K_s]:
            self.dx-= math.cos(degToRad(self.a))*self.sp
            self.dy-= math.sin(degToRad(self.a))*self.sp
            
        if keys[pygame.K_LEFT]:
            self.dy-= math.cos(degToRad(self.a))*self.sp
            self.dx+= math.sin(degToRad(self.a))*self.sp
        if keys[pygame.K_RIGHT]:
            self.dy+= math.cos(degToRad(self.a))*self.sp
            self.dx-= math.sin(degToRad(self.a))*self.sp

        if keys[pygame.K_e]:
            print("ATTACK!!!!")
        
        if self.airbrn:
            self.fr = 1.001
        else:
            self.bhwait = True 
        
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz
        
        self.dx *= self.fr
        self.dy *= self.fr
        self.dz *= self.fr
        
    def drawAMap(self, screen):
        pygame.draw.line(screen,"black",(self.x,self.y),(self.x+(self.dx*3),self.y+(self.dy*3)))
        pygame.draw.line(screen,"green",(self.x,self.y),(self.x-(math.sin(degToRad(self.a)))*4,self.y+(math.cos(degToRad(self.a))*4)))
        pygame.draw.line(screen,"red",(self.x,self.y),(self.x+(math.cos(degToRad(self.a)))*10,self.y+(math.sin(degToRad(self.a))*10))) #sorry i had to go fix this real quick lmao
        
                         
                         
                         