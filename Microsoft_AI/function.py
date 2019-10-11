# function
# check move and click event:

import pygame
import sys
key=False

def checkevent(wheelchair,screen,button):
    for event in pygame.event.get():
        # quit
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                wheelchair.rightmove=True
            elif event.key==pygame.K_LEFT:
                wheelchair.leftmove=True
            elif event.key==pygame.K_UP:
                wheelchair.upmove=True
            elif event.key==pygame.K_DOWN:
                wheelchair.downmove=True

        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                wheelchair.rightmove=False
            elif event.key==pygame.K_LEFT:
                wheelchair.leftmove=False
            elif event.key==pygame.K_UP:
                wheelchair.upmove=False
            elif event.key==pygame.K_DOWN:
                wheelchair.downmove=False

        elif event.type==pygame.MOUSEBUTTONDOWN:
            mousex,mousey=pygame.mouse.get_pos()
            if button.rect.collidepoint(mousex,mousey):
                global key
                key=True

def display(button):
    if key==False:
        button.draw()













        
