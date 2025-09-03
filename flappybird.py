import pygame,random
pygame.init()
screen=pygame.display.set_mode((864,750))
pygame.display.set_caption("Flappy bird")

bg=pygame.image.load("birdbg.png")
ground=pygame.image.load("ground.png")
#bird1=pygame.image.load("bird1.png")
#bird2=pygame.image.load("bird2.png")
#bird3=pygame.image.load("bird3.png")
#pipe=pygame.image.load("pipe.png")

flying=False
class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.anims=[]
        self.index=0
        for i in range(1,4):
            img=pygame.image.load(f"bird{i}.png")
            self.anims.append(img)
        self.image=self.anims[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.velocity=0
        self.counter=0
    def update(self):
        if flying==True:
            self.velocity+=0.5
            if self.rect.bottom<632:
                self.rect.y+=self.velocity
            self.counter+=1
            if self.counter>=3:
                self.index+=1
                if self.index>3:
                    self.index=0
        

        

flappy=bird(50,400)
birdgroup=pygame.sprite.Group()
birdgroup.add(flappy)





while True:
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    birdgroup.update()
    screen.blit(ground,(0,632))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False:
            flying=True


    pygame.display.update()