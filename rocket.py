import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

spacebg=pygame.image.load("space.png")



class rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("rocket.png")
        self.rect=self.image.get_rect()
    def update(self,keys):
        if keys[pygame.K_w]:
            self.rect.move_ip(0,-5)
        if keys[pygame.K_s]:
            self.rect.move_ip(0,5)
        if keys[pygame.K_a]:
            self.rect.move_ip(-5,0)
        if keys[pygame.K_d]:
            self.rect.move_ip(5,0)
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>800:
            self.rect.right=800
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>600:
            self.rect.bottom=600

player=rocket()
sprites=pygame.sprite.Group()
sprites.add(player)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    keys=pygame.key.get_pressed()
    screen.blit(spacebg,(0,0))
    player.update(keys)
    sprites.draw(screen)
    
    


    pygame.display.update()