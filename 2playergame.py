import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

yellowship=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("yellow.png"),(50,50)),270)
redship=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("red.png"),(50,50)),90)
space=pygame.image.load("space.png")

yellowrect=pygame.Rect(700,300,50,50)
redrect=pygame.Rect(100,300,50,50)
border=pygame.Rect(390,0,20,600)
font=pygame.font.SysFont("Times New roman",50)
winner=""
over=False

def draw():
    global win
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"black",border)
    screen.blit(yellowship,(yellowrect.x,yellowrect.y))
    screen.blit(redship,(redrect.x,redrect.y))
    redhealth=font.render(f"{rhealth}",True,"Red")
    yellowhealth=font.render(f"{yhealth}",True,"Yellow")
    screen.blit(redhealth,(10,10))
    screen.blit(yellowhealth,(770,10))
    for i in yelbullets:
        pygame.draw.rect(screen,"yellow",i)
    for i in redbullets:
        pygame.draw.rect(screen,"red",i)
    if over:
        win=font.render(f"{winner} WINS",True,"white")
        screen.blit(win,(350,250))




def gameover():
    global yhealth
    global rhealth
    global winner
    global over
    if yhealth<=0 and not rhealth<=0:
        over=True
        winner="RED"
    elif rhealth<=0 and not yhealth<=0:
        over=True
        winner="YELLOW"
    


def ymovement(keys):
    if keys[pygame.K_UP] and yellowrect.y>0:
        yellowrect.y-=5
    if keys[pygame.K_DOWN] and yellowrect.y<600:
        yellowrect.y+=5
    if keys[pygame.K_LEFT] and yellowrect.x>390:
        yellowrect.x-=5
    if keys[pygame.K_RIGHT] and yellowrect.x<800 :
        yellowrect.x+=5
    

def rmovement(keys):
    if keys[pygame.K_w] and redrect.y>0:
        redrect.y-=5
    if keys[pygame.K_s] and redrect.y<600:
        redrect.y+=5
    if keys[pygame.K_a] and redrect.x>0:
        redrect.x-=5
    if keys[pygame.K_d] and redrect.x<370:
        redrect.x+=5

def bulletmove(yelbullets,redbullets):
    global rhealth
    global yhealth
    for i in yelbullets:
        i.x-=10
        if redrect.colliderect(i):
            yelbullets.remove(i)
            rhealth-=1
        elif i.x<0:
            yelbullets.remove(i)
    for i in redbullets:
        i.x+=10
        if yellowrect.colliderect(i):
            redbullets.remove(i)
            yhealth-=1
        elif i.x>800:
            redbullets.remove(i)
    

            




rhealth=3
yhealth=3

redbullets=[]
yelbullets=[]

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit() 
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bullet=pygame.Rect(yellowrect.x+25,yellowrect.y+25,10,5)
                yelbullets.append(bullet)
            if event.key==pygame.K_e:
                bullet=pygame.Rect(redrect.x+25,redrect.y+25,10,5)
                redbullets.append(bullet)
    keys=pygame.key.get_pressed()
    
    if not over:
        ymovement(keys)
        rmovement(keys)
        bulletmove(yelbullets,redbullets)
    gameover()
    draw()



    pygame.display.update()
    