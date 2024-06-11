# ui library

import pygame


mini = pygame.image.load("tzuiassets\minimize.png")
maxi = pygame.image.load("tzuiassets\maximize.png")

class Button:
    def __init__(self,size):
        self.w = size[0]
        self.h = size[1]
    
class Switch:
    def __init__(self,size):
        self.w = size[0]
        self.h = size[1]
class TextInput:
    def __init__(self,size):
        self.w = size[0]
        self.h = size[1]
class Dropdown:
    def __init__(self,size):
        self.w = size[0]
        self.h = size[1]
class Window:
    

    
    def __init__(self,pos,size,name,comps):
        self.x = pos[0]
        self.y = pos[1]
        self.w = size[0]
        self.h = size[1]
        self.n = name
        self.m = True
        
    def draw(self,surf):
        mspos = pygame.mouse.get_pos()
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        
        if self.m == True:
            pygame.draw.rect(surf,(26,25,50),((self.x,self.y),(self.w,self.h)))
            pygame.draw.rect(surf,(42,47,78),((self.x,self.y),(self.w,self.h)),1)
            pygame.draw.rect(surf,(26,25,50),((self.x,self.y),(self.w,16)))
            pygame.draw.rect(surf,(42,47,78),((self.x,self.y),(self.w,16)),1)
            surf.blit(mini,((self.x+2,self.y+2),(12,12)))
        else:
            pygame.draw.rect(surf,(26,25,50),((self.x,self.y),(self.w,16)))
            pygame.draw.rect(surf,(42,47,78),((self.x,self.y),(self.w,16)),1)
            surf.blit(maxi,((self.x+2,self.y+2),(12,12)))
        

        
        
        
        if mspos[0] in range(self.x+2,self.x+14):
            if mspos[1] in range(self.y+2,self.y+14):
                if clicked:
                    self.m = not self.m
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        