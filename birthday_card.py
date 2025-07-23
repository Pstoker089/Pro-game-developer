import pygame , time
pygame.init()
screen=pygame.display.set_mode((600,600))

pygame.display.set_caption("Birthday greetings")

font=pygame.font.SysFont("Comic sans",50)



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    
    card=pygame.image.load("card.jpg")
    text=font.render("Happy Birthday!",True,"black")
    screen.blit(card,(0,0))
    screen.blit(text,(150,200))
    pygame.display.update()
    time.sleep(2)
    bdpopper=pygame.image.load("birthday_popper.jpg")
    screen.blit(bdpopper,(0,0))
    text2=font.render("From Penri",True,"black")
    screen.blit(text2,(150,200))
    pygame.display.update()
    time.sleep(2)
    cake=pygame.image.load("cake.jpg")
    text3=font.render("Have a wonderful day!",True,"black")
    screen.blit(cake,(0,0))
    screen.blit(text3,(100,200))
    pygame.display.update()
    time.sleep(2)

