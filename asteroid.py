import pygame , math
pygame.init()

screenx=800
screeny=750
screen=pygame.display.set_mode((screenx,screeny))
font=pygame.font.SysFont("Times New roman",25)

bg=pygame.image.load("images/spacebg2.png")
clock=pygame.time.Clock()

def background():
    screen.blit(bg,(0,0))
    playert.draw(screen)
    pygame.display.update()

pship=pygame.image.load("images/playership.png")
aship=pygame.image.load("images/alienship.png")
ast5=pygame.image.load("images/asteroid 50.png")
ast10=pygame.image.load("images/asteroid 100.png")
ast15=pygame.image.load("images/asteroid 150.png")


class player():
    def __init__(self):
        self.image=pship
        self.rect=self.image.get_rect()
        self.x=400
        self.y=375
        self.angle=0
        self.rotate=pygame.transform.rotate(self.image,self.angle)
        self.rotaterect=self.rotate.get_rect()
        self.rotatepos=self.x,self.y
        
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))



        
playert=player()

while True:
    clock.tick(60)
    background()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()





    pygame.display.update()