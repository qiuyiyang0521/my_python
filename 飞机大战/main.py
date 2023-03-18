# coding:utf-8
import traceback
import pygame as p
import sys
import myplane
import bullet
import enemy
import supply
from pygame.locals import *
from random import *

p.init()
p.mixer.init()

bg_size = width, height = 480, 700
screen = p.display.set_mode(bg_size)
p.display.set_caption("飞机大战")

background = p.image.load("images/background.png").convert()

# 载入音乐
p.mixer.music.load("sound/game_music.ogg")
p.mixer.music.set_volume(0.2)
bullet_sound = p.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = p.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = p.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = p.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = p.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = p.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = p.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = p.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = p.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = p.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = p.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)


def main():
    p.mixer.music.play(-1)

    # 生成我方飞机
    me = myplane.MyPlane(bg_size)

    clock = p.time.Clock()
    running = True

    while running:
        for event in p.event.get():
            if event.type == QUIT:
                p.quit()
                sys.exit()

        # 检测用户的键盘操作
        key_pressed = p.key.get_pressed()
        # 移动我方飞机
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveRight()

        screen.blit(background, (0, 0))

        p.display.flip()
        clock.tick(60)

    if __name__ == "__main__":
        try:
            main()
        except SystemExit:
            pass
        except:
            traceback.print_exc()
            p.quit()
            input()
