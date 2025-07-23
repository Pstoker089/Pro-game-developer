import pygame, random
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Paint brush app")
screen.fill("white")
colours=["red","orange","yellow","green","blue","purple","pink","black"]

setcolour="black"
drawing=False
lastpos=None
currentpos=None
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            lastpos=event.pos
            drawing=True
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            drawing=False
            pygame.display.update()
        elif event.type==pygame.MOUSEMOTION:
            if drawing:
                currentpos=event.pos
                pygame.draw.line(screen,setcolour,lastpos,currentpos)
                lastpos=currentpos
                pygame.display.update()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e:
                randcolour=random.choice(colours)
                setcolour=randcolour
            if event.key==pygame.K_q:
                colindex=colours.index(setcolour)
                setcolour=colours[(colindex+1)%len(colours)]
                