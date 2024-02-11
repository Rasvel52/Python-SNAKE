import pygame
from random import randrange
from MainScript import Sett

s_settings = Sett()
pygame.init()
sc = pygame.display.set_mode([s_settings.Res, s_settings.Res])
pygame.display.set_caption("SNAKE")
Clock = pygame.time.Clock()
while True:
    sc.fill(s_settings.bg_color)
    render_score = s_settings.Font_Score.render(f'SCORE: {s_settings.score}', True , (255,0,0))
    sc.blit(render_score, (10, 10))

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
        s_settings.score += s_settings.New_Score

    if newX < 0 or newX > s_settings.Res - s_settings.Size or newY < 0 or newY > s_settings.Res - s_settings.Size:
        while True:
            render_end = s_settings.Font_End.render('GAME OVER', True, (255, 0, 0))
            sc.blit(render_end, (s_settings.Res // 2 - 239, s_settings.Res // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    
    if len(s_settings.snake) != len(set(s_settings.snake)):
            render_end = s_settings.Font_End.render('GAME OVER', True, (255, 0, 0))
            sc.blit(render_end, (s_settings.Res // 2 - 239, s_settings.Res // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_w] and s_settings.Control['W']:
            s_settings.dirx, s_settings.diry = 0, -s_settings.Size
            s_settings.Control = {'W':True, 'S':False, 'A':True, 'D':True}
        if key[pygame.K_s] and s_settings.Control['S']:
            s_settings.dirx, s_settings.diry = 0, s_settings.Size
            s_settings.Control = {'W':False, 'S':True, 'A':True, 'D':True}
        if key[pygame.K_a] and s_settings.Control['A']:
            s_settings.dirx, s_settings.diry = -s_settings.Size, 0
            s_settings.Control = {'W':True, 'S':True, 'A':True, 'D':False}
        if key[pygame.K_d] and s_settings.Control['D']:
            s_settings.dirx, s_settings.diry = s_settings.Size, 0
            s_settings.Control = {'W':True, 'S':True, 'A':False, 'D':False}