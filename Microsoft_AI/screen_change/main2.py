# main2
# screen chaneg:

# import library:
import pygame
import sys
import json
from speech_MS import speechToText_MS 
key = "344213864bc24fb5ab30081d44ba1f15"
region = "westus"
def main():
    voice_MC = speechToText_MS(key, region)
    pygame.init()
    screen = pygame.display.set_mode((900,600)) # adjust in own pc later
    screencolor=(0,0,0)
    pygame.display.set_caption('XXX') #change to project name
    home = pygame.image.load("home.jpg").convert()
    home = pygame.transform.scale(home, (900, 600))
    company = pygame.image.load("company.jpg").convert()
    company = pygame.transform.scale(company, (900, 600))
    play= pygame.image.load("play.jpg").convert()
    play = pygame.transform.scale(play, (900, 600))

    pic_array=[home,company,play]
    index=0
    destination=['Home.','Company.','Play.']
    while True:
        screen.fill(screencolor)
        voice_WC.start()
        with open('data.json') as file:
            data = json.loads(file)
            command= data["DisplayText"]
            
            index=destination.index(command)
            screen.blit(pic_array[index], [0, 0])
            
        '''
        
        for event in pygame.event.get():
        # quit
            if event.type==pygame.QUIT:
                sys.exit()

        # change imag:
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    index+=1
                elif event.key == pygame.K_LEFT:
                    index-=1

        # load json:
        
'''
        pygame.display.flip()

main()
        
