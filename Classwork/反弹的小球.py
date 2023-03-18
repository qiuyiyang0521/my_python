import random as r
from turtle import screensize
import pygame as pg
import sys
pg.init()
screen = pg.display.set_mode([900, 600])
keep_going = True
pic = pg.image.load('../素材/CrazySmile.bmp')
picx = 0
BLACK = (0, 0, 0)
picy = 0
timer = pg.time.Clock()
speedx = 5
speedy = 5
while keep_going:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keep_going = False
            pg.quit()
            sys.exit()

    picx += speedx
    picy += speedy
    if picx <= 0 or picx + pic.get_width() >= screen.get_width():
        speedx = -speedx
    if picy <= 0 or picy + pic.get_height() >= screen.get_height():
        speedy = -speedy
    # screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    pg.display.update()
    timer.tick(60)  # 暂停1/60s
pg.quit()
sys.exit()
