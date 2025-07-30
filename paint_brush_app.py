import pygame, random
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Paint brush app")
screen.fill("white")
colours=["red","orange","yellow","green","blue","purple","pink","black"]
font=pygame.font.SysFont("Comic sans",10)


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
            if event.key==pygame.K_1:
                setcolour=colours[0]
            if event.key==pygame.K_2:
                setcolour=colours[1]
            if event.key==pygame.K_3:
                setcolour=colours[2]
            if event.key==pygame.K_4:
                setcolour=colours[3]
            if event.key==pygame.K_5:
                setcolour=colours[4]
            if event.key==pygame.K_6:
                setcolour=colours[5]
            if event.key==pygame.K_7:
                setcolour=colours[6]
            if event.key==pygame.K_8:
                setcolour=colours[7]
    text=font.render("1=Red 2=Orange 3=Yellow 4=Green 5=Blue 6=Purple 7=Pink 8=Black", True, "Black")
    screen.blit(text,(10,10))
    pygame.display.update()
                