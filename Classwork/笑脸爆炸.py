from tkinter import Y
import pygame as p
import random as r
import sys


class Smiley(p.sprite.Sprite):
    pos = (0, 0)
    xvel = 1
    yvel = 1
    scale = 100  # (%)

    def __init__(self, pos, xvel, yvel) -> None:
        super().__init__()
        self.image = pic
        self.rect = self.image.get_rect()  # 得到笑脸的矩形框
        self.pos = pos
        self.rect.x = pos[0] - self.scale / 2
        self.rect.y = pos[1] - self.scale / 2
        self.xvel = xvel
        self.yvel = yvel
        self.scale = r.randint(30, 100)
        self.image = p.transform.scale(self.image, (self.scale, self.scale))

    def update(self) -> None:
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x <= 0 or self.rect.x + self.scale >= root.get_width():
            self.xvel = -self.xvel
        if self.rect.y <= 0 or self.rect.y + self.scale >= root.get_height():
            self.yvel = -self.yvel


p.init()
root = p.display.set_mode([800, 600])
p.display.set_caption("笑脸爆炸")
mouseDown = False
BLACK = (0, 0, 0)
clock = p.time.Clock()
pic = p.image.load("F:\GitHub\my_python\素材\CrazySmile.bmp")
colorKey = pic.get_at((0, 0))
pic.set_colorkey(colorKey)
sprite_list = p.sprite.Group()


while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            print("程序结束")
            sys.exit()
        if event.type == p.MOUSEBUTTONDOWN:
            if p.mouse.get_pressed()[0]:
                mouseDown = True
            elif p.mouse.get_pressed()[2]:
                pos = p.mouse.get_pos()
                clicked_smiley = [
                    s for s in sprite_list if s.rect.collidepoint(pos)]
                sprite_list.remove(clicked_smiley)
        if event.type == p.MOUSEBUTTONUP:
            mouseDown = False
    root.fill(BLACK)
    sprite_list.update()
    sprite_list.draw(root)
    clock.tick(60)
    p.display.update()
    if mouseDown:
        speedx = r.randint(-5, 5)
        speedy = r.randint(-5, 5)
        newSmiley = Smiley(p.mouse.get_pos(), speedx, speedy)
        sprite_list.add(newSmiley)
