# ui library

import pygame

mini = pygame.image.load("tzuiassets\minimize.png")
maxi = pygame.image.load("tzuiassets\maximize.png")

class Button:
    def __init__(self,pos,size):
        self.x = pos[0]
        self.y = pos[1]
        self.w = size[0]
        self.h = size[1]
    
class Switch:
    def __init__(self,pos,size):
        self.x = pos[0]
        self.y = pos[1]
        self.w = size[0]
        self.h = size[1]
class TextInput:
    def __init__(self,pos,size,text): # xy pos (tuple), size (tuple), default text (str)
        self.x = pos[0]
        self.y = pos[1]
        self.w = size[0]
        self.h = size[1]
        self.d = text

    def draw(self,surf):
        mspos = pygame.mouse.get_pos()
        if mspos[0] in range(self.x,self.w+1):
            if mspos[1] in range(self.y,self.h+1):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
class Dropdown:
    def __init__(self,pos,size):
        self.x = pos[0]
        self.y = pos[1]
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
        self.mxmn = mini
        if self.w < 100:
            self.w = 100
        if self.h < 100:
            self.h = 100
        
    def draw(self,surf):
        mspos = pygame.mouse.get_pos()
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        
        if self.m == True:
            pygame.draw.rect(surf,(26,25,50),((self.x,self.y),(self.w,self.h)))
            pygame.draw.rect(surf,(42,47,78),((self.x,self.y),(self.w,self.h)),1)
            self.mxmn = mini
        else:
            self.mxmn = maxi
        pygame.draw.rect(surf,(26,25,50),((self.x,self.y),(self.w,16)))
        pygame.draw.rect(surf,(42,47,78),((self.x,self.y),(self.w,16)),1)
        surf.blit(mxmn,((self.x+2,self.y+2),(12,12)))
        

        
        
        
        if mspos[0] in range(self.x+2,self.x+15):
            if mspos[1] in range(self.y+2,self.y+15):
                if clicked:
                    self.m = not self.m
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            
        
        if mspos[0] in range(self.x+self.w-2,self.x+self.w+3) or mspos[0] in range(self.x-2,self.x+3):        # sides
            if mspos[1] in range(self.y+2,self.y+(self.h*int(self.m)+1)+(16*int(not self.m))+1):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
                if pygame.mouse.get_pressed()[0] == True:
                    if (self.w += pygame.mouse.get_rel()[0]) >= 100:
                        self.w += pygame.mouse.get_rel()[0]
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if mspos[0] in range(self.x+2,self.x+self.w-1):        # tops and bottoms
            if mspos[1] in range(self.y+self.h-2,self.y+self.h+3) or mspos[1] in range(self.y-2,self.y+3):
                if self.m == True:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
                    if pygame.mouse.get_pressed()[0] == True:
                        if (self.h += pygame.mouse.get_rel()[1]) >= 100:
                            self.h += pygame.mouse.get_rel()[1]
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
