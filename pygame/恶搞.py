import pygame as p
p.init()
screen = p.display.set_mode([1920, 1080], p.FULLSCREEN | p.NOFRAME)
clock = p.time.Clock()
font = p.font.Font("./font/STXINGKA.TTF", 100)
speed = 1
t = "邱一阳"
text = font.render(t, True, (255, 255, 255))
text_rect = text.get_rect()
while True:
    for event in p.event.get():
        if event.type == p.MOUSEBUTTONDOWN:
            pass
        if event.type == p.QUIT:
            pass
    screen.fill((0, 0, 0))
    text_rect.right += 1
    p.mouse.set_pos(1920 // 2, 1080 // 2)

    if text_rect.right > 1920:
        text_rect.right = 1920
        speed = -speed
    if text_rect.right < text_rect.width:
        text_rect.right = text_rect.right
        speed = -speed
    screen.blit(text, text_rect)
    p.display.flip()
    clock.tick(60)

