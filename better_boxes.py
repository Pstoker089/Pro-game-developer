import pygame , random
pygame.init()
screen=pygame.display.set_mode((800,600))

class block(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image=pygame.Surface((20,15))
        self.rect=self.image.get_rect()
        self.image.fill(colour)
    def death(self):
        self.rect.x=random.randint(30,770)
        self.rect.y=random.randint(-300,-20)
    def update(self):
        self.rect.y+=1
        if self.rect.y>=620:
            self.death()

class redblock(block):
    def update(self):
        mpos=pygame.mouse.get_pos()
        self.rect.x=mpos[0]
        self.rect.y=mpos[1]

black=pygame.sprite.Group()
boxes=pygame.sprite.Group()

rb=redblock("red")

for i in range(50):
    bb=block("Black")
    black.add(bb)
    boxes.add(bb)

boxes.add(rb)

score=0
clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit() 
    screen.fill("white")
    mpos=pygame.mouse.get_pos()
    rb.rect.x=mpos[0]
    rb.rect.y=mpos[1]
    hitlist=pygame.sprite.spritecollide(rb,black,False)
    for i in hitlist:
        score+=1
        print(score)
        i.death()
    boxes.update()
    boxes.draw(screen)
    clock.tick(60)
    pygame.display.update()