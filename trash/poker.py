#!/usr/bin/env python
# coding: utf-8

# In[1]:


import holdem_calc


# In[2]:


print(holdem_calc.calculate(["As", "Ks", "Jd"], True, 1, None, ["8s", "7s", "Qc", "Th", "Kc", "Kd"], False))


# In[22]:


print(holdem_calc.calculate(None, False, 100000, None, ["8s", "7s", "Qc", "Th", "Kc", "Kd"], False))


# In[20]:


print(holdem_calc.calculate(None, False, 100000, None, ["8s", "7s", "Qc", "Th"], False))


# In[1]:


import pygame
import sys
import random


# In[24]:


WIDTH, HEIGHT = 1500, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Poker Odds Game')

WHITE = (5,100, 32)

WIN.fill(WHITE)

class button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        print(self.rect)
        self.topleft = (x, y)
        self.clicked = False
        
    def draw(self):
#         WIN.blit(self.image, (200, 200))

        pos = pygame.mouse.get_pos()
    
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print("clicked")
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            

        WIN.blit(self.image, (self.rect.x, self.rect.y))

def draw_window():
    pygame.display.update()

def main():
    
    start_button = button(100,100, start_img)
    exit_button = button(150,200, exit_img)
     
    run = True
    while run:
        
        start_button.draw()
        exit_button.draw()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window()
        
    pygame.quit()
    
start_img = pygame.image.load('./images/start.png').convert_alpha()
exit_img = pygame.image.load('./images/exit.jpeg').convert_alpha()
    

        
    
if __name__ == "__main__":
    main()

