import pygame ,random, time
from pygame.locals import *
pygame.init()
screenx=900
screeny=750
screen=pygame.display.set_mode((screenx,screeny))
font=pygame.font.SysFont("Times New roman",25)
gameover=False

bg=pygame.image.load("plantbg.png")

clock=pygame.time.Clock()
starttime=time.time()

allgroup=pygame.sprite.Group()
goodgroup=pygame.sprite.Group()
plastic=pygame.sprite.Group()
goodimages=["pencil.png","box.png","paper.png"]

class bin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("bin.png")
        self.image=pygame.transform.scale(self.image,(40,50))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y



class good(pygame.sprite.Sprite):
    def __init__(self, type, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(type)
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    

class bad(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("plastic bag.png")
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y    
        
for i in range(20):
    bitem=bad(random.randint(30,875),random.randint(30,720))
    plastic.add(bitem)
    allgroup.add(bitem)

for i in range(50):
    choice=random.choice(goodimages)
    
    gitem=good(choice,random.randint(30,875),random.randint(30,720))
    goodgroup.add(gitem)
    allgroup.add(gitem)

player=bin(20,20)
allgroup.add(player)
score=0



while True:
    clock.tick(60)
    screen.blit(bg,(0,0))
    
    allgroup.draw(screen)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.rect.y-=1
    if keys[pygame.K_DOWN]:
        player.rect.y+=1
    if keys[pygame.K_LEFT]:
        player.rect.x-=1
    if keys[pygame.K_RIGHT]:
        player.rect.x+=1
        
    goodhit=pygame.sprite.spritecollide(player,goodgroup,True)
    badhit=pygame.sprite.spritecollide(player,plastic,True)
    for i in goodhit:
        score+=1     
    for i in badhit:
        score-=1

    text=font.render(f"Score : {score}",True,"black")
    screen.blit(text,(0,0))

    endtime=time.time()
    alapsedtime=endtime-starttime
    if alapsedtime>=60:
        if score>=10:
            win=font.render("YOU WON",True,"black")
            screen.blit(win,(screenx/2,screeny/2))
            
    pygame.display.update()