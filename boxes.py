import pygame , random
pygame.init()
screen=pygame.display.set_mode((800,600))

class block(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image=pygame.Surface((20,15))
        self.rect=self.image.get_rect()
        self.image.fill(colour)
black=pygame.sprite.Group()
boxes=pygame.sprite.Group()

rb=block("red")

for i in range(50):
    bb=block("Black")
    bb.rect.x=random.randrange(800)
    bb.rect.y=random.randrange(600)
    black.add(bb)
    boxes.add(bb)

boxes.add(rb)

score=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit() 
    screen.fill("white")
    mpos=pygame.mouse.get_pos()
    rb.rect.x=mpos[0]
    rb.rect.y=mpos[1]
    hitlist=pygame.sprite.spritecollide(rb,black,True)
    for i in hitlist:
        score+=1
        print(score)
    boxes.draw(screen)
    pygame.display.update()
