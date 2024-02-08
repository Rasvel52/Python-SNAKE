import pygame
from random import randrange
from MainScript import Sett

s_settings = Sett()
pygame.init()
sc = pygame.display.set_mode([s_settings.Res, s_settings.Res])
Clock = pygame.time.Clock()
while True:
    sc.fill(s_settings.bg_color)

    [pygame.draw.rect(sc, pygame.Color('green'), (i, j, s_settings.Size - 1, s_settings.Size - 1)) for i, j in s_settings.snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*s_settings.apple, s_settings.Size, s_settings.Size))


    pygame.display.flip()
    Clock.tick(Sett.fps)

    newX = s_settings.snake[-1][0] + s_settings.dirx
    newY = s_settings.snake[-1][1] + s_settings.diry
    s_settings.snake.append((newX, newY))
    s_settings.snake = s_settings.snake[-s_settings.length-1:]

    if s_settings.snake[-1] == s_settings.apple:
        s_settings.apple = randrange(0, s_settings.Res, s_settings.Size), randrange(0, s_settings.Res, s_settings.Size)
        s_settings.length += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            s_settings.dirx, s_settings.diry = 0, -s_settings.Size
        if key[pygame.K_s]:
            s_settings.dirx, s_settings.diry = 0, s_settings.Size
        if key[pygame.K_a]:
            s_settings.dirx, s_settings.diry = -s_settings.Size, 0
        if key[pygame.K_d]:
            s_settings.dirx, s_settings.diry = s_settings.Size, 0