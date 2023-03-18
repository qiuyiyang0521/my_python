import pygame
import random
import sys
import time
pygame.init()
screen = pygame.display.set_mode([1920, 1028])
BLACK = [0, 0, 0]
colors = [0] * 100
locations = [0] * 100
sizes = [0] * 100
speedx = 5
speedy = 5
timer = pygame.time.Clock()
going = True
f = open(r"./帧数.txt", "w")
for n in range(100):
    colors[n] = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    locations[n] = (
        random.randint(0, screen.get_width()),
        random.randint(0, screen.get_height())
    )
    sizes[n] = random.randint(20, 100)


while True:
    start = time.time()
    # 常规操作
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f.close()
            pygame.quit()
            sys.exit()

    # 主体
    for n in range(100):
        pygame.draw.circle(screen, colors[n], locations[n], sizes[n],)
        new_x = locations[n][0] + speedx
        new_y = locations[n][1] + speedy
        if new_x > screen.get_width():
            new_x -= screen.get_width()
        if new_y > screen.get_height():
            new_y -= screen.get_height()
        locations[n] = (new_x, new_y)

    # 刷新页面，为下一次循环坐准备
    pygame.display.update()
    screen.fill(BLACK)
    timer.tick(120)
    end = time.time()
    str1 = str(1 / (end - start)) + '\r\n'
    f.write(str1)
