import pgzrun
import random

TITLE="Bouncing ball"
WIDTH=600
HEIGHT=600

gravity=2000
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)

class ball:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.vx=200
        self.vy=0
        self.radius=40
    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,(red,green,blue))

b1=ball(50,50)

def draw():
    screen.clear()
    b1.draw()

def update(t):
    global gravity
    uy=b1.vy
    b1.vy+=gravity*t
    b1.y+=(uy+b1.vy)*0.5*t
    if b1.y>600:
        b1.y=600
        b1.vy=-b1.vy*0.9
    b1.x+=b1.vx*t
    if b1.x>=600 or b1.x<=0:
        b1.vx=-b1.vx

def on_key_down(key):
    if key==keys.SPACE:
        b1.vy=-500

pgzrun.go()
