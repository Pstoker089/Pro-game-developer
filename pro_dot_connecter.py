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

usedmatch=[]
score=0

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
            spos=pygame.mouse.get_pos()
        elif event.type==pygame.MOUSEBUTTONUP:
            epos=pygame.mouse.get_pos()
            slabel=None
            elabel=None
            for label,rect in gamepos.items():
                if rect.collidepoint(spos):
                    slabel=label
                    break
            for label,rect in textpos.items():
                if rect.collidepoint(epos):
                    elabel=label
                    break
            if slabel and elabel:
                pygame.draw.line(screen,"black",spos,epos,5)
                if matches[slabel]==elabel and (slabel,elabel) not in usedmatch:
                    score+=1
                    usedmatch.append((slabel,elabel))
                    print(f"correct match! \n the score is {score}")
                else:
                    print("Wrong match!")
                    
                    
            

    pygame.display.update()