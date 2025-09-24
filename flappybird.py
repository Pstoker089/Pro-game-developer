import pygame,random
pygame.init()
screen=pygame.display.set_mode((864,750))
pygame.display.set_caption("Flappy bird")
screenx=864
screeny=750

bg=pygame.image.load("birdbg.png")
ground=pygame.image.load("ground.png")
button=pygame.image.load("restartbutton.png")


clock=pygame.time.Clock()
pipegap=120
pipetime=pygame.time.get_ticks()-1500
gscroll=0
gameover=False
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
        if gameover==False:
            self.counter+=1
            if self.counter>=5:
                self.index+=1
                self.counter=0
                if self.index>=len(self.anims):
                    self.index=0
                self.image=self.anims[self.index]
            if pygame.mouse.get_pressed()[0]==1:
                self.velocity=-5
                
class pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,face):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("pipe.png")
        self.rect=self.image.get_rect()
        if face==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-int(pipegap/2)]
        elif face==-1:
            self.rect.topleft=[x,y+int(pipegap/2)]
    def update(self):
        self.rect.x-=5
        if self.rect.right<0:
            self.kill()

class restart(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        self.x=x
        self.y=y
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    def draw(self):
        screen.blit(self.image,(self.rect.x, self.rect.y))
        reset=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] ==1:
                reset=True
                return reset

        
rb=restart((screenx//2),(screeny//2),button)

#the class thats gonna do all the reset stuff
def reset_game():
    global gameover
    global flappy
    global flying
    gameover=False
    pipegroup.empty()
    flappy.rect.x=50
    flappy.rect.y=400
    flying=False
    score=0
    return score





pipegroup=pygame.sprite.Group()

flappy=bird(50,400)
birdgroup=pygame.sprite.Group()
birdgroup.add(flappy)





while True:
    clock.tick(60)
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    birdgroup.update()
    pipegroup.draw(screen)
    screen.blit(ground,(0,632))
    if flying==True and gameover==False:
        gscroll-=5
        if gscroll<-35:
            gscroll=0
        screen.blit(ground,(gscroll,632))
        nowtime=pygame.time.get_ticks()
        if (nowtime-pipetime)>1500:
            pipeheight=random.randint(-100,100)
            toppipe=pipe(864,375+pipeheight,1)
            bottompipe=pipe(864,375+pipeheight,-1)
            pipegroup.add(toppipe)
            pipegroup.add(bottompipe)
            pipetime=nowtime
        pipegroup.update()
    #if bird hits bottom of screen, game over
    if flappy.rect.bottom>=632:
        gameover=True
        flying=False
    #if bird hits top of screen or a pipe, game over
    if pygame.sprite.groupcollide(birdgroup,pipegroup,False,False) or flappy.rect.top < 0:
        gameover=True
    if gameover==True:
        if rb.draw():
            score=reset_game()
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False:
            flying=True

   



    pygame.display.update()