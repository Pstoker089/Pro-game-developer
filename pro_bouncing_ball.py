import pygame
from random import randint
pygame.init()
screen=pygame.display.set_mode((800,600))

pygame.display.set_caption("Bouncing ball")

ball=pygame.draw.circle(surface=screen,color="green",center=(50,50),radius=40)

speed=[randint(1,5),randint(1,5)]

clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    clock.tick(200)
    screen.fill("black")
    ball=ball.move(speed)
    if ball.x>=800 or ball.x<=0:
        speed[0]=-speed[0]
    if ball.y>=600 or ball.y<=0:
        speed[1]=-speed[1]
    pygame.draw.circle(surface=screen,color="green",center=(ball.center),radius=40)
    pygame.display.update()