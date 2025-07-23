import pygame
pygame.init()
screen=pygame.display.set_mode((225,225))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        onbulb=pygame.image.load("bulb_on.jpg")
        offbulb=pygame.image.load("bulb_off.jpg")  

        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.blit(onbulb,(0,0))
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONUP:
            screen.blit(offbulb,(0,0))
            pygame.display.update()