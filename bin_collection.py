import pygame ,random
pygame.init()
screenx=900
screeny=750
screen=pygame.display.set_mode((screenx,screeny))

gameover=False

bg=pygame.image.load("plantbg.png")

clock=pygame.time.Clock()

allgroup=pygame.sprite.Group()
goodgroup=pygame.sprite.Group()
plastic=pygame.sprite.Group()
goodimages=["pencil.png","box.png","paper.png"]
class bin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("bin.png")
        self.rect=self.image.get_rect()

 

class good(pygame.sprite.Sprite):
    def __init__(self, type, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(type)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.image=pygame.transform.scale(self.image,(40,40))
    

class bad(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("plastic bag.png")
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.image=pygame.transform.scale(self.image,(40,40))
        
for i in range(20):
    

for i in range(50):
    choice=random.choice(goodimages)
    
    gitem=good(choice,random.randint(5,895),random.randint(5,745))
    goodgroup.add(gitem)
    allgroup.add(gitem)



while True:
    clock.tick(60)
    screen.blit(bg,(0,0))
    
    allgroup.draw(screen)







    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    
    pygame.display.update()