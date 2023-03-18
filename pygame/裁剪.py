import pygame as p
import sys
import os
from pygame.locals import *

p.init()

size = width, height = 800, 600
WHITE = (255, 255, 255)

clock = p.time.Clock()
screen = p.display.set_mode(size)
p.display.set_caption("turtle")

turtle = p.image.load("../素材/turtle.png")

# 0 -> 未选择, 1 -> 选择中, 2 -> 完成选择
select = 0
select_rect = p.Rect(0, 0, 0, 0)
# 0 -> 未拖拽, 1 -> 拖拽中, 2 -> 完成拖拽
drag = 0

position = turtle.get_rect()
position.center = width // 2, height // 2

while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            sys.quit()

        elif event.type == p.MOUSEBUTTONDOWN:
            if event.button == 1:
                # 第一次点击
                if select == 0 and drag == 0:
                    pos_start = p.mouse.get_pos()
                    select = 1
                # 第二次，拖拽
                elif select == 2 and drag == 0:
                    capture = screen.subsurface(select_rect).copy()
                    cap_rect = capture.get_rect()
                    drag = 1
                # 第三次，初始化
                elif select == 2 and drag == 2:
                    select = 0
                    drag = 0

        elif event.type == p.MOUSEBUTTONUP:
            if event.button == 1:
                # 第一次释放，结束选择
                if select == 1 and drag == 0:
                    pos_stop = p.mouse.get_pos()
                    select = 2
                # 第二次释放，结束拖拽
                if select == 2 and drag == 1:
                    drag = 2

        screen.blit(turtle, position)

# 未完
