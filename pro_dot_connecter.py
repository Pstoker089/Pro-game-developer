import pygame
pygame.init()
screen=pygame.display.set_mode((600,500))
screen.fill("white")
font=pygame.font.SysFont("Comic sans",30)
images={
    "candy crush":pygame.image.load("candy crush.jpg"),
    "temple run":pygame.image.load("temple_run.png"),
    "subway surfers":pygame.image.load("subway surfers.png"),
    "ludo":pygame.image.load("ludo.png")
}

gamepos={
    "candy crush":pygame.Rect(200,100,100,100),
    "temple run":pygame.Rect(200,200,100,100),
    "subway surfers":pygame.Rect(200,300,100,100),
    "ludo":pygame.Rect(200,400,100,100)
}

textpos={
    "ludo":pygame.Rect(400,100,100,100),
    "candy crush":pygame.Rect(400,200,100,100),
    "subway surfers":pygame.Rect(400,300,100,100),
    "temple run":pygame.Rect(400,400,100,100),
}

matches={
    "candy crush":"candy crush",
    "temple run":"temple run",
    "subway surfers":"subway surfers",
    "ludo":"ludo"
}



for name,pos in gamepos.items():
    screen.blit(images[name],(pos.x,pos.y))

for t,poss in textpos.items():
    text=font.render(t,True,"Black")
    screen.blit(text,(poss.x,poss.y))

pygame.display.update()



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            pass
        
    pygame.display.update()