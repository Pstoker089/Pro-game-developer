import pygame
pygame.init()
screen=pygame.display.set_mode((600,500))
screen.fill("white")
candy=pygame.image.load("candy crush.jpg")
temple=pygame.image.load("temple_run.png")
subway=pygame.image.load("subway surfers.png")
ludo=pygame.image.load("ludo.png")

screen.blit(candy,(200,100))
screen.blit(temple,(200,200))
screen.blit(subway,(200,300))
screen.blit(ludo,(200,400))

font=pygame.font.SysFont("Comic sans",30)
text=font.render("Ludo", True,"black")
text2=font.render("Candy crush", True,"black")
text3=font.render("Subway surfers", True,"black")
text4=font.render("Temple run", True,"black")
screen.blit(text,(400,100))
screen.blit(text2,(400,200))
screen.blit(text3,(400,300))
screen.blit(text4,(400,400))



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(screen,"Black",pos,5)
        if event.type==pygame.MOUSEBUTTONUP:
            pos2=pygame.mouse.get_pos()
            pygame.draw.circle(screen,"Black",pos2,5)
            pygame.draw.line(screen,"Black",pos,pos2,5)
    pygame.display.update()