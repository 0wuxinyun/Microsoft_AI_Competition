# main.py:

# import library:
import pygame
import function
from button import Button 
from wheelchair import Wheelchair 
def main():
    pygame.init()
    screen = pygame.display.set_mode((900,600)) # adjust in own pc later
    screencolor=(0,0,0)
    pygame.display.set_caption('WHEELCHAIR DEMO')
    msg="START"
    wheelchair=Wheelchair(screen)
    button=Button(screen,msg) # refer to Button class
    while True:
        screen.fill(screencolor)
        wheelchair.show()
        function.checkevent(wheelchair,screen,button)
        function.display(button)
        if function.key:
            wheelchair.move()
            
        


        pygame.display.flip()

main()
