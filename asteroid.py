import pygame , math, random
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
    for i in bulletlist:
        i.draw(screen)
    for i in astlist:
        i.draw(screen)
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
        self.rotaterect.center=(self.x,self.y)
        self.cosine=math.cos(math.radians(self.angle+90))
        self.sine=math.sin(math.radians(self.angle+90))
        self.head=(self.x+self.cosine*self.x//2, self.y-self.sine*self.y//2)

    def draw(self,screen):
        screen.blit(self.rotate,self.rotaterect)

    def left(self):
        self.angle+=5
        self.rotate=pygame.transform.rotate(self.image,self.angle)
        self.rotaterect=self.rotate.get_rect()
        self.rotaterect.center=(self.x,self.y)
        self.cosine=math.cos(math.radians(self.angle+90))
        self.sine=math.sin(math.radians(self.angle+90))
        self.head=(self.x+self.cosine*self.x//2, self.y-self.sine*self.y//2)

    def right(self):
        self.angle-=5
        self.rotate=pygame.transform.rotate(self.image,self.angle)
        self.rotaterect=self.rotate.get_rect()
        self.rotaterect.center=(self.x,self.y)
        self.cosine=math.cos(math.radians(self.angle+90))
        self.sine=math.sin(math.radians(self.angle+90))
        self.head=(self.x+self.cosine*self.x//2, self.y-self.sine*self.y//2)
    
    def forward(self):
        self.x+=self.cosine*6
        self.y-=self.sine*6
        self.rotate=pygame.transform.rotate(self.image,self.angle)
        self.rotaterect=self.rotate.get_rect()
        self.rotaterect.center=(self.x,self.y)
        self.cosine=math.cos(math.radians(self.angle+90))
        self.sine=math.sin(math.radians(self.angle+90))
        self.head=(self.x+self.cosine*self.x//2, self.y-self.sine*self.y//2)

class bullet():
    def __init__(self):
        self.point=playert.head
        self.x,self.y = self.point
        self.w=5
        self.h=7.5
        self.sine=playert.sine
        self.cosine=playert.cosine
        self.xv=self.cosine*10
        self.yv=self.sine*10

    def move(self):
        self.x+=self.xv
        self.y+=self.yv

    def draw(self,screen):
        pygame.draw.rect(screen,"white",[self.x,self.y,self.w,self.h])

class asteroids():
    def __init__(self,type):
        self.type=type
        if self.type==1:
            self.image=ast5
        elif self.type==2:
            self.image=ast10
        elif self.type==3:
            self.image=ast15
        self.rect=self.image.get_rect()
        #self.x=random.randint(0,screenx)
        #self.y=random.randint(0,screeny)
        self.s=50*type
        self.ranPoint = random.choice([(random.randrange(0, screenx-self.s), random.choice([-1*self.s - 5, screeny + 5])), (random.choice([-1*self.s - 5, screenx + 5]), random.randrange(0, screeny - self.s))])
        self.x, self.y = self.ranPoint
        if self.x<screenx//2:
            self.xdir=1
        else:
            self.xdir=-1
        if self.y<screeny//2:
            self.ydir=1
        else:
            self.ydir=-1
        self.xv=self.xdir*random.randint(1,3)
        self.yv=self.ydir*random.randint(1,3)

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def collide(self):
        if self.rect.colliderect(bullet):
            self.x, self.y= random.randint(0,screenx)


playert=player()
bulletlist=[]
astlist=[]

while True:
    #essentials
    clock.tick(60)
    background()

    #asteroid creation
    asttype=random.randint(1,3)
    astlist.append(asteroids(asttype))
    
    for i in astlist:
        i.x+=i.xv
        i.y+=i.yv
        
    #bullet essentials
    for i in bulletlist:
        bulletshot.move()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if keys[pygame.K_SPACE]:
                bulletshot=bullet()
                bulletlist.append(bulletshot)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playert.left()
    if keys[pygame.K_RIGHT]:
        playert.right()
    if keys[pygame.K_UP]:
        playert.forward()


    pygame.display.update()